package ca.ualberta.smr.detection;

import ca.ualberta.smr.detection.field.FieldAnalyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.parsing.rules.Rule;
import ca.ualberta.smr.parsing.rules.RuleParser;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.FieldDeclaration;
import lombok.val;
import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.detection.AnalyzerUtils.getRule;
import static ca.ualberta.smr.detection.AnalyzerUtils.parse;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

public class FieldAnalyzerTest {

    @Test
    void test1() {
        val cu = parse(
                "class Foo {",
                "@C private A fooA;",
                "",
                "@B private Z fooZ;", // violation because does not have @C xor @D
                "",
                "@C @B private A fooAB;",
                "",
                "@D @C @B private A fooABCD;", // violation because has both @C and @D
                "}"
        );

        val rule = getRule(
                "field with type \"A\" or annotation \"B\" must have one of (annotation \"C\" or annotation \"D\" )"
        );

        val results = new FieldAnalyzer().analyze(cu, rule);

        assertEquals(2, results.size());
        val r1 = (FieldDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("fooZ", r1.getVariable(0).getNameAsString());

        val r2 = (FieldDeclaration) results.stream().skip(1).findFirst().get().treeElement();
        assertEquals("fooABCD", r2.getVariable(0).getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);
    }

    @Test
    void test2_withNo() {
        val cu = parse(
                "class Foo {",
                "@C private A fooA;",
                "",
                "@B private Z fooZ;",
                "",
                "@C @B private A fooAB;",
                "",
                "@D private A fooAD;", // violates because it does not have @C
                "}"
        );

        val rule = getRule(
                "field with type \"A\" and no annotation \"B\" must have annotation \"C\" "
        );

        val results = new FieldAnalyzer().analyze(cu, rule);

        assertEquals(1, results.size());
        val r1 = (FieldDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("fooAD", r1.getVariable(0).getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);
    }

    @Test
    void test3_withNo() {
        val cu = parse(
                "class Foo {",
                "@C private A fooA;", // violates: has @C
                "",
                "@B private Z fooZ;",
                "",
                "@C @B private A fooAB;", // violates: has @C
                "",
                "@D private A fooAD;",
                "}"
        );

        val rule = getRule(
                "field with type \"A\" or annotation \"B\" must have no annotation \"C\" "
        );

        val results = new FieldAnalyzer().analyze(cu, rule);

        assertEquals(2, results.size());
        val r1 = (FieldDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("fooA", r1.getVariable(0).getNameAsString());

        val r2 = (FieldDeclaration) results.stream().skip(1).findFirst().get().treeElement();
        assertEquals("fooAB", r2.getVariable(0).getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);
    }

    @Test
    void test3_withAnnotationValue() {
        val cu = parse(
                "class Foo {",
                "@C(name=\"sunny\") private A fooA;",

                "@C(name=\"sonny\") private B fooB;",
                "}"
        );

        val rule = getRule(
                "field with annotation \"C\" must have annotation \"C\" with parameter \"name\" with value \"sunny\" "
        );

        val results = new FieldAnalyzer().analyze(cu, rule);

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);

        assertEquals(1, results.size());
        val r1 = (FieldDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("fooB", r1.getVariable(0).getNameAsString());
    }

    @Test
    void test4_withAnnotationValue() {
        val cu = parse(
                "class Foo {",
                "@C(maxInterval=12345) private A fooA;",

                "@C(maxInterval=Integer.INT_MAX) private B fooB;",
                "}"
        );

        val rule = getRule(
                "field with annotation \"C\" must have annotation \"C\" with parameter \"maxInterval\" with value \"12345\" "
        );

        val results = new FieldAnalyzer().analyze(cu, rule);

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);

        assertEquals(1, results.size());
        val r1 = (FieldDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("fooB", r1.getVariable(0).getNameAsString());
    }

    @Test
    void test4_withThreeAnds() {
        val cu = parse(
                "class Foo {",
                "@X @C(maxInterval=12345) private A fooA;",

                "@C(maxInterval=Integer.INT_MAX) private B fooB;",
                "}"
        );

        val rule = getRule(
                "field with annotation \"C\" must have type \"A\" and annotation \"C\" with parameter \"maxInterval\" and annotation \"X\" "
        );

        val results = new FieldAnalyzer().analyze(cu, rule);

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);

        assertEquals(1, results.size());
        val r1 = (FieldDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("fooB", r1.getVariable(0).getNameAsString());
    }

    @Test
    void test4_withEnclosingClass() {
        val cu = parse(
                "class Foo {",
                "@ConfigProperty private A fooA;",
                "@ConfigProperty @Inject private B fooB;",
                "}"
        );

        val rule = getRule(
                "field with annotation \"ConfigProperty\" and no enclosing class with annotation \"ConfigProperties\" must have annotation \"Inject\" "
        );

        val results = new FieldAnalyzer().analyze(cu, rule);

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);

        assertEquals(1, results.size());
        val r1 = (FieldDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("fooA", r1.getVariable(0).getNameAsString());
    }

    @Test
    void test4_withEnclosingClass_2() {
        val cu = parse(
                "class Foo {",
                "@ConfigProperty private A fooA;",
                "@ConfigProperty @Inject private B fooB;",
                "}"
        );

        val rule = getRule(
                "field with annotation \"ConfigProperty\" must have annotation \"Inject\" or enclosing class with annotation \"ConfigProperties\" "
        );

        val results = new FieldAnalyzer().analyze(cu, rule);

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);

        assertEquals(1, results.size());
        val r1 = (FieldDeclaration) results.stream().findFirst().get().treeElement();
        assertEquals("fooA", r1.getVariable(0).getNameAsString());
    }

}
