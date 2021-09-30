package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.ast.body.*;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.AnnotationUtils.*;
import static ca.ualberta.smr.utils.Utils.*;
import static java.util.Collections.*;
import static java.util.stream.Collectors.toList;

public class ClassConsequentFilter {

    public static Collection<ViolationInfo> doFilter(Collection<ClassOrInterfaceDeclaration> declarations, Condition<JavaClass> klass) {
        return declarations.stream()
                .map(cd -> doFilter(cd, klass))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    private static Collection<ViolationInfo> doFilter(ClassOrInterfaceDeclaration declaration, Condition<JavaClass> expected) {
        var requiredAnnotations = getMissingAnnotations(declaration, expected.flatMap(JavaClass::annotations));
        var requiredAnnotationParameters = getMissingParameters(declaration, expected.flatMap(JavaClass::annotations));

        Collection<Condition<Type>> requiredInterfaces = new ArrayList<>();
        for (var anInterface : expected.flatMap(JavaClass::implementedInterfaces)) {
            for (var implementedType : declaration.getImplementedTypes()) {
                if (anInterface.test(i -> !i.equalsTypeString(implementedType.getNameAsString()))) {
                    requiredInterfaces.add(anInterface);
                }
            }
        }

        Collection<Condition<Type>> requiredTypeToExtend = new ArrayList<>();

        var hasExtended = declaration.getExtendedTypes().stream().anyMatch(e ->
                expected.test(klazz -> klazz.extendedClass().test(t -> t.equalsTypeString(e.getNameAsString()))));

        if (!hasExtended) {
            requiredTypeToExtend = expected.map(JavaClass::extendedClass);
        }
        var methodViolations = getMethodViolations(declaration, expected.map(JavaClass::method));
        var fieldViolations = getFieldViolations(declaration, expected.map(JavaClass::field));

        var missingAnnotations = new ViolationInfo(declaration, requiredAnnotations.stream().map(Condition::toString).collect(toList()));
        var missingInterfaces = new ViolationInfo(declaration, requiredInterfaces.stream().map(Condition::toString).collect(toList()));
        var missingExtension = new ViolationInfo(declaration, requiredTypeToExtend.stream().map(Condition::toString).collect(toList()));

        var missingAnnotationParameters = requiredAnnotationParameters
                .stream()
                .map(p -> new ViolationInfo(p.key(), p.value().stream().map(Condition::toString).collect(toList())));

        return concat(
                Stream.of(missingAnnotations, missingInterfaces, missingExtension),
                fieldViolations.stream(),
                methodViolations.stream(),
                missingAnnotationParameters
        )
                .filter(ViolationInfo::isNotEmpty)
                .collect(toList());
    }

    private static Collection<ViolationInfo> getMethodViolations(ClassOrInterfaceDeclaration declaration, Collection<Condition<Method>> methodConditions) {
        return methodConditions.stream()
                .map(mc -> MethodConsequentFilter.doFilter(declaration.getMethods(), mc))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    private static Collection<ViolationInfo> getFieldViolations(ClassOrInterfaceDeclaration declaration, Collection<Condition<Field>> fieldConditions) {
        return fieldConditions.stream()
                .map(fc -> FieldConsequentFilter.doFilter(declaration.getFields(), fc))
                .flatMap(Collection::stream)
                .collect(toList());
    }

}
