package ca.ualberta.smr.consequent;

import ca.ualberta.smr.antecedent.FieldAntecedentFilter;
import ca.ualberta.smr.antecedent.MethodAntecedentFilter;
import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.ast.body.*;
import lombok.val;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.AnnotationUtils.*;
import static ca.ualberta.smr.utils.Utils.*;
import static java.util.stream.Collectors.toList;

public class ClassConsequentFilter {

    @SuppressWarnings("unchecked")
    public static Collection<ViolationInfo> filterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, StaticAnalysisRule rule) {
        Condition<JavaClass> klass = (Condition<JavaClass>) rule.consequent();
        return declarations.stream()
                .map(cd -> doFilter(cd, klass, rule))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    public static Collection<ViolationInfo> filterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Condition<JavaClass> klass){
        return declarations.stream()
                .map(cd -> doFilter(cd, klass, null))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    private static Collection<ViolationInfo> doFilter(ClassOrInterfaceDeclaration declaration, Condition<JavaClass> classCondition, StaticAnalysisRule rule) {
        return classCondition.evaluate(javaClass -> {
            val requiredAnnotations = getMissingAnnotations(declaration, javaClass.annotations());
            val requiredAnnotationParameters = getMissingParameters(declaration, javaClass.annotations());
            val requiredInterfaces = getRequiredInterfaces(declaration, javaClass);
            val requiredTypeToExtend = getRequiredTypeToExtend(declaration, javaClass);

            val methodViolations = getMethodViolations(declaration, javaClass.method(), rule);
            val fieldViolations = getFieldViolations(declaration, javaClass.field(), rule);

            val missingAnnotations = new ViolationInfo(declaration, collectionToString(requiredAnnotations));
            val missingInterfaces = new ViolationInfo(declaration, collectionToString(requiredInterfaces));
            val missingExtension = new ViolationInfo(declaration, collectionToString(requiredTypeToExtend));

            val missingAnnotationParameters = requiredAnnotationParameters
                    .stream()
                    .map(p -> new ViolationInfo(p.key(), collectionToString(p.value())));

            return concat(
                    Stream.of(missingAnnotations, missingInterfaces, missingExtension),
                    fieldViolations.stream(),
                    methodViolations.stream(),
                    missingAnnotationParameters
            )
                    .filter(ViolationInfo::isNotEmpty)
                    .collect(toList());
        });
    }

    private static Collection<Condition<Type>> getRequiredTypeToExtend(ClassOrInterfaceDeclaration declaration, JavaClass javaClass) {
        Collection<Condition<Type>> requiredTypeToExtend = new ArrayList<>();

        val hasExtended = declaration.getExtendedTypes().stream()
                .anyMatch(e ->
                        javaClass.extendedClass().test(t -> t.equalsTypeString(e.getNameAsString())));

        if (!hasExtended) {
            requiredTypeToExtend.add(javaClass.extendedClass());
        }
        return requiredTypeToExtend;
    }

    private static Collection<Condition<Type>> getRequiredInterfaces(ClassOrInterfaceDeclaration declaration, JavaClass javaClass) {
        Collection<Condition<Type>> requiredInterfaces = new ArrayList<>();
        for (val anInterface : javaClass.implementedInterfaces()) {
            for (val implementedType : declaration.getImplementedTypes()) {
                if (anInterface.test(i -> !i.equalsTypeString(implementedType.getNameAsString()))) {
                    requiredInterfaces.add(anInterface);
                }
            }
        }
        return requiredInterfaces;
    }

    private static Collection<ViolationInfo> getMethodViolations(ClassOrInterfaceDeclaration declaration, Condition<Method> methodCondition, StaticAnalysisRule rule) {
        val methods = declaration.getMethods();
        if (methods.isEmpty()) {
            // element is missing
            return listOf(new ViolationInfo(declaration, collectionToString(listOf(methodCondition)), true));
        }

        if (rule != null) {
            final Condition<Method> methodAntecedentCondition = ((JavaClass) rule.antecedent()).method();
            if (methodAntecedentCondition.isNotEmpty()) {
                final Collection<MethodDeclaration> filteredMethods = MethodAntecedentFilter.doFilter(methods, methodAntecedentCondition);
                return MethodConsequentFilter.filterFromMethodDeclarations(filteredMethods, methodCondition);
            }
        }

        return MethodConsequentFilter.filterFromMethodDeclarations(methods, methodCondition);
    }

    private static Collection<ViolationInfo> getFieldViolations(ClassOrInterfaceDeclaration declaration, Condition<Field> fieldCondition, StaticAnalysisRule rule) {
        val fields = declaration.getFields();
        if (fields.isEmpty()) {
            // element is missing
            return listOf(new ViolationInfo(declaration, collectionToString(listOf(fieldCondition)), true));
        }
        if (rule != null) {
            val fieldAntecedentCondition = ((JavaClass) rule.antecedent()).field();
            if (fieldAntecedentCondition.isNotEmpty()) {
                val filteredFields = FieldAntecedentFilter.doFilter(fields, fieldAntecedentCondition);
                return FieldConsequentFilter.filter(filteredFields, fieldCondition);
            }
        }

        return FieldConsequentFilter.filterFromFieldDeclarations(fields, fieldCondition);
    }

}
