package ca.ualberta.smr;

import ca.ualberta.smr.analyzer.*;
import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;

import java.io.IOException;
import java.util.*;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.single;

public class Main {

    public static void main(String[] args) throws IOException {
        final TypeResolver typeResolver = new TypeResolver("D:\\UAlberta Masters\\Research\\API Misuse\\sandbox\\process\\type-resolution\\lib");
        final Method method2 = Method.builder().parameters(List.of(
                single(Parameter.builder().type(new Type("java.lang.String")).build())
        )).build();
        var antecedent = JavaClass.builder()
                .method(single(method2))
                .annotations(List.of(
                        single(annotation("org.eclipse.microprofile.rest.client.inject.RegisterRestClient")),
                        single(annotation("javax.ws.rs.Path"))
                ))
                .build();

        final AnnotationParameter name1 = AnnotationParameter.builder().type(new Type("java.lang.String")).name("name").build();
        final var name = annotation("org.eclipse.microprofile.config.inject.ConfigProperty");
        name.parameters().add(single(name1));
        final Method method = Method.builder()
                .annotations(List.of(single(name)))
                .build();
        var consequent = JavaClass.builder().method(single(method)).build();

        final var violationDetector = new ViolationDetector(
                typeResolver,
                List.of(new StaticAnalysisRule(antecedent, consequent), getJsonWebTokenRule()),
                List.of(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer())
        );

        final var strings = violationDetector
                .detectViolations("D:\\Projects\\CodeQL\\sample_projects\\java_code_ql_samples\\src\\main\\java\\io\\code\\annotations\\WebTokenThing.java");

        for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : strings.entrySet()) {
            for (ViolationInfo violationInfo : entry.getValue()) {
                System.out.println(violationInfo.treeElement());
                System.out.println(violationInfo.missingElements());
                System.out.println("=======");
            }
        }
    }

    private static StaticAnalysisRule getJsonWebTokenRule() {
        var antecedent = Field.builder()
                .type(Type.type("org.eclipse.microprofile.jwt.JsonWebToken"))
                .build();

        final Annotation build = Annotation.builder().type(Type.type("javax.inject.Inject")).build();
        var consequent = Field.builder()
                .annotations(List.of(single(build)))
                .build();

        return new StaticAnalysisRule(antecedent, consequent);
    }

    private static StaticAnalysisRule getJsonWebTokenRule2() {
        var antecedent = JavaClass.builder()
                .annotations(List.of(single(annotation("org.eclipse.microprofile.rest.client.inject.RegisterRestClient"))));

        final Condition<JavaClass> consequent = Condition.any(
                JavaClass.builder().annotations(List.of(single(annotation("org.eclipse.microprofile.config.inject.ConfigProperty")))).build(),
                JavaClass.builder().field(single(Field.builder().type(Type.type("java.lang.String")).annotations(
                        List.of(single(annotation("javax.inject.Inject")))
                ).build())).build()
        );

        return new StaticAnalysisRule(antecedent, consequent);
    }

}