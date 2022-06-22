package ca.ualberta.smr.parsing.field;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.javaelements.Field;
import ca.ualberta.smr.parsing.annotation.AnnotationVisitor;
import lombok.val;
import org.antlr.v4.runtime.ParserRuleContext;

import static ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility.extractEnclosingClass;
import static ca.ualberta.smr.parsing.utils.CombinatorialWordsExtractorUtility.extractType;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.acceptIfAvailable;

public class FieldParsingUtils {

    public static Field createFieldFromCtx(ParserRuleContext generalCtx) {
        final RulepadGrammarParser.TypesContext typesContext;
        final RulepadGrammarParser.AnnotationsContext annotationsContext;
        final RulepadGrammarParser.EnclosingClassContext enclosingClassContext;

        if (generalCtx instanceof RulepadGrammarParser.DeclarationStatementExpressionContext) {
            val ctx = (RulepadGrammarParser.DeclarationStatementExpressionContext) generalCtx;
            typesContext = ctx.types();
            annotationsContext = ctx.annotations();
            enclosingClassContext = ctx.enclosingClass();
        } else if (generalCtx instanceof RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext) {
            val ctx = (RulepadGrammarParser.DeclarationStatementExpressionAggregateContentsContext) generalCtx;
            typesContext = ctx.types();
            annotationsContext = ctx.annotations();
            enclosingClassContext = ctx.enclosingClass();
        } else {
            // generalCtx instanceof RulepadGrammarParser.DeclarationStatementExpressionNoContext
            val ctx = (RulepadGrammarParser.DeclarationStatementExpressionNoContext) generalCtx;
            typesContext = ctx.types();
            annotationsContext = ctx.annotations();
            enclosingClassContext = ctx.enclosingClass();
        }

        val types = extractType(typesContext);
        val annotations = acceptIfAvailable(annotationsContext, new AnnotationVisitor());
        val enclosingClass = extractEnclosingClass(enclosingClassContext);

        return new Field(types, annotations, enclosingClass);
    }

}
