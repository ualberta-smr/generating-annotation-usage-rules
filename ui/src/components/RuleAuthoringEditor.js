import "./RuleAuthoringEditor.scss";
import MonacoEditor from "react-monaco-editor";

const __MONACO_EDITOR_OPTIONS = {
    readOnly: false,
    folding: false,
    minimap: {
        enabled: false,
    },
    lineNumbers: "off",
    wordWrap: "on",
}

function RuleAuthoringEditor(props) {
    const handleChange = (text) => {
        props.onChange(text);
    };

    return (
        <MonacoEditor
            width={750}
            height={220}
            value={props.text}
            options={__MONACO_EDITOR_OPTIONS}
            onChange={handleChange}
            className={props.className}
        />
    );
}

export default RuleAuthoringEditor;
