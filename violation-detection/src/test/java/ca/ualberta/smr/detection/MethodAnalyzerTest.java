package ca.ualberta.smr.detection;

import ca.ualberta.smr.detection.method.MethodAnalyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.parsing.rules.Rule;
import ca.ualberta.smr.parsing.rules.RuleParser;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import lombok.val;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

public class MethodAnalyzerTest {

    @Test
    void test1() {
        val cu = parse(
                "class Foo {",
                "void hello(String p1, @A int p2, double p3) {}", // violation: p1 does not have @A
                "void hi(@A String p1, @A int p2, double p3) {}",
                "}"
        );

        val rule = getRule(
                "method with parameter \"String\" must have parameter with annotation \"A\" "
        );

        val results = new MethodAnalyzer().analyze(cu, rule);

        assertEquals(1, results.size());
        val r1 = (MethodDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("hello", r1.getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);
    }

    private static CompilationUnit parse(String... lines) {
        String javaCode = String.join("\n", lines);
        val parseResult = new JavaParser().parse(javaCode);
        assumeTrue(parseResult.isSuccessful() && parseResult.getResult().isPresent(),
                "Parsing should be successful");
        return parseResult.getResult().get();
    }

    private static StaticAnalysisRule getRule(String ruleString) {
        val rule = new Rule();
        rule.setId("id");
        rule.setSpecification(ruleString);
        return RuleParser.parseRule(rule);
    }

}
