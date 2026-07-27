import { useState } from "react";
import CodePanel from "./CodePanel.jsx";
import TestRunner from "./TestRunner.jsx";

const TABS = [
  { id: "description", label: "Description" },
  { id: "solution", label: "Solution" },
  { id: "tests", label: "Tests" },
  { id: "run", label: "Run" },
];

function badgeForKata(kata) {
  if (kata.source === "codewars" && kata.kyu) {
    return `${kata.kyu} kyu`;
  }
  if (kata.source === "sololearn" && kata.difficulty) {
    return kata.difficulty;
  }
  return kata.source;
}

export default function KataDetail({ kata }) {
  const [tab, setTab] = useState("description");

  if (!kata) {
    return (
      <section className="detail detail--empty">
        <h2>Select a kata</h2>
        <p>Pick a challenge from the sidebar to view the task, solution, and tests.</p>
      </section>
    );
  }

  return (
    <section className="detail">
      <header className="detail__header">
        <div>
          <p className="detail__meta">
            <span className="badge">{badgeForKata(kata)}</span>
            <span className="badge badge--muted">{kata.source}</span>
            <span className="badge badge--muted">{kata.language}</span>
          </p>
          <h2>{kata.title}</h2>
        </div>
        <a
          className="detail__github"
          href={`https://github.com/bmalvo/battlefield/tree/main/${kata.slug}`}
          target="_blank"
          rel="noreferrer"
        >
          View on GitHub
        </a>
      </header>

      <div className="tabs">
        {TABS.map((item) => (
          <button
            key={item.id}
            type="button"
            className={`tabs__tab ${tab === item.id ? "active" : ""}`}
            onClick={() => setTab(item.id)}
          >
            {item.label}
          </button>
        ))}
      </div>

      <div className="detail__body">
        {tab === "description" && (
          <article className="description">
            {kata.description ? (
              <pre>{kata.description}</pre>
            ) : (
              <p>No description found in the solution docstring.</p>
            )}
          </article>
        )}

        {tab === "solution" && (
          <CodePanel code={kata.solution} filename={kata.solutionFile} />
        )}

        {tab === "tests" && (
          kata.tests ? (
            <CodePanel code={kata.tests} filename={kata.testFile} />
          ) : (
            <p className="detail__empty-tab">No tests available.</p>
          )
        )}

        {tab === "run" && <TestRunner kata={kata} />}
      </div>
    </section>
  );
}
