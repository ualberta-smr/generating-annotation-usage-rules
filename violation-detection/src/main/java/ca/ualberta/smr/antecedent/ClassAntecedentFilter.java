package ca.ualberta.smr.antecedent;

import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.*;

import java.util.Collection;
import java.util.stream.Collectors;

import static ca.ualberta.smr.antecedent.FieldAntecedentFilter.fieldHasAnnotations;
import static ca.ualberta.smr.antecedent.FieldAntecedentFilter.fieldHasType;
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

    private static boolean classImplements(ClassOrInterfaceDeclaration clazz, Collection<Condition<Type>> implementedInterfaces) {
        return implementedInterfaces.stream().allMatch(i -> classImplementsAnInterface(clazz, i));
    }

    private static boolean classImplementsAnInterface(ClassOrInterfaceDeclaration clazz, Condition<Type> implementedInterfaceCondition) {
        return implementedInterfaceCondition.test(anInterface -> clazz.getImplementedTypes()
                .stream()
                .anyMatch(e -> e.getName().asString().equals(anInterface.name())));
    }

    private static boolean classHasAnnotations(ClassOrInterfaceDeclaration klass, Collection<Condition<Annotation>> annotations) {
        return annotations.stream().allMatch(a -> containsAnnotation(klass, a));
    }

    private static boolean classHasMethod(ClassOrInterfaceDeclaration klass, Condition<Method> method) {
        final var methodDeclarations = klass.findAll(MethodDeclaration.class);

        final var methodStream = methodDeclarations.stream();

        return methodStream
                .filter(m -> methodHasAnnotations(m, method))
                .filter(m -> methodHasReturnType(m, method))
                .anyMatch(m -> methodHasParameters(m, method));
    }

    private static boolean classHasField(ClassOrInterfaceDeclaration klass, Condition<Field> fieldCondition) {
        return klass.findAll(FieldDeclaration.class)
                .stream()
                .filter(f -> fieldHasAnnotations(f, fieldCondition))
                .anyMatch(f -> fieldHasType(f, fieldCondition));
    }

}
