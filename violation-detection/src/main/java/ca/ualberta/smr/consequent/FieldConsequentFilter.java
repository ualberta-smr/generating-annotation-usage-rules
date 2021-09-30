package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.*;
import com.github.javaparser.ast.body.*;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.Utils.*;
import static java.util.Collections.*;
import static java.util.stream.Collectors.toList;
import static ca.ualberta.smr.utils.AnnotationUtils.*;

public class FieldConsequentFilter {

    @SuppressWarnings("unchecked")
    public static <T extends BodyDeclaration<T>> Collection<ViolationInfo> doFilter(Collection<T> declarations, Field field) {
        if (declarations.isEmpty()) return emptyList();

        var sampleItem = declarations.stream().findAny().get();
        if (sampleItem instanceof ClassOrInterfaceDeclaration) {
            return doFilterFromClassDeclarations((Collection<ClassOrInterfaceDeclaration>) declarations, field);
        } else if (sampleItem instanceof FieldDeclaration) {
            return doFilterFromFieldDeclarations((Collection<FieldDeclaration>) declarations, field);
        }
        throw new IllegalArgumentException("Required a collection of one of the following types (ClassOrInterfaceDeclaration, FieldDeclaration) got %s instead".formatted(sampleItem.getClass()));
    }

    private static Collection<ViolationInfo> doFilterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Field field) {
        var fieldDeclarations = declarations.stream()
                .flatMap(cd -> cd.findAll(FieldDeclaration.class).stream())
                .collect(toList());
        return doFilterFromFieldDeclarations(fieldDeclarations, field);
    }

    private static <T extends BodyDeclaration<T>> Collection<ViolationInfo> doFilterFromFieldDeclarations(Collection<FieldDeclaration> fieldDeclarations, Field field) {
        return fieldDeclarations.stream()
                .map(fd -> doFilter(fd, field))
                .flatMap(Collection::stream)
                .collect(toList());
    }

    private static Collection<ViolationInfo> doFilter(FieldDeclaration fieldDeclaration, Field expected) {
        // TODO: annotations
        var requiredAnnotations = getMissingAnnotations(fieldDeclaration, expected.annotations());
        var requiredAnnotationParameters = getMissingParameters(fieldDeclaration, expected.annotations());
        // TODO: type
        Type requiredType = null;
        final boolean hasType = expected.type() == null || fieldDeclaration.getElementType().asString().equals(expected.type().name());
        if (!hasType) {
            requiredType = expected.type();
        }

        var missingAnnotations = new ViolationInfo(fieldDeclaration, requiredAnnotations.stream().map(Annotation::toString).collect(toList()));
        var missingType = new ViolationInfo(fieldDeclaration, requiredType == null ? emptyList() : singleton(requiredType.name()));

        var missingAnnotationParameters = requiredAnnotationParameters
                .stream()
                .map(p -> new ViolationInfo(p.key(), p.value().stream().map(AnnotationParameter::toString).collect(toList())));


        return concat(Stream.of(missingType, missingAnnotations), missingAnnotationParameters)
                .filter(ViolationInfo::isNotEmpty)
                .collect(toList());
    }

}
