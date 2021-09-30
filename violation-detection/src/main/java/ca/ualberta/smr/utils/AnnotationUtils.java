package ca.ualberta.smr.utils;

import ca.ualberta.smr.model.Annotation;
import ca.ualberta.smr.model.AnnotationParameter;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.nodeTypes.NodeWithAnnotations;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Optional;
import java.util.stream.Collectors;

public class AnnotationUtils {

    public static Collection<Annotation> getMissingAnnotations(NodeWithAnnotations<?> node, Collection<Annotation> annotations) {
        return annotations
                .stream()
                .filter(annotation -> !containsAnnotation(node, annotation))
                .collect(Collectors.toList());
    }


    public static boolean containsAnnotation(NodeWithAnnotations<?> node, Annotation annotation) {
        return node.getAnnotations()
                .stream()
                .map(AnnotationExpr::getName)
                .map(Node::toString)
                .anyMatch(e -> e.equals(annotation.type().name()));
    }

    public static Collection<Pair<AnnotationExpr, Collection<AnnotationParameter>>> getMissingParameters(NodeWithAnnotations<?> node, Collection<Annotation> annotations) {
        return annotations
                .stream()
                .map(annotation -> getMissingParameters(node, annotation))
                .filter(p -> p.hasValue() && !p.value().isEmpty())
                .collect(Collectors.toList());
    }


    public static Pair<AnnotationExpr, Collection<AnnotationParameter>> getMissingParameters(NodeWithAnnotations<?> node, Annotation annotation) {
        final Optional<AnnotationExpr> annotationFound = node.getAnnotations()
                .stream()
                .filter(a -> a.getName().toString().equals(annotation.type().name()))
                .findAny();

        if (annotationFound.isEmpty()) return Pair.empty();

        final var nodeAnnotation = annotationFound.get();

        if (nodeAnnotation instanceof MarkerAnnotationExpr) {
            return new Pair<>(nodeAnnotation, annotation.parameters());
        } else if (nodeAnnotation instanceof SingleMemberAnnotationExpr) {
            return Pair.empty();
        } else if (nodeAnnotation instanceof NormalAnnotationExpr nae) {
            return getMissingParameters(annotation, nae);
        }
        return Pair.empty();
    }

    private static Pair<AnnotationExpr, Collection<AnnotationParameter>> getMissingParameters(Annotation expected, NormalAnnotationExpr actual) {
        Collection<AnnotationParameter> missingParams = new ArrayList<>();
        for (var parameter : expected.parameters()) {
            boolean found = false;
            for (MemberValuePair pair : actual.getPairs()) {
                final String toString = pair.toString();
                if (toString.contains(parameter.name()) || toString.contains(parameter.type().name())) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                missingParams.add(parameter);
            }
        }
        return new Pair<>(actual, missingParams);
    }

}
