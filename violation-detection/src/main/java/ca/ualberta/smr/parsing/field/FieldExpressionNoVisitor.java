package ca.ualberta.smr.parsing.field;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.Field;
import lombok.val;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.acceptIfAvailable;

class FieldExpressionNoVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitDeclarationStatementExpressionNo(RulepadGrammarParser.DeclarationStatementExpressionNoContext ctx) {
        val types = CombinatorialWordsExtractorUtility.extractType(ctx.types());
        val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
        return AggregateCondition.not(new Field(types, annotations));
    }
}
