import { useState } from "react";
import { runKataTests } from "../runners/pythonRunner.js";

function formatValue(value) {
  if (value === null) return "None";
  if (typeof value === "string") return JSON.stringify(value);
  return JSON.stringify(value);
}

export default function TestRunner({ kata }) {
  const [state, setState] = useState("idle");
  const [output, setOutput] = useState(null);
  const [error, setError] = useState(null);

  async function handleRun() {
    setState("loading");
    setError(null);
    setOutput(null);
    try {
      const result = await runKataTests(kata);
      setOutput(result);
      setState("done");
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
      setState("error");
    }
  }

  if (!kata.runnable) {
    return (
      <div className="test-runner test-runner--disabled">
        <p>No test file for this kata yet.</p>
      </div>
    );
  }

  return (
    <div className="test-runner">
      <div className="test-runner__actions">
        <button
          type="button"
          className="button button--primary"
          onClick={handleRun}
          disabled={state === "loading"}
        >
          {state === "loading" ? "Running…" : "Run tests"}
        </button>
        {output && (
          <span className={`test-runner__summary ${output.passed === output.total ? "pass" : "fail"}`}>
            {output.passed === output.total ? "✓" : "✗"} {output.passed}/{output.total} passed · {output.durationMs}ms
          </span>
        )}
      </div>

      {state === "loading" && (
        <p className="test-runner__hint">Loading Python runtime (first run may take a few seconds)…</p>
      )}
      {error && <pre className="test-runner__error">{error}</pre>}

      {output?.mode === "cases" && (
        <ul className="test-results">
          {output.results.map((item) => (
            <li key={item.index} className={item.passed ? "pass" : "fail"}>
              <span className="test-results__icon">{item.passed ? "✓" : "✗"}</span>
              <span>
                {item.function}({item.args.map(formatValue).join(", ")}) → expected {formatValue(item.expected)}
                {!item.passed && `, got ${formatValue(item.actual)}`}
                {item.error && ` · ${item.error}`}
              </span>
            </li>
          ))}
        </ul>
      )}

      {output?.mode === "pytest" && (
        <ul className="test-results">
          {output.results.map((item) => (
            <li key={item.name} className={item.passed ? "pass" : "fail"}>
              <span className="test-results__icon">{item.passed ? "✓" : "✗"}</span>
              <span>
                {item.name}
                {item.error && ` · ${item.error}`}
              </span>
            </li>
          ))}
        </ul>
      )}

      {output?.stdout && <pre className="test-runner__io">stdout:\n{output.stdout}</pre>}
      {output?.stderr && <pre className="test-runner__io">stderr:\n{output.stderr}</pre>}
    </div>
  );
}
