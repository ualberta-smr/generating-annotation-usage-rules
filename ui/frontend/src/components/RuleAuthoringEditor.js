import "./RuleAuthoringEditor.scss";
import { useEffect, useState } from "react";
import MonacoEditor from "react-monaco-editor";
import { useResizeDetector } from 'react-resize-detector';

const __MONACO_EDITOR_OPTIONS = {
    readOnly: false,
    folding: false,
    minimap: {
        enabled: false,
    },
    lineNumbers: "off",
    wordWrap: "on",
    fontSize: "17px"
};

function RuleAuthoringEditor(props) {
    const [editorData, setEditor] = useState(null);

    const { width, height, ref } = useResizeDetector();

    useEffect(() => {
        if (width || height) {
            console.log(width, height)
            adjustEditorSize();
        }
    }, [width, height]);

    const handleChange = (text) => {
        props.onChange(text);
    };

    const editorDidMount = (editor, monaco) => {
        setEditor({ editor, monaco });
    };

    const adjustEditorSize = () => {
        if (editorData) {
            const { editor, monaco } = editorData;
            editor.layout();
            editor.updateOptions({"fontSize": Math.floor(height * 0.035)})
        }
    }

    return (
        <div className="resize-detecting-wrapper" ref={ref}>
            <MonacoEditor
                width={"40vw"}
                height={"50vh"}
                value={props.text}
                options={__MONACO_EDITOR_OPTIONS}
                onChange={handleChange}
                className={props.className}
                editorDidMount={editorDidMount}
                theme="shortRulePadTheme"
                language="shortRulepad"
            />
        </div>
    );
}

export default RuleAuthoringEditor;
