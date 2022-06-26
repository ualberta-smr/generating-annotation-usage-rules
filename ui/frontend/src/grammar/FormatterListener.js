import RulepadGrammarListener from './generated/RulepadGrammarListener'

export default class FormatterListener extends RulepadGrammarListener {

    constructor() {
        super()
        this.depth = 0
        this.finalString = ""

        // to make sure we do not put a tab between the opening parenthesis
        // and the next non-space character
        this.seenLPAREN = false;
    }

    getFinalString() {
        return this.finalString;
    }

    getPrefix() {
        let result = "\t".repeat(this.depth)
        if (this.seenLPAREN) {
            result = ""
            this.seenLPAREN = false;
        }
        return result;
    }

    openParenthesisIfRequired(ctx) {
        if (ctx.LPAREN() !== null) {
            this.finalString += this.getPrefix() + "("
            this.seenLPAREN = true; 
        }
        return ctx.LPAREN() !== null;
    }

    closeParenthesisIfRequired(ctx) {
        if (ctx.RPAREN() !== null) {
            this.finalString += ")"
        }
        return ctx.RPAREN() !== null
    }

    // Enter a parse tree produced by RulepadGrammarParser#must.
    enterMust(ctx) {
        this.finalString += "\nmust"
        this.depth = 0
    }

    // Enter a parse tree produced by RulepadGrammarParser#and_.
    enterAnd_(ctx) {
        this.finalString += `\n${this.getPrefix()}and\n`
    }

    // Enter a parse tree produced by RulepadGrammarParser#or_.
    enterOr_(ctx) {
        this.finalString += `\n${this.getPrefix()}or\n`
    }

    // Enter a parse tree produced by RulepadGrammarParser#have.
    enterHave(ctx) {
        this.finalString += " have\n"
        this.depth++;
    }


    // Enter a parse tree produced by RulepadGrammarParser#names.
	enterNames(ctx) {
        this.finalString += this.getPrefix() + ctx.getText()
	}

    // Enter a parse tree produced by RulepadGrammarParser#values.
	enterValues(ctx) {
        this.finalString += this.getPrefix() + ctx.getText()
	}


    // Enter a parse tree produced by RulepadGrammarParser#annotations.
    enterAnnotations(ctx) {
        this.finalString += this.getPrefix() + ctx.ANNOTATION().getText();
    }

    // Enter a parse tree produced by RulepadGrammarParser#annotationCondition.
    enterAnnotationCondition(ctx) {
        if (ctx.combinatorialWords() !== null) {
            this.finalString += ctx.combinatorialWords().getText() + " "
        }
    }


    // Enter a parse tree produced by RulepadGrammarParser#annotationConditionTransition.
    enterAnnotationConditionTransition(ctx) {
        this.finalString += ctx.withWord().getText() + "\n"
        this.depth++;
    }

    // Exit a parse tree produced by RulepadGrammarParser#annotationConditionTransition.
    exitAnnotationConditionTransition(ctx) {
        this.depth--;
    }


    // Enter a parse tree produced by RulepadGrammarParser#annotationExpression.
    enterAnnotationExpression(ctx) {
        if (this.openParenthesisIfRequired(ctx)) return;
    }

    // Exit a parse tree produced by RulepadGrammarParser#annotationExpression.
    exitAnnotationExpression(ctx) {
        if (this.closeParenthesisIfRequired(ctx)) return;
    }


    // Enter a parse tree produced by RulepadGrammarParser#extensions.
    enterExtensions(ctx) {
        this.finalString += this.getPrefix() + ctx.getText();
    }

    // Enter a parse tree produced by RulepadGrammarParser#implementations.
    enterImplementations(ctx) {
        this.finalString += this.getPrefix() + ctx.getText();
    }

    // Enter a parse tree produced by RulepadGrammarParser#overriddenFunctions.
    enterOverriddenFunctions(ctx) {
        const methodSignature = ctx.combinatorialWords().getText().replaceAll('"', "")
        // Example: foobar(String, int, double, Custom)
        // Example: foobar(String)
        // Example: foobar()
        const lparenPos = methodSignature.indexOf("(");
        const rparenPos = methodSignature.lastIndexOf(")");
        if (lparenPos === -1 || rparenPos === -1) {
            // error
        } else {
            const methodName = methodSignature.slice(0, lparenPos);
            const parameters = methodSignature
                                    .slice(lparenPos + 1, rparenPos)
                                    .split(",")
                                    .map(e => e.trim())
                                    .filter(e => e.length > 0)
                                    .join(", ")
            this.finalString += this.getPrefix() + ctx.OVERRIDDEN_FUNCTION().getText() + `"${methodName}(${parameters})"`;
        }
    }

    // Enter a parse tree produced by RulepadGrammarParser#functions.
    enterFunctions(ctx) {
        this.finalString += this.getPrefix() + ctx.FUNCTION().getText()
        this.depth++;
    }

    // Exit a parse tree produced by RulepadGrammarParser#functions.
    exitFunctions(ctx) {
        this.depth--;
    }


    // Enter a parse tree produced by RulepadGrammarParser#functionCondition.
    enterFunctionCondition(ctx) {
        this.finalString += ctx.withWord().getText() + "\n"
    }


    // Enter a parse tree produced by RulepadGrammarParser#functionExpression.
    enterFunctionExpression(ctx) {
        if (this.openParenthesisIfRequired(ctx)) return;
    }

    // Exit a parse tree produced by RulepadGrammarParser#functionExpression.
    exitFunctionExpression(ctx) {
        if (this.closeParenthesisIfRequired(ctx)) return;
    }


    // Enter a parse tree produced by RulepadGrammarParser#parameters.
    enterAnnotationParameters(ctx) {
        this.finalString += this.getPrefix() + ctx.PARAMETER().getText()
    }

    // Enter a parse tree produced by RulepadGrammarParser#parameterCondition.
    enterAnnotationParameterCondition(ctx) {
        if (ctx.combinatorialWords() !== null) {
            this.finalString += ctx.combinatorialWords().getText() + " ";
        }
    }

    enterAnnotationParameterConditionTransition(ctx) {
        this.finalString += ctx.withWord().getText() + "\n";
        this.depth++;
    }

    exitAnnotationParameterConditionTransition(ctx) {
        this.depth--;
    }

    // Enter a parse tree produced by RulepadGrammarParser#parameterExpression.
    enterAnnotationParameterExpression(ctx) {
        if (this.openParenthesisIfRequired(ctx)) return;
    }

    // Exit a parse tree produced by RulepadGrammarParser#parameterExpression.
    exitAnnotationParameterExpression(ctx) {
        if (this.closeParenthesisIfRequired(ctx)) return;
    }


    // Enter a parse tree produced by RulepadGrammarParser#functionParameters.
    enterFunctionParameters(ctx) {
        this.finalString += this.getPrefix() + ctx.PARAMETER().getText()
    }

    // Enter a parse tree produced by RulepadGrammarParser#functionParameterCondition.
    enterFunctionParameterCondition(ctx) {
        if (ctx.combinatorialWords() !== null) {
            this.finalString += ctx.combinatorialWords().getText() + " ";
        }
    }

    // Enter a parse tree produced by RulepadGrammarParser#functionParameterConditionTransition.
    enterFunctionParameterConditionTransition(ctx) {
        this.finalString += ctx.withWord().getText() + "\n";
        this.depth++;
    }

    // Exit a parse tree produced by RulepadGrammarParser#functionParameterConditionTransition.
    exitFunctionParameterConditionTransition(ctx) {
        this.depth--;
    }


    // Enter a parse tree produced by RulepadGrammarParser#functionParameterExpression.
    enterFunctionParameterExpression(ctx) {
        if (this.openParenthesisIfRequired(ctx)) return;
    }

    // Exit a parse tree produced by RulepadGrammarParser#functionParameterExpression.
    exitFunctionParameterExpression(ctx) {
        if (this.closeParenthesisIfRequired(ctx)) return;
    }


    // Enter a parse tree produced by RulepadGrammarParser#types.
    enterTypes(ctx) {
        this.finalString += this.getPrefix() + ctx.TYPES().getText()
        const cond = ctx.typeCondition();
        if (cond != null) {
            if (cond.combinatorialWords() != null) {
                this.finalString += `${cond.combinatorialWords().getText()} `
            }
        }
    }

    // Enter a parse tree produced by RulepadGrammarParser#returnTypes.
    enterReturnTypes(ctx) {
        this.finalString += this.getPrefix() + ctx.RETURN_TYPES().getText()
        const cond = ctx.returnTypeCondition();
        if (cond != null) {
            if (cond.combinatorialWords() != null) {
                this.finalString += `${cond.combinatorialWords().getText()} `
            }
        }
    }


    // Enter a parse tree produced by RulepadGrammarParser#declarationStatements.
    enterDeclarationStatements(ctx) {
        const prefix = this.getPrefix()
        this.finalString += prefix + ctx.DeclarationStatement().getText()
        this.depth++;
    }

    // Exit a parse tree produced by RulepadGrammarParser#declarationStatements.
    exitDeclarationStatements(ctx) {
        this.depth--;
    }

    // Enter a parse tree produced by RulepadGrammarParser#declarationStatementCondition.
    enterDeclarationStatementCondition(ctx) {
        this.finalString += ctx.withWord().getText() + "\n"
    }

    // Enter a parse tree produced by RulepadGrammarParser#declarationStatementExpression.
    enterDeclarationStatementExpression(ctx) {
        if (this.openParenthesisIfRequired(ctx)) return;
    }

    // Exit a parse tree produced by RulepadGrammarParser#declarationStatementExpression.
    exitDeclarationStatementExpression(ctx) {
        if (this.closeParenthesisIfRequired(ctx)) return;
    }

    // Enter a parse tree produced by RulepadGrammarParser#configurationFiles.
    enterConfigurationFiles(ctx) {
        this.finalString += this.getPrefix() + ctx.ConfigurationFile().getText();
    }

    // Enter a parse tree produced by RulepadGrammarParser#configurationFileCondition.
    enterConfigurationFileCondition(ctx) {
        this.finalString += ctx.withWord().getText() + "\n";
        this.depth++;
    }

    exitConfigurationFileCondition(ctx) {
        this.depth--;
    }

    // Enter a parse tree produced by RulepadGrammarParser#configurationFileExpression.
    enterConfigurationFileExpression(ctx) {
        if (this.openParenthesisIfRequired(ctx)) return;
    }

    // Exit a parse tree produced by RulepadGrammarParser#configurationFileExpression.
    exitConfigurationFileExpression(ctx) {
        if (this.closeParenthesisIfRequired(ctx)) return;
    }


    // Enter a parse tree produced by RulepadGrammarParser#configurationProperties.
    enterConfigurationProperties(ctx) {
        this.finalString += this.getPrefix() + ctx.CONFIGURATION_PROPERTIES().getText();
    }

    // Enter a parse tree produced by RulepadGrammarParser#configurationPropertyCondition.
    enterConfigurationPropertyCondition(ctx) {
        if (ctx.combinatorialWords() != null) {
            this.finalString += ctx.combinatorialWords().getText() + " ";
        }
    }

    enterConfigurationPropertyConditionTransition(ctx) {
        this.finalString += ctx.withWord().getText() + "\n";
        this.depth++;
    }

    exitConfigurationPropertyConditionTransition(ctx) {
        this.depth--;   
    }


    // Enter a parse tree produced by RulepadGrammarParser#configurationPropertyExpression.
    enterConfigurationPropertyExpression(ctx) {
        if (this.openParenthesisIfRequired(ctx)) return;
    }

    // Exit a parse tree produced by RulepadGrammarParser#configurationPropertyExpression.
    exitConfigurationPropertyExpression(ctx) {
        if (this.closeParenthesisIfRequired(ctx)) return;
    }


    // Enter a parse tree produced by RulepadGrammarParser#classes.
    enterClasses(ctx) {
        this.finalString += this.getPrefix() + ctx.CLASSES().getText();
    }


    // Enter a parse tree produced by RulepadGrammarParser#classCondition.
    enterClassCondition(ctx) {
        this.finalString += ctx.withWord().getText() + "\n";
        this.depth++;
    }

    // Exit a parse tree produced by RulepadGrammarParser#classCondition.
    exitClassCondition(ctx) {
        this.depth--;
    }


    // Enter a parse tree produced by RulepadGrammarParser#classExpression.
    enterClassExpression(ctx) {
        if (this.openParenthesisIfRequired(ctx)) return;
    }

    // Exit a parse tree produced by RulepadGrammarParser#classExpression.
    exitClassExpression(ctx) {
        if (this.closeParenthesisIfRequired(ctx)) return;
    }

    enterBeans(ctx) {
        this.finalString += this.getPrefix() + ctx.BEAN_DECL().getText();
    }

    enterBeansFile(ctx) {
        this.finalString += this.getPrefix() + ctx.BEANS_FILE().getText();
    }

    // Aggregates start
    enterClassExpressionNoneOf(ctx) {
        this.handleEnterAggregateOf(ctx, ctx => ctx.NONE_OF())
    }

    exitClassExpressionNoneOf(ctx) {
        this.handleExitAggregateOf()
    }

    enterClassExpressionOneOf(ctx) {
        this.handleEnterAggregateOf(ctx, ctx => ctx.ONE_OF())
    }

    exitClassExpressionOneOf(ctx) {
        this.handleExitAggregateOf()
    }

    enterClassExpressionNo(ctx) {
        this.finalString += this.getPrefix() + ctx.NO().getText().trim();
    }

    enterFunctionExpressionNoneOf(ctx) {
        this.handleEnterAggregateOf(ctx, ctx => ctx.NONE_OF())
    }

    exitFunctionExpressionNoneOf(ctx) {
        this.handleExitAggregateOf()
    }

    enterFunctionExpressionOneOf(ctx) {
        this.handleEnterAggregateOf(ctx, ctx => ctx.ONE_OF())
    }

    exitFunctionExpressionOneOf(ctx) {
        this.handleExitAggregateOf()
    }

    enterFunctionExpressionNo(ctx) {
        this.finalString += this.getPrefix() + ctx.NO().getText().trim();
    }

    enterDeclarationStatementExpressionNoneOf(ctx) {
        this.handleEnterAggregateOf(ctx, ctx => ctx.NONE_OF())
    }

    exitDeclarationStatementExpressionNoneOf(ctx) {
        this.handleExitAggregateOf()
    }

    enterDeclarationStatementExpressionOneOf(ctx) {
        this.handleEnterAggregateOf(ctx, ctx => ctx.ONE_OF())
    }

    exitDeclarationStatementExpressionOneOf(ctx) {
        this.handleExitAggregateOf()
    }

    enterDeclarationStatementExpressionNo(ctx) {
        this.finalString += this.getPrefix() + ctx.NO().getText().trim();
    }

    handleEnterAggregateOf(ctx, keywordSelector) {
        this.finalString += this.getPrefix() + keywordSelector(ctx).getText() + "(";
        this.finalString += "\n"
        this.depth++;
    }

    handleExitAggregateOf() {
        this.finalString += ")"
        this.depth--;
    }
    // Aggregates end

    enterEnclosingClass(ctx) {
        this.finalString += this.getPrefix() + ctx.ENCLOSING_CLASS().getText();
    }

}