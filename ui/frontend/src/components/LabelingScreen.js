import "./LabelingScreen.scss";
import { useEffect, useState } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";

import FieldsetWrapper from "./FieldsetWrapper";
import RuleAuthoringEditor from "./RuleAuthoringEditor";
import makeCancellablePromise from "./superPromise";
import CodeEditor from "./CodeEditor";

function LabelingScreen() {
    const [currentRuleId, setCurrentRuleId] = useState(null);
    const [buttonAvailability, setButtonAvailability] = useState({
        hasPrev: false,
        hasNext: false,
    });
    const [grammarText, setGrammarText] = useState("");
    const [propertiesFileData, setPropertiesFileData] = useState();

    const [code, setRuleCode] = useState("");
    const [ruleLabel, setRuleLabel] = useState(null);

    const [previousGrammarToCodeRequest, setCancelCurrentRequestHandle] =
        useState({
            cancel: () => {},
        });

    const handleLabeling = (label) => {
        let newRuleLabel = ["correct", "not_a_rule"].includes(label)
            ? label
            : "unlabeled";
        
        /* 
            Basic idea is that if it is 'correct' already and you click the button again,
            it will be unlabeled...the same for 'not_a_rule' as well
            and if it is 'unlabeled' for some reason, we do nothing
        */

        let requestOptions = {}
        if (newRuleLabel === "correct") {
            if (newRuleLabel === ruleLabel) {
                newRuleLabel = "unlabeled"
            } else {
                // label to correct
                requestOptions = {
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        ruleString: grammarText,
                    })
                }
            }
        } else if (newRuleLabel === "not_a_rule") {
            if (newRuleLabel === ruleLabel) {
                newRuleLabel = "unlabeled"
            } else {
                // label to not a rule
            }
        } else if (newRuleLabel === "unlabeled") {
            return
        }

        fetch(`http://localhost:5000/rules/${currentRuleId}/${newRuleLabel}`, {
                method: "POST", ...requestOptions
            })
                .then((resp) => {
                    if (resp.status === 204) {
                        setRuleLabel(newRuleLabel);
                    }
                })
                .catch((e) => {
                    console.error(e);
                });
    };

    useEffect(() => {
        getNextRule();
    }, []);

    const getNextRule = () => {
        const id_str = currentRuleId == null ? "" : `/${currentRuleId}/next`;
        makeCancellablePromise(
            `http://localhost:5000/rules${id_str}`,
            (json) => {
                const { hasNext, hasPrev, label } = json;
                setButtonAvailability({
                    hasNext,
                    hasPrev,
                });
                setRuleLabel(label);
                const data = json.data;

                const { id, ruleString, grammar } = data;

                setCurrentRuleId(id);
                setGrammarText(ruleString);
                processGrammarToCodeResponse(grammar);
            }
        );
    };
    const getPrevRule = () => {
        makeCancellablePromise(
            `http://localhost:5000/rules/${currentRuleId}/prev`,
            (json) => {
                const { hasNext, hasPrev, label } = json;
                setButtonAvailability({
                    hasNext,
                    hasPrev,
                });
                setRuleLabel(label);

                const data = json.data;

                const { id, ruleString, grammar } = data;

                setCurrentRuleId(id);
                setGrammarText(ruleString);
                processGrammarToCodeResponse(grammar);
            }
        );
    };

    const clearData = () => {
        setRuleCode("");
        setPropertiesFileData(null);
    };

    const processGrammarToCodeResponse = (grammar) => {
        if (grammar == null) {
            clearData();
        } else {
            const codeText = grammar.code;
            if (codeText) {
                setRuleCode(codeText.trim());
            }

            const configuration = grammar.configuration;
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
                    <h2>Candidate Rule {currentRuleId}</h2>
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
                                    code={propertiesFileData.text}
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
                    <div className="controls-wrapper">
                        <div className="controls">
                            <div
                                className={
                                    "left-btn-div" +
                                    (buttonAvailability.hasPrev
                                        ? ""
                                        : " disabledBtn")
                                }
                            >
                                <button
                                    className="btn-round btn-left"
                                    onClick={() => getPrevRule()}
                                    disabled={!buttonAvailability.hasPrev}
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

                            <div
                                className={
                                    "right-btn-div" +
                                    (buttonAvailability.hasNext
                                        ? ""
                                        : " disabledBtn")
                                }
                            >
                                <button
                                    className="btn-round btn-right"
                                    onClick={() => getNextRule()}
                                    disabled={!buttonAvailability.hasNext}
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
