package ca.ualberta.smr.antecedent;

import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.Method;
import ca.ualberta.smr.model.javaelements.MethodParameter;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;

import java.util.Collection;

import static ca.ualberta.smr.utils.AnnotationUtils.containsAnnotation;

public class MethodAntecedentFilter {

    public static Collection<MethodDeclaration> doFilter(CompilationUnit cu, Condition<Method> method) {
        return cu.findAll(MethodDeclaration.class, m ->
                methodHasAnnotations(m, method)
                        && methodHasParameters(m, method)
                        && methodHasReturnType(m, method)
        );
    }

    static boolean methodHasAnnotations(MethodDeclaration methodDeclaration, Condition<Method> methodCondition) {
        return methodCondition.test(method ->
                method.annotations().stream().allMatch(a -> containsAnnotation(methodDeclaration, a)));
    }

    static boolean methodHasParameters(MethodDeclaration methodDeclaration, Condition<Method> methodCondition) {
        return methodCondition.test(method ->
                method.parameters().stream().allMatch(mp ->
                        methodDeclaration.findAll(Parameter.class).stream().anyMatch(p -> parameterMatches(p, mp))));
    }

    static boolean parameterMatches(Parameter parameterDeclaration, Condition<MethodParameter> parameterCondition) {
        return parameterCondition
                .test(p -> {
                    final boolean sameType = p.type().test(t -> t.equalsTypeString(parameterDeclaration.getTypeAsString()));
                    // checks for sameType and containing all required annotations
                    return sameType && p.annotations().stream().allMatch(a -> containsAnnotation(parameterDeclaration, a));
                });
    }

    static boolean methodHasReturnType(MethodDeclaration methodDeclaration, Condition<Method> methodCondition) {
        return methodCondition.test(method ->
                method.returnType() == null ||
                        method.returnType().test(t -> t.equalsTypeString(methodDeclaration.getTypeAsString()))
        );
    }

}
