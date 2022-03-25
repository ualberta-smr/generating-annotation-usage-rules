import antlr4 from 'antlr4';
import RulepadGrammarLexer from './RulepadGrammarLexer'
import RulepadGrammarParser from './RulepadGrammarParser'
import FormatterListener from './FormatterListener'

export default function prettify(input) {
    try {
        const chars = new antlr4.InputStream(onelineify(input));
        const lexer = new RulepadGrammarLexer(chars);
        const tokens = new antlr4.CommonTokenStream(lexer);
        const parser = new RulepadGrammarParser(tokens);
        parser.buildParseTrees = true;

        const tree = parser.inputSentence();
        const formatter = new FormatterListener();

        antlr4.tree.ParseTreeWalker.DEFAULT.walk(formatter, tree);
        return formatter.getFinalString();
    } catch (error) {
        console.error(error)
    }
    return input;

}

export function onelineify(input) {
    return input
        .replaceAll("\n", " ")
        .replaceAll("\t", " ")
        .replace(/\s\s+/g, ' ')
        .replaceAll("( ", "(")
        .replaceAll(")", " )")
        .trim() + " "
}

