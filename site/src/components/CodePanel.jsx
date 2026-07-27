import CodeMirror from "@uiw/react-codemirror";
import { python } from "@codemirror/lang-python";
import { oneDark } from "@codemirror/theme-one-dark";

export default function CodePanel({ code, filename }) {
  return (
    <div className="code-panel">
      <div className="code-panel__header">{filename}</div>
      <CodeMirror
        value={code}
        height="100%"
        theme={oneDark}
        extensions={[python()]}
        editable={false}
        basicSetup={{
          lineNumbers: true,
          foldGutter: true,
          highlightActiveLine: false,
        }}
      />
    </div>
  );
}
