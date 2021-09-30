package ca.ualberta.smr.antecedent;

import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.Field;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.FieldDeclaration;

import java.util.Collection;
import java.util.stream.Collectors;

import static ca.ualberta.smr.utils.AnnotationUtils.containsAnnotation;

public class FieldAntecedentFilter {

    public static Collection<FieldDeclaration> doFilter(CompilationUnit cu, Condition<Field> field) {
        final var fields = cu.findAll(FieldDeclaration.class);

        return fields.stream()
                .filter(m -> fieldHasAnnotations(m, field))
                .filter(m -> fieldHasType(m, field))
                .collect(Collectors.toList());
    }

    static boolean fieldHasAnnotations(FieldDeclaration fieldDeclaration, Condition<Field> fieldCondition) {
        return fieldCondition.test(field ->
                field.annotations().stream().allMatch(a -> containsAnnotation(fieldDeclaration, a)));
    }

    static boolean fieldHasType(FieldDeclaration fieldDeclaration, Condition<Field> fieldCondition) {
        return fieldCondition.test(field -> {
            if (field.type() == null) return true;
            return field.type().test(t -> t.equalsTypeString(fieldDeclaration.getElementType().asString()));
        });
    }

}
