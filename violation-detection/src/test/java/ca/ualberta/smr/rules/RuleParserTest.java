package ca.ualberta.smr.rules;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import lombok.SneakyThrows;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.InputStream;
import java.util.Collection;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.any;
import static ca.ualberta.smr.model.javaelements.Condition.single;
import static ca.ualberta.smr.utils.Utils.listOf;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class RuleParserTest {

    @Test
    @SneakyThrows
    void testParsingRulesFromJsonFile() {
        final InputStream is = RuleParserTest.class.getResourceAsStream("/rulesSimplified.json");
        final Collection<StaticAnalysisRule> parsedRules = RuleParser.parseRules(is);

        final Collection<StaticAnalysisRule> actualRules = listOf(
                getRule_OutgoingAndScope(),
                getRule_RestClientInjectField(),
                getRule_ClaimInjectField(),
                getRule_JsonWebTokenField(),
                getRule_QueryMutationGraphQLAPI(),
                getRule_PathParam()
                );

        assertEquals(6, parsedRules.size());
        assertTrue(parsedRules.containsAll(actualRules));
    }

    @Test
    @SneakyThrows
    void testGeneratedRulesFromJsonFile() {
        final InputStream is = RuleParserTest.class.getResourceAsStream("/rulesGenerated.json");
        final Collection<StaticAnalysisRule> parsedRules = RuleParser.parseRules(is);

        assertEquals(3, parsedRules.size());
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

        return new StaticAnalysisRule("PathParam-Path", single(antecedent), consequent, "class with function with parameter with annotation \"PathParam\" must have annotation \"Path\" or function with annotation \"Path\" ");
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

}