package ca.ualberta.smr.detection;

import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import lombok.val;

import java.util.Collection;
import java.util.stream.Collectors;

public class ClassAntecedentScanner {

    public static Collection<ClassOrInterfaceDeclaration> findClasses(CompilationUnit cu, AggregateCondition clazz) {
        val fieldDeclarations = cu.findAll(ClassOrInterfaceDeclaration.class);

        return fieldDeclarations.stream()
                .filter(clazz::matches)
                .collect(Collectors.toList());
    }

}
