package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.rules.Rule;
import ca.ualberta.smr.utils.Pair;
import lombok.RequiredArgsConstructor;
import lombok.val;

import java.util.List;
import java.util.Stack;

import static ca.ualberta.smr.model.javaelements.Condition.single;
import static ca.ualberta.smr.utils.Utils.listOf;

@RequiredArgsConstructor
class Data {
    final NodeType comingFrom;
    final Object node;
}

enum NodeType {
    CLASS, METHOD, FIELD, METHOD_PARAMETER, ANNOTATION, ANNOTATION_PARAMETER, CONSTRUCTOR, _OR_, _AND_
}

public class DefaultRulePadGrammarListener extends AbstractRulePadGrammarListener {

    private final Stack<Data> stack;
    private Condition<? extends AnalysisItem> antecedent;
    private Condition<? extends AnalysisItem> consequent;

    /**
     * Flag for setting antecedent or consequent <br>
     * Initially, it is false because we start from antecedent part
     */
    private boolean passedMustHave = false;

    private final Rule rule;

    public DefaultRulePadGrammarListener(Rule rule) {
        this.stack = new Stack<>();
        this.antecedent = null;
        this.consequent = null;
        this.rule = rule;
    }

    public StaticAnalysisRule getStaticAnalysisRule() {
        // currently, it only takes the first element from antecedent which is actually incorrect
        // because there can be 2 or more elements in the `antecedent condition elements`
        // this code assumes there's only ones
        return new StaticAnalysisRule(rule.getId(), antecedent.getFirst(), consequent, rule.getSpecification());
    }

    private boolean isComingFromBinary(Data datum) {
        return datum.comingFrom == NodeType._OR_ || datum.comingFrom == NodeType._AND_;
    }

    private void setAntecedentOrConsequent(Condition<? extends AnalysisItem> newValue) {
        if (passedMustHave) {
            this.consequent = newValue;
        } else {
            this.antecedent = newValue;
        }
    }

    @Override
    @SuppressWarnings("unchecked")
    // TODO: parenthesis contexts are problematic
    public void enterClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {
        if (ctx.op == null) {
            val javaClass = new JavaClass();
            if (stack.isEmpty()) {
                // if the stack is empty it means 2 things
                // 1: either we have just started parsing antecedent
                // 2: we have finished antecedent section, and we're entering consequent part
                setAntecedentOrConsequent(single(javaClass));
            } else {
                final Data mostRecentData = stack.peek();
                if (isComingFromBinary(mostRecentData)) {
                    Condition<JavaClass> binary = (Condition<JavaClass>) mostRecentData.node;
                    binary.update(javaClass);
                }
                // TODO: in future it may come from a function or a field
                // TODO: for now, only <binary context>
            }
            pushToStack(NodeType.CLASS, javaClass);
        } else {
            // meaning that we have a rule of form: class ... must have A or/and B
            // class with annotation A or function B
            final Pair<NodeType, Condition<JavaClass>> values = getBinaryContextValues(ctx.op, JavaClass.class);
            final NodeType operation = values.key();
            final Condition<JavaClass> condition = values.value();
            if (stack.isEmpty()) {
                // if the stack is empty it means 2 things
                // 1: either we have just started parsing antecedent
                // 2: we have finished antecedent section, and we're entering consequent part
                setAntecedentOrConsequent(condition);
            }
            pushToStack(operation, condition);
        }
    }

    @Override
    public void exitClassExpression(RulepadGrammarParser.ClassExpressionContext ctx) {
        popFromStack();
    }

    @Override
    @SuppressWarnings("unchecked")
    public void enterFunctionExpression(RulepadGrammarParser.FunctionExpressionContext ctx) {
        if (ctx.op == null) {
            final Method method = new Method();
            if (stack.isEmpty()) {
                // if the stack is empty it means 2 things
                // 1: either we have just started parsing antecedent
                // 2: we have finished antecedent section, and we're entering consequent part
                setAntecedentOrConsequent(single(method));
            } else {
                final Data mostRecentData = stack.peek();
                if (isComingFromBinary(mostRecentData)) {
                    Condition<Method> binary = (Condition<Method>) mostRecentData.node;
                    binary.update(method);
                } else if (mostRecentData.comingFrom == NodeType.CLASS) {
                    JavaClass javaClass = (JavaClass) mostRecentData.node;
                    javaClass.method(single(method));
                }
            }
            pushToStack(NodeType.METHOD, method);
        } else {
            final Pair<NodeType, Condition<Method>> values = getBinaryContextValues(ctx.op, Method.class);
            final NodeType operation = values.key();
            final Condition<Method> methodCondition = values.value();
            if (stack.isEmpty()) {
                // if the stack is empty it means 2 things
                // 1: either we have just started parsing antecedent
                // 2: we have finished antecedent section, and we're entering consequent part
                setAntecedentOrConsequent(methodCondition);
            } else {
                final Data mostRecentData = stack.peek();
                if (mostRecentData.comingFrom == NodeType.CLASS) {
                    JavaClass javaClass = (JavaClass) mostRecentData.node;
                    javaClass.method(methodCondition);
                }
            }
            pushToStack(operation, methodCondition);
        }
    }

    @Override
    public void exitFunctionExpression(RulepadGrammarParser.FunctionExpressionContext ctx) {
        popFromStack();
    }

    @Override
    @SuppressWarnings("unchecked")
    public void enterDeclarationStatementExpression(RulepadGrammarParser.DeclarationStatementExpressionContext ctx) {
        if (ctx.op == null) {
            final Field field = new Field();
            if (stack.isEmpty()) {
                // if the stack is empty it means 2 things
                // 1: either we have just started parsing antecedent
                // 2: we have finished antecedent section, and we're entering consequent part
                setAntecedentOrConsequent(single(field));
            } else {
                final Data mostRecentData = stack.peek();
                if (isComingFromBinary(mostRecentData)) {
                    Condition<Field> binary = (Condition<Field>) mostRecentData.node;
                    binary.update(field);
                } else if (mostRecentData.comingFrom == NodeType.CLASS) {
                    JavaClass javaClass = (JavaClass) mostRecentData.node;
                    javaClass.field(single(field));
                }
            }
            pushToStack(NodeType.FIELD, field);
        } else {
            final Pair<NodeType, Condition<Field>> values = getBinaryContextValues(ctx.op, Field.class);
            final NodeType operation = values.key();
            final Condition<Field> fieldCondition = values.value();
            if (stack.isEmpty()) {
                // if the stack is empty it means 2 things
                // 1: either we have just started parsing antecedent
                // 2: we have finished antecedent section, and we're entering consequent part
                setAntecedentOrConsequent(fieldCondition);
            } else {
                final Data mostRecentData = stack.peek();
                if (mostRecentData.comingFrom == NodeType.CLASS) {
                    JavaClass javaClass = (JavaClass) mostRecentData.node;
                    javaClass.field(fieldCondition);
                }
            }
            pushToStack(operation, fieldCondition);
        }
    }

    @Override
    public void exitDeclarationStatementExpression(RulepadGrammarParser.DeclarationStatementExpressionContext ctx) {
        popFromStack();
    }

    @SuppressWarnings("DuplicatedCode")
    @Override
    // TODO: for now there's no branching in annotations
    public void enterAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {
        val words = ctx.annotationCondition().combinatorialWords();
        Condition<Type> annotationType = Condition.empty(Type.class);
        if (words != null) {
            annotationType = Type.type(words.getText().replace("\"", "").trim());
        }
        final Annotation annotation = new Annotation();
        annotation.type(annotationType);

        final Data data = stack.peek();
        if (ANNOTATION_CONTAINING_NODES.contains(data.comingFrom)) {
            WithAnnotation node = (WithAnnotation) data.node;
            node.annotations().add(single(annotation));
        }
        pushToStack(NodeType.ANNOTATION, annotation);
    }

    @Override
    public void exitAnnotations(RulepadGrammarParser.AnnotationsContext ctx) {
        popFromStack();
    }

    /**
     * Specific to annotations at the moment
     */
    @Override
    public void enterParameters(RulepadGrammarParser.ParametersContext ctx) {
        final AnnotationParameter ap = new AnnotationParameter();
        val words = ctx.parameterCondition().combinatorialWords();
        if (words != null) {
            final String[] parts = words.getText().replace("\"", "").trim().split("\\s+");
            // TODO: this may have either 1 or 2 parts
            if (parts.length == 2) {
                // e.g. `int delayTime`
                ap.type(single(new Type(parts[0])));
                ap.name(parts[1]);
            } else if (parts.length == 1) {
                // e.g. `int`
                ap.type(single(new Type(parts[0])));
            }
        }

        final Data data = stack.peek();

        if (data.comingFrom == NodeType.ANNOTATION) {
            Annotation node = (Annotation) data.node;
            node.parameters().add(single(ap));
        }
        pushToStack(NodeType.ANNOTATION_PARAMETER, ap);
    }

    @Override
    public void exitParameters(RulepadGrammarParser.ParametersContext ctx) {
        popFromStack();
    }

    @Override
    public void enterFunctionParameters(RulepadGrammarParser.FunctionParametersContext ctx) {
        val paramCondition = ctx.functionParameterCondition();
        final MethodParameter parameter = new MethodParameter();
        if (paramCondition.combinatorialWords() != null) {
            final String text = paramCondition.combinatorialWords().getText().replace("\"", "");
            final String typeString = text.trim();
            parameter.type(single(new Type(typeString)));
        }

        final Data data = stack.peek();
        if (data.comingFrom == NodeType.METHOD) {
            Method node = (Method) data.node;
            node.parameters().add(single(parameter));
        } else if (data.comingFrom == NodeType.CONSTRUCTOR) {
            // TODO: not implemented yet
            throw new UnsupportedOperationException("Constructors are not supported yet");
        }

        pushToStack(NodeType.METHOD_PARAMETER, parameter);
    }

    @Override
    public void exitFunctionParameters(RulepadGrammarParser.FunctionParametersContext ctx) {
        popFromStack();
    }

    @Override
    public void enterTypes(RulepadGrammarParser.TypesContext ctx) {
        String typeString;
        val combWords = ctx.typeCondition().combinatorialWords();
        if (combWords == null) {
            typeString = ctx.typeCondition().words().getText().replace("\"", "").trim();
        } else {
            typeString = combWords.getText().replace("\"", "").trim();
        }

        final Data data = stack.peek();
        if (TYPE_CONTAINING_NODES.contains(data.comingFrom)) {
            WithType withTypeNode = (WithType) data.node;
            withTypeNode.type(single(new Type(typeString)));
        }
    }

    @Override
    public void exitHave(RulepadGrammarParser.HaveContext ctx) {
        this.passedMustHave = true;
    }

    private void pushToStack(NodeType type, Object element) {
        stack.push(new Data(type, element));
    }

    private void popFromStack() {
        this.stack.pop();
    }

    private <T extends ProgramElement> Pair<NodeType, Condition<T>> getBinaryContextValues(RulepadGrammarParser.BinaryContext ctx, Class<T> clazz) {
        final Condition<T> condition;
        final NodeType operation;
        if (ctx.getText().trim().equals("or")) {
            // it's or
            condition = Condition.any(clazz);
            operation = NodeType._OR_;
        } else {
            // it's and (for now)
            condition = Condition.all(clazz);
            operation = NodeType._AND_;
        }
        return new Pair<>(operation, condition);
    }

    private static final List<NodeType> ANNOTATION_CONTAINING_NODES = listOf(NodeType.CLASS, NodeType.METHOD, NodeType.FIELD, NodeType.METHOD_PARAMETER, NodeType.CONSTRUCTOR);
    // TODO: many more should be considered
    private static final List<NodeType> TYPE_CONTAINING_NODES = listOf(NodeType.METHOD, NodeType.FIELD, NodeType.METHOD_PARAMETER);
}
