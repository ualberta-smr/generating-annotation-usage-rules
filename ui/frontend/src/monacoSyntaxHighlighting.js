import * as monaco from "monaco-editor/esm/vs/editor/editor.api";
import prettify from "./grammar/formatter";

export default class ShortRulepad {

    constructor() {
        this.name = "shortRulepad"
        this.themeName = "shortRulepadTheme"
    }

    getTokenProvider() {
        return {
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

                    [/"[a-zA-Z0-9\s.\[\]\|]+"/, "srp-string"],
                ],
            },
        }
    }

    getThemeDefinition = () => {
        return {
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
        }
    }

    provideDocumentFormattingEdits(model, options, token) {
        const allText = model.getValue()
        const prettified = prettify(allText)

        model.setValue(prettified);

        // actually does not have any effect
        return prettified.split("\n").map((line, ix) => {
            return {
                range: new monaco.Range(
                    ix + 1, 1,
                    ix + 1, line.length
                ),
                text: line
            }
        })
    }

    register() {
        monaco.languages.register({ id: this.name });
        monaco.languages.setMonarchTokensProvider(this.name, this.getTokenProvider());
        monaco.languages.registerDocumentFormattingEditProvider(this.name, this)
        // Define a new theme that contains only rules that match this language
        monaco.editor.defineTheme(this.themeName, this.getThemeDefinition());
    }
}
