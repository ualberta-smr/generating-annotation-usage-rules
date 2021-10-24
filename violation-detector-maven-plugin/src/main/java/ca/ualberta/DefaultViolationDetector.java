package ca.ualberta;

import ca.ualberta.smr.ViolationDetector;
import ca.ualberta.smr.analyzer.*;
import ca.ualberta.smr.model.*;
import ca.ualberta.smr.typeresolution.TypeResolver;

import javax.inject.*;
import java.io.File;
import java.io.InputStream;
import java.util.*;
import java.util.stream.Collectors;

import static ca.ualberta.smr.utils.Utils.listOf;

@Named
@Singleton
public class DefaultViolationDetector {

    private final ViolationDetector violationDetector;

    @Inject
    public DefaultViolationDetector(final RuleProvider ruleProvider) {
        final Collection<InputStream> jarFiles = JAR_FILES.stream()
                .map(DefaultViolationDetector.class::getResourceAsStream)
                .filter(Objects::nonNull)
                .collect(Collectors.toList());
        final TypeResolver typeResolver = new TypeResolver(jarFiles);
        final Collection<StaticAnalysisRule> rules = ruleProvider.getRules();
        final List<AnalysisRunner> analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());

        this.violationDetector = new ViolationDetector(typeResolver, rules, analyzers);
    }

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> analyze(String filename) {
        return violationDetector.detectViolations(filename);
    }

    public Map<StaticAnalysisRule, Collection<ViolationInfo>> analyze(File file) {
        return violationDetector.detectViolations(file.getAbsolutePath());
    }

    private static final Collection<String> JAR_FILES = Arrays.asList(
            "/lib/cdi-api-2.0.jar",
            "/lib/javax.inject-1.jar",
            "/lib/javax.ws.rs-api-2.1.1.jar",
            "/lib/microprofile-fault-tolerance-api-3.0.jar",
            "/lib/microprofile-graphql-api-1.1.0.jar",
            "/lib/microprofile-health-api-3.0.jar",
            "/lib/microprofile-jwt-auth-api-1.2.jar",
            "/lib/microprofile-openapi-api-2.0.jar",
            "/lib/microprofile-reactive-messaging-api-2.0.jar",
            "/lib/microprofile-rest-client-api-2.0.jar"
    );



}