package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.javaelements.*;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.body.MethodDeclaration;
import lombok.val;
import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.newmodel.javaelements.AggregateCondition.empty;
import static ca.ualberta.smr.newmodel.javaelements.AggregateCondition.single;
import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

class MethodConsequentScannerTest {

    @Test
    void findViolationsSimple() {
        String javaCode = "public class Foo {\n" +
                "    @Demo\n" +
                "    void hello() {}\n" +
                "\n" +
                "    @Nemo\n" +
                "    void hi() {}\n" +
                "\n" +
                "    @Demo\n" +
                "    void hey() {}\n" +
                "\n" +
                "\n" +
                "    void howdy() {}\n" +
                "}";

        val parseResult = new JavaParser().parse(javaCode);
        assumeTrue(parseResult.isSuccessful(), "Parsing should be successful");

        // methods need to have Demo annotation
        val consequent = single(new Method(
                empty(),
                single(new Annotation(Type.of("Demo"), empty())),
                empty()
        ));

        val cu = parseResult.getResult().get();
        val results = MethodConsequentScanner.findViolations(cu.findAll(MethodDeclaration.class), consequent);

        assertEquals(2, results.size());
        assertEquals("hi", ((MethodDeclaration) results.stream().findFirst().get().treeElement()).getNameAsString());
        assertEquals("howdy", ((MethodDeclaration) results.stream().skip(1).findFirst().get().treeElement()).getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);
    }

    @Test
    void matchSimple2() {
        String javaCode = "public class Foo {\n" +
                "    @Demo\n" +
                "    void hello() {}\n" +
                "\n" +
                "    @Nemo\n" +
                "    void hi(String str) {}\n" +
                "\n" +
                "    int hey(double dbl) {return 1;}\n" +
                "}";

        val parseResult = new JavaParser().parse(javaCode);
        assumeTrue(parseResult.isSuccessful(), "Parsing should be successful");

        // method with @Demo or method with parameter String
        val consequent = new AggregateCondition(
                new Method(
                        empty(),
                        single(new Annotation(Type.of("Demo"), empty())),
                        empty()
                ),
                new Method(
                        empty(),
                        empty(),
                        single(new MethodParameter(Type.of("String"), empty()))
                ), AggregateConditionOperation.OR
        );

        val cu = parseResult.getResult().get();
        val results = MethodConsequentScanner.findViolations(cu.findAll(MethodDeclaration.class), consequent);

        assertEquals(1, results.size());
        assertEquals("hey", ((MethodDeclaration) results.stream().findFirst().get().treeElement()).getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);
    }

    @Test
    void matchSimpleXor() {
        String javaCode = "public class Foo {\n" +
                "    @Demo\n" +
                "    void hello() {}\n" +
                "\n" +
                "    @Nemo\n" +
                "    void hi(String str) {}\n" +
                "\n" +
                "    @Demo\n" +
                "    int hey(String str) {}\n" +
                "}";

        val parseResult = new JavaParser().parse(javaCode);
        assumeTrue(parseResult.isSuccessful(), "Parsing should be successful");

        val antecedent = new AggregateCondition(
                new Method(
                        empty(),
                        single(new Annotation(Type.of("Demo"), empty())),
                        empty()
                ),
                new Method(
                        empty(),
                        empty(),
                        single(new MethodParameter(Type.of("String"), empty()))
                ), AggregateConditionOperation.XOR
        );

        val cu = parseResult.getResult().get();
        val results = MethodConsequentScanner.findViolations(cu.findAll(MethodDeclaration.class), antecedent);

        assertEquals(1, results.size());
        assertEquals("hey", ((MethodDeclaration) results.stream().findFirst().get().treeElement()).getNameAsString());

        results.stream().map(ViolationCombination::describe).forEach(System.out::println);
    }

}