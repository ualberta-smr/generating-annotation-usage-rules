package ca.ualberta.smr.deprecated.consequent;

import ca.ualberta.smr.deprecated.model.ViolationInfo;
import ca.ualberta.smr.deprecated.model.javaelements.*;
import ca.ualberta.smr.parsing.utils.GeneralUtility;
import com.github.javaparser.ast.body.*;
import lombok.val;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.deprecated.utils.Utils.*;
import static ca.ualberta.smr.deprecated.AnnotationUtils.*;
import static java.util.stream.Collectors.*;

public class FieldConsequentFilter {

    @SuppressWarnings("unchecked")
    public static Collection<ViolationInfo> filter(Collection<FieldDeclaration> declarations, Condition<? extends AnalysisItem> condition) {
        final Class<? extends AnalysisItem> type = condition.getType();
        if (type.equals(JavaClass.class)) {
            val javaClassCondition = (Condition<JavaClass>) condition;
            val classDeclarations = getClassDeclarations(declarations);

            return ClassConsequentFilter.filterFromClassDeclarations(classDeclarations, javaClassCondition);
        } else if (type.equals(Field.class)) {
            return filterFromFieldDeclarations(declarations, (Condition<Field>) condition);
        }
        throw new RuntimeException("Analysis item type should be one of the following: [JavaClass, Field]");
    }

    public static Collection<ViolationInfo> filterFromFieldDeclarations(Collection<FieldDeclaration> declarations, Condition<Field> fieldCondition) {
        return findViolations(declarations, fieldCondition).stream()
                .collect(toMap(ViolationInfo::treeElement, v -> v, ViolationInfo::merge))
                .values();
    }

    private static <T extends BodyDeclaration<T>> Collection<ViolationInfo> findViolations(Collection<FieldDeclaration> declarations, Condition<Field> fieldCondition) {
        val results = doFilterFromFieldDeclarations(declarations, fieldCondition);
        return results.stream().flatMap(Collection::stream).collect(toList());
    }

    public static Collection<ViolationInfo> filterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Condition<Field> fieldCondition) {
        Collection<ViolationInfo> violations = new ArrayList<>();
        for (val classDeclaration : declarations) {
            val fields = classDeclaration.findAll(FieldDeclaration.class);
            if (fields.isEmpty()) {
                // if there's no fields in the class, then what we are searching for is missing
                violations.add(new ViolationInfo(classDeclaration, collectionToString(GeneralUtility.listOf(fieldCondition)), true));
            } else {
                // otherwise, just look for the fields
                val results = doFilterFromFieldDeclarations(fields, fieldCondition);
                final boolean noMatchingField = results.stream().noneMatch(Collection::isEmpty);
                if (noMatchingField) {
                    // if all the elements are violations, then we are missing that field in the class
                    violations.add(new ViolationInfo(classDeclaration, collectionToString(GeneralUtility.listOf(fieldCondition))));
                }
                // if we found matching element, then there's no violation that needs to be added
            }
        }
        return violations;
    }

    private static <T extends BodyDeclaration<T>> Collection<Collection<ViolationInfo>> doFilterFromFieldDeclarations(
            Collection<FieldDeclaration> fieldDeclarations,
            Condition<Field> fieldCondition
    ) {
        return fieldDeclarations.stream()
                .map(fd -> doFilter(fd, fieldCondition))
                .collect(toList());
    }

    private static Collection<ViolationInfo> doFilter(FieldDeclaration fieldDeclaration, Condition<Field> fieldCondition) {
        return fieldCondition.evaluate(field -> findViolations(fieldDeclaration, field));
    }

    private static Collection<ViolationInfo> findViolations(FieldDeclaration fieldDeclaration, Field field) {
        val requiredAnnotations = getMissingAnnotations(fieldDeclaration, field.annotations());
        val requiredAnnotationParameters = getMissingParameters(fieldDeclaration, field.annotations());
        val requiredType = new ArrayList<Condition<Type>>();
        val hasType = field.type().test(t -> t.equalsTypeString(fieldDeclaration.getElementType().asString()));
        if (!hasType) {
            requiredType.add(field.type());
        }

        val missingAnnotations = new ViolationInfo(fieldDeclaration, collectionToString(requiredAnnotations));
        val missingType = new ViolationInfo(fieldDeclaration, collectionToString(requiredType));

        val missingAnnotationParameters = requiredAnnotationParameters
                .stream()
                .map(p -> new ViolationInfo(p.key(), collectionToString(p.value())));


        return concat(Stream.of(missingType, missingAnnotations), missingAnnotationParameters)
                .filter(ViolationInfo::isNotEmpty)
                .collect(toList());
    }

}
