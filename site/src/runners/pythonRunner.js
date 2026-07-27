const PYODIDE_CDN = "https://cdn.jsdelivr.net/pyodide/v0.27.7/full/";

let pyodidePromise = null;

async function loadPyodide() {
  if (!pyodidePromise) {
    pyodidePromise = (async () => {
      if (!globalThis.loadPyodide) {
        await import(/* @vite-ignore */ `${PYODIDE_CDN}pyodide.js`);
      }
      const pyodide = await globalThis.loadPyodide({
        indexURL: PYODIDE_CDN,
      });
      return pyodide;
    })();
  }
  return pyodidePromise;
}

function buildRunnerScript(solution, tests, imports) {
  return `
import sys
import traceback
from io import StringIO
from types import ModuleType, SimpleNamespace

results = []
stdout_buffer = StringIO()
stderr_buffer = StringIO()
sys.stdout = stdout_buffer
sys.stderr = stderr_buffer

class _ParametrizeDecorator:
    def __call__(self, *args, **kwargs):
        def wrapper(func):
            return func
        return wrapper

pytest = SimpleNamespace(mark=SimpleNamespace(parametrize=_ParametrizeDecorator()))
sys.modules["pytest"] = pytest

solution_ns = {"__name__": "solution"}
imports = ${JSON.stringify(imports)}

try:
    exec(${JSON.stringify(solution)}, solution_ns)

    modules = {}
    for item in imports:
        module_name = item["module"]
        if module_name not in modules:
            module = ModuleType(module_name)
            for key, value in solution_ns.items():
                if not key.startswith("_") and callable(value):
                    setattr(module, key, value)
            for item2 in imports:
                if item2["module"] == module_name and item2["name"] in solution_ns:
                    setattr(module, item2["name"], solution_ns[item2["name"]])
            modules[module_name] = module
            sys.modules[module_name] = module

    test_ns = {"__name__": "tests", "pytest": pytest}
    exec(${JSON.stringify(tests)}, test_ns)

    tests_to_run = [
        (name, test_ns[name])
        for name in sorted(test_ns)
        if name.startswith("test_") and callable(test_ns[name])
    ]

    if not tests_to_run:
        results.append({
            "name": "discovery",
            "passed": False,
            "error": "No test functions found.",
        })
    else:
        for name, func in tests_to_run:
            try:
                func()
                results.append({"name": name, "passed": True})
            except Exception as exc:
                results.append({
                    "name": name,
                    "passed": False,
                    "error": f"{type(exc).__name__}: {exc}",
                })
except Exception:
    results.append({
        "name": "setup",
        "passed": False,
        "error": traceback.format_exc(),
    })
finally:
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

{
    "results": results,
    "stdout": stdout_buffer.getvalue(),
    "stderr": stderr_buffer.getvalue(),
}
`;
}

export async function runPythonTests(kata) {
  const pyodide = await loadPyodide();
  const script = buildRunnerScript(kata.solution, kata.tests, kata.imports ?? []);
  const output = await pyodide.runPythonAsync(script);
  return output.toJs({ dict_converter: Object.fromEntries, list_converter: Array.from });
}

export async function runParametrizeCases(kata) {
  if (!kata.cases?.length || !kata.imports?.length) {
    return null;
  }

  const targetName = kata.imports.length === 1 ? kata.imports[0].name : null;
  if (!targetName) {
    return null;
  }

  const pyodide = await loadPyodide();
  const script = `
solution_ns = {}
exec(${JSON.stringify(kata.solution)}, solution_ns)
fn = solution_ns.get(${JSON.stringify(targetName)})
if fn is None:
    raise RuntimeError("Function ${targetName} not found in solution.")
results = []
for index, case in enumerate(${JSON.stringify(kata.cases)}):
    try:
        args = case.get("args") or []
        expected = case.get("expected")
        actual = fn(*args)
        passed = actual == expected
        results.append({
            "index": index,
            "function": case.get("function"),
            "args": args,
            "expected": expected,
            "actual": actual,
            "passed": passed,
        })
    except Exception as exc:
        results.append({
            "index": index,
            "function": case.get("function"),
            "args": case.get("args") or [],
            "expected": case.get("expected"),
            "actual": None,
            "passed": False,
            "error": f"{type(exc).__name__}: {exc}",
        })
results
`;
  const results = await pyodide.runPythonAsync(script);
  return results.toJs({ dict_converter: Object.fromEntries, list_converter: Array.from });
}

export async function runKataTests(kata) {
  const started = performance.now();
  const caseResults = await runParametrizeCases(kata);
  if (caseResults?.length) {
    const passed = caseResults.filter((item) => item.passed).length;
    return {
      mode: "cases",
      passed,
      total: caseResults.length,
      durationMs: Math.round(performance.now() - started),
      results: caseResults,
    };
  }

  const pytestLike = await runPythonTests(kata);
  const passed = pytestLike.results.filter((item) => item.passed).length;
  return {
    mode: "pytest",
    passed,
    total: pytestLike.results.length,
    durationMs: Math.round(performance.now() - started),
    stdout: pytestLike.stdout,
    stderr: pytestLike.stderr,
    results: pytestLike.results,
  };
}
