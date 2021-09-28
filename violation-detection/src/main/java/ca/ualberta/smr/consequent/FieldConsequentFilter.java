package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.Annotation;
import ca.ualberta.smr.model.Field;
import ca.ualberta.smr.model.Type;
import ca.ualberta.smr.model.ViolationInfo;
import com.github.javaparser.ast.body.BodyDeclaration;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;

import java.util.*;
import java.util.stream.Stream;

import static ca.ualberta.smr.utils.Utils.containsAnnotation;
import static java.util.Collections.*;
import static java.util.stream.Collectors.toList;

public class FieldConsequentFilter {

    @SuppressWarnings("unchecked")
    public static <T extends BodyDeclaration<T>> Map<FieldDeclaration, Collection<ViolationInfo>> doFilter(Collection<T> declarations, Field field) {
        if (declarations.isEmpty()) return emptyMap();

        var sampleItem = declarations.stream().findAny().get();
        if (sampleItem instanceof ClassOrInterfaceDeclaration) {
            return doFilterFromClassDeclarations((Collection<ClassOrInterfaceDeclaration>) declarations, field);
        } else if (sampleItem instanceof FieldDeclaration) {
            return doFilterFromFieldDeclarations((Collection<FieldDeclaration>) declarations, field);
        }
        throw new IllegalArgumentException("Required a collection of one of the following types (ClassOrInterfaceDeclaration, FieldDeclaration) got %s instead".formatted(sampleItem.getClass()));
    }

    private static Map<FieldDeclaration, Collection<ViolationInfo>> doFilterFromClassDeclarations(Collection<ClassOrInterfaceDeclaration> declarations, Field field) {
        var fieldDeclarations = declarations.stream()
                .flatMap(cd -> cd.findAll(FieldDeclaration.class).stream())
                .collect(toList());
        return doFilterFromFieldDeclarations(fieldDeclarations, field);
    }

    private static <T extends BodyDeclaration<T>> Map<FieldDeclaration, Collection<ViolationInfo>> doFilterFromFieldDeclarations(Collection<FieldDeclaration> fieldDeclarations, Field field) {
        Map<FieldDeclaration, Collection<ViolationInfo>> res = new HashMap<>();
        for (FieldDeclaration fieldDeclaration : fieldDeclarations) {
            final Collection<ViolationInfo> violations = doFilter(fieldDeclaration, field);
            res.put(fieldDeclaration, violations);
        }
        return res;
    }

    private static Collection<ViolationInfo> doFilter(FieldDeclaration fieldDeclaration, Field expected) {
        // TODO: annotations
        List<Annotation> requiredAnnotations = new ArrayList<>();
        for (var annotation : expected.annotations()) {
            if (!containsAnnotation(fieldDeclaration, annotation)) {
                requiredAnnotations.add(annotation);
            }
        }
        // TODO: type
        Type requiredType = null;
        final boolean hasType = fieldDeclaration.getElementType().asString().equals(expected.type().name());
        if (!hasType) {
            requiredType = expected.type();
        }

        if (requiredAnnotations.isEmpty() && requiredType == null) {
            // when this is the exact method, nothing is missing, no violation
            return emptyList();
        } else {
            var missingAnnotations = new ViolationInfo(fieldDeclaration, requiredAnnotations.stream().map(Annotation::toString).collect(toList()));
            var missingType = new ViolationInfo(fieldDeclaration, requiredType == null ? emptyList() : singleton(requiredType.name()));

            return Stream.of(missingType, missingAnnotations)
                    .filter(v -> !v.missingElements().isEmpty())
                    .collect(toList());
        }
    }

}
