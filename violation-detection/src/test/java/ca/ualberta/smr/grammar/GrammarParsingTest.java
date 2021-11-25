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
import static ca.ualberta.smr.model.javaelements.Condition.*;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.params.provider.Arguments.arguments;

public class GrammarParsingTest {

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
        map.put("function_with_multiple_ors", getRule_function_with_multiple_ors());
        map.put("class_with_multiple_ors", getRule_class_with_multiple_ors());
        map.put("field_with_multiple_ors", getRule_field_with_multiple_ors());
        map.put("function_with_multiple_ors_parenthesis", getRule_function_with_multiple_ors_parenthesis());
        map.put("field_with_multiple_ors_parenthesis", getRule_field_with_multiple_ors_parenthesis());
        map.put("class_with_multiple_ors_parenthesis", getRule_class_with_multiple_ors_parenthesis());
        map.put("antecedent_class_with_or", getRule_antecedent_class_with_or());
        map.put("antecedent_function_with_or_plus_consequent_with_or", getRule_antecedent_function_with_or_plus_consequent_with_or());
        map.put("field_with_or_plus_consequent_with_or", getRule_antecedent_field_with_or_plus_consequent_with_or());
        map.put("field_with_or_plus_consequent_with_and", getRule_antecedent_field_with_and_plus_consequent_with_and());
        map.put("mixingAll", getRule_mixingAll());
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
        return new StaticAnalysisRule("function_simple", single(antecedent), single(consequent), "function with annotation \"Demo\" must have annotation \"Hello\" ");
    }

    private static StaticAnalysisRule getRule_field_simple() {
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("Demo")));
        final Field consequent = new Field();
        consequent.annotations().add(single(annotation("Hello")));
        return new StaticAnalysisRule("field_simple", single(antecedent), single(consequent), "field with annotation \"Demo\" must have annotation \"Hello\" ");
    }

    private static StaticAnalysisRule getRule_class_simple() {
        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("Demo")));
        final JavaClass consequent = new JavaClass();
        consequent.annotations().add(single(annotation("Hello")));
        return new StaticAnalysisRule("class_simple", single(antecedent), single(consequent), "class with annotation \"Demo\" must have annotation \"Hello\" ");
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
        return new StaticAnalysisRule("OutgoingAndScope", single(antecedent), consequent, "class with function with annotation \"Outgoing\" or annotation \"Incoming\" must have annotation \"ApplicationScoped\" or annotation \"Dependent\" ");
    }

    private static StaticAnalysisRule getRule_RestClientInjectField() {
        // if field has annotation @RestClient
        // then it must have @Inject
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("RestClient")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("RestClientInjectField", single(antecedent), consequent, "field with annotation \"RestClient\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_ClaimInjectField() {
        // if field has annotation @Claim
        // then it must have @Inject
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("Claim")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("ClaimInjectField", single(antecedent), consequent, "field with annotation \"Claim\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_JsonWebTokenField() {
        // if field is of type JsonWebToken
        // then it must have annotation @Inject
        final Field antecedent = new Field();
        antecedent.type(single(new Type("JsonWebToken")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("JsonWebTokenField", single(antecedent), consequent, "field with type \"JsonWebToken\" must have annotation \"Inject\" ");
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

        return new StaticAnalysisRule("PathParam", single(antecedent), consequent, "class with function with parameter with annotation \"PathParam\" must have annotation \"Path\" or function with annotation \"Path\" ");
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
        return new StaticAnalysisRule("QueryMutationGraphQLAPI", single(antecedent), consequent, "class with function with annotation \"Query\" or annotation \"Mutation\" must have annotation \"GraphQLApi\" ");
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

        return new StaticAnalysisRule("function_with_OR_in_consequent", single(antecedent), consequent, "function with type \"C\" must have annotation \"A\" or annotation \"B\" ");
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

        return new StaticAnalysisRule("field_with_OR_in_consequent", single(antecedent), consequent, "field with type \"C\" must have annotation \"A\" or annotation \"B\" ");
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

        return new StaticAnalysisRule("class_field_with_OR_in_consequent", single(antecedent), consequent, "class with field with type \"C\" must have field with annotation \"A\" or annotation \"B\" ");
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
        return new StaticAnalysisRule("annotation_with_parameter_both_type_and_name", single(antecedent), consequent, "field with type \"K\" must have annotation \"A\" with parameter \"B C\" ");
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
        return new StaticAnalysisRule("annotation_with_parameter_both_type_and_name", single(antecedent), consequent, "field with type \"K\" must have annotation \"A\" with parameter \"B\" ");
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

        return new StaticAnalysisRule("function_with_param_string", single(antecedent), consequent, "function with parameter \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_function_with_multiple_ors() {
        String ruleString = "class with annotation \"A\" must have function with annotation \"B\" or annotation \"C\" or annotation \"D\" ";
        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("A")));

        final Method m1 = new Method();
        m1.annotations().add(single(annotation("B")));
        final Method m2 = new Method();
        m2.annotations().add(single(annotation("C")));
        final Method m3 = new Method();
        m3.annotations().add(single(annotation("D")));

        final JavaClass consequent = new JavaClass();
        consequent.method(any(m1, m2, m3));

        return new StaticAnalysisRule("function_with_multiple_ors", single(antecedent), single(consequent), ruleString);
    }

    private static StaticAnalysisRule getRule_class_with_multiple_ors() {
        String ruleString = "class with annotation \"A\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ";
        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("A")));

        final JavaClass j1 = new JavaClass();
        j1.annotations().add(single(annotation("B")));
        final JavaClass j2 = new JavaClass();
        j2.annotations().add(single(annotation("C")));
        final JavaClass j3 = new JavaClass();
        j3.annotations().add(single(annotation("D")));

        return new StaticAnalysisRule("class_with_multiple_ors", single(antecedent), any(j1, j2, j3), ruleString);
    }

    private static StaticAnalysisRule getRule_field_with_multiple_ors() {
        String ruleString = "field with annotation \"A\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ";
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("A")));

        final Field f1 = new Field();
        f1.annotations().add(single(annotation("B")));
        final Field f2 = new Field();
        f2.annotations().add(single(annotation("C")));
        final Field f3 = new Field();
        f3.annotations().add(single(annotation("D")));

        return new StaticAnalysisRule("field_with_multiple_ors", single(antecedent), any(f1, f2, f3), ruleString);
    }

    private static StaticAnalysisRule getRule_function_with_multiple_ors_parenthesis() {
        String ruleString = "class with annotation \"A\" must have function with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ";
        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("A")));

        final Method m1 = new Method();
        m1.annotations().add(single(annotation("B")));
        final Method m2 = new Method();
        m2.annotations().add(single(annotation("C")));
        final Method m3 = new Method();
        m3.annotations().add(single(annotation("D")));

        final JavaClass consequent = new JavaClass();
        consequent.method(any(m1, m2, m3));

        return new StaticAnalysisRule("function_with_multiple_ors_parenthesis", single(antecedent), single(consequent), ruleString);
    }

    private static StaticAnalysisRule getRule_field_with_multiple_ors_parenthesis() {
        String ruleString = "class with annotation \"A\" must have field with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ";
        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("A")));

        final Field f1 = new Field();
        f1.annotations().add(single(annotation("B")));
        final Field f2 = new Field();
        f2.annotations().add(single(annotation("C")));
        final Field f3 = new Field();
        f3.annotations().add(single(annotation("D")));

        final JavaClass consequent = new JavaClass();
        consequent.field(any(f1, f2, f3));

        return new StaticAnalysisRule("field_with_multiple_ors_parenthesis", single(antecedent), single(consequent), ruleString);
    }

    private static StaticAnalysisRule getRule_class_with_multiple_ors_parenthesis() {
        String ruleString = "class with annotation \"A\" must have (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ";
        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("A")));

        final JavaClass j1 = new JavaClass();
        j1.annotations().add(single(annotation("B")));
        final JavaClass j2 = new JavaClass();
        j2.annotations().add(single(annotation("C")));
        final JavaClass j3 = new JavaClass();
        j3.annotations().add(single(annotation("D")));

        final Condition<JavaClass> consequent = any(j1, j2, j3);

        return new StaticAnalysisRule("class_with_multiple_ors_parenthesis", single(antecedent), consequent, ruleString);
    }

    private static StaticAnalysisRule getRule_mixingAll() {
        String ruleString = "class with annotation \"A\" must have (function with annotation \"B\" or annotation \"C\" " +
                "or annotation \"D\" ) or (field with type \"X\" or type \"Y\" ) or (annotation \"M\" or annotation \"L\" ) ";

        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("A")));

        final JavaClass j1 = new JavaClass();

        final Method methodJ11 = new Method();
        methodJ11.annotations().add(single(annotation("B")));
        final Method methodJ12 = new Method();
        methodJ12.annotations().add(single(annotation("C")));
        final Method methodJ13 = new Method();
        methodJ13.annotations().add(single(annotation("D")));
        j1.method(any(methodJ11, methodJ12, methodJ13));

        final JavaClass j2 = new JavaClass();

        final Field f21 = new Field();
        f21.type(Type.type("X"));
        final Field f22 = new Field();
        f22.type(Type.type("Y"));
        j2.field(any(f21, f22));

        final JavaClass j3 = new JavaClass();
        j3.annotations().add(single(annotation("M")));

        final JavaClass j4 = new JavaClass();
        j4.annotations().add(single(annotation("L")));

        final Condition<JavaClass> consequent = any(j1, j2, j3, j4);

        return new StaticAnalysisRule("mixingAll", single(antecedent), consequent, ruleString);
    }

    private static StaticAnalysisRule getRule_antecedent_class_with_or() {
        String ruleString = "class with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) must have annotation \"A\" ";

        final JavaClass j1 = new JavaClass();
        j1.annotations().add(single(annotation("B")));
        final JavaClass j2 = new JavaClass();
        j2.annotations().add(single(annotation("C")));
        final JavaClass j3 = new JavaClass();
        j3.annotations().add(single(annotation("D")));

        final Condition<JavaClass> antecedent = any(j1, j2, j3);

        final JavaClass consequent = new JavaClass();
        consequent.annotations().add(single(annotation("A")));

        return new StaticAnalysisRule("antecedent_class_with_or", antecedent, single(consequent), ruleString);
    }

    private static StaticAnalysisRule getRule_antecedent_function_with_or_plus_consequent_with_or() {
        String ruleString = "function with type \"B\" or parameter \"C\" or annotation \"D\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ";

        final Method m1 = new Method();
        m1.returnType(Type.type("B"));

        final Method m2 = new Method();
        final MethodParameter m2p = new MethodParameter();
        m2p.type(Type.type("C"));
        m2.parameters().add(single(m2p));

        final Method m3 = new Method();
        m3.annotations().add(single(annotation("D")));

        Condition<Method> antecedent = any(m1, m2, m3);

        final Method m4 = new Method();
        m4.annotations().add(single(annotation("B")));

        final Method m5 = new Method();
        m5.annotations().add(single(annotation("C")));

        final Method m6 = new Method();
        m6.annotations().add(single(annotation("D")));

        Condition<Method> consequent = any(m4, m5, m6);

        return new StaticAnalysisRule("antecedent_function_with_or_plus_consequent_with_or", antecedent, consequent, ruleString);
    }

    private static StaticAnalysisRule getRule_antecedent_field_with_or_plus_consequent_with_or() {
        String ruleString = "field with type \"B\" or annotation \"D\" must have (annotation \"B\" or annotation \"C\" ) or annotation \"D\" ";

        final Field m1 = new Field();
        m1.type(Type.type("B"));

        final Field m2 = new Field();
        m2.annotations().add(single(annotation("D")));

        Condition<Field> antecedent = any(m1, m2);

        final Field m4 = new Field();
        m4.annotations().add(single(annotation("B")));

        final Field m5 = new Field();
        m5.annotations().add(single(annotation("C")));

        final Field m6 = new Field();
        m6.annotations().add(single(annotation("D")));

        Condition<Field> consequent = any(m4, m5, m6);

        return new StaticAnalysisRule("antecedent_field_with_or_plus_consequent_with_or", antecedent, consequent, ruleString);
    }

    private static StaticAnalysisRule getRule_antecedent_field_with_and_plus_consequent_with_and() {
        String ruleString = "field with type \"B\" and annotation \"D\" must have (annotation \"B\" and annotation \"C\" ) and annotation \"D\" ";

        final Field m1 = new Field();
        m1.type(Type.type("B"));

        final Field m2 = new Field();
        m2.annotations().add(single(annotation("D")));

        Condition<Field> antecedent = all(m1, m2);

        final Field m4 = new Field();
        m4.annotations().add(single(annotation("B")));

        final Field m5 = new Field();
        m5.annotations().add(single(annotation("C")));

        final Field m6 = new Field();
        m6.annotations().add(single(annotation("D")));

        Condition<Field> consequent = all(m4, m5, m6);

        return new StaticAnalysisRule("antecedent_field_with_and_plus_consequent_with_and", antecedent, consequent, ruleString);
    }

}
