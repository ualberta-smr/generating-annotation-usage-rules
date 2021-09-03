import FieldsetWrapper from "./FieldsetWrapper";
import "./CodeEditor.scss";

const getOrDefault = (value, defaultValue = null) =>
    value ? value : defaultValue;

function CodeEditor(props) {
    const code  = props.code;
    const fileName = getOrDefault(props.fileName, "Foo.java");
    const { height, width } = props.measurements;

    return (
        <FieldsetWrapper title={`Code: ${fileName}`}>
            <pre
                style={{
                    width,
                    minHeight: height
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
