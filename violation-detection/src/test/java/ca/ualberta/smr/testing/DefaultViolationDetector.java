package ca.ualberta.smr.testing;

import ca.ualberta.smr.ViolationDetector;
import ca.ualberta.smr.analyzer.*;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.typeresolution.TypeResolver;
import lombok.val;
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
        final List<AnalysisRunner> analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());
        this.violationDetector = new ViolationDetector(typeResolver, RuleProvider.getRules(), analyzers);
    }

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> analyze(String filename) {
        return violationDetector.detectViolations(filename);
    }

    private static StaticAnalysisRule getJsonWebTokenRule2() {
        val antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("org.eclipse.microprofile.rest.client.inject.RegisterRestClient")));

        val consequent1 = new JavaClass();
        consequent1.annotations().add(single(annotation("org.eclipse.microprofile.config.inject.ConfigProperty")));

        val consequent2 = new JavaClass();
        final Field field = new Field();
        field.type(Type.type("java.lang.String"));
        field.annotations().add(single(annotation("javax.inject.Inject")));
        consequent2.field(single(field));

        final Condition<JavaClass> consequent = Condition.any(
                consequent1,
                consequent2
        );

        return new StaticAnalysisRule("JsonWebTokenRule2", antecedent, consequent);
    }

    private static StaticAnalysisRule getJsonWebTokenRule3() {
        val antecedent = new JavaClass();
        antecedent.annotations().add(single(annotation("org.eclipse.microprofile.rest.client.inject.RegisterRestClient")));

        final Field field = new Field();
        field.type(single(new Type("java.lang.String")));
        final Condition<Field> consequent = Condition.single(field);

        return new StaticAnalysisRule("JsonWebTokenRule3", antecedent, consequent);
    }

    /**
     * class with (field with (type \"org.eclipse.microprofile.jwt.JsonWebToken\" ) ) must have (declaration statement with (annotation \"javax.inject.Inject\" ) )
     */
    private static StaticAnalysisRule getJsonWebToken5() {
        final Field antecedent = new Field();
        antecedent.type(single(new Type("org.eclipse.microprofile.jwt.JsonWebToken")));

        final Field field = new Field();
        field.annotations().add(single(annotation("javax.inject.Inject")));
        final Condition<Field> consequent = single(field);

        return new StaticAnalysisRule("JWT-Inject-OnField", antecedent, consequent);
    }

}
