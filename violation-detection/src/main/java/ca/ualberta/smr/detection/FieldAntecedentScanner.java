package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.FieldDeclaration;
import lombok.val;

import java.util.Collection;
import java.util.stream.Collectors;

public class FieldAntecedentScanner {

    public static Collection<FieldDeclaration> findFields(CompilationUnit cu, AggregateCondition field) {
        val fieldDeclarations = cu.findAll(FieldDeclaration.class);

        return fieldDeclarations.stream()
                .filter(field::matches)
                .collect(Collectors.toList());
    }

}
