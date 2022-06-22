package ca.ualberta.smr.deprecated.antecedent;

import ca.ualberta.smr.deprecated.model.javaelements.*;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.*;
import lombok.val;

import java.util.Collection;
import java.util.stream.Collectors;

import static ca.ualberta.smr.deprecated.antecedent.MethodAntecedentFilter.*;
import static ca.ualberta.smr.deprecated.AnnotationUtils.containsAnnotation;

/**
 * Used when the topmost (hierarchy-wise) antecedent element is a java class
 */
public class ClassAntecedentFilter {

    public static Collection<ClassOrInterfaceDeclaration> doFilter(CompilationUnit cu, Condition<JavaClass> classCondition) {
        return classCondition.select(k -> doFilter(cu, k));
    }

    private static Collection<ClassOrInterfaceDeclaration> doFilter(CompilationUnit cu, JavaClass klass) {
        val classes = cu.findAll(ClassOrInterfaceDeclaration.class, e -> !e.isAbstract() && !e.isInterface());

        val classesWithAnnotations = classes.stream().filter(clazz -> classHasAnnotations(clazz, klass.annotations()));

        val classesWithMethod = klass.method().isNotEmpty() ?
                classesWithAnnotations.filter(clazz -> classHasMethod(clazz, klass.method()))
                : classesWithAnnotations;

        val classesWithField = klass.field().isNotEmpty() ?
                classesWithMethod.filter(clazz -> classHasField(clazz, klass.field()))
                : classesWithMethod;

        val classesWithExtends = klass.extendedClass().isNotEmpty() ?
                classesWithField
                        .filter(clazz ->
                                klass.extendedClass().test(aClass ->
                                        clazz.getExtendedTypes().stream().anyMatch(c -> c.getName().asString().equals(aClass.name()))))
                : classesWithField;

        return classesWithExtends
                .filter(clazz -> classImplements(clazz, klass.implementedInterfaces()))
                .collect(Collectors.toList());
    }

    private static boolean classImplements(ClassOrInterfaceDeclaration clazz, Collection<Condition<Type>> implementedInterfaces) {
        return implementedInterfaces.stream().allMatch(i -> classImplementsAnInterface(clazz, i));
    }

    private static boolean classImplementsAnInterface(ClassOrInterfaceDeclaration clazz, Condition<Type> implementedInterfaceCondition) {
        return implementedInterfaceCondition.test(anInterface -> clazz.getImplementedTypes()
                .stream()
                .anyMatch(e -> e.getName().asString().equals(anInterface.name())));
    }

    /**
     * Checks if the class has the annotations given with the condition
     *
     * @param clazz                 class declaration to query
     * @param annotationsConditions can be something like: List[any(annotationsA, annotationsB), all(any(annotationsC, annotationsD))]
     * @return true if annotationsCondition exists, false otherwise
     */
    private static boolean classHasAnnotations(ClassOrInterfaceDeclaration clazz, Collection<Condition<Annotation>> annotationsConditions) {
        return annotationsConditions.stream().allMatch(a -> containsAnnotation(clazz, a));
    }

    /**
     * Checks if the class has the method given with the condition
     *
     * @param clazz           class declaration to query
     * @param methodCondition can be something like: any(methodA, methodB)
     * @return true if methodCondition exists, false otherwise
     */
    private static boolean classHasMethod(ClassOrInterfaceDeclaration clazz, Condition<Method> methodCondition) {
        return clazz.findAll(MethodDeclaration.class, m -> isFirstLevelChild(clazz, m))
                .stream()
                .filter(m -> methodHasAnnotations(m, methodCondition))
                .filter(m -> methodHasReturnType(m, methodCondition))
                .anyMatch(m -> methodHasParameters(m, methodCondition));
    }

    /**
     * Checks if the class has the field given with the condition
     *
     * @param clazz          class declaration to query
     * @param fieldCondition can be something like: any(fieldA, fieldB)
     * @return true if fieldCondition exists, false otherwise
     */
    private static boolean classHasField(ClassOrInterfaceDeclaration clazz, Condition<Field> fieldCondition) {
        return clazz.findAll(FieldDeclaration.class, f -> isFirstLevelChild(clazz, f))
                .stream()
                .filter(f -> FieldAntecedentFilter.fieldHasAnnotations(f, fieldCondition))
                .anyMatch(f -> FieldAntecedentFilter.fieldHasType(f, fieldCondition));
    }

    /**
     * Checks if the node is a first-level element in the class. First-level being direct child, and not something declared in an inner class
     *
     * @param clazz is the class we are querying in
     * @param node  is the node that we are checking
     * @return true if node is a first-level child, false otherwise
     */
    // TODO: check against inheritance
    private static boolean isFirstLevelChild(ClassOrInterfaceDeclaration clazz, Node node) {
        return node.getParentNode().filter(p -> p.equals(clazz)).isPresent();
    }

}
