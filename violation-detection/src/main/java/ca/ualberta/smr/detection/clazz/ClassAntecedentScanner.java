package ca.ualberta.smr.detection.clazz;

import ca.ualberta.smr.model.javaelements.AggregateCondition;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import lombok.val;

import java.util.Collection;

import static java.util.stream.Collectors.toList;

public class ClassAntecedentScanner {

    public static Collection<ClassOrInterfaceDeclaration> findClasses(CompilationUnit cu, AggregateCondition clazz) {
        val classDeclarations = cu.findAll(ClassOrInterfaceDeclaration.class);

        return classDeclarations.stream()
                .filter(clazz::matches)
                .collect(toList());
    }

    public static Collection<MethodDeclaration> findMethodsFromClassDeclaration(ClassOrInterfaceDeclaration cd, AggregateCondition clazz) {
        val methodDeclarations = cd.getMethods();

        val matchingMethods = methodDeclarations.stream()
                .filter(clazz::matches)
                .collect(toList());

        if (matchingMethods.isEmpty()) return methodDeclarations;
        return matchingMethods;
    }

    public static Collection<FieldDeclaration> findFieldsFromClassDeclaration(ClassOrInterfaceDeclaration cd, AggregateCondition clazz) {
        val fieldDeclarations = cd.getFields();

        val matchingFields = fieldDeclarations.stream()
                .filter(clazz::matches)
                .collect(toList());

        if (matchingFields.isEmpty()) return fieldDeclarations;
        return matchingFields;
    }
}
