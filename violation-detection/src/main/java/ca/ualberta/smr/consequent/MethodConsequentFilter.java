package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.Parameter;
import ca.ualberta.smr.utils.Pair;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.AnnotationExpr;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.Utils.containsAnnotation;
import static ca.ualberta.smr.utils.Utils.getMissingParameters;
import static java.util.Collections.emptyList;
import static java.util.Collections.singleton;
import static java.util.stream.Collectors.toList;

public class MethodConsequentFilter {

    @SuppressWarnings("unchecked")
    public static <T extends BodyDeclaration<T>> Map<MethodDeclaration, Collection<ViolationInfo>> doFilter(Collection<T> declarations, Method method) {
        if (declarations.isEmpty()) return Collections.emptyMap();

        var sampleItem = declarations.stream().findAny().get();
        if (sampleItem instanceof MethodDeclaration) {
            return doFilterFromMethodDeclarations((Collection<MethodDeclaration>) declarations, method);
        } else if (sampleItem instanceof ClassOrInterfaceDeclaration) {
            return doFilterFromClassDeclarations((Collection<ClassOrInterfaceDeclaration>) declarations, method);
        }
        throw new IllegalArgumentException("Required a collection of one of the following types (ClassOrInterfaceDeclaration, MethodDeclaration) got %s instead".formatted(sampleItem.getClass()));
    }

    private static Map<MethodDeclaration, Collection<ViolationInfo>> doFilterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Method method) {
        var methodDeclarations = declarations.stream()
                .flatMap(cd -> cd.findAll(MethodDeclaration.class).stream())
                .collect(toList());
        return doFilterFromMethodDeclarations(methodDeclarations, method);
    }

    private static Map<MethodDeclaration, Collection<ViolationInfo>> doFilterFromMethodDeclarations(Collection<MethodDeclaration> methodDeclarations, Method method) {
        Map<MethodDeclaration, Collection<ViolationInfo>> res = new HashMap<>();
        for (MethodDeclaration methodDeclaration : methodDeclarations) {
            final Collection<ViolationInfo> violations = doFilter(methodDeclaration, method);
            if (!violations.isEmpty()) {
                res.put(methodDeclaration, violations);
            }
        }
        return res;
    }

    /**
     * Returns collection of facts
     * @param methodDeclaration
     * @param expected
     * @return
     */
    private static Collection<ViolationInfo> doFilter(MethodDeclaration methodDeclaration, Method expected) {
        // TODO: annotations
        List<Annotation> requiredAnnotations = new ArrayList<>();
        List<Pair<AnnotationExpr, Collection<AnnotationParameter>>> requiredAnnotationParameters = new ArrayList<>();
        for (var annotation : expected.annotations()) {
            if (!containsAnnotation(methodDeclaration, annotation)) {
                requiredAnnotations.add(annotation);
            } else {
                final var missingParameters = getMissingParameters(methodDeclaration, annotation);
                if (missingParameters.hasValue() && !missingParameters.value().isEmpty()) {
                    requiredAnnotationParameters.add(missingParameters);
                }
            }
        }
        // TODO: return type
        Type requiredReturnType = null;
        if (expected.returnType() != null) {
            final boolean hasReturnType = methodDeclaration.getTypeAsString().equals(expected.returnType().name());
            if (!hasReturnType) {
                requiredReturnType = expected.returnType();
            }
        }
        List<Parameter> requiredParameters = new ArrayList<>();
        // TODO: parameters
        for (var expectedParam : expected.parameters()) {
            for (var actualParam : methodDeclaration.getParameters()) {
                boolean hasParam = actualParam.getTypeAsString().equals(expectedParam.type().name());
                if (!hasParam) {
                    requiredParameters.add(expectedParam);
                }
            }
        }

        if (requiredAnnotations.isEmpty() && requiredReturnType == null && requiredParameters.isEmpty() && requiredAnnotationParameters.isEmpty()) {
            // when this is the exact method, nothing is missing, no violation
            return Collections.emptyList();
        } else {
            var missingAnnotations = new ViolationInfo(methodDeclaration, requiredAnnotations.stream().map(Annotation::toString).collect(toList()));

            var missingAnnotationParameters = requiredAnnotationParameters
                    .stream()
                    .map(p -> new ViolationInfo(p.key(), p.value().stream().map(AnnotationParameter::toString).collect(toList())));

            var missingParameters = new ViolationInfo(methodDeclaration, requiredParameters.stream().map(Parameter::toString).collect(toList()));
            var missingReturnType = new ViolationInfo(methodDeclaration, requiredReturnType == null ? emptyList() : singleton(requiredReturnType.name()));

            return Stream.concat(missingAnnotationParameters, Stream.of(missingReturnType, missingAnnotations, missingParameters))
                    .filter(v -> !v.missingElements().isEmpty())
                    .collect(toList());
        }
    }

}
