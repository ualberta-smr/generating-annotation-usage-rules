package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.ViolationInfo;
import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.body.*;
import lombok.val;
import org.junit.jupiter.api.Test;

import java.util.Collection;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.single;
import static ca.ualberta.smr.utils.Utils.listOf;
import static org.junit.jupiter.api.Assertions.*;

class ClassConsequentFilterTest {

    @Test
    void doFilter_whenOnlyOneOrConditionHolds_shouldReturnNoViolations() {
        val classDeclarations = getClassDeclarations(lines(
                "@RegisterRestClient",
                "@ConfigProperty",
                "class Example1 {",
                "    private String name;",
                "}"
        ));
        val classCondition = getAntecedent1();
        val violations = ClassConsequentFilter.filterFromClassDeclarations(classDeclarations, classCondition);
        assertTrue(violations.isEmpty());
    }

    @Test
    void doFilter_whenNoOrConditionHolds_shouldReturnEither() {
        val classDeclarations = getClassDeclarations(lines(
                "@RegisterRestClient",
                "class Example2 {",
                "    private String name;",
                "}"
        ));
        val classCondition = getAntecedent1();
        val violations = ClassConsequentFilter.filterFromClassDeclarations(classDeclarations, classCondition);
        assertEquals(1, violations.size(), "There should be exactly 1 violation");
        final ViolationInfo violationInfo = violations.stream().findFirst().get();
        assertTrue(violationInfo.treeElement() instanceof FieldDeclaration, "Field is missing @Inject annotation");
        assertTrue(violationInfo.missingElements().contains("@Inject"), "Inject annotation is missing");
    }

    @Test
    void doFilter_whenNoOrConditionHolds_and_noObjectDefined() {
        val classDeclarations = getClassDeclarations(lines(
                "@RegisterRestClient",
                "class Example2 {",
                "}"
        ));
        val classCondition = getAntecedent1();
        val violations = ClassConsequentFilter.filterFromClassDeclarations(classDeclarations, classCondition);
        assertEquals(1, violations.size(), "There should be exactly 1 violation");
        final ViolationInfo violationInfo = violations.stream().findFirst().get();
        assertTrue(violationInfo.treeElement() instanceof ClassOrInterfaceDeclaration, "Class is missing @ConfigProperty annotation");
        assertTrue(violationInfo.missingElements().contains("@ConfigProperty"), "ConfigProperty annotation is missing");
    }

    private Condition<JavaClass> getAntecedent1() {
        // class must have (annotation ConfigProperty) or (field with annotation Inject)
        return Condition.any(JavaClass.class,
                JavaClass.builder()
                        .field(
                                single(Field.builder().type(Type.type("String")).annotations(
                                        listOf(single(annotation("Inject")))
                                ).build()))
                        .build(),

                JavaClass.builder().annotations(
                        listOf(single(annotation("ConfigProperty")))
                ).build()
        );
    }

    private Collection<ClassOrInterfaceDeclaration> getClassDeclarations(String classBody) {
        return StaticJavaParser.parse(classBody).findAll(ClassOrInterfaceDeclaration.class);
    }

    private String lines(String...lines) {
        val sb = new StringBuilder();
        for (String line : lines) {
            sb.append(line);
        }
        return sb.toString();
    }

}