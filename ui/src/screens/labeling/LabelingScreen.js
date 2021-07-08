import "./LabelingScreen.css";
import "react-grid-layout/css/styles.css";
import "react-resizable/css/styles.css";
import Prism from "prismjs";
import ContentEditable from "react-contenteditable";
import { useEffect, useState } from "react";
import { FaArrowRight, FaArrowLeft } from "react-icons/fa";
import Editor from "react-simple-code-editor";
import { highlight, languages } from "prismjs/components/prism-core";
import "prismjs/components/prism-clike";
import "prismjs/components/prism-java";
import "prismjs/themes/prism.css";
import MonacoEditor from "react-monaco-editor";

import {
    getNextRuleToLabel,
    getPreviousRuleToLabel,
    highlightWords,
} from "./helper";
import TextualRuleEditor from "./TextualRuleEditor";

function LabelingScreen() {

    const [grammarText, setGrammarText] = useState("");

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
                    height={300}
                    language="java"
                    theme="vs-dark"
                    value={value}
                    options={{
                        readOnly: disabled,
                        folding: false,
                    }}
                    onChange={onValueChange}
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

    

    return (
        <div className="flautas">
            <div className="code-example">
                <div className="code-snippet-sidebar">
                    {newCodeEditor(code, setRuleCode)}
                </div>
            </div>

            <div className="code-desc-container">
                <div className="code-description">
                    <TextualRuleEditor text={grammarText}/>
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
