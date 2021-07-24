import "./LabelingScreen.css";
import "react-grid-layout/css/styles.css";
import "react-resizable/css/styles.css";
import Prism from "prismjs";
import { useEffect, useState, useRef } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";
import Editor from "react-simple-code-editor";
import { highlight, languages } from "prismjs/components/prism-core";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-java";
import "prismjs/themes/prism.css";
import MonacoEditor from "react-monaco-editor";

import { getNextRuleToLabel, getPreviousRuleToLabel } from "./helper";
import TextualRuleEditor from "./TextualRuleEditor";

function LabelingScreen() {
    const [grammarText, setGrammarText] = useState("");
    const [oldDecorations, setNewDecorations] = useState([])

    useEffect(() => {
        const rule = getNextRuleToLabel();
        if (rule != null) {
            updateFields(rule);
        } else {
            updateFields({
                grammar: "",
                ruleCode: "",
                compliantExamples: [""],
                nonCompliantExamples: [""],
                label: null,
            });
        }
    }, []);

    const [code, setRuleCode] = useState("");
    const [compliant, setCompliantCode] = useState("");
    const [nonCompliant, setNonCompliantCode] = useState("");
    const [ruleLabel, setRuleLabel] = useState(null);
    const [editorData, setEditor] = useState(null);

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

    const getNextRule = () => {
        updateFields(getNextRuleToLabel());
    };

    const getPrevRule = () => {
        updateFields(getPreviousRuleToLabel());
    };

    const editorDidMount = (editor, monaco) => {
        // const r = new monaco.Range(2, 1, 2, 10);
        // editor.deltaDecorations(
        //     [],
        //     [
        //         {
        //             range: r,
        //             options: {
        //                 inlineClassName: "myInlineDecoration",
        //             },
        //         },
        //     ]
        // );
        setEditor({editor, monaco})
    };

    const newCodeEditor = (value, onValueChange, disabled = false) => {
        return (
            <>
                <h4
                    style={{
                        color: "white",
                    }}
                >
                    Foo.java
                </h4>
                <MonacoEditor
                    width={800}
                    height={400}
                    language="java"
                    theme="vs-light"
                    value={value}
                    // options={{
                    //     readOnly: disabled,
                    //     folding: false,
                    //     formatOnType: true,
                    //     formatOnPaste: true,
                    // }}
                    onChange={onValueChange}
                    editorDidMount={editorDidMount}
                />
            </>
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

    const updateStuff = (text) => {
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

                    const codeText = code.map((e) => e[0]).join("\n")
                    const ranges = code.map((e) => e[1]).flat()

                    const {editor, monaco} = editorData;

                    const rangez = ranges.map((rangeData) => {
                        const row = rangeData[0] + 1
                        const s = rangeData[1] + 1
                        const e = rangeData[2] + 1
                        const isAntecedent = rangeData[3] === "["
                        const r = new monaco.Range(row, s, row, e);
                        return {
                            range: r,
                            options: { inlineClassName: isAntecedent ? "antecedent" : "consequent"},
                        }
                    })

                    const newDecorations = editor.deltaDecorations(
                        oldDecorations,
                        rangez
                    );

                    setNewDecorations(newDecorations);

                    setRuleCode(codeText.trim());
                }
            });
    };

    return (
        <div className="flautas">
            <div className="code-example">
                <div className="code-snippet-sidebar">
                    {newCodeEditor(code, (value) => {
                        setRuleCode(value);
                        
                    })}
                </div>
            </div>

            <div className="code-desc-container">
                <div className="code-description">
                    <TextualRuleEditor
                        text={grammarText}
                        onChange={(text) => updateStuff(text)}
                    />
                </div>
                <div className="code-snippet-examples">
                    <div className="correct">
                        <h1>Compliant</h1>
                        {codeEditor(compliant, setRuleCode, true)}
                    </div>
                    <div className="violation">
                        <h1>Non-compliant</h1>
                        {codeEditor(nonCompliant, setRuleCode, true)}
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
                            CORRECT
                        </button>
                        <button
                            className={`btn best-practice ${
                                ruleLabel === "best_practice"
                                    ? "btn-selected"
                                    : ""
                            }`}
                            onClick={() => handleLabeling("best_practice")}
                        >
                            BEST PRACTICE
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
