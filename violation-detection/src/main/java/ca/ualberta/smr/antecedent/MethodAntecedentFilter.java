package ca.ualberta.smr.antecedent;

import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.Method;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;

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
                        mp.test(p -> methodDeclaration.hasParametersOfType(p.type().name()))));

    }

    static boolean methodHasReturnType(MethodDeclaration methodDeclaration, Condition<Method> methodCondition) {
        return methodCondition.test(method ->
                method.returnType() == null ||
                        method.returnType().test(t -> t.equalsTypeString(methodDeclaration.getTypeAsString()))
        );
    }

}
