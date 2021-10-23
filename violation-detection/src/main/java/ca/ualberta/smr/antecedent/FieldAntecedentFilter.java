package ca.ualberta.smr.antecedent;

import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.Field;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.FieldDeclaration;

import java.util.Collection;

import static ca.ualberta.smr.utils.AnnotationUtils.containsAnnotation;

public class FieldAntecedentFilter {

    public static Collection<FieldDeclaration> doFilter(CompilationUnit cu, Condition<Field> field) {
        return cu.findAll(FieldDeclaration.class, fd ->
                fieldHasAnnotations(fd, field) &&
                        fieldHasType(fd, field));
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
