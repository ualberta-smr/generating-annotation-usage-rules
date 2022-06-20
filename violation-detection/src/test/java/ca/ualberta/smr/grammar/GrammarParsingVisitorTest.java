package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.grammar.visitor.DefaultRulePadGrammarVisitor;
import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.javaelements.*;
import lombok.val;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

import static ca.ualberta.smr.newmodel.javaelements.AggregateCondition.empty;
import static ca.ualberta.smr.newmodel.javaelements.AggregateCondition.single;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.params.provider.Arguments.arguments;

public class GrammarParsingVisitorTest {

    @ParameterizedTest(name = "{index} : {0}")
    @MethodSource("dataProvider")
    void test(String id, StaticAnalysisRule rule) {
        parseAndCheckRule(rule);
    }

    static Stream<Arguments> dataProvider() {
        final Map<String, StaticAnalysisRule> map = new HashMap<>();

        // made up rules
        map.put("function_simple", getRule_function_simple());
        map.put("function_with_OR_in_consequent", getRule_function_with_OR_in_consequent());
        map.put("function_with_param_string", getRule_function_with_param_string());
        map.put("antecedent_function_with_or_plus_consequent_with_or", getRule_antecedent_function_with_or_plus_consequent_with_or());
        map.put("function_with_multiple_ors", getRule_function_with_multiple_ors());
        map.put("function_with_multiple_ors_parenthesis", getRule_function_with_multiple_ors_parenthesis());
        map.put("class_simple", getRule_class_simple());
        map.put("field_simple", getRule_field_simple());
        map.put("field_with_OR_in_consequent", getRule_field_with_OR_in_consequent());
        map.put("class_field_with_OR_in_consequent", getRule_class_field_with_OR_in_consequent());
        map.put("annotation_with_parameter_both_type_and_name", getRule_annotation_with_parameter_both_type_and_name());
        map.put("annotation_with_parameter_name_only", getRule_annotation_with_parameter_name_only());
        map.put("class_with_multiple_ors", getRule_class_with_multiple_ors());
        map.put("field_with_multiple_ors", getRule_field_with_multiple_ors());
        map.put("field_with_multiple_ors_parenthesis", getRule_field_with_multiple_ors_parenthesis());
        map.put("antecedent_field_with_or_plus_consequent_with_or_parenthesis", getRule_antecedent_field_with_or_plus_consequent_with_or_parenthesis());
        map.put("class_with_multiple_ors_parenthesis", getRule_class_with_multiple_ors_parenthesis());
        map.put("antecedent_class_with_or", getRule_antecedent_class_with_or());
        map.put("field_with_or_plus_consequent_with_or", getRule_antecedent_field_with_or_plus_consequent_with_or());
        map.put("antecedent_field_with_and_plus_consequent_with_and", getRule_antecedent_field_with_and_plus_consequent_with_and());
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
        val visitor = new DefaultRulePadGrammarVisitor(data.name(), data.description());
        val actual = visitor.visit(tree);
        assertEquals(data, actual);
    }

    private static ParseTree getTree(String input) {
        final RulepadGrammarLexer lexer = new RulepadGrammarLexer(CharStreams.fromString(input));
        final RulepadGrammarParser parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
        return parser.inputSentence();
    }

    private static StaticAnalysisRule getRule_function_simple() {
        final Method antecedent = new Method(
                empty(),
                single(new Annotation(Type.of("Demo"), empty())),
                empty()
        );
        final Method consequent = new Method(
                empty(),
                single(new Annotation(Type.of("Hello"), empty())),
                empty()
        );
        return new StaticAnalysisRule("function_simple",
                single(antecedent),
                single(consequent),
                "function with annotation \"Demo\" must have annotation \"Hello\" "
        );
    }

    private static StaticAnalysisRule getRule_field_simple() {
        val antecedent = new Field(
                empty(), single(new Annotation(Type.of("Demo"), empty()))
        );
        val consequent = new Field(
                empty(), single(new Annotation(Type.of("Hello"), empty()))
        );
        return new StaticAnalysisRule("field_simple", single(antecedent), single(consequent), "field with annotation \"Demo\" must have annotation \"Hello\" ");
    }

    private static StaticAnalysisRule getRule_class_simple() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("Demo"), empty())),
                empty(), empty(), empty(), empty()
        );

        val consequent = new JavaClass(
                single(new Annotation(Type.of("Hello"), empty())),
                empty(), empty(), empty(), empty()
        );

        return new StaticAnalysisRule("class_simple", single(antecedent), single(consequent), "class with annotation \"Demo\" must have annotation \"Hello\" ");
    }

    private static StaticAnalysisRule getRule_OutgoingAndScope() {

        val antecedent = new JavaClass(
                empty(), empty(),
                new AggregateCondition(
                        new Method(empty(), single(new Annotation(Type.of("Outgoing"), empty())), empty()),
                        new Method(empty(), single(new Annotation(Type.of("Incoming"), empty())), empty()),
                        AggregateConditionOperation.OR
                ), empty(), empty()
        );

        val j1 = new JavaClass(single(new Annotation(Type.of("ApplicationScoped"), empty())),
                empty(), empty(), empty(), empty());

        val j2 = new JavaClass(single(new Annotation(Type.of("Dependent"), empty())),
                empty(), empty(), empty(), empty());

        val consequent = new AggregateCondition(j1, j2, AggregateConditionOperation.OR);

        return new StaticAnalysisRule("OutgoingAndScope", single(antecedent), consequent, "class with function with annotation \"Outgoing\" or annotation \"Incoming\" must have annotation \"ApplicationScoped\" or annotation \"Dependent\" ");
    }

    private static StaticAnalysisRule getRule_RestClientInjectField() {
        val antecedent = single(new Field(empty(), single(new Annotation(Type.of("RestClient"), empty()))));
        val consequent = single(new Field(empty(), single(new Annotation(Type.of("Inject"), empty()))));

        return new StaticAnalysisRule("RestClientInjectField", antecedent, consequent, "field with annotation \"RestClient\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_ClaimInjectField() {
        val antecedent = single(new Field(empty(), single(new Annotation(Type.of("Claim"), empty()))));
        val consequent = single(new Field(empty(), single(new Annotation(Type.of("Inject"), empty()))));
        return new StaticAnalysisRule("ClaimInjectField", antecedent, consequent, "field with annotation \"Claim\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_JsonWebTokenField() {
        val antecedent = single(new Field(Type.of("JsonWebToken"), empty()));
        val consequent = single(new Field(empty(), single(new Annotation(Type.of("Inject"), empty()))));
        return new StaticAnalysisRule("JsonWebTokenField", antecedent, consequent, "field with type \"JsonWebToken\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_PathParam() {
        val antecedent = new JavaClass(empty(), empty(), single(
                new Method(empty(), empty(), single(
                        new MethodParameter(empty(), single(new Annotation(Type.of("PathParam"), empty())))))
        ), empty(), empty());

        val j1 = new JavaClass(single(new Annotation(Type.of("Path"), empty())), empty(), empty(), empty(), empty());
        val j2 = new JavaClass(empty(), empty(), single(
                new Method(empty(), single(new Annotation(Type.of("Path"), empty())), empty())
        ), empty(), empty());

        val consequent = new AggregateCondition(j1, j2, AggregateConditionOperation.OR);

        return new StaticAnalysisRule("PathParam", single(antecedent), consequent, "class with function with parameter with annotation \"PathParam\" must have annotation \"Path\" or function with annotation \"Path\" ");
    }

    private static StaticAnalysisRule getRule_QueryMutationGraphQLAPI() {
        val m1 = new Method(empty(), single(new Annotation(Type.of("Query"), empty())), empty());
        val m2 = new Method(empty(), single(new Annotation(Type.of("Mutation"), empty())), empty());

        val antecedent = new JavaClass(empty(), empty(), new AggregateCondition(m1, m2, AggregateConditionOperation.OR), empty(), empty());

        val consequent = new JavaClass(single(new Annotation(Type.of("GraphQLApi"), empty())), empty(), empty(), empty(), empty());

        return new StaticAnalysisRule("QueryMutationGraphQLAPI", single(antecedent), single(consequent), "class with function with annotation \"Query\" or annotation \"Mutation\" must have annotation \"GraphQLApi\" ");
    }

    private static StaticAnalysisRule getRule_function_with_OR_in_consequent() {
        val antecedent = new Method(
                Type.of("C"),
                empty(),
                empty()
        );

        val method1 = new Method(
                empty(),
                single(new Annotation(Type.of("A"), empty())),
                empty()
        );

        val method2 = new Method(
                empty(),
                single(new Annotation(Type.of("B"), empty())),
                empty()
        );

        val consequent = new AggregateCondition(method1, method2, AggregateConditionOperation.OR);

        return new StaticAnalysisRule("function_with_OR_in_consequent", single(antecedent), consequent, "function with return type \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_field_with_OR_in_consequent() {
        val antecedent = new Field(
                Type.of("C"), empty()
        );

        val field1 = new Field(empty(), single(new Annotation(Type.of("A"), empty())));
        val field2 = new Field(empty(), single(new Annotation(Type.of("B"), empty())));

        val consequent = new AggregateCondition(field1, field2, AggregateConditionOperation.OR);

        return new StaticAnalysisRule("field_with_OR_in_consequent", single(antecedent), consequent, "field with type \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_class_field_with_OR_in_consequent() {
        val antecedent = new JavaClass(
                empty(), single(new Field(Type.of("C"), empty())), empty(), empty(), empty()
        );

        val consequent = new JavaClass(empty(),
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("A"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))), AggregateConditionOperation.OR
                ), empty(), empty(), empty());

        return new StaticAnalysisRule("class_field_with_OR_in_consequent", single(antecedent), single(consequent), "class with field with type \"C\" must have field with annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_annotation_with_parameter_both_type_and_name() {
        val antecedent = new Field(
                Type.of("K"), empty()
        );

        val consequent = new Field(
                empty(),
                single(
                        new Annotation(Type.of("A"),
                                single(new AnnotationParameter(Type.of("B"), Name.of("C"), empty())))
                ));

        return new StaticAnalysisRule("annotation_with_parameter_both_type_and_name", single(antecedent), single(consequent), "field with type \"K\" must have annotation \"A\" with parameter \"B C\" ");
    }

    private static StaticAnalysisRule getRule_annotation_with_parameter_name_only() {
        val antecedent = new Field(
                Type.of("K"), empty()
        );

        val consequent = new Field(
                empty(),
                single(
                        new Annotation(Type.of("A"),
                                single(new AnnotationParameter(empty(), Name.of("B"), empty())))
                ));

        return new StaticAnalysisRule("annotation_with_parameter_name_only", single(antecedent), single(consequent), "field with type \"K\" must have annotation \"A\" with parameter \"B\" ");
    }

    private static StaticAnalysisRule getRule_function_with_param_string() {
        val antecedent = new Method(
                empty(),
                empty(),
                single(new MethodParameter(Type.of("C"), empty()))
        );

        val method1 = new Method(
                empty(),
                single(new Annotation(Type.of("A"), empty())),
                empty()
        );

        val method2 = new Method(
                empty(),
                single(new Annotation(Type.of("B"), empty())),
                empty()
        );

        val consequent = new AggregateCondition(method1, method2, AggregateConditionOperation.OR);

        return new StaticAnalysisRule("function_with_param_string", single(antecedent), consequent, "function with parameter \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_function_with_multiple_ors() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty()
        );

        val method = new AggregateCondition(
                new AggregateCondition(
                        new Method(empty(), single(new Annotation(Type.of("B"), empty())), empty()),
                        new Method(empty(), single(new Annotation(Type.of("C"), empty())), empty()),
                        AggregateConditionOperation.OR
                ),
                new Method(empty(), single(new Annotation(Type.of("D"), empty())), empty()),
                AggregateConditionOperation.OR
        );

        val consequent = new JavaClass(empty(), empty(), method, empty(), empty());

        return new StaticAnalysisRule("function_with_multiple_ors", single(antecedent), single(consequent), "class with annotation \"A\" must have function with annotation \"B\" or annotation \"C\" or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_class_with_multiple_ors() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty()
        );

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new JavaClass(
                                single(new Annotation(Type.of("B"), empty())),
                                empty(), empty(), empty(), empty()),
                        new JavaClass(
                                single(new Annotation(Type.of("C"), empty())),
                                empty(), empty(), empty(), empty()
                        ), AggregateConditionOperation.OR
                ),
                new JavaClass(
                        single(new Annotation(Type.of("D"), empty())),
                        empty(), empty(), empty(), empty()
                ), AggregateConditionOperation.OR
        );

        return new StaticAnalysisRule("class_with_multiple_ors", single(antecedent), consequent, "class with annotation \"A\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_field_with_multiple_ors() {
        val antecedent = new Field(empty(), single(new Annotation(Type.of("A"), empty())));

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        AggregateConditionOperation.OR),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR);

        return new StaticAnalysisRule("field_with_multiple_ors", single(antecedent), consequent, "field with annotation \"A\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_function_with_multiple_ors_parenthesis() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty()
        );

        val method = new AggregateCondition(
                new AggregateCondition(
                        new Method(empty(), single(new Annotation(Type.of("B"), empty())), empty()),
                        new Method(empty(), single(new Annotation(Type.of("C"), empty())), empty()),
                        AggregateConditionOperation.OR
                ),
                new Method(empty(), single(new Annotation(Type.of("D"), empty())), empty()),
                AggregateConditionOperation.OR
        );

        val consequent = new JavaClass(empty(), empty(), method, empty(), empty());

        return new StaticAnalysisRule("function_with_multiple_ors_parenthesis", single(antecedent), single(consequent), "class with annotation \"A\" must have function with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ");
    }

    private static StaticAnalysisRule getRule_field_with_multiple_ors_parenthesis() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty()
        );

        val field = new AggregateCondition(
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        AggregateConditionOperation.OR
                ),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR
        );

        val consequent = new JavaClass(empty(), field, empty(), empty(), empty());

        return new StaticAnalysisRule("field_with_multiple_ors_parenthesis", single(antecedent), single(consequent), "class with annotation \"A\" must have field with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ");
    }

    private static StaticAnalysisRule getRule_class_with_multiple_ors_parenthesis() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty()
        );

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new JavaClass(
                                single(new Annotation(Type.of("B"), empty())),
                                empty(), empty(), empty(), empty()),
                        new JavaClass(
                                single(new Annotation(Type.of("C"), empty())),
                                empty(), empty(), empty(), empty()
                        ), AggregateConditionOperation.OR
                ),
                new JavaClass(
                        single(new Annotation(Type.of("D"), empty())),
                        empty(), empty(), empty(), empty()
                ), AggregateConditionOperation.OR
        );

        return new StaticAnalysisRule("class_with_multiple_ors_parenthesis", single(antecedent), consequent, "class with annotation \"A\" must have (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ");
    }

    private static StaticAnalysisRule getRule_mixingAll() {
        val antecedent = new JavaClass(single(new Annotation(Type.of("A"), empty())), empty(), empty(), empty(), empty());

        val m1 = new Method(empty(), single(new Annotation(Type.of("B"), empty())), empty());
        val m2 = new Method(empty(), single(new Annotation(Type.of("C"), empty())), empty());
        val m3 = new Method(empty(), single(new Annotation(Type.of("D"), empty())), empty());

        val methods = new AggregateCondition(
                new AggregateCondition(m1, m2, AggregateConditionOperation.OR),
                m3,
                AggregateConditionOperation.OR
        );

        val f1 = new Field(Type.of("X"), empty());
        val f2 = new Field(Type.of("Y"), empty());

        val fields = new AggregateCondition(f1, f2, AggregateConditionOperation.OR);

        val j1 = new JavaClass(single(new Annotation(Type.of("M"), empty())), empty(), empty(), empty(), empty());
        val j2 = new JavaClass(single(new Annotation(Type.of("L"), empty())), empty(), empty(), empty(), empty());

        val classes = new AggregateCondition(j1, j2, AggregateConditionOperation.OR);

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new JavaClass(empty(), empty(), methods, empty(), empty()),
                        new JavaClass(empty(), fields, empty(), empty(), empty()),
                        AggregateConditionOperation.OR),
                classes,
                AggregateConditionOperation.OR
        );

        return new StaticAnalysisRule("mixingAll", single(antecedent), consequent, "class with annotation \"A\" must have (function with annotation \"B\" or annotation \"C\" or annotation \"D\" ) or (field with type \"X\" or type \"Y\" ) or (annotation \"M\" or annotation \"L\" ) ");
    }

    private static StaticAnalysisRule getRule_antecedent_class_with_or() {

        val j1 = new JavaClass(single(new Annotation(Type.of("B"), empty())), empty(), empty(), empty(), empty());
        val j2 = new JavaClass(single(new Annotation(Type.of("C"), empty())), empty(), empty(), empty(), empty());
        val j3 = new JavaClass(single(new Annotation(Type.of("D"), empty())), empty(), empty(), empty(), empty());

        val consequent = new JavaClass(single(new Annotation(Type.of("A"), empty())), empty(), empty(), empty(), empty());

        val antecedent = new AggregateCondition(
                new AggregateCondition(j1, j2, AggregateConditionOperation.OR),
                j3, AggregateConditionOperation.OR
        );

        return new StaticAnalysisRule("antecedent_class_with_or", antecedent, single(consequent), "class with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) must have annotation \"A\" ");
    }

    private static StaticAnalysisRule getRule_antecedent_function_with_or_plus_consequent_with_or() {
        String ruleString = "function with return type \"B\" or parameter \"C\" or annotation \"D\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ";

        val m1a = new Method(
                Type.of("B"), empty(), empty()
        );

        val m2a = new Method(
                empty(), empty(), single(new MethodParameter(Type.of("C"), empty()))
        );

        val m3a = new Method(
                empty(), single(new Annotation(Type.of("D"), empty())), empty()
        );

        val antecedent = new AggregateCondition(new AggregateCondition(m1a, m2a, AggregateConditionOperation.OR),
                m3a, AggregateConditionOperation.OR);

        val m1c = new Method(
                empty(), single(new Annotation(Type.of("B"), empty())), empty()
        );
        val m2c = new Method(
                empty(), single(new Annotation(Type.of("C"), empty())), empty()
        );
        val m3c = new Method(
                empty(), single(new Annotation(Type.of("D"), empty())), empty()
        );

        val consequent = new AggregateCondition(new AggregateCondition(m1c, m2c, AggregateConditionOperation.OR),
                m3c, AggregateConditionOperation.OR);

        return new StaticAnalysisRule("antecedent_function_with_or_plus_consequent_with_or", antecedent, consequent, ruleString);
    }

    private static StaticAnalysisRule getRule_antecedent_field_with_or_plus_consequent_with_or() {
        val antecedent = new AggregateCondition(
                new Field(Type.of("B"), empty()),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR
        );

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        AggregateConditionOperation.OR),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR);

        return new StaticAnalysisRule("antecedent_field_with_or_plus_consequent_with_or", antecedent, consequent, "field with type \"B\" or annotation \"D\" must have (annotation \"B\" or annotation \"C\" ) or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_antecedent_field_with_or_plus_consequent_with_or_parenthesis() {
        val antecedent = new AggregateCondition(
                new Field(Type.of("B"), empty()),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR
        );

        val consequent = new AggregateCondition(
                new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                        AggregateConditionOperation.OR),
                AggregateConditionOperation.OR);

        return new StaticAnalysisRule("antecedent_field_with_or_plus_consequent_with_or_parenthesis", antecedent, consequent, "field with type \"B\" or annotation \"D\" must have annotation \"B\" or (annotation \"C\" or annotation \"D\" ) ");
    }

    private static StaticAnalysisRule getRule_antecedent_field_with_and_plus_consequent_with_and() {
        val antecedent = new AggregateCondition(
                new Field(Type.of("B"), empty()),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.AND
        );

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        AggregateConditionOperation.AND),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.AND);

        return new StaticAnalysisRule("antecedent_field_with_and_plus_consequent_with_and", antecedent, consequent, "field with type \"B\" and annotation \"D\" must have (annotation \"B\" and annotation \"C\" ) and annotation \"D\" ");
    }

}
