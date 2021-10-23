package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.ast.body.*;
import lombok.val;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.AnnotationUtils.*;
import static ca.ualberta.smr.utils.Utils.*;
import static java.util.stream.Collectors.toList;

public class ClassConsequentFilter {

    public static Collection<ViolationInfo> filterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Condition<JavaClass> klass) {
        return declarations.stream()
                .map(cd -> doFilter(cd, klass))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    private static Collection<ViolationInfo> doFilter(ClassOrInterfaceDeclaration declaration, Condition<JavaClass> classCondition) {
        return classCondition.evaluate(javaClass -> {
            val requiredAnnotations = getMissingAnnotations(declaration, javaClass.annotations());
            val requiredAnnotationParameters = getMissingParameters(declaration, javaClass.annotations());

            Collection<Condition<Type>> requiredInterfaces = new ArrayList<>();
            for (val anInterface : javaClass.implementedInterfaces()) {
                for (val implementedType : declaration.getImplementedTypes()) {
                    if (anInterface.test(i -> !i.equalsTypeString(implementedType.getNameAsString()))) {
                        requiredInterfaces.add(anInterface);
                    }
                }
            }

            Collection<Condition<Type>> requiredTypeToExtend = new ArrayList<>();

            val hasExtended = declaration.getExtendedTypes().stream().anyMatch(e -> javaClass.extendedClass().test(t -> t.equalsTypeString(e.getNameAsString())));

            if (!hasExtended) {
                requiredTypeToExtend.add(javaClass.extendedClass());
            }

            val methodViolations = getMethodViolations(declaration, javaClass.method());
            val fieldViolations = getFieldViolations(declaration, javaClass.field());

            val missingAnnotations = new ViolationInfo(declaration, collectionToString(requiredAnnotations));
            val missingInterfaces = new ViolationInfo(declaration, collectionToString(requiredInterfaces));
            val missingExtension = new ViolationInfo(declaration, collectionToString(requiredTypeToExtend));

            val missingAnnotationParameters = requiredAnnotationParameters
                    .stream()
                    .map(p -> new ViolationInfo(p.key(), collectionToString(p.value())));

            return concat(
                    Stream.of(missingAnnotations, missingInterfaces, missingExtension),
                    fieldViolations.stream(),
                    methodViolations.stream(),
                    missingAnnotationParameters
            )
                    .filter(ViolationInfo::isNotEmpty)
                    .collect(toList());
        });
    }

    private static Collection<ViolationInfo> getMethodViolations(ClassOrInterfaceDeclaration declaration, Condition<Method> methodCondition) {
        val methods = declaration.getMethods();
        if (methods.isEmpty()) {
            // element is missing
            return listOf(new ViolationInfo(declaration, collectionToString(listOf(methodCondition)), true));
        }
        return MethodConsequentFilter.filterFromMethodDeclarations(declaration.getMethods(), methodCondition);
    }

    private static Collection<ViolationInfo> getFieldViolations(ClassOrInterfaceDeclaration declaration, Condition<Field> fieldCondition) {
        val fields = declaration.getFields();
        if (fields.isEmpty()) {
            // element is missing
            return listOf(new ViolationInfo(declaration, collectionToString(listOf(fieldCondition)), true));
        }
        return FieldConsequentFilter.filterFromFieldDeclarations(fields, fieldCondition);
    }

}
