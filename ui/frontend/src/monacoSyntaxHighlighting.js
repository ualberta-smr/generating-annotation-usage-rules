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
