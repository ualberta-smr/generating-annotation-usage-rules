package miner.config;

import java.util.Collection;
import java.util.Optional;
import java.util.regex.Pattern;

public class SubApiConfiguration {
    private Collection<String> prefixes;

    public Collection<String> prefixes() {
        return prefixes;
    }

    /**
     * @param relationshipExpression example: "Class --(annotatedWith)--> Annotation_org.eclipse.microprofile.problemdetails.Title" or <br/>
     *                               Annotation_org.eclipse.microprofile.faulttolerance.CircuitBreaker --(hasParam)--> Param_failureRatio:double
     * @return optional of the annotation: e.g., Annotation_org.eclipse.microprofile.problemdetails.Title
     */
    public Optional<String> extractMatchingAnnotation(String relationshipExpression) {
        String[] pieces = exprSplitter.split(relationshipExpression);
        if (pieces.length != 2) return Optional.empty();

        String first = pieces[0].trim();
        String second = pieces[1].trim();

        final String annotation;

        if (first.isEmpty()) {
            annotation = second.substring(0, second.indexOf("--")).trim();
        } else {
            annotation = second.trim();
        }

        if (prefixes.stream().anyMatch(annotation::startsWith)) {
            return Optional.of("Annotation_" + annotation);
        }
        return Optional.empty();
    }

    private static final Pattern exprSplitter = Pattern.compile("Annotation_");
}
