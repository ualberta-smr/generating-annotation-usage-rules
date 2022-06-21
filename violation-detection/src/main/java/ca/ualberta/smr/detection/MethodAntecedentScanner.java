package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import lombok.val;

import java.util.Collection;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.toList;

public class MethodAntecedentScanner {

    public static Collection<MethodDeclaration> findMethods(CompilationUnit cu, AggregateCondition method) {
        val methodDeclarations = cu.findAll(MethodDeclaration.class);

        return methodDeclarations.stream()
                .filter(method::matches)
                .collect(Collectors.toList());
    }

    public static Collection<Parameter> findMethodParametersFromMethodDeclaration(MethodDeclaration md, AggregateCondition method) {
        val parameters = md.findAll(Parameter.class);

        val matchingParams = parameters.stream()
                .filter(method::matches)
                .collect(toList());

        if (matchingParams.isEmpty()) return parameters;
        return matchingParams;
    }

}
