package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationInfo;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.expr.MemberValuePair;
import com.github.javaparser.ast.expr.NormalAnnotationExpr;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

import java.util.HashMap;
import java.util.Map;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.describe;

@Getter
@Accessors(fluent = true)
@RequiredArgsConstructor
@EqualsAndHashCode(callSuper = false)
public class AnnotationParameter extends ProgramElement {

    private final AggregateCondition type;
    private final AggregateCondition name;
    private final AggregateCondition value;

    @Override
    public boolean matches(Object bd) {
        val expr = (AnnotationExpr) bd;

        if (expr instanceof NormalAnnotationExpr) {
            val normal = (NormalAnnotationExpr) expr;
            return normal.getPairs().stream()
                    .anyMatch(this::parameterMatches);
        }

        return false;
    }

    private boolean parameterMatches(MemberValuePair p) {
        // TODO: handle type situation:type.matches(...)
        val identifier = p.getName().getIdentifier();
        val valueExpr = p.getValue().toString();

        return name.matches(identifier) && value.matches(valueExpr);
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        val expr = (AnnotationExpr) bd;

        if (expr instanceof NormalAnnotationExpr) {
            val normal = (NormalAnnotationExpr) expr;
            for (val pair : normal.getPairs()) {
                val identifier = pair.getName().getIdentifier();
                val valueExpr = pair.getValue().toString();
                if (name.matches(identifier)) {
                    if (value.matches(valueExpr)) return ViolationCombination.EMPTY;
                    return new ViolationInfo(
                            expr, String.format("Annotation %s should have the value: %s, but has %s", expr.getNameAsString(), value, valueExpr), true
                    );
                }
            }
        }
        return new ViolationInfo(bd, String.format("Annotation %s must have the parameter '%s' with value '%s'", expr.getNameAsString(), name, value));
    }

    @Override
    public String description() {
        Map<String, AggregateCondition> keyValues = new HashMap<>();
        keyValues.put("type", type);
        keyValues.put("name", name);
        keyValues.put("value", value);
        return describe("param", keyValues);
    }

}
