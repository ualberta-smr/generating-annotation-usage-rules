package ca.ualberta.smr.grammar.visitor.field;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.CombinatorialWordsExtractorUtility;
import ca.ualberta.smr.grammar.visitor.annotation.AnnotationVisitor;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import ca.ualberta.smr.newmodel.javaelements.Field;
import ca.ualberta.smr.newmodel.javaelements.ProgramElement;
import lombok.val;

import static ca.ualberta.smr.grammar.visitor.GeneralUtility.acceptIfAvailable;

class FieldExpressionNoVisitor extends RulepadGrammarBaseVisitor<AggregateCondition> {

    @Override
    public AggregateCondition visitDeclarationStatementExpressionNo(RulepadGrammarParser.DeclarationStatementExpressionNoContext ctx) {
        val types = CombinatorialWordsExtractorUtility.extractType(ctx.types());
        val annotations = acceptIfAvailable(ctx.annotations(), new AnnotationVisitor());
        return AggregateCondition.not(
                new Field(types, annotations), ProgramElement.ProgramElementType.FIELD
        );
    }
}
