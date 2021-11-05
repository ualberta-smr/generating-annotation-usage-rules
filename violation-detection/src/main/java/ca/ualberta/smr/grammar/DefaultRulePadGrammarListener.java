package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.CopyStaticAnalysisRule;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.rules.Rule;
import ca.ualberta.smr.utils.Pair;
import javassist.compiler.Javac;
import lombok.RequiredArgsConstructor;
import lombok.ToString;
import lombok.val;

import java.util.List;
import java.util.Stack;

import static ca.ualberta.smr.model.javaelements.Condition.single;
import static ca.ualberta.smr.utils.Utils.listOf;

@RequiredArgsConstructor
@ToString
class Datum {
    final NType comingFrom;
    final Object node;
}

enum NType {
    CLASS, METHOD, FIELD, METHOD_PARAMETER, ANNOTATION, ANNOTATION_PARAMETER, CONSTRUCTOR, _OR_, _AND_
}

public class DefaultRulePadGrammarListener extends AbstractRulePadGrammarListener {

    private final Stack<Datum> stack;
    private Condition<? extends AnalysisItem> antecedent;
    private Condition<? extends AnalysisItem> consequent;

    private boolean passedMustHave = false;

    private final Rule rule;

    public DefaultRulePadGrammarListener(Rule rule) {
        this.stack = new Stack<>();
        this.antecedent = null;
        this.consequent = null;
        this.rule = rule;
    }

    public StaticAnalysisRule getRule() {
        return new StaticAnalysisRule(rule.getId(), antecedent.getFirst(), consequent, rule.getSpecification());
    }

    private boolean isComingFromBinary(Datum datum) {
        return datum.comingFrom == NType._OR_; // || datum.comingFrom == NType._AND_;
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
            final JavaClass javaClass = new JavaClass();
            if (!stack.isEmpty()) {
                final Datum mostRecentData = stack.peek();
                if (isComingFromBinary(mostRecentData)) {
                    Condition<JavaClass> binary = (Condition<JavaClass>) mostRecentData.node;
                    binary.update(javaClass);
                }
                // TODO: in future it may come from a function or a field
                // TODO: for now, only <binary context>
            } else {
                setAntecedentOrConsequent(single(javaClass));
            }
            pushToStack(NType.CLASS, javaClass);
        } else {
            // meaning that we have a rule of form: class ... must have A or/and B
            // class with annotation A or function B
            final Pair<NType, Condition<JavaClass>> values = getBinaryContextValues(ctx.op, JavaClass.class);
            final NType operation = values.key();
            final Condition<JavaClass> condition = values.value();
            if (stack.isEmpty()) {
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
            if (!stack.isEmpty()) {
                final Datum mostRecentData = stack.peek();
                if (isComingFromBinary(mostRecentData)) {
                    Condition<Method> binary = (Condition<Method>) mostRecentData.node;
                    binary.update(method);
                } else if (mostRecentData.comingFrom == NType.CLASS) {
                    JavaClass javaClass = (JavaClass) mostRecentData.node;
                    javaClass.method(single(method));
                }
            } else {
                setAntecedentOrConsequent(single(method));
            }
            pushToStack(NType.METHOD, method);
        } else {
            final Pair<NType, Condition<Method>> values = getBinaryContextValues(ctx.op, Method.class);
            final NType operation = values.key();
            final Condition<Method> methodCondition = values.value();
            if (!stack.isEmpty()) {
                final Datum mostRecentData = stack.peek();
                if (mostRecentData.comingFrom == NType.CLASS) {
                    JavaClass javaClass = (JavaClass) mostRecentData.node;
                    javaClass.method(methodCondition);
                }
            } else {
                // TODO: probably means the function is the first/root element
                setAntecedentOrConsequent(methodCondition);
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
            if (!stack.isEmpty()) {
                final Datum mostRecentData = stack.peek();
                if (isComingFromBinary(mostRecentData)) {
                    Condition<Field> binary = (Condition<Field>) mostRecentData.node;
                    binary.update(field);
                } else if (mostRecentData.comingFrom == NType.CLASS) {
                    JavaClass javaClass = (JavaClass) mostRecentData.node;
                    javaClass.field(single(field));
                }
            } else {
                setAntecedentOrConsequent(single(field));
            }
            pushToStack(NType.FIELD, field);
        } else {
            final Pair<NType, Condition<Field>> values = getBinaryContextValues(ctx.op, Field.class);
            final NType operation = values.key();
            final Condition<Field> fieldCondition = values.value();
            if (!stack.isEmpty()) {
                final Datum mostRecentData = stack.peek();
                if (mostRecentData.comingFrom == NType.CLASS) {
                    JavaClass javaClass = (JavaClass) mostRecentData.node;
                    javaClass.field(fieldCondition);
                }
            } else {
                // TODO: probably means the field is the first/root element
                setAntecedentOrConsequent(fieldCondition);
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
        final Type annotationType;
        if (words == null) {
            annotationType = Type.EMPTY_TYPE;
        } else {
            annotationType = new Type(words.getText().replace("\"", "").trim());
        }
        final Annotation annotation = new Annotation();
        annotation.type(single(annotationType));

        final Datum data = stack.peek();
        if (ANNOTATION_CONTAINING_NODES.contains(data.comingFrom)) {
            WithAnnotation node = (WithAnnotation) data.node;
            node.annotations().add(single(annotation));
        }
        pushToStack(NType.ANNOTATION, annotation);
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
        final Datum data = stack.peek();
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
        if (data.comingFrom == NType.ANNOTATION) {
            Annotation node = (Annotation) data.node;
            node.parameters().add(single(ap));
        }
        pushToStack(NType.ANNOTATION_PARAMETER, ap);
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

        final Datum data = stack.peek();
        if (data.comingFrom == NType.METHOD) {
            Method node = (Method) data.node;
            node.parameters().add(single(parameter));
        } else if (data.comingFrom == NType.CONSTRUCTOR) {
            // TODO: not implemented yet
            throw new UnsupportedOperationException("Constructors are not supported yet");
        }

        pushToStack(NType.METHOD_PARAMETER, parameter);
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

        final Datum data = stack.peek();
        if (TYPE_CONTAINING_NODES.contains(data.comingFrom)) {
            WithType withTypeNode = (WithType) data.node;
            withTypeNode.type(single(new Type(typeString)));
        }
    }

    @Override
    public void exitHave(RulepadGrammarParser.HaveContext ctx) {
        this.passedMustHave = true;
    }

    private void pushToStack(NType type, Object element) {
        stack.push(new Datum(type, element));
    }

    private void popFromStack() {
        this.stack.pop();
    }

    private <T extends ProgramElement> Pair<NType, Condition<T>> getBinaryContextValues(RulepadGrammarParser.BinaryContext ctx, Class<T> clazz) {
        final Condition<T> condition;
        final NType operation;
        if (ctx.getText().trim().equals("or")) {
            // it's or
            condition = Condition.any(clazz);
            operation = NType._OR_;
        } else {
            // it's and (for now)
            condition = Condition.all(clazz);
            operation = NType._AND_;
        }
        return new Pair<>(operation, condition);
    }

    private static final List<NType> ANNOTATION_CONTAINING_NODES = listOf(NType.CLASS, NType.METHOD, NType.FIELD, NType.METHOD_PARAMETER, NType.CONSTRUCTOR);
    // TODO: many more should be considered
    private static final List<NType> TYPE_CONTAINING_NODES = listOf(NType.METHOD, NType.FIELD, NType.METHOD_PARAMETER);
}
