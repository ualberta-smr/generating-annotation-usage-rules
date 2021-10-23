package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.model.javaelements.Parameter;
import com.github.javaparser.ast.body.*;
import lombok.val;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.Utils.*;
import static java.util.Collections.emptyList;
import static java.util.stream.Collectors.toList;
import static ca.ualberta.smr.utils.AnnotationUtils.*;
import static java.util.stream.Collectors.toMap;

public class MethodConsequentFilter {

    /**
     * Returns violations on methods based on the provided condition
     * @param declarations is a collection method declarations (basically wherever a method can exist)
     * @param methodCondition is the condition to check against
     * @return collection of violations
     */
    public static Collection<ViolationInfo> filterFromMethodDeclarations(Collection<MethodDeclaration> declarations, Condition<Method> methodCondition) {
        return findViolations(declarations, methodCondition).stream()
                .collect(toMap(ViolationInfo::treeElement, v -> v, ViolationInfo::merge))
                .values();
    }

    private static List<ViolationInfo> findViolations(Collection<MethodDeclaration> declarations, Condition<Method> methodCondition) {
        val results = doFilterFromMethodDeclarations(declarations, methodCondition);
        final boolean foundMatchingMethod = results.stream().anyMatch(Collection::isEmpty);
        if (foundMatchingMethod) {
            // if there's a match, it means no violations
            return emptyList();
        }
        return results.stream().flatMap(Collection::stream).collect(toList());
    }

    public static Collection<ViolationInfo> filterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Condition<Method> methodCondition) {
        Collection<ViolationInfo> violations = new ArrayList<>();
        for (val classDeclaration : declarations) {
            val methods = classDeclaration.findAll(MethodDeclaration.class);
            if (methods.isEmpty()) {
                // if there's no methods in the class, then what we are searching for is missing
                violations.add(new ViolationInfo(classDeclaration, collectionToString(listOf(methodCondition)), true));
            } else {
                val results = doFilterFromMethodDeclarations(methods, methodCondition);
                final boolean foundMatchingMethod = results.stream().anyMatch(Collection::isEmpty);
                if (!foundMatchingMethod) {
                    // if all the elements are violations, then we are missing that method in the class
                    violations.add(new ViolationInfo(classDeclaration, collectionToString(listOf(methodCondition))));
                }
            }
        }

        return violations;
    }

    private static Collection<Collection<ViolationInfo>> doFilterFromMethodDeclarations(Collection<MethodDeclaration> methodDeclarations, Condition<Method> methodCondition) {
        return methodDeclarations.stream()
                .map(md -> doFilter(md, methodCondition))
                .collect(toList());
    }

    private static Collection<ViolationInfo> doFilter(MethodDeclaration methodDeclaration, Condition<Method> expectedMethod) {
        return expectedMethod.evaluate(method -> findViolations(methodDeclaration, method));
    }

    private static List<ViolationInfo> findViolations(MethodDeclaration methodDeclaration, Method method) {
        val requiredAnnotations = getMissingAnnotations(methodDeclaration, method.annotations());

        val requiredAnnotationParameters = getMissingParameters(methodDeclaration, method.annotations());

        Collection<Condition<Type>> requiredReturnType = new ArrayList<>();
        // If any element in the condition has a return type
        if (method.returnType().isNotEmpty()) {
            val hasReturnType = method.returnType().test(t -> t.equalsTypeString(methodDeclaration.getTypeAsString()));
            if (!hasReturnType) {
                // TODO: can be simplified
                requiredReturnType.add(method.returnType());
            }
        }

        // TODO: check parameter annotations as well
        List<Condition<Parameter>> requiredParameters = new ArrayList<>();
        for (val expectedParam : method.parameters()) {
            for (val actualParam : methodDeclaration.getParameters()) {
                val hasParam = expectedParam.test(p -> p.type().equalsTypeString(actualParam.getTypeAsString()));
                if (!hasParam) {
                    requiredParameters.add(expectedParam);
                }
            }
        }

        val missingAnnotations = new ViolationInfo(methodDeclaration, collectionToString(requiredAnnotations));
        val missingAnnotationParameters = requiredAnnotationParameters
                .stream()
                .map(p -> new ViolationInfo(p.key(), collectionToString(p.value())));

        val missingParameters = new ViolationInfo(methodDeclaration, collectionToString(requiredParameters));
        val missingReturnType = new ViolationInfo(methodDeclaration, collectionToString(requiredReturnType));

        return concat(missingAnnotationParameters, Stream.of(missingReturnType, missingAnnotations, missingParameters))
                .filter(ViolationInfo::isNotEmpty)
                .collect(toList());
    }


}
