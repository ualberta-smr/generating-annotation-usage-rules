import "./LabelingScreen.scss";
import { useState } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";

import FieldsetWrapper from "./FieldsetWrapper";
import RuleAuthoringEditor from "./RuleAuthoringEditor";
import CodeExampleVisualizer from "./CodeExampleVisualizer";
import makeCancellablePromise from "./superPromise";
import CodeEditor from "./CodeEditor";

function LabelingScreen() {
    const [grammarText, setGrammarText] = useState("");
    const [propertiesFileData, setPropertiesFileData] = useState();

    const [code, setRuleCode] = useState("");
    const [ruleLabel, setRuleLabel] = useState(null);

    const [previousGrammarToCodeRequest, setCancelCurrentRequestHandle] =
        useState({
            cancel: () => {},
        });

    const handleLabeling = (label) => {
        const ruleLabel = ["correct", "not_a_rule"].includes(label)
            ? label
            : null;
        setRuleLabel(ruleLabel);
    };

    const getNextRule = () => {};
    const getPrevRule = () => {};

    const clearData = () => {
        setRuleCode("");
        setPropertiesFileData(null);
    };

    const processGrammarToCodeResponse = (json) => {
        if (json == null) {
            clearData();
        } else {
            const codeText = json.code;
            if (codeText) {
                setRuleCode(codeText.trim());
            }

            const configuration = json.configuration;
            if (configuration) {
                const { filename, code } = configuration;
                setPropertiesFileData({
                    name: filename,
                    text: code,
                });
            } else {
                setPropertiesFileData(null);
            }
        }
    };

    const updateRelatedFields = (text) => {
        setGrammarText(text);

        previousGrammarToCodeRequest.cancel();

        if (text.trim() === "") {
            clearData();
            return null;
        }

        setCancelCurrentRequestHandle(
            makeCancellablePromise(
                `http://localhost:5000/grammarToCode?grammar=${text}`,
                processGrammarToCodeResponse
            )
        );
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
                            <CodeEditor
                                code={code}
                                measurements={{
                                    width: 800,
                                    height:
                                        300 *
                                        (1 /
                                            (propertiesFileData == null
                                                ? 1
                                                : 2)),
                                }}
                            />

                            {propertiesFileData == null ? null : (
                                <CodeEditor
                                    value={propertiesFileData.text}
                                    fileName={propertiesFileData.name}
                                    measurements={{
                                        width: 800,
                                        height:
                                            300 *
                                            (1 /
                                                (propertiesFileData == null
                                                    ? 1
                                                    : 2)),
                                    }}
                                />
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
