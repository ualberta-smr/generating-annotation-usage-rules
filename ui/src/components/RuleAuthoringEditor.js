import "./RuleAuthoringEditor.scss";
import { useState } from "react";
import MonacoEditor from "react-monaco-editor";

const __MONACO_EDITOR_OPTIONS = {
    readOnly: false,
    folding: false,
    minimap: {
        enabled: false,
    },
    lineNumbers: "off",
    wordWrap: "on",
};

function RuleAuthoringEditor(props) {
    const [editorData, setEditor] = useState(null);

    const handleChange = (text) => {
        props.onChange(text);
    };

    const editorDidMount = (editor, monaco) => {
        setEditor({ editor, monaco });
    };

    return (
        <MonacoEditor
            width={750}
            height={220}
            value={props.text}
            options={__MONACO_EDITOR_OPTIONS}
            onChange={handleChange}
            className={props.className}
            editorDidMount={editorDidMount}
            theme="myCoolTheme"
            language="shortRulepad"
        />
    );
}

export default RuleAuthoringEditor;
