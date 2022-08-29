package ca.ualberta.smr.parsing;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import lombok.val;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

import static ca.ualberta.smr.model.javaelements.AggregateCondition.empty;
import static ca.ualberta.smr.model.javaelements.AggregateCondition.single;
import static ca.ualberta.smr.model.javaelements.AggregateConditionOperation.*;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;
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
        map.put("annotation_with_or_shortcut", getRule_annotation_with_or_shortcut());
        map.put("annotation_with_xor_shortcut", getRule_annotation_with_xor_shortcut());
        map.put("class_with_multiple_ors", getRule_class_with_multiple_ors());
        map.put("field_with_multiple_ors", getRule_field_with_multiple_ors());
        map.put("field_with_multiple_ors_parenthesis", getRule_field_with_multiple_ors_parenthesis());
        map.put("antecedent_field_with_or_plus_consequent_with_or_parenthesis", getRule_antecedent_field_with_or_plus_consequent_with_or_parenthesis());
        map.put("class_with_multiple_ors_parenthesis", getRule_class_with_multiple_ors_parenthesis());
        map.put("antecedent_class_with_or", getRule_antecedent_class_with_or());
        map.put("field_with_or_plus_consequent_with_or", getRule_antecedent_field_with_or_plus_consequent_with_or());
        map.put("antecedent_field_with_and_plus_consequent_with_and", getRule_antecedent_field_with_and_plus_consequent_with_and());
        map.put("class_method_override_no_params", getRule_class_method_override_no_params());
        map.put("class_method_override_one_param", getRule_class_method_override_one_param());
        map.put("class_method_override_many_params", getRule_class_method_override_many_params());
        map.put("class_bean_declaration_antecedent", getRule_class_bean_declaration_antecedent());
        map.put("class_bean_declaration_consequent", getRule_class_bean_declaration_consequent());
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

    private static StaticAnalysisRule getRule_class_bean_declaration_antecedent() {
        val antecedent = new JavaClass(
                empty(), empty(), empty(), empty(), empty(), empty(), single(new JavaClass.BeanDeclaration())
        );

        val consequent = new JavaClass(
                single(
                        new Annotation(Type.of("Foo"), empty())
                ), empty(), empty(), empty(), empty(), empty(), empty()
        );

        return new StaticAnalysisRule("class_bean_declaration_antecedent",
                single(antecedent),
                single(consequent),
                "class with bean declaration must have annotation \"Foo\" ");
    }

    private static StaticAnalysisRule getRule_class_bean_declaration_consequent() {
        val antecedent = new JavaClass(
                single(
                        new Annotation(Type.of("Foo"), empty())
                ), empty(), empty(), empty(), empty(), empty(), empty()
        );

        val consequent = new JavaClass(
                empty(), empty(), empty(), empty(), empty(), empty(), single(new JavaClass.BeanDeclaration())
        );

        return new StaticAnalysisRule("class_bean_declaration_consequent",
                single(antecedent),
                single(consequent),
                "class with annotation \"Foo\" must have bean declaration ");
    }

    private static StaticAnalysisRule getRule_class_method_override_no_params() {
        val antecedent = new JavaClass(
                empty(), empty(), empty(), Type.InterfaceType.of("Foo"), empty(), empty(), empty()
        );

        val consequent = new JavaClass(
                empty(), empty(), empty(), empty(), empty(), single(new JavaClass.OverriddenMethod("foobar", Collections.emptyList())), empty()
        );

        return new StaticAnalysisRule("class_method_override_no_params",
                single(antecedent),
                single(consequent),
                "class with extension of \"Foo\" must have overridden method \"foobar()\" ");
    }

    private static StaticAnalysisRule getRule_class_method_override_one_param() {
        val antecedent = new JavaClass(
                empty(), empty(), empty(), Type.InterfaceType.of("Foo"), empty(), empty(), empty()
        );

        val consequent = new JavaClass(
                empty(), empty(), empty(), empty(), empty(), single(
                new JavaClass.OverriddenMethod(
                        "foobar",
                        Collections.singletonList(new MethodParameter(
                                Type.of("String"), empty()
                        )))),
                empty()
        );

        return new StaticAnalysisRule("class_method_override_one_param",
                single(antecedent),
                single(consequent),
                "class with extension of \"Foo\" must have overridden method \"foobar(String)\" ");
    }

    private static StaticAnalysisRule getRule_class_method_override_many_params() {
        val antecedent = new JavaClass(
                empty(), empty(), empty(), Type.InterfaceType.of("Foo"), empty(), empty(), empty()
        );

        val consequent = new JavaClass(
                empty(), empty(), empty(), empty(), empty(), single(new JavaClass.OverriddenMethod("foobar",
                listOf(
                        new MethodParameter(Type.of("String"), empty()),
                        new MethodParameter(Type.of("int"), empty()),
                        new MethodParameter(Type.of("double"), empty()),
                        new MethodParameter(Type.of("Custom"), empty())
                ))),
                empty()
        );

        return new StaticAnalysisRule("class_method_override_many_params",
                single(antecedent),
                single(consequent),
                "class with extension of \"Foo\" must have overridden method \"foobar(String, int, double, Custom)\" ");
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
        return parser.start();
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
        return new StaticAnalysisRule("field_simple",
                single(antecedent),
                single(consequent),
                "field with annotation \"Demo\" must have annotation \"Hello\" "
        );
    }

    private static StaticAnalysisRule getRule_class_simple() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("Demo"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty()
        );

        val consequent = new JavaClass(
                single(new Annotation(Type.of("Hello"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty()
        );

        return new StaticAnalysisRule("class_simple",
                single(antecedent),
                single(consequent),
                "class with annotation \"Demo\" must have annotation \"Hello\" ");
    }

    private static StaticAnalysisRule getRule_OutgoingAndScope() {

        val antecedent = new JavaClass(
                empty(), empty(),
                new AggregateCondition(
                        new Method(empty(), single(new Annotation(Type.of("Outgoing"), empty())), empty()),
                        new Method(empty(), single(new Annotation(Type.of("Incoming"), empty())), empty()),
                        AggregateConditionOperation.OR,
                        ProgramElement.ProgramElementType.METHOD
                ), empty(), empty(), empty(), empty()
        );

        val j1 = new JavaClass(single(new Annotation(Type.of("ApplicationScoped"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty());

        val j2 = new JavaClass(single(new Annotation(Type.of("Dependent"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty());

        val consequent = new AggregateCondition(j1, j2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS);

        return new StaticAnalysisRule("OutgoingAndScope", single(antecedent), consequent, "class with function with annotation \"Outgoing\" or annotation \"Incoming\" must have annotation \"ApplicationScoped\" or annotation \"Dependent\" ");
    }

    private static StaticAnalysisRule getRule_RestClientInjectField() {
        val antecedent = single(new Field(empty(), single(new Annotation(Type.of("RestClient"), empty()))));
        val consequent = single(new Field(empty(), single(new Annotation(Type.of("Inject"), empty()))));

        return new StaticAnalysisRule("RestClientInjectField", antecedent, consequent,
                "field with annotation \"RestClient\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_ClaimInjectField() {
        val antecedent = single(new Field(empty(), single(new Annotation(Type.of("Claim"), empty()))));
        val consequent = single(new Field(empty(), single(new Annotation(Type.of("Inject"), empty()))));
        return new StaticAnalysisRule("ClaimInjectField", antecedent, consequent,
                "field with annotation \"Claim\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_JsonWebTokenField() {
        val antecedent = single(new Field(Type.of("JsonWebToken"), empty()));
        val consequent = single(new Field(empty(), single(new Annotation(Type.of("Inject"), empty()))));
        return new StaticAnalysisRule("JsonWebTokenField", antecedent, consequent,
                "field with type \"JsonWebToken\" must have annotation \"Inject\" ");
    }

    private static StaticAnalysisRule getRule_PathParam() {
        val antecedent = new JavaClass(empty(), empty(), single(
                new Method(empty(), empty(), single(
                        new MethodParameter(empty(), single(new Annotation(Type.of("PathParam"), empty())))))
        ), empty(), empty(), empty(), empty());

        val j1 = new JavaClass(single(new Annotation(Type.of("Path"), empty())), empty(), empty(), empty(), empty(), empty(), empty());
        val j2 = new JavaClass(empty(), empty(), single(
                new Method(empty(), single(new Annotation(Type.of("Path"), empty())), empty())
        ), empty(), empty(), empty(), empty());

        val consequent = new AggregateCondition(j1, j2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS);

        return new StaticAnalysisRule("PathParam", single(antecedent), consequent,
                "class with function with parameter with annotation \"PathParam\" must have annotation \"Path\" or function with annotation \"Path\" ");
    }

    private static StaticAnalysisRule getRule_QueryMutationGraphQLAPI() {
        val m1 = new Method(empty(), single(new Annotation(Type.of("Query"), empty())), empty());
        val m2 = new Method(empty(), single(new Annotation(Type.of("Mutation"), empty())), empty());

        val antecedent = new JavaClass(empty(), empty(),
                new AggregateCondition(m1, m2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD),
                empty(), empty(), empty(), empty());

        val consequent = new JavaClass(single(new Annotation(Type.of("GraphQLApi"), empty())), empty(), empty(), empty(), empty(), empty(), empty());

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

        val consequent = new AggregateCondition(method1, method2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD);

        return new StaticAnalysisRule("function_with_OR_in_consequent", single(antecedent), consequent, "function with return type \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_field_with_OR_in_consequent() {
        val antecedent = new Field(
                Type.of("C"), empty()
        );

        val field1 = new Field(empty(), single(new Annotation(Type.of("A"), empty())));
        val field2 = new Field(empty(), single(new Annotation(Type.of("B"), empty())));

        val consequent = new AggregateCondition(field1, field2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD);

        return new StaticAnalysisRule("field_with_OR_in_consequent", single(antecedent), consequent, "field with type \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_class_field_with_OR_in_consequent() {
        val antecedent = new JavaClass(
                empty(), single(new Field(Type.of("C"), empty())), empty(), empty(), empty(), empty(), empty()
        );

        val consequent = new JavaClass(empty(),
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("A"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        AggregateConditionOperation.OR,
                        ProgramElement.ProgramElementType.FIELD
                ), empty(), empty(), empty(), empty(), empty());

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

        return new StaticAnalysisRule("annotation_with_parameter_both_type_and_name", single(antecedent), single(consequent),
                "field with type \"K\" must have annotation \"A\" with parameter \"B C\" ");
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

        return new StaticAnalysisRule("annotation_with_parameter_name_only", single(antecedent), single(consequent),
                "field with type \"K\" must have annotation \"A\" with parameter \"B\" ");
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

        val consequent = new AggregateCondition(method1, method2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD);

        return new StaticAnalysisRule("function_with_param_string", single(antecedent), consequent,
                "function with parameter \"C\" must have annotation \"A\" or annotation \"B\" ");
    }

    private static StaticAnalysisRule getRule_function_with_multiple_ors() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty()
        );

        val method = new AggregateCondition(
                new AggregateCondition(
                        new Method(empty(), single(new Annotation(Type.of("B"), empty())), empty()),
                        new Method(empty(), single(new Annotation(Type.of("C"), empty())), empty()),
                        AggregateConditionOperation.OR,
                        ProgramElement.ProgramElementType.METHOD
                ),
                new Method(empty(), single(new Annotation(Type.of("D"), empty())), empty()),
                AggregateConditionOperation.OR,
                ProgramElement.ProgramElementType.METHOD
        );

        val consequent = new JavaClass(empty(), empty(), method, empty(), empty(), empty(), empty());

        return new StaticAnalysisRule("function_with_multiple_ors", single(antecedent), single(consequent),
                "class with annotation \"A\" must have function with annotation \"B\" or annotation \"C\" or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_class_with_multiple_ors() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty()
        );

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new JavaClass(
                                single(new Annotation(Type.of("B"), empty())),
                                empty(), empty(), empty(), empty(), empty(), empty()),
                        new JavaClass(
                                single(new Annotation(Type.of("C"), empty())),
                                empty(), empty(), empty(), empty(), empty(), empty()
                        ), AggregateConditionOperation.OR,
                        ProgramElement.ProgramElementType.CLASS
                ),
                new JavaClass(
                        single(new Annotation(Type.of("D"), empty())),
                        empty(), empty(), empty(), empty(), empty(), empty()
                ), AggregateConditionOperation.OR,
                ProgramElement.ProgramElementType.CLASS
        );

        return new StaticAnalysisRule("class_with_multiple_ors", single(antecedent), consequent,
                "class with annotation \"A\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_field_with_multiple_ors() {
        val antecedent = new Field(empty(), single(new Annotation(Type.of("A"), empty())));

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD);

        return new StaticAnalysisRule("field_with_multiple_ors", single(antecedent), consequent,
                "field with annotation \"A\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_function_with_multiple_ors_parenthesis() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty()
        );

        val method = new AggregateCondition(
                new AggregateCondition(
                        new Method(empty(), single(new Annotation(Type.of("B"), empty())), empty()),
                        new Method(empty(), single(new Annotation(Type.of("C"), empty())), empty()),
                        AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD
                ),
                new Method(empty(), single(new Annotation(Type.of("D"), empty())), empty()),
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD
        );

        val consequent = new JavaClass(empty(), empty(), method, empty(), empty(), empty(), empty());

        return new StaticAnalysisRule("function_with_multiple_ors_parenthesis", single(antecedent), single(consequent),
                "class with annotation \"A\" must have function with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ");
    }

    private static StaticAnalysisRule getRule_field_with_multiple_ors_parenthesis() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty()
        );

        val field = new AggregateCondition(
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD
                ),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD
        );

        val consequent = new JavaClass(empty(), field, empty(), empty(), empty(), empty(), empty());

        return new StaticAnalysisRule("field_with_multiple_ors_parenthesis", single(antecedent), single(consequent),
                "class with annotation \"A\" must have field with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ");
    }

    private static StaticAnalysisRule getRule_class_with_multiple_ors_parenthesis() {
        val antecedent = new JavaClass(
                single(new Annotation(Type.of("A"), empty())),
                empty(), empty(), empty(), empty(), empty(), empty()
        );

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new JavaClass(
                                single(new Annotation(Type.of("B"), empty())),
                                empty(), empty(), empty(), empty(), empty(), empty()),
                        new JavaClass(
                                single(new Annotation(Type.of("C"), empty())),
                                empty(), empty(), empty(), empty(), empty(), empty()
                        ), AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS
                ),
                new JavaClass(
                        single(new Annotation(Type.of("D"), empty())),
                        empty(), empty(), empty(), empty(), empty(), empty()
                ), AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS
        );

        return new StaticAnalysisRule("class_with_multiple_ors_parenthesis", single(antecedent), consequent,
                "class with annotation \"A\" must have (annotation \"B\" or annotation \"C\" or annotation \"D\" ) ");
    }

    private static StaticAnalysisRule getRule_mixingAll() {
        val antecedent = new JavaClass(single(new Annotation(Type.of("A"), empty())), empty(), empty(), empty(), empty(), empty(), empty());

        val m1 = new Method(empty(), single(new Annotation(Type.of("B"), empty())), empty());
        val m2 = new Method(empty(), single(new Annotation(Type.of("C"), empty())), empty());
        val m3 = new Method(empty(), single(new Annotation(Type.of("D"), empty())), empty());

        val methods = new AggregateCondition(
                new AggregateCondition(m1, m2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD),
                m3,
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD
        );

        val f1 = new Field(Type.of("X"), empty());
        val f2 = new Field(Type.of("Y"), empty());

        val fields = new AggregateCondition(f1, f2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD);

        val j1 = new JavaClass(single(new Annotation(Type.of("M"), empty())), empty(), empty(), empty(), empty(), empty(), empty());
        val j2 = new JavaClass(single(new Annotation(Type.of("L"), empty())), empty(), empty(), empty(), empty(), empty(), empty());

        val classes = new AggregateCondition(j1, j2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS);

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new JavaClass(empty(), empty(), methods, empty(), empty(), empty(), empty()),
                        new JavaClass(empty(), fields, empty(), empty(), empty(), empty(), empty()),
                        AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS),
                classes,
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS
        );

        return new StaticAnalysisRule("mixingAll", single(antecedent), consequent,
                "class with annotation \"A\" must have (function with annotation \"B\" or annotation \"C\" or annotation \"D\" ) or (field with type \"X\" or type \"Y\" ) or (annotation \"M\" or annotation \"L\" ) ");
    }

    private static StaticAnalysisRule getRule_antecedent_class_with_or() {

        val j1 = new JavaClass(single(new Annotation(Type.of("B"), empty())), empty(), empty(), empty(), empty(), empty(), empty());
        val j2 = new JavaClass(single(new Annotation(Type.of("C"), empty())), empty(), empty(), empty(), empty(), empty(), empty());
        val j3 = new JavaClass(single(new Annotation(Type.of("D"), empty())), empty(), empty(), empty(), empty(), empty(), empty());

        val consequent = new JavaClass(single(new Annotation(Type.of("A"), empty())), empty(), empty(), empty(), empty(), empty(), empty());

        val antecedent = new AggregateCondition(
                new AggregateCondition(j1, j2, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS),
                j3, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.CLASS
        );

        return new StaticAnalysisRule("antecedent_class_with_or", antecedent, single(consequent),
                "class with (annotation \"B\" or annotation \"C\" or annotation \"D\" ) must have annotation \"A\" ");
    }

    private static StaticAnalysisRule getRule_antecedent_function_with_or_plus_consequent_with_or() {
        val m1a = new Method(
                Type.of("B"), empty(), empty()
        );

        val m2a = new Method(
                empty(), empty(), single(new MethodParameter(Type.of("C"), empty()))
        );

        val m3a = new Method(
                empty(), single(new Annotation(Type.of("D"), empty())), empty()
        );

        val antecedent = new AggregateCondition(new AggregateCondition(m1a, m2a, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD),
                m3a, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD);

        val m1c = new Method(
                empty(), single(new Annotation(Type.of("B"), empty())), empty()
        );
        val m2c = new Method(
                empty(), single(new Annotation(Type.of("C"), empty())), empty()
        );
        val m3c = new Method(
                empty(), single(new Annotation(Type.of("D"), empty())), empty()
        );

        val consequent = new AggregateCondition(new AggregateCondition(m1c, m2c, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD),
                m3c, AggregateConditionOperation.OR, ProgramElement.ProgramElementType.METHOD);

        return new StaticAnalysisRule("antecedent_function_with_or_plus_consequent_with_or", antecedent, consequent,
                "function with return type \"B\" or parameter \"C\" or annotation \"D\" must have annotation \"B\" or annotation \"C\" or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_antecedent_field_with_or_plus_consequent_with_or() {
        val antecedent = new AggregateCondition(
                new Field(Type.of("B"), empty()),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD
        );

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD);

        return new StaticAnalysisRule("antecedent_field_with_or_plus_consequent_with_or", antecedent, consequent,
                "field with type \"B\" or annotation \"D\" must have (annotation \"B\" or annotation \"C\" ) or annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_antecedent_field_with_or_plus_consequent_with_or_parenthesis() {
        val antecedent = new AggregateCondition(
                new Field(Type.of("B"), empty()),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD
        );

        val consequent = new AggregateCondition(
                new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                        AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD),
                AggregateConditionOperation.OR, ProgramElement.ProgramElementType.FIELD);

        return new StaticAnalysisRule("antecedent_field_with_or_plus_consequent_with_or_parenthesis", antecedent, consequent,
                "field with type \"B\" or annotation \"D\" must have annotation \"B\" or (annotation \"C\" or annotation \"D\" ) ");
    }

    private static StaticAnalysisRule getRule_antecedent_field_with_and_plus_consequent_with_and() {
        val antecedent = new AggregateCondition(
                new Field(Type.of("B"), empty()),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AND, ProgramElement.ProgramElementType.FIELD
        );

        val consequent = new AggregateCondition(
                new AggregateCondition(
                        new Field(empty(), single(new Annotation(Type.of("B"), empty()))),
                        new Field(empty(), single(new Annotation(Type.of("C"), empty()))),
                        AND, ProgramElement.ProgramElementType.FIELD),
                new Field(empty(), single(new Annotation(Type.of("D"), empty()))),
                AND, ProgramElement.ProgramElementType.FIELD);

        return new StaticAnalysisRule("antecedent_field_with_and_plus_consequent_with_and", antecedent, consequent,
                "field with type \"B\" and annotation \"D\" must have (annotation \"B\" and annotation \"C\" ) and annotation \"D\" ");
    }

    private static StaticAnalysisRule getRule_annotation_with_or_shortcut() {
        val antecedent = single(
                new Field(empty(), single(
                        new Annotation(
                                new AggregateCondition(new AggregateCondition(
                                        new Type("a.b.c.X"), new Type("a.b.c.Y"), OR
                                ), new Type("a.b.c.Z"), OR), empty()
                        )
                ))
        );

        val consequent = single(
                new Field(empty(), single(new Annotation(Type.of("x.y.z.A"), empty())))
        );

        return new StaticAnalysisRule("annotation_with_or_shortcut", antecedent, consequent,
                "field with annotation \"a.b.c.[X|Y|Z]\" must have annotation \"x.y.z.[A]\" ");
    }

    private static StaticAnalysisRule getRule_annotation_with_xor_shortcut() {
        val antecedent = single(
                new Field(empty(), single(
                        new Annotation(
                                new AggregateCondition(new AggregateCondition(
                                        new Type("a.b.c.X"), new Type("a.b.c.Y"), XOR
                                ), new Type("a.b.c.Z"), XOR), empty()
                        )
                ))
        );

        val consequent = single(
                new Field(empty(), single(new Annotation(Type.of("x.y.z.A"), empty())))
        );

        return new StaticAnalysisRule("annotation_with_xor_shortcut", antecedent, consequent,
                "field with annotation \"a.b.c.[X^Y^Z]\" must have annotation \"x.y.z.[A]\" ");
    }

}
