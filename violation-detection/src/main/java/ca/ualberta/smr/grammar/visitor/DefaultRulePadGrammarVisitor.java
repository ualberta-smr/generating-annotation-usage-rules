package ca.ualberta.smr.grammar.visitor;

import ca.ualberta.grammar.RulepadGrammarBaseVisitor;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.clazz.ClassExpressionVisitor;
import ca.ualberta.smr.grammar.visitor.field.FieldExpressionVisitor;
import ca.ualberta.smr.grammar.visitor.function.FunctionExpressionVisitor;
import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.val;
import org.antlr.v4.runtime.tree.ParseTree;

@RequiredArgsConstructor
@Getter
public class DefaultRulePadGrammarVisitor extends RulepadGrammarBaseVisitor<StaticAnalysisRule> {

    private final String ruleName;
    private final String ruleDescription;

    @Override
    public StaticAnalysisRule visit(ParseTree tree) {
        val mustClause = ((RulepadGrammarParser.InputSentenceContext) tree).mustClause();
        return this.visitMustClause(mustClause);
    }

    @Override
    public StaticAnalysisRule visitMustClause(RulepadGrammarParser.MustClauseContext ctx) {
        if (ctx.functions() != null) {
            val antecedent = ctx
                    .functions()
                    .functionCondition()
                    .functionExpression()
                    .accept(new FunctionExpressionVisitor());
            val consequent = ctx
                    .functionExpression()
                    .accept(new FunctionExpressionVisitor());
            return new StaticAnalysisRule(this.ruleName, antecedent, consequent, this.ruleDescription);
        }

        if (ctx.declarationStatements() != null) {
            val antecedent = ctx
                    .declarationStatements()
                    .declarationStatementCondition()
                    .declarationStatementExpression()
                    .accept(new FieldExpressionVisitor());

            val consequent = ctx
                    .declarationStatementExpression()
                    .accept(new FieldExpressionVisitor());
            return new StaticAnalysisRule(this.ruleName, antecedent, consequent, this.ruleDescription);
        }

        if (ctx.classes() != null) {
            val antecedent = ctx
                    .classes()
                    .classCondition()
                    .classExpression()
                    .accept(new ClassExpressionVisitor());

            val consequent = ctx
                    .classExpression()
                    .accept(new ClassExpressionVisitor());

            return new StaticAnalysisRule(this.ruleName, antecedent, consequent, this.ruleDescription);
        }

        return null;
    }
}

