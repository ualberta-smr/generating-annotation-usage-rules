package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import lombok.RequiredArgsConstructor;
import lombok.ToString;
import lombok.val;

import java.util.List;
import java.util.Stack;

import static ca.ualberta.smr.model.javaelements.Condition.single;
import static ca.ualberta.smr.utils.Utils.listOf;

@RequiredArgsConstructor
@ToString
class Data {
    final NodeType comingFrom;
    final ProgramElement node;
}

enum NodeType {
    CLASS, METHOD, FIELD, METHOD_PARAMETER, ANNOTATION, ANNOTATION_PARAMETER, CONSTRUCTOR, _OR_
}

public class ConcreteRulePadGrammarListener extends AbstractRulePadGrammarListener {

    private final Stack<Data> stack;
    private AnalysisItem antecedent;
    private Condition<? extends AnalysisItem> consequent;

    private Data initialItem;
    private ProgramElement previousCompleteElement;

    private final String name;

    public ConcreteRulePadGrammarListener(String name) {
        // TODO: init stuff here
        this.stack = new Stack<>();
        this.antecedent = null;
        this.consequent = null;
        this.initialItem = null;
        this.previousCompleteElement = null;
        this.name = name;
    }

    public StaticAnalysisRule getRule() {
        return new StaticAnalysisRule(name, antecedent, consequent);
    }

    @Override
    public void enterClasses(RulepadGrammarParser.ClassesContext ctx) {
        final JavaClass javaClass = new JavaClass();
        if (initialItem == null) {
            initialItem = new Data(NodeType.CLASS, javaClass);
        } else {
            // TODO: this part will be useful when handling "enclosing class" thing
            // TODO: ex: function xxx must have enclosing class of ...
        }
        pushToStack(NodeType.CLASS, javaClass);
    }

    @Override
    public void exitClasses(RulepadGrammarParser.ClassesContext ctx) {
        this.previousCompleteElement = popFromStack().node;
    }

    @Override
    public void enterClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {

    }

    @Override
    public void exitClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {

    }

    @Override
    public void enterFunctions(RulepadGrammarParser.FunctionsContext ctx) {
        final Method method = new Method();
        if (initialItem == null) {
            initialItem = new Data(NodeType.METHOD, method);
        } else {
            boolean comingFromOr = isComingFromOr();

            final Data data = stack.peek();
            if (data.comingFrom == NodeType.CLASS) {
                JavaClass klass = (JavaClass) data.node;
                // TODO: in cases of ORs this will get complicated and we will use merge function
                if (comingFromOr) {
                    if (previousCompleteElement instanceof Method) {
                        klass.method().update(method, Condition.ConditionOperation.OR);
                    }
                } else {
                    klass.method(single(method));
                }
            }
        }
        pushToStack(NodeType.METHOD, method);
    }

    @Override
    public void exitFunctions(RulepadGrammarParser.FunctionsContext ctx) {
        this.previousCompleteElement = popFromStack().node;
    }

    @Override
    public void enterDeclarationStatements(RulepadGrammarParser.DeclarationStatementsContext ctx) {
        final Field field = new Field();
        if (initialItem == null) {
            initialItem = new Data(NodeType.FIELD, field);
        } else {
            final Data data = stack.peek();
            if (data.comingFrom == NodeType.CLASS) {
                JavaClass klass = (JavaClass) data.node;
                // TODO: in cases of ORs this will get complicated and we will use merge function
                klass.field(single(field));
            }
        }
        pushToStack(NodeType.FIELD, field);
    }

    @Override
    public void exitDeclarationStatements(RulepadGrammarParser.DeclarationStatementsContext ctx) {
        this.previousCompleteElement = popFromStack().node;
    }

    @Override
    public void enterAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {
        // TODO: so far only handling single annotation case, but ORs will get involved as well
        boolean comingFromOr = isComingFromOr();

        final Data data = stack.peek();
        val words = ctx.annotationCondition().combinatorialWords();
        final Type annotationType;
        if (words == null) {
            annotationType = Type.EMPTY_TYPE;
        } else {
            annotationType = new Type(words.getText().replace("\"", "").trim());
        }
        final Annotation annotation = new Annotation();
        annotation.type(single(annotationType));

        if (ANNOTATION_CONTAINING_NODES.contains(data.comingFrom)) {
            WithAnnotation node = (WithAnnotation) data.node;

            if (comingFromOr) {
                if (previousCompleteElement instanceof Annotation) {
                    node.annotations().stream()
                            .reduce((first, second) -> second) // just returns the last element of the collection
                            .ifPresent(c ->
                                    c.update(annotation, Condition.ConditionOperation.OR));
                }
            } else {
                node.annotations().add(single(annotation));
            }
        }
        pushToStack(NodeType.ANNOTATION, annotation);
    }

    private boolean isComingFromOr() {
        boolean comingFromOr = false;
        if (stack.peek().comingFrom == NodeType._OR_) {
            comingFromOr = true;
            stack.pop();
        }
        return comingFromOr;
    }

    @Override
    public void exitAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {
        this.previousCompleteElement = popFromStack().node;
    }

    @Override
    public void enterTypes(RulepadGrammarParser.TypesContext ctx) {
        boolean comingFromOr = isComingFromOr();

        final Data data = stack.peek();
        String typeString;
        val combWords = ctx.typeCondition().combinatorialWords();
        if (combWords != null) {
            typeString = combWords.getText().replace("\"", "").trim();
        } else {
            typeString = ctx.typeCondition().words().getText().replace("\"", "").trim();
        }

        final Type type = new Type(typeString);
        Condition<Type> typeCondition = null;
        if (data.comingFrom == NodeType.METHOD) {
            Method node = (Method) data.node;
            typeCondition = node.returnType();
        } else if (data.comingFrom == NodeType.FIELD) {
            Field node = (Field) data.node;
            typeCondition = node.type();
        } else if (data.comingFrom == NodeType.METHOD_PARAMETER) {
            MethodParameter node = (MethodParameter) data.node;
            typeCondition = node.type();
        } else if (data.comingFrom == NodeType.ANNOTATION_PARAMETER) {
            AnnotationParameter node = (AnnotationParameter) data.node;
            typeCondition = node.type();
        }

        if (comingFromOr) {
            typeCondition.update(type, Condition.ConditionOperation.OR);
        } else {
            typeCondition.update(type, Condition.ConditionOperation.AND);
        }
    }

    @Override
    public void enterOr_(RulepadGrammarParser.Or_Context ctx) {
        pushToStack(NodeType._OR_, stack.peek().node);
    }

    @Override
    public void enterMust(RulepadGrammarParser.MustContext ctx) {
        this.antecedent = (AnalysisItem) initialItem.node;
        if (initialItem.comingFrom == NodeType.CLASS) {
            pushToStack(NodeType.CLASS, new JavaClass());
        } else if (initialItem.comingFrom == NodeType.FIELD) {
            pushToStack(NodeType.FIELD, new Field());
        } else if (initialItem.comingFrom == NodeType.METHOD) {
            pushToStack(NodeType.METHOD, new Method());
        }
    }

    @Override
    public void exitMustClause(RulepadGrammarParser.MustClauseContext ctx) {
        final Data data = popFromStack();
        if (data.comingFrom == NodeType.CLASS) {
            consequent = single((JavaClass) data.node);
        } else if (data.comingFrom == NodeType.FIELD) {
            consequent = single((Field) data.node);
        } else if (data.comingFrom == NodeType.METHOD) {
            consequent = single((Method) data.node);
        }
    }

    private void pushToStack(NodeType type, ProgramElement element) {
        stack.push(new Data(type, element));
    }

    private Data popFromStack() {
        return this.stack.pop();
    }

    private static final List<NodeType> ANNOTATION_CONTAINING_NODES = listOf(NodeType.CLASS, NodeType.METHOD, NodeType.FIELD, NodeType.METHOD_PARAMETER, NodeType.CONSTRUCTOR);
    // TODO: many more should be considered
    private static final List<NodeType> TYPE_CONTAINING_NODES = listOf(NodeType.METHOD, NodeType.FIELD, NodeType.METHOD_PARAMETER);
}
