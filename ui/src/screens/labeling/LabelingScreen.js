import "./LabelingScreen.css";
import "react-grid-layout/css/styles.css";
import "react-resizable/css/styles.css";
import Prism from "prismjs";
import { useEffect, useState } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";
import Editor from "react-simple-code-editor";
import { highlight, languages } from "prismjs/components/prism-core";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-java";
import "prismjs/themes/prism.css";
import MonacoEditor from "react-monaco-editor";

import TextualRuleEditor from "./TextualRuleEditor";

function LabelingScreen() {
    const [grammarText, setGrammarText] = useState("");
    const [oldDecorations, setNewDecorations] = useState([]);
    const [propertiesFileData, setPropertiesFileData] = useState({
        text: "aa",
        name: "aa"
    });

    const [code, setRuleCode] = useState("");
    const [compliant, setCompliantCode] = useState("");
    const [nonCompliant, setNonCompliantCode] = useState("");
    const [ruleLabel, setRuleLabel] = useState(null);
    const [editorData, setEditor] = useState(null);

    useEffect(() => {
        updateFields({
            grammar: "",
            ruleCode: "",
            compliantExamples: [""],
            nonCompliantExamples: [""],
            label: null,
        });
    }, []);

    const updateFields = (rule) => {
        if (rule != null) {
            setGrammarText(rule.grammar);
            setRuleCode(rule.ruleCode);
            setCompliantCode(rule.compliantExamples[0]); // TODO: dangerous
            setNonCompliantCode(rule.nonCompliantExamples[0]); // TODO: dangerous
            setRuleLabel(rule.label);
        }
    };

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

    const newCodeEditor = (
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
            <fieldset
                style={{
                    color: "white",
                    border: "4px solid white",
                }}
            >
                <legend>
                    <strong>Code editor:</strong> <em>{fileName}</em>
                </legend>
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
            </fieldset>
        );
    };

    const codeEditor = (value, onValueChange, disabled = false) => {
        return (
            <Editor
                value={value}
                onValueChange={(code) => onValueChange(code)}
                highlight={(code) => highlight(code, languages.java)}
                padding={10}
                style={{
                    fontFamily: '"Fira code", "Fira Mono", monospace',
                }}
                className="code-snippet-textbar"
                disabled={disabled}
            />
        );
    };

    const updateRelatedFields = (text) => {
        setGrammarText(text);
        fetch(`http://localhost:5000/grammarToCode?grammar=${text}`)
            .then((response) => {
                const status = response.status;
                if (status === 200) {
                    return response.json();
                } else {
                    return null;
                }
            })
            .then((json) => {
                if (json == null) {
                    console.log("Error");
                } else {
                    const code = json.code;

                    const codeText = code.map((e) => e[0]).join("\n");
                    const ranges = code.map((e) => e[1]).flat();

                    const { editor, monaco } = editorData;

                    const rangez = ranges.map((rangeData) => {
                        const row = rangeData[0] + 1;
                        const s = rangeData[1] + 1;
                        const e = rangeData[2] + 1;
                        const isAntecedent = rangeData[3] === "[";
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
                        rangez
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
            });
    };

    return (
        <div className="flautas">
            <div className="code-example">
                <div className="instructions">
                    <h2>Candidate Rule 15</h2>
                    <fieldset
                        style={{
                            color: "white",
                            border: "4px solid white",
                        }}
                    >
                        <legend>
                            <strong>Instructions</strong>
                        </legend>
                        <p>
                            <em>
                                Edit the candidate rule as needed and then confirm
                                the rule once done. If the candidate rule is
                                completely not correct or not useful for
                                authoring a rule, click <strong>"Not rule"</strong>
                            </em>
                        </p>
                    </fieldset>
                </div>
                <div className="code-snippet-sidebar">
                    {newCodeEditor(code, (value) => {
                        setRuleCode(value);
                    })}
                    {propertiesFileData == null
                        ? null
                        : newCodeEditor(
                              propertiesFileData.text,
                              setRuleCode,
                              (a, b) => {},
                              propertiesFileData.name,
                              true,
                              null
                          )}
                </div>
            </div>

            <div className="code-desc-container">
                <div className="code-description">
                    <TextualRuleEditor
                        text={grammarText}
                        onChange={(text) => updateRelatedFields(text)}
                    />
                </div>
                <div className="code-snippet-examples">
                    <div className="correct">
                        <h1>Example of Complying Code</h1>
                        {codeEditor(
                            `class Foo   {
    @Fallback(fallbackMethod="doWhenFails")
    public void method() {}
}`,
                            setRuleCode,
                            true
                        )}
                    </div>
                    <div className="violation">
                        <h1>Example of Violation</h1>
                        {codeEditor(
                            `class Foo   {
    @Fallback
    public void method() {}
}`,
                            setRuleCode,
                            true
                        )}
                    </div>
                </div>
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
                                ruleLabel === "correct" ? "btn-selected" : ""
                            }`}
                            onClick={() => handleLabeling("correct")}
                        >
                            CONFIRM RULE
                        </button>
                        <button
                            className={`btn btn-incorrect ${
                                ruleLabel === "not_a_rule" ? "btn-selected" : ""
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
    );
}

export default LabelingScreen;
