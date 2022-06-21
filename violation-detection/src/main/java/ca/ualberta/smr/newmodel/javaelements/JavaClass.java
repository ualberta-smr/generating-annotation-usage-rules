package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.detection.ClassAntecedentScanner;
import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombinationAnd;
import ca.ualberta.smr.newmodel.violationreport.ViolationInfo;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.nodeTypes.NodeWithSimpleName;
import lombok.*;
import lombok.experimental.Accessors;

import java.util.*;

import static ca.ualberta.smr.utils.Utils.describe;
import static ca.ualberta.smr.utils.Utils.listOf;
import static java.util.stream.Collectors.toList;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
@ToString
public final class JavaClass extends ProgramElement implements AnalysisItem {
    private final AggregateCondition annotations;
    private final AggregateCondition field;
    private final AggregateCondition method;
    private final AggregateCondition extendedClass;
    private final AggregateCondition implementedInterfaces;
    // TODO: support for configuration files
    // TODO: support for constructors (that actually can be treated like methods)

    @Override
    public boolean matches(Object bd) {
        if (bd instanceof ClassOrInterfaceDeclaration) {
            val cd = (ClassOrInterfaceDeclaration) bd;
            boolean annotationMatches = annotations.matches(cd.getAnnotations());
            boolean fieldsMatch = field.isEmpty() || cd.getFields().stream().anyMatch(field::matches);
            boolean methodsMatch = method.isEmpty() || cd.getMethods().stream().anyMatch(method::matches);
            boolean extendMatch = extendedClass.isEmpty() || cd.getExtendedTypes().stream().map(NodeWithSimpleName::getNameAsString).anyMatch(extendedClass::matches);
            boolean implMatch = implementedInterfaces.isEmpty() || cd.getImplementedTypes().stream().map(NodeWithSimpleName::getNameAsString).anyMatch(implementedInterfaces::matches);

            return annotationMatches
                    && fieldsMatch
                    && methodsMatch
                    && extendMatch
                    && implMatch;
        } else if (bd instanceof MethodDeclaration) {
            val md = (MethodDeclaration) bd;
            return method.matches(md);
        } else if (bd instanceof FieldDeclaration) {
            val fd = (FieldDeclaration) bd;
            return field.matches(fd);
        }

        return false;
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        val cd = (ClassOrInterfaceDeclaration) bd;

        val missingAnnotations = annotations.getMissing(cd.getAnnotations(), rule);
        val missingField = findMissing(field, ClassAntecedentScanner.findFieldsFromClassDeclaration(cd, rule.antecedent()), cd, rule);
        val missingMethod = findMissing(method, ClassAntecedentScanner.findMethodsFromClassDeclaration(cd, rule.antecedent()), cd, rule);
        val missingExtensions = findMissing(extendedClass,
                cd.getExtendedTypes().stream().map(NodeWithSimpleName::getNameAsString).collect(toList()), cd, rule);
        val missingImplementation = findMissing(implementedInterfaces,
                cd.getImplementedTypes().stream().map(NodeWithSimpleName::getNameAsString).collect(toList()), cd, rule);

        return new ViolationCombinationAnd(cd, listOf(
                missingField, missingMethod, missingExtensions, missingImplementation, missingAnnotations
        ));
    }

    private ViolationCombination findMissing(AggregateCondition prop, Collection<?> elements, ClassOrInterfaceDeclaration cd, StaticAnalysisRule rule) {
        if (prop.isEmpty() || elements.stream().map(e -> prop.getMissing(e, rule)).anyMatch(ViolationCombination::isEmpty)) {
            return ViolationCombination.EMPTY;
        }
        return new ViolationInfo(cd, prop.toString());
    }

    @Override
    String description() {
        Map<String, AggregateCondition> keyValues = new HashMap<>();
        keyValues.put("annotations", annotations);
        keyValues.put("field", field);
        keyValues.put("method", method);
        keyValues.put("extends", extendedClass);
        keyValues.put("implements", implementedInterfaces);
        return describe("class", keyValues);
    }
}
