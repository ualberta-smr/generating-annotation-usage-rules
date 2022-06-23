import * as monaco from "monaco-editor/esm/vs/editor/editor.api";
import lookup from "./classNameDatabase";
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
                    [/return/, "srp-keyword"],
                    [/name/, "srp-keyword"],
                    [/value/, "srp-keyword"],
                    [/extension of/, "srp-keyword"],
                    [/implementation of/, "srp-keyword"],
                    [/property/, "srp-keyword"],
                    [/configuration file/, "srp-keyword"],
                    [/bean declaration/, "srp-keyword"],
                    [/beans file/, "srp-keyword"],

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

        model.pushEditOperations(
            [],
            [{ range: model.getFullModelRange(), text: prettified }],
            () => null
        );

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

    newTextSuggestion(obj, range) {
        return {
            kind: monaco.languages.CompletionItemKind.Text,
            insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
            range: range,
            ...obj
        }
    };

    __getAllSuggestions(range) {
        const newSuggestion = (obj) => {
            return {
                kind: monaco.languages.CompletionItemKind.Function,
                insertTextRules: monaco.languages.CompletionItemInsertTextRule.InsertAsSnippet,
                range: range,
                ...obj
            }
        };

        return [
            newSuggestion({
                label: 'conf',
                documentation: 'configuration property autocomplete',
                insertText: 'configuration file with property "${1}"',
            }),
            newSuggestion({
                label: 'ann',
                documentation: 'annotation',
                insertText: 'annotation "${1}"',
            }),
            newSuggestion({
                label: 'impl',
                documentation: 'implementation',
                insertText: 'implementation of "${1}"',
            }),
            newSuggestion({
                label: 'ext',
                documentation: 'extension',
                insertText: 'extension of "${1}"',
            }),
            newSuggestion({
                label: 'bean',
                documentation: 'bean declaration ${1}',
                insertText: 'bean declaration',
            }),
            newSuggestion({
                label: 'beans',
                documentation: 'beans file ${1}',
                insertText: 'beans file',
            }),
            newSuggestion({
                label: 'ret',
                documentation: 'return type',
                insertText: 'return type "${1}"',
            })
        ]
    }

    provideCompletionItems(model, position) {
        const word = model.getWordUntilPosition(position);

        const range = {
            startLineNumber: position.lineNumber,
            endLineNumber: position.lineNumber,
            startColumn: word.startColumn,
            endColumn: word.endColumn
        }

        const isSurroundedByQuotes = this.__isCursorBetweenQuotes(model, position)

        if (isSurroundedByQuotes) {
            const suggestions = lookup(word.word)
                .map(result => this.__createNewTextSuggestion(result, range))

            return { suggestions }
        }

        return {
            suggestions: this.__getAllSuggestions(range)
        }
    }

    __createNewTextSuggestion = ({ label, simpleName, fullyQualifiedName }, range) => this.newTextSuggestion({
        label: label,
        insertText: fullyQualifiedName,
        filterText: simpleName,
        sortText: simpleName,
    }, range);
    

    __isCursorBetweenQuotes(model, position) { // cursor is zero-based
        const [cursorStart, cursorEnd] = [position.column - 2, position.column - 1];

        const allText = model.getValue()
        const line = allText.split("\n")[position.lineNumber - 1]

        const pos = []
        for (let i = 0; i < line.length; i++) {
            if (line[i] == "\"") {
                pos.push(i);
            }
        }

        for (let i = 0; i < pos.length; i += 2) {
            const start = pos[i]
            const end = pos[i + 1]
            if (cursorStart >= start && cursorEnd <= end) {
                return true;
            }
        }
        return false;
    }
    
    register() {
        monaco.languages.register({ id: this.name });
        monaco.languages.setMonarchTokensProvider(this.name, this.getTokenProvider());
        monaco.languages.registerDocumentFormattingEditProvider(this.name, this);
        monaco.languages.registerCompletionItemProvider(this.name, this)
        // Define a new theme that contains only rules that match this language
        monaco.editor.defineTheme(this.themeName, this.getThemeDefinition());
    }
}
