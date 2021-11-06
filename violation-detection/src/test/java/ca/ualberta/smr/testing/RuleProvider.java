package ca.ualberta.smr.testing;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.rules.RuleParser;
import lombok.SneakyThrows;

import java.io.InputStream;
import java.util.Collection;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.any;
import static ca.ualberta.smr.model.javaelements.Condition.single;

public class RuleProvider {

    @SneakyThrows
    public static Collection<StaticAnalysisRule> getRules() {
        final InputStream is = RuleProvider.class.getResourceAsStream("/rules.json");
        return RuleParser.parseRules(is);
    }

    private static StaticAnalysisRule getRule_OutgoingAndScope() {
        // if a method is annotated with @Outgoing or @Incoming
        // then the class must be annotation with @ApplicationScoped or @Dependent

        final Method method = new Method();
        method.annotations().add(
                any(
                        annotation("org.eclipse.microprofile.reactive.messaging.Outgoing"),
                        annotation("org.eclipse.microprofile.reactive.messaging.Incoming")
                )
        );

        final JavaClass antecedent = new JavaClass();
        antecedent.method(Condition.single(method));

        final JavaClass javaClass = new JavaClass();
        javaClass.annotations().add(
                any(
                        annotation("javax.enterprise.context.ApplicationScoped"),
                        annotation("javax.enterprise.context.Dependent")
                )
        );

        Condition<? extends AnalysisItem> consequent = single(javaClass);
        return new StaticAnalysisRule("[In|Out]goingAndScopeOnFieldOnClass", antecedent, consequent, "");
    }

    private static StaticAnalysisRule getRule_RestClientInjectField() {
        // if field has annotation @RestClient
        // then it must have @Inject
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("org.eclipse.microprofile.rest.client.inject.RestClient")));

        final Field field = new Field();
        field.annotations().add(single(annotation("javax.inject.Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("RestClientInjectOnField", antecedent, consequent, "");
    }

    private static StaticAnalysisRule getRule_ClaimInjectField() {
        // if field has annotation @Claim
        // then it must have @Inject
        final Field antecedent = new Field();
        antecedent.annotations().add(single(annotation("org.eclipse.microprofile.jwt.Claim")));

        final Field field = new Field();
        field.annotations().add(single(annotation("javax.inject.Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("ClaimInjectOnField", antecedent, consequent, "");
    }

    private static StaticAnalysisRule getRule_JsonWebTokenField() {
        // if field is of type JsonWebToken
        // then it must have annotation @Inject
        final Field antecedent = new Field();
        antecedent.type(single(new Type("org.eclipse.microprofile.jwt.JsonWebToken")));

        final Field field = new Field();
        field.annotations().add(single(annotation("javax.inject.Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("JWT-Inject-OnField", antecedent, consequent, "");
    }

    private static StaticAnalysisRule getRule_PathParam() {
        // if method parameter has @PathParam
        // then either method or class must have @Path

        final Method antecedentMethod = new Method();
        final MethodParameter param = new MethodParameter();
        param.annotations().add(single(annotation("javax.ws.rs.PathParam")));
        antecedentMethod.parameters()
                .add(single(param));

        final JavaClass klass = new JavaClass();
        klass.annotations().add(single(annotation("javax.ws.rs.Path")));

        final Method method = new Method();
        method.annotations().add(single(annotation("javax.ws.rs.Path")));

        final Condition<? extends AnalysisItem> consequent = any(
                method, klass
        );

        return new StaticAnalysisRule("PathParamPath", antecedentMethod, consequent, "");
    }

    private static StaticAnalysisRule getRule_QueryMutationGraphQLAPI() {
        // if a method is annotated with @Query or @Mutation
        // then the class is annotation with @GraphQLApi

        final Method method = new Method();
        method.annotations().add(
                any(
                        annotation("org.eclipse.microprofile.graphql.Query"),
                        annotation("org.eclipse.microprofile.graphql.Mutation")
                )
        );

        final JavaClass antecedent = new JavaClass();
        antecedent.method(Condition.single(method));

        final JavaClass javaClass = new JavaClass();
        javaClass.annotations().add(single(annotation("org.eclipse.microprofile.graphql.GraphQLApi")));

        Condition<? extends AnalysisItem> consequent = single(javaClass);
        return new StaticAnalysisRule("QueryMutationGraphQLAPI", antecedent, consequent, "");
    }

}
