package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.rules.Rule;
import lombok.val;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.any;
import static ca.ualberta.smr.model.javaelements.Condition.single;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.params.provider.Arguments.arguments;

public class RulePadTest {

    @ParameterizedTest(name = "{index} : {0}")
    @MethodSource("dataProvider")
    void test(String id, StaticAnalysisRule rule) {
        parseAndCheckRule(rule);
    }

    static Stream<Arguments> dataProvider() {
        final Map<String, StaticAnalysisRule> map = new HashMap<>();

        // made up rules
        map.put("class_simple", getRule_class_simple());
        map.put("field_simple", getRule_field_simple());
        map.put("function_simple", getRule_function_simple());
        map.put("function_with_OR_in_consequent", getRule_function_with_OR_in_consequent());
        map.put("field_with_OR_in_consequent", getRule_field_with_OR_in_consequent());
        map.put("class_field_with_OR_in_consequent", getRule_class_field_with_OR_in_consequent());
        map.put("annotation_with_parameter_both_type_and_name", getRule_annotation_with_parameter_both_type_and_name());
        map.put("annotation_with_parameter_both_type_only", getRule_annotation_with_parameter_both_type_only());
        map.put("function_with_param_string", getRule_function_with_param_string());
        // actual rules
        map.put("OutgoingAndScope", getRule_OutgoingAndScope());
        map.put("RestClientInjectField", getRule_RestClientInjectField());
        map.put("ClaimInjectField", getRule_ClaimInjectField());
        map.put("JsonWebTokenField", getRule_JsonWebTokenField());
        map.put("PathParam", getRule_PathParam());
        map.put("QueryMutationGraphQLAPI", getRule_QueryMutationGraphQLAPI());

        return map.values()
                .stream().map(staticAnalysisRule -> arguments(staticAnalysisRule.name(), staticAnalysisRule));
    }


    void parseAndCheckRule(StaticAnalysisRule data) {
        val tree = getTree(data.description());

        val walker = new ParseTreeWalker();
        val listener = new DefaultRulePadGrammarListener(toRule(data));
        walker.walk(listener, tree);

        val actualRule = listener.getStaticAnalysisRule();

        assertEquals(data, actualRule);
    }

    private static Rule toRule(StaticAnalysisRule staticAnalysisRule) {
        val rule = new Rule();
        rule.setId(staticAnalysisRule.name());
        rule.setSpecification(staticAnalysisRule.description());
        return rule;
    }

    private static ParseTree getTree(String input) {
        final RulepadGrammarLexer lexer = new RulepadGrammarLexer(CharStreams.fromString(input));
        final RulepadGrammarParser parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
        return parser.inputSentence();
    }

    private static StaticAnalysisRule getRule_function_simple() {
        final Method antecedent = new Method();
        antecedent.annotations().add(single(annotation("Demo")));
        final Method consequent = new Method();
        consequent.annotations().add(single(annotation("Hello")));
        return new StaticAnalysisRule("function_simple", antecedent, single(consequent), "function with annotation \"Demo\" must have annotation \"Hello\" ");
    }

    private static StaticAnalysisRule getRule_field_simple() {
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("Demo")));
        final Field consequent = new Field();
        consequent.annotations().add(single(annotation("Hello")));
        return new StaticAnalysisRule("field_simple", antecedent, single(consequent), "field with annotation \"Demo\" must have annotation \"Hello\" ");
    }

    private static StaticAnalysisRule getRule_class_simple() {
        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("Demo")));
        final JavaClass consequent = new JavaClass();
        consequent.annotations().add(single(annotation("Hello")));
        return new StaticAnalysisRule("class_simple", antecedent, single(consequent), "class with annotation \"Demo\" must have annotation \"Hello\" ");
    }

    private static StaticAnalysisRule getRule_OutgoingAndScope() {
        // if a method is annotated with @Outgoing or @Incoming
        // then the class must be annotation with @ApplicationScoped or @Dependent

        final Method method1 = new Method();
        method1.annotations().add(single(annotation("Outgoing")));

        final Method method2 = new Method();
        method2.annotations().add(single(annotation("Incoming")));

        final JavaClass antecedent = new JavaClass();
        antecedent.method(Condition.any(method1, method2));

        final JavaClass javaClass1 = new JavaClass();
        javaClass1.annotations().add(
                single(annotation("ApplicationScoped"))
        );

        final JavaClass javaClass2 = new JavaClass();
        javaClass2.annotations().add(
                single(annotation("Dependent"))
        );

        Condition<? extends AnalysisItem> consequent = any(javaClass1, javaClass2);
        return new StaticAnalysisRule("OutgoingAndScope", antecedent, consequent, "class with function with annotation \"Outgoing\" or annotation \"Incoming\" must have annotation \"ApplicationScoped\" or annotation \"Dependent\" ");
    }

    private static StaticAnalysisRule getRule_RestClientInjectField() {
        // if field has annotation @RestClient
        // then it must have @Inject
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("RestClient")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("RestClientInjectField", antecedent, consequent, "field with annotation \"RestClient\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_ClaimInjectField() {
        // if field has annotation @Claim
        // then it must have @Inject
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("Claim")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("ClaimInjectField", antecedent, consequent, "field with annotation \"Claim\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_JsonWebTokenField() {
        // if field is of type JsonWebToken
        // then it must have annotation @Inject
        final Field antecedent = new Field();
        antecedent.type(single(new Type("JsonWebToken")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("JsonWebTokenField", antecedent, consequent, "field with type \"JsonWebToken\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_PathParam() {
        // if method parameter has @PathParam
        // then either method or class must have @Path

        final Method antecedentMethod = new Method();
        final MethodParameter param = new MethodParameter();
        param.annotations().add(single(annotation("PathParam")));
        antecedentMethod.parameters().add(single(param));

        final JavaClass antecedent = new JavaClass();
        antecedent.method(single(antecedentMethod));

        final JavaClass klass1 = new JavaClass();
        klass1.annotations().add(single(annotation("Path")));

        final Method method = new Method();
        method.annotations().add(single(annotation("Path")));
        final JavaClass klass2 = new JavaClass();
        klass2.method(single(method));

        final Condition<? extends AnalysisItem> consequent = any(
                klass1, klass2
        );

        return new StaticAnalysisRule("PathParam", antecedent, consequent, "class with function with parameter with annotation \"PathParam\" must have annotation \"Path\" or function with annotation \"Path\" ");
    }

    private static StaticAnalysisRule getRule_QueryMutationGraphQLAPI() {
        // if a method is annotated with @Query or @Mutation
        // then the class is annotation with @GraphQLApi

        final Method method1 = new Method();
        method1.annotations().add(single(annotation("Query")));

        final Method method2 = new Method();
        method2.annotations().add(single(annotation("Mutation")));

        final JavaClass antecedent = new JavaClass();
        antecedent.method(Condition.any(method1, method2));

        final JavaClass javaClass = new JavaClass();
        javaClass.annotations().add(single(annotation("GraphQLApi")));

        Condition<? extends AnalysisItem> consequent = single(javaClass);
        return new StaticAnalysisRule("QueryMutationGraphQLAPI", antecedent, consequent, "class with function with annotation \"Query\" or annotation \"Mutation\" must have annotation \"GraphQLApi\" ");
    }

    private static StaticAnalysisRule getRule_function_with_OR_in_consequent() {
        val antecedent = new Method();
        antecedent.returnType(Type.type("C"));

        val method1 = new Method();
        method1.annotations().add(single(annotation("A")));

        val method2 = new Method();
        method2.annotations().add(single(annotation("B")));

        val consequent = Condition.any(
                method1, method2
        );

        return new StaticAnalysisRule("function_with_OR_in_consequent", antecedent, consequent, "function with type \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_field_with_OR_in_consequent() {
        val antecedent = new Field();
        antecedent.type(Type.type("C"));

        val field1 = new Field();
        field1.annotations().add(single(annotation("A")));

        val field2 = new Field();
        field2.annotations().add(single(annotation("B")));

        val consequent = Condition.any(
                field1, field2
        );

        return new StaticAnalysisRule("field_with_OR_in_consequent", antecedent, consequent, "field with type \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_class_field_with_OR_in_consequent() {
        val antecedentField = new Field();
        antecedentField.type(Type.type("C"));

        val antecedent = new JavaClass();
        antecedent.field(single(antecedentField));

        val field1 = new Field();
        field1.annotations().add(single(annotation("A")));

        val field2 = new Field();
        field2.annotations().add(single(annotation("B")));

        val consequentClass = new JavaClass();
        consequentClass.field(Condition.any(
                field1, field2
        ));

        val consequent = single(consequentClass);

        return new StaticAnalysisRule("class_field_with_OR_in_consequent", antecedent, consequent, "class with field with type \"C\" must have field with annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_annotation_with_parameter_both_type_and_name() {
        val antecedent = new Field();
        antecedent.type(Type.type("K"));

        val field = new Field();

        final Annotation annotation = new Annotation();
        annotation.type(Type.type("A"));
        final AnnotationParameter ap = new AnnotationParameter();
        ap.name("C");
        ap.type(Type.type("B"));
        annotation.parameters().add(single(ap));

        field.annotations().add(single(annotation));
        val consequent = single(field);
        return new StaticAnalysisRule("annotation_with_parameter_both_type_and_name", antecedent, consequent, "field with type \"K\" must have annotation \"A\" with parameter \"B C\" ");
    }

    private static StaticAnalysisRule getRule_annotation_with_parameter_both_type_only() {
        val antecedent = new Field();
        antecedent.type(Type.type("K"));

        val field = new Field();

        final Annotation annotation = new Annotation();
        annotation.type(Type.type("A"));
        final AnnotationParameter ap = new AnnotationParameter();
        ap.type(Type.type("B"));
        annotation.parameters().add(single(ap));

        field.annotations().add(single(annotation));
        val consequent = single(field);
        return new StaticAnalysisRule("annotation_with_parameter_both_type_and_name", antecedent, consequent, "field with type \"K\" must have annotation \"A\" with parameter \"B\" ");
    }

    private static StaticAnalysisRule getRule_function_with_param_string() {
        val antecedent = new Method();
        final MethodParameter mp = new MethodParameter();
        mp.type(Type.type("C"));
        antecedent.parameters().add(single(mp));

        val method1 = new Method();
        method1.annotations().add(single(annotation("A")));

        val method2 = new Method();
        method2.annotations().add(single(annotation("B")));

        val consequent = Condition.any(
                method1, method2
        );

        return new StaticAnalysisRule("function_with_param_string", antecedent, consequent, "function with parameter \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

}
