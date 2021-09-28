package ca.ualberta.smr;

import ca.ualberta.smr.model.*;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.nodeTypes.NodeWithAnnotations;

import java.io.IOException;
import java.util.Collection;
import java.util.List;

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

        final ViolationDetector violationDetector = new ViolationDetector(typeResolver, List.of(
            new StaticAnalysisRule(antecedent, consequent)
        ));

        final var strings = violationDetector
                .detectViolations("D:\\Projects\\CodeQL\\sample_projects\\java_code_ql_samples\\src\\main\\java\\io\\code\\annotations\\DemoDemo.java");

        strings.entrySet().forEach(System.out::println);
    }

}