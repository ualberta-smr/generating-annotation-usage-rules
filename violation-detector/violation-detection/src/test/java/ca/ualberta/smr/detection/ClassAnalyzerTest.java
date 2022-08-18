package ca.ualberta.smr.detection;

import ca.ualberta.smr.detection.clazz.ClassAnalyzer;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import lombok.val;
import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.detection.AnalyzerUtils.getRule;
import static ca.ualberta.smr.detection.AnalyzerUtils.parse;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class ClassAnalyzerTest {

    @Test
    public void test_simple() {
        val cu = parse(
                "class Foo extends Bar {",
                "@Override public void foobar(String a, int b) {}",
                "}"
        );

        val rule = getRule(
                "class with extension of \"Bar\" must have overridden method \"foobar(String,int)\" "
        );

        val results = new ClassAnalyzer().analyze(cu, rule);
        assertTrue(results.isEmpty());
    }

    @Test
    public void test_simple_2() {
        val cu = parse(
                "class Foo extends Bar {",
                "@Override public void foobar(int a, String b) {}",
                "}"
        );

        val rule = getRule(
                "class with extension of \"Bar\" must have overridden method \"foobar(String,int)\" "
        );

        val results = new ClassAnalyzer().analyze(cu, rule);

        assertEquals(1, results.size());
        val r1 = (MethodDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("foobar", r1.getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);
    }

}
