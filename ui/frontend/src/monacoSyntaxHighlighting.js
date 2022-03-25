import * as monaco from "monaco-editor/esm/vs/editor/editor.api";
import prettify from "./grammar/formatter";

export class RulepadFormatter {

    getIndentLevel (text) {
        let level = 0;
        for (let ch of text) {
            if (ch !== "\t") {
                return level;
            }
            level++;
        }
        return level;
    }

    tabs(count) {
        let res = "";
        for (let i = 0; i < count; i++) {
            res += "\t"
        }
        return res;
    }

    provideDocumentFormattingEdits (model, options, token) {
        const allText = model.getValue()
        const prettified = prettify(allText)

        model.setValue(prettified);

        // actually does not have any effect
        const result = prettified.split("\n").map((line, ix) => {
            return {
                range: new monaco.Range(
                    ix + 1, 1,
                    ix + 1, line.length
                ),
                text: line
            }
        })


        return result;
    }

}

export default function registerSyntaxHighlighting() {
    monaco.languages.register({ id: "shortRulepad" });

    monaco.languages.setMonarchTokensProvider("shortRulepad", {
        tokenizer: {
            root: [
                [/annotation/, "srp-keyword"],
                [/class/, "srp-keyword"],
                [/field/, "srp-keyword"],
                [/function/, "srp-keyword"],
                [/method/, "srp-keyword"],
                [/parameter/, "srp-keyword"],
                [/type/, "srp-keyword"],
                [/name/, "srp-keyword"],
                [/extension/, "srp-keyword"],
                [/implementation/, "srp-keyword"],
                [/property/, "srp-keyword"],
                [/configuration file/, "srp-keyword"],

                [/must have/, "srp-must-have"],
                [/with/, "srp-with"],

                [/"[a-zA-Z0-9\s.]+"/, "srp-string"],
            ],
        },
    });

    monaco.languages.registerDocumentFormattingEditProvider('shortRulepad', new RulepadFormatter())

    // Define a new theme that contains only rules that match this language
    monaco.editor.defineTheme("shortRulePadTheme", {
        base: "vs",
        inherit: false,
        rules: [
            { token: "srp-keyword", fontStyle: "italic", foreground: "0000ff" },
            { token: "srp-must-have", fontStyle: "bold", foreground: "ff0000" },
            { token: "srp-with", fontStyle: "bold", foreground: "ff0000" },
            {
                token: "srp-string",
                fontStyle: "bold italic",
                foreground: "008000",
            },
        ],
    });
}
