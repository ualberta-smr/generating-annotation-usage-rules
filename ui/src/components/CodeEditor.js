import { useEffect, useState } from "react";
import FieldsetWrapper from "./FieldsetWrapper";
import MonacoEditor from "react-monaco-editor/lib/editor";
import "./CodeEditor.scss";

const getOrDefault = (value, defaultValue = null) =>
    value ? value : defaultValue;

function CodeEditor(props) {
    const { code, ranges } = props.value;
    const onValueChange = props.onValueChange;
    let editorDidMountAction = getOrDefault(props.editorDidMountAction);
    const fileName = getOrDefault(props.fileName, "Foo.java");
    const disabled = getOrDefault(props.disabled, false);
    const language = getOrDefault(props.language, "java");
    const { height, width } = props.measurements;

    const [editorData, setEditor] = useState(null);
    const [oldDecorations, setNewDecorations] = useState([]);

    useEffect(() => {
        if (editorData) {
            clearCodeEditor();
            handleRanges(ranges);
        }
    });

    const clearCodeEditor = () => {
        const { editor, monaco } = editorData;
        setNewDecorations(
            editor.deltaDecorations(oldDecorations, [
                { range: new monaco.Range(1, 1, 1, 1), options: {} },
            ])
        );
    };

    const handleRanges = (rangeValues) => {
        const { editor, monaco } = editorData;

        const ranges = rangeValues.map((rangeData) => {
            const row = rangeData[0] + 1;
            const s = rangeData[1] + 1;
            const e = rangeData[2] + 1;
            const isAntecedent = rangeData[3];
            const r = new monaco.Range(row, s, row, e);
            return {
                range: r,
                options: {
                    inlineClassName: isAntecedent ? "antecedent" : "consequent",
                },
            };
        });

        const newDecorations = editor.deltaDecorations(oldDecorations, ranges);

        setNewDecorations(newDecorations);
    };

    const editorDidMount = (editor, monaco) => {
        setEditor({ editor, monaco });
    };

    if (editorDidMountAction == null) editorDidMountAction = editorDidMount;

    return (
        <FieldsetWrapper title={`Code editor: ${fileName}`}>
            <pre
                style={{
                    width,
                    height,
                }}
                className="code-editor-text"
                dangerouslySetInnerHTML={{
                    __html: code,
                }}
            ></pre>
        </FieldsetWrapper>
    );
}

export default CodeEditor;
