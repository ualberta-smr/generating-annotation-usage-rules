package ca.ualberta.smr.antecedent;

import ca.ualberta.smr.model.Method;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;

import java.util.Collection;
import java.util.stream.Collectors;

import static ca.ualberta.smr.utils.Utils.containsAnnotation;

public class MethodAntecedentFilter {

    public static Collection<MethodDeclaration> doFilter(CompilationUnit cu, Method method) {
        final var methods = cu.findAll(MethodDeclaration.class);

        return methods.stream()
                .filter(m -> methodHasAnnotations(m, method))
                .filter(m -> methodHasParameters(m, method))
                .filter(m -> methodHasReturnType(m, method))
                .collect(Collectors.toList());
    }

    static boolean methodHasAnnotations(MethodDeclaration methodDeclaration, Method method) {
        return method.annotations().stream().allMatch(a -> containsAnnotation(methodDeclaration, a));
    }

    static boolean methodHasParameters(MethodDeclaration methodDeclaration, Method method) {
        return method.parameters().stream().allMatch(p -> methodDeclaration.hasParametersOfType(p.type().name()));
    }

    static boolean methodHasReturnType(MethodDeclaration methodDeclaration, Method method) {
        if (method.returnType() == null) return true;
        return methodDeclaration.getTypeAsString().equals(method.returnType().name());
    }

}
