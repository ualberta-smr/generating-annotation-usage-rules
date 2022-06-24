import antlr4 from 'antlr4';
import RulepadGrammarLexer from './RulepadGrammarLexer'
import RulepadGrammarParser from './RulepadGrammarParser'
import FormatterListener from './FormatterListener'
import VisualizerListener, { stringifyClass } from './VisualizerListener';

export default function prettify(input) {
    try {
        const chars = new antlr4.InputStream(onelineify(input));
        const lexer = new RulepadGrammarLexer(chars);
        const tokens = new antlr4.CommonTokenStream(lexer);
        const parser = new RulepadGrammarParser(tokens);
        parser.buildParseTrees = true;

        const tree = parser.start();
        const formatter = new FormatterListener();

        antlr4.tree.ParseTreeWalker.DEFAULT.walk(formatter, tree);

        return formatter.getFinalString();
    } catch (error) {
        console.error(error)
    }
    return input;

}

export function visualize(input) {
    try {
        const chars = new antlr4.InputStream(onelineify(input));
        const lexer = new RulepadGrammarLexer(chars);
        const tokens = new antlr4.CommonTokenStream(lexer);
        const parser = new RulepadGrammarParser(tokens);
        parser.buildParseTrees = true;

        const tree = parser.start();
        const visualizer = new VisualizerListener();
        antlr4.tree.ParseTreeWalker.DEFAULT.walk(visualizer, tree);
        const jc = visualizer.getJavaClass()
        return resultWrapper(stringifyClass(jc))
    } catch (error) {
        console.error(error)
        return resultWrapper(null)
    }
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

function resultWrapper(data) {
    if (data == null) {
        return {
            status: "failure",
            data: null
        }
    }
    return {
        status: "success",
        data: data
    }
}
