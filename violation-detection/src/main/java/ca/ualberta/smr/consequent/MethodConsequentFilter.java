package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.Parameter;
import com.github.javaparser.ast.body.*;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.Utils.concat;
import static java.util.Collections.*;
import static java.util.stream.Collectors.toList;
import static ca.ualberta.smr.utils.AnnotationUtils.*;

public class MethodConsequentFilter {

    @SuppressWarnings("unchecked")
    public static <T extends BodyDeclaration<T>> Collection<ViolationInfo> doFilter(Collection<T> declarations, Method method) {
        if (declarations.isEmpty()) return Collections.emptyList();

        var sampleItem = declarations.stream().findAny().get();
        if (sampleItem instanceof MethodDeclaration) {
            return doFilterFromMethodDeclarations((Collection<MethodDeclaration>) declarations, method);
        } else if (sampleItem instanceof ClassOrInterfaceDeclaration) {
            return doFilterFromClassDeclarations((Collection<ClassOrInterfaceDeclaration>) declarations, method);
        }
        throw new IllegalArgumentException("Required a collection of one of the following types (ClassOrInterfaceDeclaration, MethodDeclaration) got %s instead".formatted(sampleItem.getClass()));
    }

    private static Collection<ViolationInfo> doFilterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Method method) {
        var methodDeclarations = declarations.stream()
                .flatMap(cd -> cd.findAll(MethodDeclaration.class).stream())
                .collect(toList());
        return doFilterFromMethodDeclarations(methodDeclarations, method);
    }

    private static Collection<ViolationInfo> doFilterFromMethodDeclarations(Collection<MethodDeclaration> methodDeclarations, Method method) {
        return methodDeclarations.stream()
                .map(md -> doFilter(md, method))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    /**
     * Returns collection of facts
     * @param methodDeclaration
     * @param expected
     * @return
     */
    private static Collection<ViolationInfo> doFilter(MethodDeclaration methodDeclaration, Method expected) {
        var requiredAnnotations = getMissingAnnotations(methodDeclaration, expected.annotations());
        var requiredAnnotationParameters = getMissingParameters(methodDeclaration, expected.annotations());

        Type requiredReturnType = null;
        if (expected.returnType() != null) {
            final boolean hasReturnType = methodDeclaration.getTypeAsString().equals(expected.returnType().name());
            if (!hasReturnType) {
                requiredReturnType = expected.returnType();
            }
        }

        // TODO: check parameter annotations as well
        List<Parameter> requiredParameters = new ArrayList<>();
        for (var expectedParam : expected.parameters()) {
            for (var actualParam : methodDeclaration.getParameters()) {
                boolean hasParam = actualParam.getTypeAsString().equals(expectedParam.type().name());
                if (!hasParam) {
                    requiredParameters.add(expectedParam);
                }
            }
        }

        var missingAnnotations = new ViolationInfo(methodDeclaration, requiredAnnotations.stream().map(Annotation::toString).collect(toList()));
        var missingAnnotationParameters = requiredAnnotationParameters
                .stream()
                .map(p -> new ViolationInfo(p.key(), p.value().stream().map(AnnotationParameter::toString).collect(toList())));

        var missingParameters = new ViolationInfo(methodDeclaration, requiredParameters.stream().map(Parameter::toString).collect(toList()));
        var missingReturnType = new ViolationInfo(methodDeclaration, requiredReturnType == null ? emptyList() : singleton(requiredReturnType.name()));

        return concat(missingAnnotationParameters, Stream.of(missingReturnType, missingAnnotations, missingParameters))
                .filter(ViolationInfo::isNotEmpty)
                .collect(toList());
    }

}
