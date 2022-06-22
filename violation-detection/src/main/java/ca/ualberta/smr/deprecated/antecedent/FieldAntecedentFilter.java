package ca.ualberta.smr.deprecated.antecedent;

import ca.ualberta.smr.deprecated.model.javaelements.Condition;
import ca.ualberta.smr.deprecated.model.javaelements.Field;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.FieldDeclaration;

import java.util.Collection;

import static ca.ualberta.smr.deprecated.AnnotationUtils.containsAnnotation;
import static java.util.stream.Collectors.toList;

public class FieldAntecedentFilter {

    public static Collection<FieldDeclaration> doFilter(CompilationUnit cu, Condition<Field> field) {
        return doFilter(cu.findAll(FieldDeclaration.class), field);
    }

    public static Collection<FieldDeclaration> doFilter(Collection<FieldDeclaration> fieldDeclarations, Condition<Field> field) {
        return fieldDeclarations.stream()
                .filter(fd -> fieldHasAnnotations(fd, field) &&
                        fieldHasType(fd, field)).collect(toList());
    }

    static boolean fieldHasAnnotations(FieldDeclaration fieldDeclaration, Condition<Field> fieldCondition) {
        return fieldCondition.test(field ->
                field.annotations().stream().allMatch(a -> containsAnnotation(fieldDeclaration, a)));
    }

    static boolean fieldHasType(FieldDeclaration fieldDeclaration, Condition<Field> fieldCondition) {
        return fieldCondition.test(field ->
                field.type() == null || field.type().test(t -> t.equalsTypeString(fieldDeclaration.getElementType().asString()))
        );
    }

}
