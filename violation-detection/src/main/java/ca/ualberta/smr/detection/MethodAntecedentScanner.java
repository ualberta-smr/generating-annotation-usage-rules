package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.MethodDeclaration;
import lombok.val;

import java.util.Collection;
import java.util.stream.Collectors;

public class MethodAntecedentScanner {

    public static Collection<MethodDeclaration> findMethods(CompilationUnit cu, AggregateCondition method) {
        val methodDeclarations = cu.findAll(MethodDeclaration.class);

        return methodDeclarations.stream()
                .filter(method::matches)
                .collect(Collectors.toList());
    }

}
