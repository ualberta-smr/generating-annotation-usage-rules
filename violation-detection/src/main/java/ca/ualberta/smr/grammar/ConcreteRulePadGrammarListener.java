package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import lombok.RequiredArgsConstructor;

import java.util.Stack;

import static ca.ualberta.smr.model.javaelements.Condition.single;

@RequiredArgsConstructor
class Data {
    final NodeType comingFrom;
    final ProgramElement node;

}

enum NodeType {
    CLASS, METHOD, FIELD, PARAMETER, ANNOTATION, CONSTRUCTOR
}

public class ConcreteRulePadGrammarListener extends AbstractRulePadGrammarListener{

    private Stack<Data> stack;
    private AnalysisItem antecedent;
    private Condition<? extends AnalysisItem> consequent;

    public ConcreteRulePadGrammarListener() {
        // TODO: init stuff here
        this.stack = new Stack<>();
        this.antecedent = null;
        this.consequent = null;
    }

    public StaticAnalysisRule getRule() {
        return new StaticAnalysisRule("", antecedent, consequent);
    }

    @Override
    public void enterClasses(RulepadGrammarParser.ClassesContext ctx) {
        // only indication that we are in the antecedent part
        // as there are no rules that have class as the consequent
        final JavaClass javaClass = new JavaClass();
        if (stack.isEmpty()) {
            this.stack.push(new Data(NodeType.CLASS, javaClass));
        }
    }

    @Override
    public void exitClasses(RulepadGrammarParser.ClassesContext ctx) {
        this.stack.pop();
    }

    @Override
    public void enterDeclarationStatements(RulepadGrammarParser.DeclarationStatementsContext ctx) {
        final Data data = stack.peek();
        final Field field = new Field();
        if (data.comingFrom == NodeType.CLASS) {
            JavaClass klass = (JavaClass) data.node;
            klass.field(single(field));
        }
    }
}
