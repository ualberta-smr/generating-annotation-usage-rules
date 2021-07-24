import MonacoEditor from "react-monaco-editor";
import { useState } from "react";

function TextualRuleEditor(props) {
    const [grammarText, setGrammarText] = useState(props.text);

    const handleChange = (text) => {
        setGrammarText(text);
        props.onChange(text)
    };

    const editorWillMount = (monaco) => {
        monaco.languages.register({
            id: "modernizer",
        });

        monaco.languages.setMonarchTokensProvider("modernizer", {
            tokenizer: {
                root: [
                    [/(class|annotation|function|declaration statement)/, "label-modern"],
                    [/(".+?")/, "str-modern"],
                    [/(must have)/, "must-have-modern"],
                ],
            },
        });

        monaco.editor.defineTheme("modernizer-th", {
            base: "vs",
            inherit: false,
            rules: [
                {
                    token: "label-modern",
                    foreground: "FF0000",
                    fontStyle: "bold",
                },
                {
                    token: "str-modern",
                    foreground: "6A8759",
                },
                {
                    token: "must-have-modern",
                    foreground: "0000FF"
                }
            ],
        });

        console.log(monaco);
    };

    return (
        <MonacoEditor
            width="90%"
            height="40%"
            value={props.text}
            options={{
                readOnly: false,
                folding: false,
                minimap: {
                    enabled: false,
                },
                lineNumbers: "off",
                wordWrap: "on",
            }}
            onChange={handleChange}
            // editorWillMount={editorWillMount}
            className="code-description-text"
        />
    );
};

export default TextualRuleEditor;
