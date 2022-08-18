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
import lombok.var;
import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.detection.AnalyzerUtils.getRule;
import static ca.ualberta.smr.detection.AnalyzerUtils.parse;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

public class MethodAnalyzerTest {

    @Test
    void test_parameters() {
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

    @Test
    void test_enclosing_class() {
        val rule = getRule(
                "method with parameter with annotation \"PathParam\" must have annotation \"Path\" or enclosing class with annotation \"Path\" "
        );

        var cu = parse(
                "class Foo {",
                "void hello(@PathParam String p1, @A int p2, double p3) {}", // violation: hello does not have @Path, class does not have @Path
                "@Path void hi(@PathParam String p1, @A int p2, double p3) {}",
                "}"
        );

        var results = new MethodAnalyzer().analyze(cu, rule);

        assertEquals(1, results.size());
        val r1 = (MethodDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("hello", r1.getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);

        // testing against another case

        cu = parse(
                "@Path class Foo {",
                "void hello(@PathParam String p1, @A int p2, double p3) {}",
                "}"
        );

        results = new MethodAnalyzer().analyze(cu, rule);
        assertTrue(results.isEmpty());
    }

}
