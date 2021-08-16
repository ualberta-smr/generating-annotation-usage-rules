import Editor from "react-simple-code-editor";
import { highlight, languages } from "prismjs/components/prism-core";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-java";
import "prismjs/themes/prism.css";
import "./CodeExampleVisualizer.scss"

// className:
// title
// code
function CodeExampleVisualizer(props) {
    const codeVisualizer = (value) => {
        return (
            <Editor
                value={value}
                highlight={(code) => highlight(code, languages.java)}
                padding={10}
                style={{
                    fontFamily: '"Fira code", "Fira Mono", monospace',
                }}
                className="code-snippet-textbar"
                disabled={true}
            />
        );
    };

    return (
        <div className={props.className}>
            <h1>{props.title}</h1>
            {codeVisualizer(props.code)}
        </div>
    );
}

export default CodeExampleVisualizer;
