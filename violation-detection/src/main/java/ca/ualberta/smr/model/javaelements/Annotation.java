package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationInfo;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.expr.AnnotationExpr;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

@Getter
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
@RequiredArgsConstructor
public class Annotation extends ProgramElement {
    private final AggregateCondition type;
    private final AggregateCondition parameters;

    @Override
    @SuppressWarnings("unchecked")
    public boolean matches(Object bd) {
        val annotationExprs = (NodeList<AnnotationExpr>) bd;
        return annotationExprs.stream()
                .filter(e -> type.matches(e.getName().toString()))
                .anyMatch(parameters::matches);
    }

    @Override
    @SuppressWarnings("unchecked")
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        val annotationExprs = (NodeList<AnnotationExpr>) bd;
        for (val expr : annotationExprs) {
            if (type.matches(expr.getName().toString())) {
                if (parameters.matches(expr)) return ViolationCombination.EMPTY;
                return parameters.getMissing(expr, rule);
            }
        }
        // tree element will be null because we do not know
        // which element this annotation should belong to
        return new ViolationInfo(null, this.toString());
    }

    @Override
    public String description() {
        val result = "@"+type.description();
        if (parameters.isEmpty()) return result;
        return result + "(" + parameters + "}";
    }
}