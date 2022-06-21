package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.violationreport.ViolationInfo;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.expr.AnnotationExpr;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

import java.util.HashMap;
import java.util.Map;

import static ca.ualberta.smr.utils.Utils.describe;

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
    public ViolationCombination getMissing(Object bd) {
        val annotationExprs = (NodeList<AnnotationExpr>) bd;
        for (val expr : annotationExprs) {
            if (type.matches(expr.getName().toString())) {
                if (parameters.matches(expr)) return ViolationCombination.EMPTY;
                return new ViolationInfo(expr, parameters.toString());
            }
        }
        // tree element will be null because we do not know
        // which element this annotation should belong to
        return new ViolationInfo(null, this.toString());
    }

    @Override
    public String description() {
        Map<String, AggregateCondition> keyValues = new HashMap<>();
        keyValues.put("type", type);
        keyValues.put("params", parameters);
        return describe("annotation", keyValues);
    }
}