#!/usr/bin/env python3
"""Scan codewars/ and sololearn/ folders and emit site/public/katas.json."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "site" / "public" / "katas.json"
SOURCES = ("codewars", "sololearn")
SKIP_FILES = {"tempCodeRunnerFile.py"}
SKIP_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".md"}


def title_from_slug(slug: str) -> str:
    return slug.replace("_", " ").strip().title()


def parse_docstring(source: str) -> str:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return ""
    doc = ast.get_docstring(tree)
    if not doc:
        return ""
    doc = doc.strip()
    if doc.lower().startswith("task:"):
        doc = doc[5:].strip()
    elif doc.lower().startswith("task "):
        doc = doc[4:].strip()
    return doc


def parse_imports(test_source: str) -> list[dict[str, str]]:
    imports: list[dict[str, str]] = []
    try:
        tree = ast.parse(test_source)
    except SyntaxError:
        return imports

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                imports.append(
                    {
                        "module": node.module,
                        "name": alias.name,
                        "alias": alias.asname or alias.name,
                    }
                )
    return imports


def parse_parametrize_cases(test_source: str) -> list[dict]:
    """Extract @pytest.mark.parametrize tuples when present."""
    cases: list[dict] = []
    try:
        tree = ast.parse(test_source)
    except SyntaxError:
        return cases

    for node in ast.walk(tree):
        if not isinstance(node, ast.FunctionDef):
            continue
        for dec in node.decorator_list:
            if not _is_parametrize_decorator(dec):
                continue
            arg_names, values = _parse_parametrize_decorator(dec)
            if not values:
                continue
            for value_tuple in values:
                if len(arg_names) == 1:
                    cases.append(
                        {
                            "function": node.name,
                            "args": [value_tuple[0]],
                            "kwargs": {},
                            "expected": value_tuple[1] if len(value_tuple) > 1 else None,
                            "argNames": arg_names,
                        }
                    )
                else:
                    cases.append(
                        {
                            "function": node.name,
                            "args": list(value_tuple[:-1]),
                            "kwargs": {},
                            "expected": value_tuple[-1],
                            "argNames": arg_names,
                        }
                    )
    return cases


def _is_parametrize_decorator(dec: ast.AST) -> bool:
    target = dec
    if isinstance(dec, ast.Call):
        target = dec.func
    if isinstance(target, ast.Attribute):
        return (
            target.attr == "parametrize"
            and isinstance(target.value, ast.Attribute)
            and target.value.attr == "mark"
        )
    return False


def _parse_parametrize_decorator(dec: ast.Call) -> tuple[list[str], list[tuple]]:
    if not isinstance(dec, ast.Call) or len(dec.args) < 2:
        return [], []

    names_node = dec.args[0]
    values_node = dec.args[1]

    if isinstance(names_node, ast.Constant):
        arg_names = [part.strip() for part in str(names_node.value).split(",") if part.strip()]
    else:
        return [], []

    values = _literal_list(values_node)
    return arg_names, values


def _literal_list(node: ast.AST) -> list[tuple]:
    if not isinstance(node, (ast.List, ast.Tuple)):
        return []
    rows: list[tuple] = []
    for elt in node.elts:
        value = _literal_value(elt)
        if isinstance(value, tuple):
            rows.append(value)
        elif value is not None:
            rows.append((value,))
    return rows


def _literal_value(node: ast.AST):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Tuple):
        return tuple(_literal_value(elt) for elt in node.elts)
    if isinstance(node, ast.List):
        return [_literal_value(elt) for elt in node.elts]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        inner = _literal_value(node.operand)
        if isinstance(inner, (int, float)):
            return -inner
    if isinstance(node, ast.Name):
        if node.id in {"True", "False", "None"}:
            return {"True": True, "False": False, "None": None}[node.id]
    return None


def discover_kata_dirs() -> list[Path]:
    dirs: list[Path] = []
    for source in SOURCES:
        base = ROOT / source
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_dir():
                continue
            py_files = [
                f
                for f in path.iterdir()
                if f.is_file()
                and f.suffix == ".py"
                and f.name not in SKIP_FILES
                and not f.name.startswith("test_")
            ]
            if py_files:
                dirs.append(path)
    return dirs


def pick_solution_file(folder: Path) -> Path | None:
    candidates = [
        f
        for f in folder.iterdir()
        if f.is_file()
        and f.suffix == ".py"
        and f.name not in SKIP_FILES
        and not f.name.startswith("test_")
    ]
    if not candidates:
        return None
    preferred = folder / f"{folder.name}.py"
    if preferred in candidates:
        return preferred
    return sorted(candidates, key=lambda p: p.name)[0]


def pick_test_file(folder: Path) -> Path | None:
    tests = sorted(f for f in folder.glob("test_*.py") if f.is_file())
    return tests[0] if tests else None


def build_entry(folder: Path) -> dict | None:
    rel = folder.relative_to(ROOT).as_posix()
    source = rel.split("/")[0]
    solution_file = pick_solution_file(folder)
    if not solution_file:
        return None

    solution_source = solution_file.read_text(encoding="utf-8")
    test_file = pick_test_file(folder)
    test_source = test_file.read_text(encoding="utf-8") if test_file else ""

    entry: dict = {
        "id": rel.replace("/", "--"),
        "slug": rel,
        "title": title_from_slug(folder.name),
        "source": source,
        "language": "python",
        "description": parse_docstring(solution_source),
        "solutionFile": solution_file.name,
        "testFile": test_file.name if test_file else None,
        "solution": solution_source,
        "tests": test_source,
        "imports": parse_imports(test_source) if test_source else [],
        "cases": parse_parametrize_cases(test_source) if test_source else [],
        "runnable": bool(test_file),
    }

    if source == "codewars":
        match = re.search(r"kata_(\d+)", rel)
        entry["kyu"] = int(match.group(1)) if match else None
    elif source == "sololearn":
        parts = rel.split("/")
        entry["difficulty"] = parts[1] if len(parts) > 2 else "unknown"

    return entry


def main() -> None:
    entries = []
    for folder in discover_kata_dirs():
        entry = build_entry(folder)
        if entry:
            entries.append(entry)

    entries.sort(key=lambda item: (item["source"], item.get("kyu") or 99, item["title"].lower()))

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")

    runnable = sum(1 for item in entries if item["runnable"])
    print(f"Wrote {len(entries)} katas ({runnable} runnable) to {OUTPUT}")


if __name__ == "__main__":
    main()
