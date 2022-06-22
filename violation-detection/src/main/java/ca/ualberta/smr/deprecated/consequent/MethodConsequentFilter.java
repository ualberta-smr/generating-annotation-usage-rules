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

public class MethodConsequentFilter {

    @SuppressWarnings("unchecked")
    public static Collection<ViolationInfo> filter(Collection<MethodDeclaration> declarations, Condition<? extends AnalysisItem> condition) {
        final Class<? extends AnalysisItem> type = condition.getType();
        if (type.equals(JavaClass.class)){
            val javaClassCondition = (Condition<JavaClass>) condition;
            val classDeclarations = getClassDeclarations(declarations);

            return ClassConsequentFilter.filterFromClassDeclarations(classDeclarations, javaClassCondition);
        } else if (type.equals(Method.class)) {
            return filterFromMethodDeclarations(declarations, (Condition<Method>) condition);
        }
        throw new RuntimeException("Analysis item type should be one of the following: [JavaClass, Method]");
    }

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
        return results.stream().flatMap(Collection::stream).collect(toList());
    }

    public static Collection<ViolationInfo> filterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Condition<Method> methodCondition) {
        Collection<ViolationInfo> violations = new ArrayList<>();
        for (val classDeclaration : declarations) {
            val methods = classDeclaration.findAll(MethodDeclaration.class);
            if (methods.isEmpty()) {
                // if there's no methods in the class, then what we are searching for is missing
                violations.add(new ViolationInfo(classDeclaration, collectionToString(GeneralUtility.listOf(methodCondition)), true));
            } else {
                val results = doFilterFromMethodDeclarations(methods, methodCondition);
                final boolean noMatchingMethod = results.stream().noneMatch(Collection::isEmpty);
                if (noMatchingMethod) {
                    // if all the elements are violations, then we are missing that method in the class
                    violations.add(new ViolationInfo(classDeclaration, collectionToString(GeneralUtility.listOf(methodCondition))));
                }
            }
        }

        return violations;
    }

    public static Collection<Collection<ViolationInfo>> doFilterFromMethodDeclarations(Collection<MethodDeclaration> methodDeclarations, Condition<Method> methodCondition) {
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
        List<Condition<MethodParameter>> requiredParameters = new ArrayList<>();
        for (val expectedParam : method.parameters()) {
            for (val actualParam : methodDeclaration.getParameters()) {
                val hasParam = expectedParam.test(p -> p.type().test(t -> t.equalsTypeString(actualParam.getTypeAsString())));
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
