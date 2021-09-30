package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.javaelements.*;
import com.github.javaparser.ast.body.*;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.Utils.*;
import static java.util.Collections.*;
import static java.util.stream.Collectors.toList;
import static ca.ualberta.smr.utils.AnnotationUtils.*;

public class FieldConsequentFilter {

    @SuppressWarnings("unchecked")
    public static <T extends BodyDeclaration<T>> Collection<ViolationInfo> doFilter(Collection<T> declarations, Condition<Field> fieldCondition) {
        if (declarations.isEmpty()) return emptyList();

        var sampleItem = declarations.stream().findAny().get();
        if (sampleItem instanceof ClassOrInterfaceDeclaration) {
            return doFilterFromClassDeclarations((Collection<ClassOrInterfaceDeclaration>) declarations, fieldCondition);
        } else if (sampleItem instanceof FieldDeclaration) {
            return doFilterFromFieldDeclarations((Collection<FieldDeclaration>) declarations, fieldCondition);
        }
        throw new IllegalArgumentException("Required a collection of one of the following types (ClassOrInterfaceDeclaration, FieldDeclaration) got %s instead".formatted(sampleItem.getClass()));
    }

    private static Collection<ViolationInfo> doFilterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Condition<Field> fieldCondition) {
        var fieldDeclarations = declarations.stream()
                .flatMap(cd -> cd.findAll(FieldDeclaration.class).stream())
                .collect(toList());
        return doFilterFromFieldDeclarations(fieldDeclarations, fieldCondition);
    }

    private static <T extends BodyDeclaration<T>> Collection<ViolationInfo> doFilterFromFieldDeclarations(Collection<FieldDeclaration> fieldDeclarations, Condition<Field> field) {
        return fieldDeclarations.stream()
                .map(fd -> doFilter(fd, field))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    private static Collection<ViolationInfo> doFilter(FieldDeclaration fieldDeclaration, Condition<Field> expected) {
        // TODO: annotations
        var requiredAnnotations = getMissingAnnotations(fieldDeclaration, expected.flatMap(Field::annotations));
        var requiredAnnotationParameters = getMissingParameters(fieldDeclaration, expected.flatMap(Field::annotations));
        // TODO: type
        Collection<Condition<Type>> requiredType = List.of();
        var hasType = expected.test(f -> f.type().test(t -> t.equalsTypeString(fieldDeclaration.getElementType().asString())));
        if (!hasType) {
            requiredType = expected.map(Field::type);
        }

        var missingAnnotations = new ViolationInfo(fieldDeclaration, requiredAnnotations.stream().map(Condition::toString).collect(toList()));
        var missingType = new ViolationInfo(fieldDeclaration, requiredType.stream().map(Condition::toString).collect(toList()));

        var missingAnnotationParameters = requiredAnnotationParameters
                .stream()
                .map(p -> new ViolationInfo(p.key(), p.value().stream().map(Condition::toString).collect(toList())));


        return concat(Stream.of(missingType, missingAnnotations), missingAnnotationParameters)
                .filter(ViolationInfo::isNotEmpty)
                .collect(toList());
    }

}
