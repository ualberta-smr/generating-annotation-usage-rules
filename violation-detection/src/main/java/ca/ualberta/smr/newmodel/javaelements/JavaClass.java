package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.ViolationCombinationAnd;
import ca.ualberta.smr.newmodel.ViolationInfo;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
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
        val cd = (ClassOrInterfaceDeclaration) bd;
        return annotations.matches(cd.getAnnotations())
                && cd.getFields().stream().anyMatch(field::matches)
                && cd.getMethods().stream().anyMatch(method::matches)
                && cd.getExtendedTypes().stream().map(NodeWithSimpleName::getNameAsString).anyMatch(extendedClass::matches)
                && cd.getImplementedTypes().stream().map(NodeWithSimpleName::getNameAsString).anyMatch(implementedInterfaces::matches);
    }

    @Override
    public ViolationCombination getMissing(Object bd) {
        val cd = (ClassOrInterfaceDeclaration) bd;

        val missingAnnotations = annotations.getMissing(cd.getAnnotations());
        val missingField = findMissing(field, cd.getFields());
        val missingMethod = findMissing(method, cd.getMethods());
        val missingExtensions = findMissing(extendedClass,
                cd.getExtendedTypes().stream().map(NodeWithSimpleName::getNameAsString).collect(toList()));
        val missingImplementation = findMissing(implementedInterfaces,
                cd.getImplementedTypes().stream().map(NodeWithSimpleName::getNameAsString).collect(toList()));

        return new ViolationCombinationAnd(cd, listOf(
                missingField, missingMethod, missingExtensions, missingImplementation, missingAnnotations
        ));
    }

    private ViolationCombination findMissing(AggregateCondition prop, Collection<?> elements) {
        if (elements.stream().map(prop::getMissing).anyMatch(ViolationCombination::isEmpty)) {
            return ViolationCombination.EMPTY;
        }
        return new ViolationInfo(null, prop.toString());
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
