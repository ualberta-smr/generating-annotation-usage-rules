package ca.ualberta;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.javaelements.*;
import lombok.val;

import javax.inject.Named;
import javax.inject.Singleton;
import java.util.Collection;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.single;
import static ca.ualberta.smr.utils.Utils.listOf;

@Named
@Singleton
public class DefaultRuleProvider implements RuleProvider {

    @Override
    public Collection<StaticAnalysisRule> getRules() {
        return listOf(
                getJsonWebTokenRule1(),
                getJsonWebTokenRule2(),
                getJsonWebTokenRule3(),
                getJsonWebTokenRule4()
        );
    }

    private StaticAnalysisRule getJsonWebTokenRule1() {
        val antecedent = Field.builder()
                .type(Type.type("org.eclipse.microprofile.jwt.JsonWebToken"))
                .build();

        final Annotation build = Annotation.builder().type(Type.type("javax.inject.Inject")).build();
        val consequent = Field.builder()
                .annotations(listOf(single(build)))
                .build();

        return new StaticAnalysisRule("JsonWebTokenRule1", antecedent, single(consequent));
    }

    private StaticAnalysisRule getJsonWebTokenRule2() {
        val antecedent = JavaClass.builder()
                .annotations(
                        listOf(single(annotation("org.eclipse.microprofile.rest.client.inject.RegisterRestClient")))
                ).build();

        final Condition<JavaClass> consequent = Condition.any(JavaClass.class,
                JavaClass.builder().annotations(
                        listOf(single(annotation("org.eclipse.microprofile.config.inject.ConfigProperty")))
                ).build(),

                JavaClass.builder()
                        .field(
                                single(Field.builder().type(Type.type("java.lang.String")).annotations(
                                        listOf(single(annotation("javax.inject.Inject")))
                                ).build()))
                        .build()
        );

        return new StaticAnalysisRule("JsonWebTokenRule2", antecedent, consequent);
    }

    private StaticAnalysisRule getJsonWebTokenRule3() {
        val antecedent = JavaClass.builder()
                .annotations(listOf(single(annotation("org.eclipse.microprofile.rest.client.inject.RegisterRestClient")))).build();

        final Condition<Field> consequent = Condition.any(Field.class, Field.builder().type(single(new Type("java.lang.String"))).build());

        return new StaticAnalysisRule("JsonWebTokenRule3", antecedent, consequent);
    }

    private StaticAnalysisRule getJsonWebTokenRule4() {
        val antecedent = JavaClass.builder()
                .field(single(Field.builder().type(single(new Type("java.lang.String"))).build()))
                .build();

        final Condition<Field> field = Condition.any(Field.class, Field.builder().annotations(listOf(
                single(Annotation.builder().type(single(new Type("java.lang.Override"))).build())
        )).build());

        return new StaticAnalysisRule("JsonWebTokenRule4", antecedent, Condition.single(
                JavaClass.builder().field(field).build()
        ));
    }
}
