import * as monaco from "monaco-editor/esm/vs/editor/editor.api";

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

    monaco.languages.registerDocumentFormattingEditProvider('shortRulepad', {
        provideDocumentFormattingEdits: function (model, options, token) {
            console.log(model)
            const getIndentLevel = (text) => {
                let level = 0;
                for (let ch of text) {
                    if (ch !== "\t") {
                        return level;
                    }
                    level++;
                }
                return level;
            }

            const tabs = (count) => {
                let res = "";
                for (let i = 0; i < count; i++) {
                    res += "\t"
                }
                return res;
            }

            const allText = model.getValue()

            let allTextFormatted = allText
                .replace("\nmust have\n", " must have ")
                .replaceAll("with\n\t", "with ")
                .replaceAll("\t", " ")
                .replaceAll("\n", " ");

            console.log(allTextFormatted);

            allTextFormatted = allText.replace(" must have ", "\nmust have\n");
            allTextFormatted = allTextFormatted.replaceAll("with ", "with\n\t")

            const partiallyFormattedLines = allTextFormatted.split("\n");

            for (let i = 0; i < partiallyFormattedLines.length; i++) {
                let currentLine = partiallyFormattedLines[i];
                if (i > 0) {
                    if (currentLine.includes("must have")) {
                        continue;
                    }

                    const prevIndentLevel = getIndentLevel(partiallyFormattedLines[i - 1]);
                    const curIndentLevel = getIndentLevel(currentLine);

                    if (prevIndentLevel + 1 !== curIndentLevel) {
                        partiallyFormattedLines[i] = `${tabs(prevIndentLevel + 1)}${currentLine.trim()} `;
                    }
                } else {
                    partiallyFormattedLines[i] = `${currentLine.trim()} `;
                }

            }

            model.setValue(partiallyFormattedLines.join("\n"));

            // actually does not have any effect
            const result = partiallyFormattedLines.map((line, ix) => {
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
    })

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
