package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.violationreport.ViolationInfo;
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

import static ca.ualberta.smr.utils.Utils.describe;

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
        // TODO: handle type situation
        val identifier = p.getName().getIdentifier();
        val valueExpr = p.getValue().toString();

        return type.matches(identifier) && name.matches(valueExpr);
    }

    @Override
    public ViolationCombination getMissing(Object bd) {
        val expr = (AnnotationExpr) bd;

        if (expr instanceof NormalAnnotationExpr) {
            val normal = (NormalAnnotationExpr) expr;
            for (val pair : normal.getPairs()) {
                if (parameterMatches(pair)) {
                    return ViolationCombination.EMPTY;
                }
            }
        }
        return new ViolationInfo(bd, this.toString());
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
