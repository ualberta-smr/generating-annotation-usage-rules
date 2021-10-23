package ca.ualberta.smr.utils;

import ca.ualberta.smr.model.javaelements.Annotation;
import ca.ualberta.smr.model.javaelements.AnnotationParameter;
import ca.ualberta.smr.model.javaelements.Condition;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.expr.*;
import com.github.javaparser.ast.nodeTypes.NodeWithAnnotations;
import lombok.var;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Optional;
import java.util.stream.Collectors;

public class AnnotationUtils {

    public static Collection<Condition<Annotation>> getMissingAnnotations(NodeWithAnnotations<?> node, Collection<Condition<Annotation>> annotations) {
        return annotations
                .stream()
                .filter(annotation -> !containsAnnotation(node, annotation))
                .collect(Collectors.toList());
    }


    public static boolean containsAnnotation(NodeWithAnnotations<?> node, Condition<Annotation> annotationCondition) {
        return node.getAnnotations()
                .stream()
                .map(AnnotationExpr::getName)
                .map(Node::toString)
                .anyMatch(e ->
                        annotationCondition.test(annotation ->
                                annotation.type().test(type -> type.equalsTypeString(e))));
    }

    public static Collection<Pair<AnnotationExpr, Collection<Condition<AnnotationParameter>>>> getMissingParameters(NodeWithAnnotations<?> node,
                                                                                                                    Collection<Condition<Annotation>> annotationConditions) {
        return annotationConditions
                .stream()
                .map(annotation -> getMissingParameters(node, annotation))
                .filter(p -> p.hasValue() && !p.value().isEmpty())
                .collect(Collectors.toList());
    }


    public static Pair<AnnotationExpr, Collection<Condition<AnnotationParameter>>> getMissingParameters(NodeWithAnnotations<?> node, Condition<Annotation> annotationCondition) {
        final Optional<AnnotationExpr> annotationFound = node.getAnnotations()
                .stream()
                .filter(a -> annotationCondition.test(annotation -> annotation.type().test(type -> type.equalsTypeString(a.getName().toString()))))
                .findAny();

        if (!annotationFound.isPresent()) return Pair.empty();

        final var nodeAnnotation = annotationFound.get();

        if (nodeAnnotation instanceof MarkerAnnotationExpr) {
            return new Pair<>(nodeAnnotation, annotationCondition.flatMap(Annotation::parameters));
        } else if (nodeAnnotation instanceof SingleMemberAnnotationExpr) {
            return Pair.empty();
        } else if (nodeAnnotation instanceof NormalAnnotationExpr) {
            return getMissingParameters(annotationCondition, (NormalAnnotationExpr) nodeAnnotation);
        }
        return Pair.empty();
    }

    private static Pair<AnnotationExpr, Collection<Condition<AnnotationParameter>>> getMissingParameters(Condition<Annotation> expected, NormalAnnotationExpr actual) {
        Collection<Condition<AnnotationParameter>> missingParams = new ArrayList<>();
        for (var parameter : expected.flatMap(Annotation::parameters)) {
            boolean found = false;
            for (MemberValuePair pair : actual.getPairs()) {
                var toString = pair.toString();
                var annotationMatches = parameter.test(p -> toString.contains(p.name()) || toString.contains(p.type().name()));
                if (annotationMatches) {
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
