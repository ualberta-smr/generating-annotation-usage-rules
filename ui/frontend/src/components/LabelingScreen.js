import "./LabelingScreen.scss";
import { useEffect, useState } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";

import FieldsetWrapper from "./FieldsetWrapper";
import RuleAuthoringEditor from "./RuleAuthoringEditor";
import makeCancellablePromise from "./superPromise";
import CodeEditor from "./CodeEditor";
import prettify, { onelineify } from "../grammar/formatter";
import { BACKEND_URL, LS_USERNAME } from "./constants";

function LabelingScreen() {
    const [username, setUsername] = useState(window.localStorage.getItem(LS_USERNAME));
    // this is a flag that represents if the current rule is a new rule or not
    // new rule here refers to the freshly retrieved rule from the server, without any edits
    // this is actually not a boolean flag but more like a representation of a change
    // every time there's a new rule, the flag is flipped
    // listening to its changes, we can run useEffect 
    const [isNewRule, setIsNewRule] = useState(true);

    const [ruleMetaData, setRuleMetaData] = useState({
        id: null,
        name: 'Default package name',
        size: 0
    });

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
            cancel: () => { },
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

        const requestOptions = {
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                ruleString: onelineify(grammarText),
                username: username
            })
        }

        if (newRuleLabel === "correct") {
            if (newRuleLabel === ruleLabel) {
                newRuleLabel = "unlabeled"
            } else {
                // label to correct
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

        fetch(`${BACKEND_URL}/rules/${ruleMetaData.id}/${newRuleLabel}`, {
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

    const processRule = (json) => {
        const { hasNext, hasPrev, label } = json;
        setButtonAvailability({
            hasNext,
            hasPrev,
        });
        setRuleLabel(label);

        const data = json.data;

        const { id, ruleString, grammar, name, size } = data;

        setRuleMetaData({ id, name, size });
        setGrammarText(prettify(ruleString));
        setIsNewRule(!isNewRule);
        processGrammarToCodeResponse(grammar);
    }

    const getNextRule = () => {
        const id_str = ruleMetaData.id == null ? "" : `/${ruleMetaData.id}/next`;
        makeCancellablePromise(
            `${BACKEND_URL}/rules${id_str}?user_id=${username}`,
            processRule
        );
    };

    const getPrevRule = () => {
        makeCancellablePromise(
            `${BACKEND_URL}/rules/${ruleMetaData.id}/prev?user_id=${username}`,
            processRule
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
            if (configuration.length > 0) {
                const configFiles = configuration.map(({ filename, code }) => {
                    return {
                        name: filename,
                        text: code
                    }
                });
                setPropertiesFileData(configFiles);
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

        const sentText = onelineify(text);

        setCancelCurrentRequestHandle(
            makeCancellablePromise(
                `${BACKEND_URL}/grammarToCode?grammar=${sentText}`,
                processGrammarToCodeResponse
            )
        );
    };

    const renderUI = () => {
        return (
            <div className="app">
                <div className="instructions">
                    <h2>{ruleMetaData.name}: Candidate Rule {ruleMetaData.id}/{ruleMetaData.size} ({username})</h2>
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
                                        resetEditorUndoStack={isNewRule}
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
                                <div className="config-file-editors">
                                    {propertiesFileData.map(conf => (
                                        <CodeEditor
                                            code={conf.text}
                                            fileName={conf.name}
                                            measurements={{
                                                width: 800 / propertiesFileData.length,
                                                height: 300 * 0.5,
                                            }}
                                        />))}
                                </div>
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
                                    className={`btn btn-correct ${ruleLabel === "correct"
                                        ? "btn-selected"
                                        : ""
                                        }`}
                                    onClick={() => handleLabeling("correct")}
                                >
                                    CONFIRM RULE
                                </button>
                                <button
                                    className={`btn btn-incorrect ${ruleLabel === "not_a_rule"
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
