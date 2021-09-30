package ca.ualberta.smr;

import ca.ualberta.smr.analyzer.*;
import ca.ualberta.smr.model.*;

import java.io.IOException;
import java.util.*;

import static ca.ualberta.smr.model.Annotation.annotation;

public class Main {

    public static void main(String[] args) throws IOException {
        final TypeResolver typeResolver = new TypeResolver("D:\\UAlberta Masters\\Research\\API Misuse\\sandbox\\process\\type-resolution\\lib");
        var antecedent = JavaClass.builder()
                .method(Method.builder().parameters(List.of(
                        Parameter.builder().type(new Type("java.lang.String")).build()
                )).build())
                .annotations(List.of(
                        annotation("org.eclipse.microprofile.rest.client.inject.RegisterRestClient"),
                        annotation("javax.ws.rs.Path")
                ))
                .build();

        final AnnotationParameter name1 = AnnotationParameter.builder().type(new Type("java.lang.String")).name("name").build();
        final var name = annotation("org.eclipse.microprofile.config.inject.ConfigProperty");
        name.parameters().add(name1);
        var consequent = JavaClass.builder().method(Method.builder()
                .annotations(List.of(name))
                .build()).build();

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
                .type(new Type("org.eclipse.microprofile.jwt.JsonWebToken"))
                .build();

        var consequent = Field.builder()
                .annotations(List.of(Annotation.builder().type(new Type("javax.inject.Inject")).build()))
                .build();

        return new StaticAnalysisRule(antecedent, consequent);
    }

}