package ca.ualberta.smr.utils;

import ca.ualberta.smr.model.Annotation;
import ca.ualberta.smr.model.AnnotationParameter;
import ca.ualberta.smr.model.Parameter;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.nodeTypes.NodeWithAnnotations;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Optional;
import java.util.stream.Collectors;

public class Utils {

    public static boolean containsAnnotation(NodeWithAnnotations<?> node, Annotation annotation) {
        return node.getAnnotations()
                .stream()
                .map(AnnotationExpr::getName)
                .map(Node::toString)
                .anyMatch(e -> e.equals(annotation.type().name()));
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
