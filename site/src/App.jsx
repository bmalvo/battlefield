import { useEffect, useMemo, useState } from "react";
import KataDetail from "./components/KataDetail.jsx";
import Sidebar from "./components/Sidebar.jsx";

function readKataFromHash(katas) {
  const hash = window.location.hash.replace(/^#/, "");
  if (!hash) return null;
  return katas.find((kata) => kata.id === hash) ?? null;
}

export default function App() {
  const [katas, setKatas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedId, setSelectedId] = useState(null);

  useEffect(() => {
    async function loadKatas() {
      try {
        const response = await fetch(`${import.meta.env.BASE_URL}katas.json`);
        if (!response.ok) {
          throw new Error(`Failed to load katas.json (${response.status})`);
        }
        const data = await response.json();
        setKatas(data);
        const fromHash = readKataFromHash(data);
        setSelectedId(fromHash?.id ?? data[0]?.id ?? null);
      } catch (err) {
        setError(err instanceof Error ? err.message : String(err));
      } finally {
        setLoading(false);
      }
    }

    loadKatas();
  }, []);

  useEffect(() => {
    function onHashChange() {
      const kata = readKataFromHash(katas);
      if (kata) setSelectedId(kata.id);
    }
    window.addEventListener("hashchange", onHashChange);
    return () => window.removeEventListener("hashchange", onHashChange);
  }, [katas]);

  const selectedKata = useMemo(
    () => katas.find((kata) => kata.id === selectedId) ?? null,
    [katas, selectedId],
  );

  function handleSelect(id) {
    setSelectedId(id);
    window.location.hash = id;
  }

  if (loading) {
    return <div className="app app--centered">Loading battlefield…</div>;
  }

  if (error) {
    return <div className="app app--centered app--error">{error}</div>;
  }

  return (
    <div className="app">
      <header className="header">
        <div>
          <p className="header__eyebrow">Coding portfolio</p>
          <h1>Battlefield Explorer</h1>
        </div>
        <div className="header__links">
          <span>{katas.length} challenges</span>
          <a href="https://github.com/bmalvo/battlefield" target="_blank" rel="noreferrer">
            GitHub
          </a>
        </div>
      </header>

      <main className="layout">
        <Sidebar katas={katas} selectedId={selectedId} onSelect={handleSelect} />
        <KataDetail kata={selectedKata} />
      </main>
    </div>
  );
}
