package ca.ualberta.smr.deprecated.antecedent;

import ca.ualberta.smr.deprecated.model.javaelements.Condition;
import ca.ualberta.smr.deprecated.model.javaelements.Method;
import ca.ualberta.smr.deprecated.model.javaelements.MethodParameter;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;

import java.util.Collection;
import java.util.stream.Collectors;

import static ca.ualberta.smr.deprecated.AnnotationUtils.containsAnnotation;

public class MethodAntecedentFilter {

    /**
     * Selects the 'MethodDeclaration's that match the method condition
     * @param cu Compilation Unit (mostly a class)
     * @param method method condition that we want to use as a filter
     * @return a collection of filtered 'MethodDeclaration's
     */
    public static Collection<MethodDeclaration> doFilter(CompilationUnit cu, Condition<Method> method) {
        return doFilter(cu.findAll(MethodDeclaration.class), method);
    }

    /**
     * Selects the 'MethodDeclaration's that match the method condition
     * @param methodDeclarations a collection of method declarations
     * @param method method condition that we want to use as a filter
     * @return a collection of filtered 'MethodDeclaration's
     */
    public static Collection<MethodDeclaration> doFilter(Collection<MethodDeclaration> methodDeclarations, Condition<Method> method) {
        return methodDeclarations.stream()
                .filter(m -> methodHasAnnotations(m, method)
                        && methodHasParameters(m, method)
                        && methodHasReturnType(m, method))
                .collect(Collectors.toList());
    }

    /**
     * Checks if the method has given annotations
     */
    static boolean methodHasAnnotations(MethodDeclaration methodDeclaration, Condition<Method> methodCondition) {
        return methodCondition.test(method ->
                method.annotations().stream().allMatch(a -> containsAnnotation(methodDeclaration, a)));
    }

    /**
     * Checks if the method has given parameters
     */
    static boolean methodHasParameters(MethodDeclaration methodDeclaration, Condition<Method> methodCondition) {
        return methodCondition.test(method ->
                method.parameters().stream().allMatch(mp ->
                        methodDeclaration.getParameters().stream().anyMatch(p -> parameterMatches(p, mp))));
    }

    /**
     * Checks if the parameter matches with the provided condition
     */
    static boolean parameterMatches(Parameter parameterDeclaration, Condition<MethodParameter> parameterCondition) {
        return parameterCondition
                .test(p -> {
                    final boolean sameType = p.type().test(t -> t.equalsTypeString(parameterDeclaration.getTypeAsString()));
                    return sameType && p.annotations().stream().allMatch(a -> containsAnnotation(parameterDeclaration, a));
                });
    }

    /**
     * Checks if the method has the given return type
     */
    static boolean methodHasReturnType(MethodDeclaration methodDeclaration, Condition<Method> methodCondition) {
        return methodCondition.test(method ->
                method.returnType() == null ||
                        method.returnType().test(t -> t.equalsTypeString(methodDeclaration.getTypeAsString()))
        );
    }

}
