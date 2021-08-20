import "./LabelingScreen.scss";
import { useState, useRef } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";
import MonacoEditor from "react-monaco-editor";

import FieldsetWrapper from "./FieldsetWrapper";
import RuleAuthoringEditor from "./RuleAuthoringEditor";
import CodeExampleVisualizer from "./CodeExampleVisualizer";
import makeCancellablePromise from "./superPromise";

function LabelingScreen() {
    const [grammarText, setGrammarText] = useState("");
    const [oldDecorations, setNewDecorations] = useState([]);
    const [propertiesFileData, setPropertiesFileData] = useState();

    const [code, setRuleCode] = useState("");
    const [ruleLabel, setRuleLabel] = useState(null);
    const [editorData, setEditor] = useState(null);

    const [cancelPreviousRequest, setCancelCurrentRequestHandle] = useState({
        cancel: () => {},
    });

    const handleLabeling = (label) => {
        if (["correct", "not_a_rule", "best_practice"].includes(label)) {
            setRuleLabel(label);
        } else {
            setRuleLabel(null);
        }
    };

    const getNextRule = () => {};
    const getPrevRule = () => {};

    const editorDidMount = (editor, monaco) => {
        setEditor({ editor, monaco });
    };

    const codeEditor = (
        value,
        onValueChange,
        editorDidMountAction = null,
        fileName = "Foo.java",
        disabled = false,
        language = "java"
    ) => {
        if (editorDidMountAction == null) editorDidMountAction = editorDidMount;
        const height = 400 * (1 / (propertiesFileData == null ? 1 : 2));
        return (
            <FieldsetWrapper title={`Code editor: ${fileName}`}>
                <MonacoEditor
                    width={800}
                    height={height}
                    language={language}
                    theme="vs-light"
                    value={value}
                    onChange={onValueChange}
                    editorDidMount={editorDidMountAction}
                    options={{
                        readOnly: disabled,
                    }}
                />
            </FieldsetWrapper>
        );
    };

    const clearCodeEditor = () => {
        const { editor, monaco } = editorData;
        setNewDecorations(
            editor.deltaDecorations(oldDecorations, [
                { range: new monaco.Range(1, 1, 1, 1), options: {} },
            ])
        );
    };

    const updateRelatedFields = (text) => {
        // console.log(`[${text}]`);
        clearCodeEditor();
        setGrammarText(text);

        cancelPreviousRequest.cancel();

        if (text.trim() === "") {
            setRuleCode("");
            setPropertiesFileData(null);
            return null;
        }

        const cancelPromise = makeCancellablePromise(
            `http://localhost:5000/grammarToCode?grammar=${text}`,
            (json) => {
                if (json == null) {
                    console.log("Error");
                    setRuleCode("");
                    setPropertiesFileData(null);
                    clearCodeEditor();
                } else {
                    // console.log(json)
                    const code = json.code;

                    const codeText = code.map((e) => e[0]).join("\n");
                    const rangeValues = code.map((e) => e[1]).flat();

                    const { editor, monaco } = editorData;

                    const ranges = rangeValues.map((rangeData) => {
                        const row = rangeData[0] + 1;
                        const s = rangeData[1] + 1;
                        const e = rangeData[2] + 1;
                        const isAntecedent = rangeData[3] === "["; // TODO: fix this
                        const r = new monaco.Range(row, s, row, e);
                        return {
                            range: r,
                            options: {
                                inlineClassName: isAntecedent
                                    ? "antecedent"
                                    : "consequent",
                            },
                        };
                    });

                    const newDecorations = editor.deltaDecorations(
                        oldDecorations,
                        ranges
                    );

                    setNewDecorations(newDecorations);
                    setRuleCode(codeText.trim());

                    const properties = json.properties;
                    if (properties) {
                        const [name, text] = properties;
                        setPropertiesFileData({
                            name,
                            text,
                        });
                    } else {
                        setPropertiesFileData(null);
                    }
                }
            }
        );

        setCancelCurrentRequestHandle(cancelPromise);
    };

    const renderUI = () => {
        return (
            <div className="app">
                <div className="instructions">
                    <h2>Candidate Rule 15</h2>
                    <p>
                        <strong>Instructions: </strong>
                        <em>
                            Edit the candidate rule as needed and then confirm
                            the rule once done. If the candidate rule is
                            completely not correct or not useful for authoring a
                            rule, click <strong>"Not a rule"</strong>
                        </em>
                    </p>
                </div>
                <div className="editors-row-wrapper">
                    <div className="editors-row">
                        <div className="rule-authoring-editor-wrapper">
                            <div className="rule-authoring-editor">
                                <FieldsetWrapper
                                    title={"Rule Authoring Editor"}
                                >
                                    <RuleAuthoringEditor
                                        text={grammarText}
                                        onChange={(text) =>
                                            updateRelatedFields(text)
                                        }
                                    />
                                </FieldsetWrapper>
                            </div>
                        </div>
                        <div className="code-editors">
                            {codeEditor(code, (value) => {
                                setRuleCode(value);
                            })}
                            {propertiesFileData == null
                                ? null
                                : codeEditor(
                                      propertiesFileData.text,
                                      setRuleCode,
                                      (a, b) => {},
                                      propertiesFileData.name,
                                      true,
                                      null
                                  )}
                        </div>
                    </div>
                </div>
                <div className="examples-and-controls-row">
                    <div className="examples">
                        <CodeExampleVisualizer
                            title="Example of Complying Code"
                            className="correct"
                            code={`class Foo {\n    @Fallback(fallbackMethod="doWhenFails")\n    public void method() {}\n}`}
                        ></CodeExampleVisualizer>

                        <CodeExampleVisualizer
                            title="Example of Violation"
                            className="violation"
                            code={`class Foo {\n    @Fallback\n    public void method() {}\n}`}
                        ></CodeExampleVisualizer>
                    </div>
                    <div className="controls-wrapper">
                        <div className="controls">
                            <div className="left-btn-div">
                                <button
                                    className="btn-round btn-left"
                                    onClick={() => getPrevRule()}
                                >
                                    <span>
                                        <FaArrowLeft />
                                    </span>
                                </button>
                            </div>

                            <div className="buttons">
                                <button
                                    className={`btn btn-correct ${
                                        ruleLabel === "correct"
                                            ? "btn-selected"
                                            : ""
                                    }`}
                                    onClick={() => handleLabeling("correct")}
                                >
                                    CONFIRM RULE
                                </button>
                                <button
                                    className={`btn btn-incorrect ${
                                        ruleLabel === "not_a_rule"
                                            ? "btn-selected"
                                            : ""
                                    }`}
                                    onClick={() => handleLabeling("not_a_rule")}
                                >
                                    NOT A RULE
                                </button>
                            </div>

                            <div className="right-btn-div">
                                <button
                                    className="btn-round btn-right"
                                    onClick={() => getNextRule()}
                                >
                                    <span>
                                        <FaArrowRight />
                                    </span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    };

    return renderUI();
}

export default LabelingScreen;
