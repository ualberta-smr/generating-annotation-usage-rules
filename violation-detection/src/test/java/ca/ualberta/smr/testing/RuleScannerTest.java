package ca.ualberta.smr.testing;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;
import static org.junit.jupiter.api.Assertions.*;

public class RuleScannerTest {

    final DefaultViolationDetector defaultDetector = new DefaultViolationDetector("src/test/data/jarfiles");

    @ParameterizedTest
    @MethodSource("dataProvider")
    public void test(File file, Collection<String> expectedRulesToViolate) {
        final Map<StaticAnalysisRule, Collection<ViolationCombination>> violations = defaultDetector.analyze(file.getAbsolutePath());

        final Collection<String> actualViolations = violations.entrySet().stream()
                .filter(e -> !e.getValue().isEmpty())
                .map(Map.Entry::getKey)
                .map(StaticAnalysisRule::toString)
                .collect(Collectors.toSet());

        final boolean allTheViolationsAreCorrect = !actualViolations.isEmpty() && expectedRulesToViolate.containsAll(actualViolations);

        if (!allTheViolationsAreCorrect) {
            for (Map.Entry<StaticAnalysisRule, Collection<ViolationCombination>> entry : violations.entrySet()) {
                if (!entry.getValue().isEmpty()) {
                    System.out.println("================================================");
                    System.out.println("For rule: " + entry.getKey().toString());
                    for (ViolationCombination violationInfo : entry.getValue()) {
                        System.out.println(violationInfo.describe());
                        Reporter.report(violationInfo);
                    }
                    System.out.println("================================================");
                }
            }
            fail(String.format("%s should violate the rules: %s [but violates :%s]",
                    file.getName(),
                    expectedRulesToViolate,
                    actualViolations)
            );
        }
    }

    static Stream<Arguments> dataProvider() {
        Map<String, Collection<String>> fileToRuleMap = new HashMap<>();
        fileToRuleMap.put("TransactionDateChangeResource.java", listOf("PathParam-Path"));
        fileToRuleMap.put("FoodResource.java", listOf("OutgoingAndScope"));
        fileToRuleMap.put("WebIdPrincipal.java", listOf("JsonWebTokenField"));
        fileToRuleMap.put("WebIdSecurityContext.java", listOf("JsonWebTokenField"));
        fileToRuleMap.put("InventoryClient.java", listOf("PathParam-Path"));
        fileToRuleMap.put("InventoryResource.java", listOf("JsonWebTokenField"));
        fileToRuleMap.put("LoginBean.java", listOf("RestClientInjectField"));
        fileToRuleMap.put("SystemResource.java", listOf("ClaimInjectField"));
        fileToRuleMap.put("SystemResource2.java", listOf("ClaimInjectField"));
        fileToRuleMap.put("HelloResource.java", listOf("RestClientInjectField"));
        fileToRuleMap.put("FoodResource2.java", listOf("OutgoingAndScope"));
        fileToRuleMap.put("MembershipGraphQLApi.java", listOf("QueryMutationGraphQLAPI"));

        return getFiles()
                .stream()
                .map(file -> {
                    String name = file.getName();
                    final Collection<String> strings = fileToRuleMap.get(name);
                    return Arguments.of(file, strings);
                });
    }

    private static Collection<File> getFiles() {
        return projectsFolder().stream()
                .flatMap(projectPath -> {
                    try {
                        return Files.walk(Paths.get(projectPath))
                                .filter(Files::isRegularFile)
                                .filter(f -> f.toAbsolutePath().toString().endsWith(".java"))
                                .map(Path::toFile);
                    } catch (IOException e) {
                        return Stream.of();
                    }
                }).collect(Collectors.toList());
    }

    private static List<String> projectsFolder() {
        return listOf(
                "src/test/data/violation_files/capstonecpp",
                "src/test/data/violation_files/citiworkshop",
                "src/test/data/violation_files/foodorder",
                "src/test/data/violation_files/membership",
                "src/test/data/violation_files/mpjwt",
                "src/test/data/violation_files/reactivemessaging",
                "src/test/data/violation_files/reactiverestclient",
                "src/test/data/violation_files/trellis"
        );
    }

}