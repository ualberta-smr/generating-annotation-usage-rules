package ca.ualberta.smr.grammar.visitor.function;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.grammar.visitor.annotation.AnnotationVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.Method;
import ca.ualberta.smr.newmodel.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.GeneralUtility.acceptIfAvailable;

class FunctionExpressionNoVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {
    @Override
    public AggregateCondition visitFunctionExpressionNo(RulepadGrammarParser.FunctionExpressionNoContext ctx) {
        val returnType = CombinatorialWordsExtractorUtility.extractReturnType(ctx.returnTypes());
        val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
        val parameters = acceptIfAvailable(ctx.functionParameters(), new FunctionParameterVisitor());
        return AggregateCondition.not(
                new Method(returnType, annotations, parameters), ProgramElement.ProgramElementType.METHOD
        );
    }
}
