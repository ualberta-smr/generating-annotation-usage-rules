package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import com.github.javaparser.ast.body.*;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.AnnotationUtils.*;
import static ca.ualberta.smr.utils.Utils.*;
import static java.util.Collections.*;
import static java.util.stream.Collectors.toList;

public class ClassConsequentFilter {

    public static Collection<ViolationInfo> doFilter(Collection<ClassOrInterfaceDeclaration> declarations, JavaClass klass) {
        return declarations.stream()
                .map(cd -> doFilter(cd, klass))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    private static Collection<ViolationInfo> doFilter(ClassOrInterfaceDeclaration declaration, JavaClass expected) {
        var requiredAnnotations = getMissingAnnotations(declaration, expected.annotations());
        var requiredAnnotationParameters = getMissingParameters(declaration, expected.annotations());

        List<Type> requiredInterfaces = new ArrayList<>();
        for (var anInterface : expected.implementedInterfaces()) {
            for (var implementedType : declaration.getImplementedTypes()) {
                if (!implementedType.getName().asString().equals(anInterface.name())) {
                    requiredInterfaces.add(anInterface);
                }
            }
        }

        Type requiredTypeToExtend = null;
        final boolean hasExtended = declaration.getExtendedTypes().stream()
                .anyMatch(e -> e.getName().asString().equals(expected.extendedClass().name()));
        if (!hasExtended) {
            requiredTypeToExtend = expected.extendedClass();
        }
        var methodViolations = getMethodViolations(declaration, expected.method());
        var fieldViolations = getFieldViolations(declaration, expected.field());

        var missingAnnotations = new ViolationInfo(declaration, requiredAnnotations.stream().map(Annotation::toString).collect(toList()));
        var missingInterfaces = new ViolationInfo(declaration, requiredInterfaces.stream().map(Type::toString).collect(toList()));
        var missingExtension = new ViolationInfo(declaration, requiredTypeToExtend == null ? emptyList() : singleton(requiredTypeToExtend.name()));

        var missingAnnotationParameters = requiredAnnotationParameters
                .stream()
                .map(p -> new ViolationInfo(p.key(), p.value().stream().map(AnnotationParameter::toString).collect(toList())));

        return concat(
                Stream.of(missingAnnotations, missingInterfaces, missingExtension),
                fieldViolations.stream(),
                methodViolations.stream(),
                missingAnnotationParameters
        )
                .filter(ViolationInfo::isNotEmpty)
                .collect(toList());
    }

    private static Collection<ViolationInfo> getMethodViolations(ClassOrInterfaceDeclaration declaration, Method method) {
        return MethodConsequentFilter
                .doFilter(declaration.getMethods(), method);
    }

    private static Collection<ViolationInfo> getFieldViolations(ClassOrInterfaceDeclaration declaration, Field field) {
        return FieldConsequentFilter
                .doFilter(declaration.getFields(), field);
    }

}
