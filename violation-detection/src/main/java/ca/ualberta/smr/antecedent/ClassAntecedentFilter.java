package ca.ualberta.smr.antecedent;

import ca.ualberta.smr.model.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.*;

import java.util.Collection;
import java.util.stream.Collectors;

import static ca.ualberta.smr.antecedent.MethodAntecedentFilter.*;
import static ca.ualberta.smr.utils.AnnotationUtils.containsAnnotation;

/**
 * Used when the topmost (hierarchy-wise) antecedent element is a java class
 */
public class ClassAntecedentFilter {

    public static Collection<ClassOrInterfaceDeclaration> doFilter(CompilationUnit cu, JavaClass klass) {
        var classes = cu.findAll(ClassOrInterfaceDeclaration.class)
                .stream()
                .filter(e -> !e.isAbstract() && !e.isInterface());

        var classesWithAnnotations = classes.filter(clazz -> classHasAnnotations(clazz, klass.annotations()));
        var classesWithMethod = klass.method() != null ?
                classesWithAnnotations.filter(clazz -> classHasMethod(clazz, klass.method())) : classesWithAnnotations;
        var classesWithField = klass.field() != null ?
                classesWithMethod.filter(clazz -> classHasField(clazz, klass.field())) : classesWithMethod;
        return classesWithField.filter(clazz -> classImplements(clazz, klass.implementedInterfaces())).collect(Collectors.toList());
    }

    private static boolean classImplements(ClassOrInterfaceDeclaration clazz, Collection<Type> implementedInterfaces) {
        return implementedInterfaces.stream().allMatch(i -> classImplementsOneInterface(clazz, i));
    }

    private static boolean classImplementsOneInterface(ClassOrInterfaceDeclaration clazz, Type implementedInterface) {
        return clazz.getImplementedTypes().stream().anyMatch(e -> e.getName().asString().equals(implementedInterface.name()));
    }

    private static boolean classHasAnnotations(ClassOrInterfaceDeclaration klass, Collection<Annotation> annotations) {
        return annotations.stream().allMatch(a -> containsAnnotation(klass, a));
    }

    private static boolean classHasMethod(ClassOrInterfaceDeclaration klass, Method method) {
        final var methodDeclarations = klass.findAll(MethodDeclaration.class);

        final var methodStream = methodDeclarations.stream();

        return methodStream
                .filter(m -> methodHasAnnotations(m, method))
                .filter(m -> methodHasReturnType(m, method))
                .anyMatch(m -> methodHasParameters(m, method));
    }

    private static boolean classHasField(ClassOrInterfaceDeclaration klass, Field field) {
        final var fieldDeclarations = klass.findAll(FieldDeclaration.class);

        final var fieldStream = fieldDeclarations.stream();

        return fieldStream
                .filter(f -> fieldHasAnnotations(f, field))
                .anyMatch(f -> fieldHasType(f, field));
    }

    private static boolean fieldHasType(FieldDeclaration fieldDeclaration, Field field) {
        if (field.type() == null) return true;
        return fieldDeclaration.getElementType().toString().equals(field.type().name());
    }

    private static boolean fieldHasAnnotations(FieldDeclaration fieldDeclaration, Field field) {
        return field.annotations().stream().allMatch(a -> containsAnnotation(fieldDeclaration, a));
    }

}
