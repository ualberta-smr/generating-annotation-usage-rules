import "./RuleAuthoringEditor.scss";
import MonacoEditor from "react-monaco-editor";
import { useState } from "react";

function RuleAuthoringEditor(props) {
    const [grammarText, setGrammarText] = useState(props.text);

    const handleChange = (text) => {
        setGrammarText(text);
        props.onChange(text);
    };

    return (
        <MonacoEditor
            width={750}
            height={220}
            value={props.text}
            options={{
                readOnly: false,
                folding: false,
                minimap: {
                    enabled: false,
                },
                lineNumbers: "off",
                wordWrap: "on",
            }}
            onChange={handleChange}
            className={props.className}
        />
    );
}

export default RuleAuthoringEditor;
