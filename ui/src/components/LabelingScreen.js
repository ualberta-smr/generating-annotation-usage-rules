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
    const [ranges, setRuleRanges] = useState([]);
    const [ruleLabel, setRuleLabel] = useState(null);

    const [cancelPreviousRequest, setCancelCurrentRequestHandle] = useState({
        cancel: () => {},
    });

    const handleLabeling = (label) => {
        const ruleLabel = ["correct", "not_a_rule", "best_practice"].includes(
            label
        )
            ? label
            : null;
        setRuleLabel(ruleLabel);
    };

    const getNextRule = () => {};
    const getPrevRule = () => {};

    const updateRelatedFields = (text) => {
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
                    setRuleCode("");
                    setPropertiesFileData(null);
                } else {
                    const source = json.code.source;
                    const codeText = source //.map((e) => e[0]).join("\n");
                    // const rangeValues = source.map((e) => e[1]).flat();

                    // handle range values somehow
                    setRuleCode(codeText.trim());
                    // setRuleRanges(rangeValues);

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
                            <CodeEditor
                                value={{ code, ranges }}
                                onValueChange={setRuleCode}
                                measurements={{
                                    width: 800,
                                    height:
                                        400 *
                                        (1 /
                                            (propertiesFileData == null
                                                ? 1
                                                : 2)),
                                }}
                            />

                            {/* {propertiesFileData == null ? null : (
                                <CodeEditor
                                    value={propertiesFileData.text}
                                    onValueChange={setRuleCode}
                                    editorDidMountAction={(a, b) => {}}
                                    fileName={propertiesFileData.name}
                                    disabled={true}
                                    language={"null"}
                                    measurements={{
                                        width: 800,
                                        height:
                                            400 *
                                            (1 /
                                                (propertiesFileData == null
                                                    ? 1
                                                    : 2)),
                                    }}
                                />
                            )} */}
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
