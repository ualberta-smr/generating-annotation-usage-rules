package ca.ualberta.smr.testing;

import ca.ualberta.smr.ViolationDetector;
import ca.ualberta.smr.analyzer.*;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.typeresolution.TypeResolver;
import lombok.var;

import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.single;
import static ca.ualberta.smr.utils.Utils.listOf;

class DefaultViolationDetector {

    private final ViolationDetector violationDetector;

    public DefaultViolationDetector() throws IOException {
        final TypeResolver typeResolver = new TypeResolver(System.getenv("JAR_FILES"));
        final List<StaticAnalysisRule> rules = listOf(
                getJsonWebTokenRule2(),
                getJsonWebTokenRule3(),
                getJsonWebToken5()
        );
        final List<AnalysisRunner> analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());
        this.violationDetector = new ViolationDetector(typeResolver, rules, analyzers);
    }

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> analyze(String filename) {
        return violationDetector.detectViolations(filename);
    }

    private static StaticAnalysisRule getJsonWebTokenRule2() {
        var antecedent = JavaClass.builder()
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

    private static StaticAnalysisRule getJsonWebTokenRule3() {
        var antecedent = JavaClass.builder()
                .annotations(listOf(single(annotation("org.eclipse.microprofile.rest.client.inject.RegisterRestClient")))).build();

        final Condition<Field> consequent = Condition.any(Field.class, Field.builder().type(single(new Type("java.lang.String"))).build());

        return new StaticAnalysisRule("JsonWebTokenRule3", antecedent, consequent);
    }

    /**
     * class with (field with (type \"org.eclipse.microprofile.jwt.JsonWebToken\" ) ) must have (declaration statement with (annotation \"javax.inject.Inject\" ) )
     */
    private static StaticAnalysisRule getJsonWebToken5() {
        final Field antecedent = Field.builder()
                .type(single(new Type("org.eclipse.microprofile.jwt.JsonWebToken"))).build();

        final Condition<Field> consequent = single(Field.builder()
                .annotations(listOf(single(annotation("javax.inject.Inject")))).build());

        return new StaticAnalysisRule("JWT-Inject-OnField", antecedent, consequent);
    }

}
