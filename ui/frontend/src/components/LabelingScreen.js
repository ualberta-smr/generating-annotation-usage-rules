import "./LabelingScreen.scss";
import { useEffect, useState } from "react";
import { FaArrowRight, FaArrowLeft, FaQuestionCircle } from "react-icons/fa";

import FieldsetWrapper from "./FieldsetWrapper";
import RuleAuthoringEditor from "./RuleAuthoringEditor";
import makeCancellablePromise from "./superPromise";
import CodePreview from "./CodePreview";
import prettify, { onelineify } from "../grammar/formatter";
import { BACKEND_URL, LS_USERNAME, TUTORIAL_URL } from "./constants";
import { visualize } from "../grammar/visualizer";

function LabelingScreen() {
    const [username] = useState(window.localStorage.getItem(LS_USERNAME));
    // this is a flag that represents if the current rule is a new rule or not
    // new rule here refers to the freshly retrieved rule from the server, without any edits
    // this is actually not a boolean flag but more like a representation of a change
    // every time there's a new rule, the flag is flipped
    // listening to its changes, we can run useEffect 
    const [isNewRule, setIsNewRule] = useState(true);

    const [ruleMetaData, setRuleMetaData] = useState({
        id: null,
        name: 'Default package name',
        size: 0,
        totalLabeledRuleCount: 0
    });

    const [buttonAvailability, setButtonAvailability] = useState({
        hasPrev: false,
        hasNext: false,
    });
    const [grammarText, setGrammarText] = useState("");
    const [propertiesFileData, setPropertiesFileData] = useState();

    const [code, setRuleCode] = useState("");
    const [ruleLabel, setRuleLabel] = useState(null);

    const handleLabeling = (label) => {
        let newRuleLabel = ["correct", "best_practice", "not_a_rule"].includes(label)
            ? label
            : "unlabeled";

        /* 
            Basic idea is that if it is 'correct' already and you click the button again,
            it will be unlabeled...the same for 'not_a_rule' and 'best_practice' as well
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

        if (newRuleLabel === ruleLabel) {
            newRuleLabel = "unlabeled"
        } else if (newRuleLabel === "unlabeled") {
            return;
        }

        fetch(`${BACKEND_URL}/rules/${ruleMetaData.id}/${newRuleLabel}`, {
            method: "POST", ...requestOptions
        })
            .then((resp) => {
                if (resp.status === 200) {
                    setRuleLabel(newRuleLabel);
                }
                return resp.json()
            })
            .then((json) => {
                if (json) {
                    const { totalLabeledRuleCount } = json
                    setRuleMetaData({ ...ruleMetaData, totalLabeledRuleCount })
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

        const { id, ruleString, name, size, totalLabeledRuleCount } = data;

        setRuleMetaData({ id, name, size, totalLabeledRuleCount });
        setGrammarText(prettify(ruleString));
        processCodePreview(ruleString);
        setIsNewRule(!isNewRule);
    }

    const processCodePreview = (ruleString) => {
        const result = visualize(ruleString);

        if (result.status === "failure") return;
        
        const [codeText, configuration] = result.data;

        if (codeText) {
            setRuleCode(codeText.trim());
        }

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

    const getNextRule = () => {
        const id_str = ruleMetaData.id == null ? "" : `/${ruleMetaData.id}/next`;
        makeCancellablePromise(
            `${BACKEND_URL}/rules${id_str}?userId=${username}`,
            processRule
        );
    };

    const getPrevRule = () => {
        makeCancellablePromise(
            `${BACKEND_URL}/rules/${ruleMetaData.id}/prev?userId=${username}`,
            processRule
        );
    };

    const clearData = () => {
        setRuleCode("");
        setPropertiesFileData(null);
    };

    const updateRelatedFields = (text) => {
        setGrammarText(text);

        if (text.trim() === "") {
            clearData();
            return null;
        }

        const ruleString = onelineify(text);
        processCodePreview(ruleString)
    };

    const goToTutorialPage = () => {
        window.open(TUTORIAL_URL, '_blank').focus();
    }


    const showButton = (clazz, name, title) => {
        return (<button
            className={`btn btn-${clazz} ${ruleLabel === name
                ? "btn-selected"
                : ""
                }`}
            onClick={() => handleLabeling(name)}
        >
            {title}
        </button>)
    }

    const renderUI = () => {
        return (
            <div className="app-labeling">
                <div className="instructions-wrapper">
                    <div className="gap"></div>
                    <div className="instructions">
                        <h2>Candidate Rule {ruleMetaData.id}/{ruleMetaData.size} : {ruleMetaData.size - ruleMetaData.totalLabeledRuleCount} rules left to label ({username})</h2>
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
                    <div className="help-button-wrapper">
                        <button
                            onClick={() => goToTutorialPage()}
                        >
                            <span>
                                <FaQuestionCircle />
                            </span>
                        </button>
                    </div>
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
                            <CodePreview
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
                                        <CodePreview
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
                                {showButton("correct", "correct", "CONFIRM RULE")}
                                {showButton("best-practice", "best_practice", "BEST PRACTICE")}
                                {showButton("incorrect", "not_a_rule", "NOT A RULE")}
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
