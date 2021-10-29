package ca.ualberta.smr.grammar;

import ca.ualberta.grammar.RulepadGrammarLexer;
import ca.ualberta.grammar.RulepadGrammarParser;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.rules.DummyListener;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.*;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.any;
import static ca.ualberta.smr.model.javaelements.Condition.single;
import static org.junit.jupiter.api.Assertions.*;

public class RulePadTest {

    void parseAndCheckRule(String rulePadRule, StaticAnalysisRule expected) {
        final ParseTree tree = getTree(rulePadRule);

        final ParseTreeWalker walker = new ParseTreeWalker();
        final ConcreteRulePadGrammarListener listener = new ConcreteRulePadGrammarListener("");

        walker.walk(new DummyListener(), tree);

        final StaticAnalysisRule actualRule = listener.getRule();

        // Construction of the expected rule ends here
        assertEquals(expected, actualRule);
    }

    @Test
    void test_input_1() {
        final String ruleString = RULEPAD_RULES_MAP.get("field_simple");
        // Construction of the expected rule
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("Demo")));
        final Field consequent = new Field();
        consequent.annotations().add(single(annotation("Hello")));
        final StaticAnalysisRule expected = new StaticAnalysisRule("", antecedent, single(consequent));
        // Construction of the expected rule ends here
        parseAndCheckRule(ruleString, expected);
    }

    @Test
    void test_input_2() {
        final String ruleString = RULEPAD_RULES_MAP.get("class_simple");
        // Construction of the expected rule
        final JavaClass antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("Demo")));
        final JavaClass consequent = new JavaClass();
        consequent.annotations().add(single(annotation("Hello")));
        final StaticAnalysisRule expected = new StaticAnalysisRule("", antecedent, single(consequent));
        // Construction of the expected rule ends here
        parseAndCheckRule(ruleString, expected);
    }

    @Test
    void test_input_3() {
        final String ruleString = RULEPAD_RULES_MAP.get("function_simple");
        // Construction of the expected rule
        final Method antecedent = new Method();
        antecedent.annotations().add(single(annotation("Demo")));
        final Method consequent = new Method();
        consequent.annotations().add(single(annotation("Hello")));
        final StaticAnalysisRule expected = new StaticAnalysisRule("", antecedent, single(consequent));
        // Construction of the expected rule ends here
        parseAndCheckRule(ruleString, expected);
    }

    @Test
    void test_input_4() {
        final String ruleString = RULEPAD_RULES_MAP.get("OutgoingAndScope");
        parseAndCheckRule(ruleString, getRule_OutgoingAndScope());
    }

    @Test
    void test_input_5() {
        final String ruleString = RULEPAD_RULES_MAP.get("RestClientInjectField");
        parseAndCheckRule(ruleString, getRule_RestClientInjectField());
    }

    @Test
    void test_input_6() {
        final String ruleString = RULEPAD_RULES_MAP.get("ClaimInjectField");
        parseAndCheckRule(ruleString, getRule_ClaimInjectField());
    }

    @Test
    void test_input_7() {
        final String ruleString = RULEPAD_RULES_MAP.get("JsonWebTokenField");
        parseAndCheckRule(ruleString, getRule_JsonWebTokenField());
    }

    @Test
    void test_input_8() {
        final String ruleString = RULEPAD_RULES_MAP.get("PathParam");
        parseAndCheckRule(ruleString, getRule_PathParam());
    }
    @Test
    void test_input_9() {
        final String ruleString = RULEPAD_RULES_MAP.get("QueryMutationGraphQLAPI");
        parseAndCheckRule(ruleString, getRule_QueryMutationGraphQLAPI());
    }


    private static ParseTree getTree(String input) {
        final RulepadGrammarLexer lexer = new RulepadGrammarLexer(CharStreams.fromString(input));
        final RulepadGrammarParser parser = new RulepadGrammarParser(new CommonTokenStream(lexer));
//        parser.setTrace(true);
        return parser.inputSentence();
    }

    private static final Map<String, String> RULEPAD_RULES_MAP = getRulePadRulesMap();

    private static Map<String, String> getRulePadRulesMap() {
        final Map<String, String> rulePadRuleStrings = new HashMap<>();
        rulePadRuleStrings.put("class_simple", "class with annotation \"Demo\" must have annotation \"Hello\" ");
        rulePadRuleStrings.put("field_simple", "field with annotation \"Demo\" must have annotation \"Hello\" ");
        rulePadRuleStrings.put("function_simple", "function with annotation \"Demo\" must have annotation \"Hello\" ");

        rulePadRuleStrings.put("OutgoingAndScope", "class with function with annotation \"Outgoing\" or annotation \"Incoming\" must have annotation \"ApplicationScoped\" or annotation \"Dependent\" ");
        rulePadRuleStrings.put("RestClientInjectField", "field with annotation \"RestClient\" must have annotation \"Inject\" ");
        rulePadRuleStrings.put("ClaimInjectField", "field with annotation \"Claim\" must have annotation \"Inject\" ");
        rulePadRuleStrings.put("JsonWebTokenField", "field with type \"JsonWebToken\" must have annotation \"Inject\" ");
        rulePadRuleStrings.put("PathParam", "class with function with parameter with annotation \"PathParam\" must have annotation \"Path\" or function with annotation \"Path\" ");
        rulePadRuleStrings.put("QueryMutationGraphQLAPI", "class with function with annotation \"Query\" or annotation \"Mutation\" must have annotation \"GraphQLApi\" ");

        return rulePadRuleStrings;
    }


    private StaticAnalysisRule getRule_OutgoingAndScope() {
        // if a method is annotated with @Outgoing or @Incoming
        // then the class must be annotation with @ApplicationScoped or @Dependent

        final Method method = new Method();
        method.annotations().add(any(annotation("Outgoing"), annotation("Incoming")));

        final JavaClass antecedent = new JavaClass();
        antecedent.method(Condition.single(method));

        final JavaClass javaClass = new JavaClass();
        javaClass.annotations().add(
                any(annotation("ApplicationScoped"), annotation("Dependent"))
        );

        Condition<? extends AnalysisItem> consequent = single(javaClass);
        return new StaticAnalysisRule("", antecedent, consequent);
    }

    private StaticAnalysisRule getRule_RestClientInjectField() {
        // if field has annotation @RestClient
        // then it must have @Inject
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("RestClient")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("", antecedent, consequent);
    }

    private StaticAnalysisRule getRule_ClaimInjectField() {
        // if field has annotation @Claim
        // then it must have @Inject
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("Claim")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("", antecedent, consequent);
    }

    private StaticAnalysisRule getRule_JsonWebTokenField() {
        // if field is of type JsonWebToken
        // then it must have annotation @Inject
        final Field antecedent = new Field();
        antecedent.type(single(new Type("JsonWebToken")));

        final Field field = new Field();
        field.annotations().add(single(annotation("Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("", antecedent, consequent);
    }

    private StaticAnalysisRule getRule_PathParam() {
        // if method parameter has @PathParam
        // then either method or class must have @Path

        final Method antecedentMethod = new Method();
        final MethodParameter param = new MethodParameter();
        param.annotations().add(single(annotation("PathParam")));
        antecedentMethod.parameters()
                .add(single(param));

        final JavaClass antecedent = new JavaClass();
        antecedent.method(single(antecedentMethod));

        final JavaClass klass = new JavaClass();
        klass.annotations().add(single(annotation("Path")));

        final Method method = new Method();
        method.annotations().add(single(annotation("Path")));

        final Condition<? extends AnalysisItem> consequent = any(
                klass, method
        );

        return new StaticAnalysisRule("", antecedent, consequent);
    }

    private StaticAnalysisRule getRule_QueryMutationGraphQLAPI() {
        // if a method is annotated with @Query or @Mutation
        // then the class is annotation with @GraphQLApi

        final Method method = new Method();
        method.annotations().add(
                any(
                        annotation("Query"),
                        annotation("Mutation")
                )
        );

        final JavaClass antecedent = new JavaClass();
        antecedent.method(Condition.single(method));

        final JavaClass javaClass = new JavaClass();
        javaClass.annotations().add(single(annotation("GraphQLApi")));

        Condition<? extends AnalysisItem> consequent = single(javaClass);
        return new StaticAnalysisRule("", antecedent, consequent);
    }
}
