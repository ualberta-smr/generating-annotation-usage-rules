import "./ExperimentalLabelingScreen.scss";
import { useEffect, useState } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";
import Prism from "prismjs";
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
        text: "",
        name: "a.prop",
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

    const fieldSetWrap = (title, element) => {
        let legend = null;
        if (title.includes(":")) {
            const [editor, fileName] = title.split(":");
            legend = (
                <legend>
                    <strong>{editor.trim()}</strong>: <em>{fileName.trim()}</em>
                </legend>
            );
        } else {
            legend = (
                <legend>
                    <strong>{title}</strong>
                </legend>
            );
        }
        return (
            <fieldset>
                {legend}
                {element}
            </fieldset>
        );
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
        return fieldSetWrap(
            `Code editor: ${fileName}`,
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
                                {fieldSetWrap(
                                    "Rule Authoring Editor",
                                    <TextualRuleEditor
                                        text={grammarText}
                                        onChange={(text) =>
                                            updateRelatedFields(text)
                                        }
                                    />
                                )}
                            </div>
                        </div>
                        <div className="code-editors">
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
                </div>
                <div className="examples-and-controls-row">
                    <div className="examples">
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
