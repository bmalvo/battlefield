import { useMemo, useState } from "react";

const SOURCE_OPTIONS = [
  { id: "all", label: "All sources" },
  { id: "codewars", label: "CodeWars" },
  { id: "sololearn", label: "SoloLearn" },
];

const KYU_OPTIONS = [5, 6, 7, 8];

export default function Sidebar({ katas, selectedId, onSelect }) {
  const [query, setQuery] = useState("");
  const [source, setSource] = useState("all");
  const [kyu, setKyu] = useState("all");

  const filtered = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    return katas.filter((kata) => {
      if (source !== "all" && kata.source !== source) return false;
      if (kyu !== "all" && kata.kyu !== Number(kyu)) return false;
      if (!normalized) return true;
      return (
        kata.title.toLowerCase().includes(normalized) ||
        kata.slug.toLowerCase().includes(normalized)
      );
    });
  }, [katas, query, source, kyu]);

  return (
    <aside className="sidebar">
      <div className="sidebar__filters">
        <input
          type="search"
          placeholder="Search katas…"
          value={query}
          onChange={(event) => setQuery(event.target.value)}
        />

        <label>
          Source
          <select value={source} onChange={(event) => setSource(event.target.value)}>
            {SOURCE_OPTIONS.map((option) => (
              <option key={option.id} value={option.id}>
                {option.label}
              </option>
            ))}
          </select>
        </label>

        <label>
          Kyu
          <select value={kyu} onChange={(event) => setKyu(event.target.value)}>
            <option value="all">All levels</option>
            {KYU_OPTIONS.map((level) => (
              <option key={level} value={level}>
                {level} kyu
              </option>
            ))}
          </select>
        </label>
      </div>

      <p className="sidebar__count">{filtered.length} katas</p>

      <ul className="kata-list">
        {filtered.map((kata) => (
          <li key={kata.id}>
            <button
              type="button"
              className={`kata-list__item ${selectedId === kata.id ? "active" : ""}`}
              onClick={() => onSelect(kata.id)}
            >
              <span className="kata-list__title">{kata.title}</span>
              <span className="kata-list__meta">
                {kata.source === "codewars" && kata.kyu ? `${kata.kyu} kyu` : kata.difficulty || kata.source}
              </span>
            </button>
          </li>
        ))}
      </ul>
    </aside>
  );
}
