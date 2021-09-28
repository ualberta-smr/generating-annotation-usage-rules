package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import com.github.javaparser.ast.body.*;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.Utils.containsAnnotation;
import static java.util.Collections.*;
import static java.util.stream.Collectors.toList;

public class ClassConsequentFilter {

    public static Map<ClassOrInterfaceDeclaration, Collection<ViolationInfo>> doFilter(Collection<ClassOrInterfaceDeclaration> declarations, JavaClass klass) {
        Map<ClassOrInterfaceDeclaration, Collection<ViolationInfo>> results = new HashMap<>();
        for (var declaration : declarations) {
            final var violations = doFilter(declaration, klass);
            if (!violations.isEmpty()) {
                results.put(declaration, violations);
            }
        }
        return results;
    }

    private static Collection<ViolationInfo> doFilter(ClassOrInterfaceDeclaration declaration, JavaClass klass) {
        // TODO: check annotations
        List<Annotation> requiredAnnotations = new ArrayList<>();
        for (var expected : klass.annotations()) {
            if (!containsAnnotation(declaration, expected)) {
                // TODO: annotation parameter handling is required
                requiredAnnotations.add(expected);
            } else {

            }
        }
        // TODO: check interface
        List<Type> requiredInterfaces = new ArrayList<>();
        for (var anInterface : klass.implementedInterfaces()) {
            for (var implementedType : declaration.getImplementedTypes()) {
                if (!implementedType.getName().asString().equals(anInterface.name())) {
                    requiredInterfaces.add(anInterface);
                }
            }
        }
        // TODO: check extension
        Type requiredTypeToExtend = null;
        final boolean hasExtended = declaration.getExtendedTypes().stream()
                .anyMatch(e -> e.getName().asString().equals(klass.extendedClass().name()));
        if (!hasExtended) {
            requiredTypeToExtend = klass.extendedClass();
        }
        // TODO: check method
        var methodViolations = getMethodViolations(declaration, klass.method());
        // TODO: check field
        var fieldViolations = getFieldViolations(declaration, klass.field());

        if (requiredAnnotations.isEmpty() && requiredTypeToExtend == null && requiredInterfaces.isEmpty() && methodViolations.isEmpty() && fieldViolations.isEmpty()) {
            // when this is the exact method, nothing is missing, no violation
            return emptyList();
        } else {
            var missingAnnotations = new ViolationInfo(declaration, requiredAnnotations.stream().map(Annotation::toString).collect(toList()));
            var missingInterfaces = new ViolationInfo(declaration, requiredInterfaces.stream().map(Type::toString).collect(toList()));
            var missingExtension = new ViolationInfo(declaration, requiredTypeToExtend == null ? emptyList() : singleton(requiredTypeToExtend.name()));

            var a1 = Stream.of(missingAnnotations, missingInterfaces, missingExtension);
            return Stream.concat(a1, Stream.concat(fieldViolations.stream(), methodViolations.stream()))
                    .filter(v -> !v.missingElements().isEmpty())
                    .collect(toList());
        }
    }

    private static Collection<ViolationInfo> getMethodViolations(ClassOrInterfaceDeclaration declaration, Method method) {
        return MethodConsequentFilter
                .doFilter(declaration.getMethods(), method)
                .entrySet()
                .stream()
                .flatMap(entry -> entry.getValue().stream())
                .collect(toList());
    }

    private static Collection<ViolationInfo> getFieldViolations(ClassOrInterfaceDeclaration declaration, Field field) {
        return FieldConsequentFilter
                .doFilter(declaration.getFields(), field)
                .entrySet()
                .stream()
                .flatMap(entry -> entry.getValue().stream())
                .collect(toList());
    }

}
