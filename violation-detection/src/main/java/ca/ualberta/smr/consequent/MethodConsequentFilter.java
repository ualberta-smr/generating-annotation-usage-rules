package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.model.javaelements.Parameter;
import com.github.javaparser.ast.body.*;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.Utils.concat;
import static java.util.stream.Collectors.toList;
import static ca.ualberta.smr.utils.AnnotationUtils.*;

public class MethodConsequentFilter {

    @SuppressWarnings("unchecked")
    public static <T extends BodyDeclaration<T>> Collection<ViolationInfo> doFilter(Collection<T> declarations, Condition<Method> methodCondition) {
        if (declarations.isEmpty()) return Collections.emptyList();

        var sampleItem = declarations.stream().findAny().get();
        if (sampleItem instanceof MethodDeclaration) {
            return doFilterFromMethodDeclarations((Collection<MethodDeclaration>) declarations, methodCondition);
        } else if (sampleItem instanceof ClassOrInterfaceDeclaration) {
            return doFilterFromClassDeclarations((Collection<ClassOrInterfaceDeclaration>) declarations, methodCondition);
        }
        throw new IllegalArgumentException("Required a collection of one of the following types (ClassOrInterfaceDeclaration, MethodDeclaration) got %s instead".formatted(sampleItem.getClass()));
    }

    private static Collection<ViolationInfo> doFilterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Condition<Method> methodCondition) {
        var methodDeclarations = declarations.stream()
                .flatMap(cd -> cd.findAll(MethodDeclaration.class).stream())
                .collect(toList());
        return doFilterFromMethodDeclarations(methodDeclarations, methodCondition);
    }

    private static Collection<ViolationInfo> doFilterFromMethodDeclarations(Collection<MethodDeclaration> methodDeclarations, Condition<Method> methodCondition) {
        return methodDeclarations.stream()
                .map(md -> doFilter(md, methodCondition))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    /**
     * Returns collection of facts
     * @param methodDeclaration
     * @param expectedCondition
     * @return
     */
    private static Collection<ViolationInfo> doFilter(MethodDeclaration methodDeclaration, Condition<Method> expectedCondition) {
        var requiredAnnotations = getMissingAnnotations(methodDeclaration, expectedCondition.flatMap(Method::annotations));

        var requiredAnnotationParameters = getMissingParameters(methodDeclaration, expectedCondition.flatMap(Method::annotations));

        Collection<Condition<Type>> requiredReturnType = new ArrayList<>();
        // If any element in the condition has a return type
        if (expectedCondition.test(a -> a.returnType().test(Objects::nonNull))) {
            var hasReturnType = expectedCondition.test(m -> m.returnType().test(t -> t.equalsTypeString(methodDeclaration.getTypeAsString())));
            if (!hasReturnType) {
                // TODO: can be simplified
                requiredReturnType = expectedCondition.map(Method::returnType);;
            }
        }

        // TODO: check parameter annotations as well
        List<Condition<Parameter>> requiredParameters = new ArrayList<>();
        for (var expectedParam : expectedCondition.flatMap(Method::parameters)) {
            for (var actualParam : methodDeclaration.getParameters()) {
                var hasParam = expectedParam.test(p -> p.type().equalsTypeString(actualParam.getTypeAsString()));
                if (!hasParam) {
                    requiredParameters.add(expectedParam);
                }
            }
        }

        var missingAnnotations = new ViolationInfo(methodDeclaration, requiredAnnotations.stream().map(Condition::toString).collect(toList()));
        var missingAnnotationParameters = requiredAnnotationParameters
                .stream()
                .map(p -> new ViolationInfo(p.key(), p.value().stream().map(Condition::toString).collect(toList())));

        var missingParameters = new ViolationInfo(methodDeclaration, requiredParameters.stream().map(Condition::toString).collect(toList()));
        var missingReturnType = new ViolationInfo(methodDeclaration, requiredReturnType.stream().map(Condition::toString).collect(toList()));

        return concat(missingAnnotationParameters, Stream.of(missingReturnType, missingAnnotations, missingParameters))
                .filter(ViolationInfo::isNotEmpty)
                .collect(toList());
    }

}
