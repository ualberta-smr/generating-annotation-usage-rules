package ca.ualberta.smr.detection;

import ca.ualberta.smr.detection.method.MethodAntecedentScanner;
import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.JavaParser;
import lombok.val;
import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.model.javaelements.AggregateCondition.empty;
import static ca.ualberta.smr.model.javaelements.AggregateCondition.single;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

public class MethodAntecedentScannerTest {

    @Test
    void matchSimple() {
        String javaCode = "package hello;\n" +
                "public class Foo {\n" +
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

        val antecedent = single(new Method(
                empty(),
                single(new Annotation(Type.of("Demo"), empty())),
                empty()
        ));

        val cu = parseResult.getResult().get();
        val results = MethodAntecedentScanner.findMethods(cu, antecedent);

        assertEquals(2, results.size());
        assertEquals("hello", results.stream().findFirst().get().getNameAsString());
        assertEquals("hey", results.stream().skip(1).findFirst().get().getNameAsString());
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
                ), AggregateConditionOperation.OR
        );

        val cu = parseResult.getResult().get();
        val results = MethodAntecedentScanner.findMethods(cu, antecedent);

        assertEquals(2, results.size());
        assertEquals("hello", results.stream().findFirst().get().getNameAsString());
        assertEquals("hi", results.stream().skip(1).findFirst().get().getNameAsString());
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
        val results = MethodAntecedentScanner.findMethods(cu, antecedent);

        assertEquals(2, results.size());
        assertEquals("hello", results.stream().findFirst().get().getNameAsString());
        assertEquals("hi", results.stream().skip(1).findFirst().get().getNameAsString());
    }

}
