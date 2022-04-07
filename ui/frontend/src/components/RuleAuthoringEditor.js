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
    wordWrap: "off",
    fontSize: "17px"
};

function RuleAuthoringEditor(props) {
    const [editorData, setEditor] = useState(null);

    const { width, height, ref } = useResizeDetector();

    useEffect(() => {
        if (width || height) {
            adjustEditorSize();
        }
    }, [width, height]);

    useEffect(() => {
        if (editorData) {
            const {editor, monaco} = editorData; 
            const model = editor.getModel();
            // this resets the undo stack
            // and it is not a good idea
            model._commandManager._undoRedoService._editStacks.clear();
            editor.focus();

            const lines = model.getValue().split("\n");

            const startRow = lines.length;
            const startCol = lines[lines.length - 1].length;
            const endRow = lines.length;
            const endCol = startCol;
    
            const selection = new monaco.Selection(startRow, startCol, endRow, endCol);
    
            editor.setSelection(selection);
        }
    }, [props.resetEditorUndoStack])

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
            editor.updateOptions({ "fontSize": Math.floor(height * 0.035) })
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
                theme="shortRulepadTheme"
                language="shortRulepad"
            />
        </div>
    );
}

export default RuleAuthoringEditor;
