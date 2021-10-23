package ca.ualberta.smr;

import ca.ualberta.smr.analyzer.*;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.typeresolution.TypeResolver;
import lombok.var;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.single;
import static ca.ualberta.smr.utils.Utils.listOf;

public class DefaultViolationDetector {

    private final ViolationDetector violationDetector;

    public DefaultViolationDetector() throws IOException {
        final TypeResolver typeResolver = new TypeResolver("D:\\UAlberta Masters\\Research\\API Misuse\\sandbox\\process\\type-resolution\\lib");
        final List<StaticAnalysisRule> rules = listOf(getJsonWebTokenRule(), getJsonWebTokenRule2(), getJsonWebTokenRule3(), getJsonWebToken4());
        final List<AnalysisRunner> analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());
        this.violationDetector = new ViolationDetector(typeResolver, rules, analyzers);
    }

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> analyze(String filename) {
        return violationDetector.detectViolations(filename);
    }

    public void analyze(Path folder) throws IOException {
        try (final Stream<Path> files = Files.walk(folder)) {
            files.filter(Files::isRegularFile)
                    .map(file -> violationDetector.detectViolations(file.toAbsolutePath().toString()))
                    .forEach(System.out::println);
        }
    }

    private static StaticAnalysisRule getJsonWebTokenRule() {
        var antecedent = Field.builder()
                .type(Type.type("org.eclipse.microprofile.jwt.JsonWebToken"))
                .build();

        final Annotation build = Annotation.builder().type(Type.type("javax.inject.Inject")).build();
        var consequent = Field.builder()
                .annotations(listOf(single(build)))
                .build();

        return new StaticAnalysisRule("JsonWebTokenRule1", antecedent, single(consequent));
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

    private static StaticAnalysisRule getJsonWebToken4() {
        var antecedent = JavaClass.builder()
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
