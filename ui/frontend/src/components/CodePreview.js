import FieldsetWrapper from "./FieldsetWrapper";
import "./CodePreview.scss";

const getOrDefault = (value, defaultValue = null) =>
    value ? value : defaultValue;

function CodePreview(props) {
    const code  = props.code;
    const fileName = getOrDefault(props.fileName, "Foo.java");
    const { height, width } = props.measurements;

    return (
        <FieldsetWrapper title={`Code Preview: ${fileName}`}>
            <pre
                style={{
                    width,
                    minHeight: height,
                    marginBottom: 0,
                    marginTop: 0,
                }}
                className="code-editor-text"
                dangerouslySetInnerHTML={{
                    __html: code,
                }}
            ></pre>
            <div className="label-div" style={{backgroundColor: "white"}}>
                <div className="label-antecedent">antecedent</div>
                <div className="label-consequent">consequent</div>
            </div>
        </FieldsetWrapper>
    );
}

export default CodePreview;
