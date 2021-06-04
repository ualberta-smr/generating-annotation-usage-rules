let antlr4 = require("antlr4");

let Traverse = require("./generateXpath").GenerateXPath;

/**
 * verify the text entered in AutoComplete based on Grammar
 */
 exports.verifyTextBasedOnGrammar = async function verifyTextBasedOnGrammar(autoCompleteText) {
    let returnedObj = antlr(autoCompleteText);
    if (returnedObj.hasOwnProperty("grammarErrors") || returnedObj.hasOwnProperty("xpathTraverseErrors"))
        return Promise.reject(returnedObj);
    return {
        quantifierXPath: returnedObj.results.quantifier,
        constraintXPath: returnedObj.results.constraint,
        grammarTree: returnedObj.grammarTree,
    };
}


/**
 * check the text against grammar and returns the XPaths for quantifier and constraint
 * @param input
 * @returns {*} {"quantifier": xpath, "constraint": xpath}
 */
exports.antlr = (input) => {

    let inputText = input + "";
    let MyGrammarLexerModule = require("./generated-parser/myGrammarLexer");
    let MyGrammarParserModule = require("./generated-parser/myGrammarParser");

    let ErrorListener = function (errors) {
        antlr4.error.ErrorListener.call(this);
        this.errors = errors;
        return this;
    };

    ErrorListener.prototype = Object.create(antlr4.error.ErrorListener.prototype);
    ErrorListener.prototype.constructor = ErrorListener;
    ErrorListener.prototype.syntaxError = function (rec, sym, line, col, msg, e) {
        this.errors.push({rec: rec, sym: sym, line: line, col: col, msg: msg, e: e});
    };

    let errors = [];
    let listener = new ErrorListener(errors);

    let orgParser = new MyGrammarParserModule.myGrammarParser(new antlr4.CommonTokenStream(new MyGrammarLexerModule.myGrammarLexer(new antlr4.InputStream(input))));
    orgParser.buildParseTrees = true;
    orgParser.removeErrorListeners();
    orgParser.addErrorListener(listener);
    let orgTree = orgParser.inputSentence();

    let chars = new antlr4.InputStream(input);
    let lexer = new MyGrammarLexerModule.myGrammarLexer(chars);
    let tokens = new antlr4.CommonTokenStream(lexer);
    let parser = new MyGrammarParserModule.myGrammarParser(tokens);
    parser.buildParseTrees = true;

    parser.removeErrorListeners();
    parser.addErrorListener(listener);
    let tree = parser.inputSentence();

    if (errors.length !== 0)
        return {grammarErrors: errors, inputText: inputText};

    try {
        let traverse = new Traverse(tree);
        traverse.traverseTree();

        return {results: {quantifier: traverse.XPathQ, constraint: traverse.XPathC}, grammarTree: orgTree};
    }
    catch (error) {
        console.log(error);
        return {xpathTraverseErrors: error};
    }
};

/**
 * parse the input text without constraint
 * used in minedRules
 * @param input text based on grammar without constraint only from "classes" tokens
 * @return {{grammarTree: *}|{grammarErrors: Array, inputText: string}}
 */
exports.verifyPartialTextBasedOnGrammar = verifyPartialTextBasedOnGrammar = (input) => {

    let MyGrammarLexerModule = require("./generated-parser/myGrammarLexer");
    let MyGrammarParserModule = require("./generated-parser/myGrammarParser");

    let ErrorListener = function (errors) {
        antlr4.error.ErrorListener.call(this);
        this.errors = errors;
        return this;
    };

    ErrorListener.prototype = Object.create(antlr4.error.ErrorListener.prototype);
    ErrorListener.prototype.constructor = ErrorListener;
    ErrorListener.prototype.syntaxError = function (rec, sym, line, col, msg, e) {
        this.errors.push({rec: rec, sym: sym, line: line, col: col, msg: msg, e: e});
    };

    let errors = [];
    let listener = new ErrorListener(errors);

    let orgParser = new MyGrammarParserModule.myGrammarParser(new antlr4.CommonTokenStream(new MyGrammarLexerModule.myGrammarLexer(new antlr4.InputStream(input))));
    orgParser.buildParseTrees = true;
    orgParser.removeErrorListeners();
    orgParser.addErrorListener(listener);
    let orgTree = orgParser.classes();

    if (errors.length !== 0)
        return {grammarErrors: errors, error: true, listOfErrors: errors};

    return {grammarTree: orgTree, error: false};

};