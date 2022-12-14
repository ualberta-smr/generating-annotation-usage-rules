package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationInfo;
import com.github.javaparser.ast.body.Parameter;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.describe;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
public class MethodParameter extends ProgramElement {
    private final AggregateCondition type;
    private final AggregateCondition annotations;

    @Override
    @SuppressWarnings("unchecked")
    public boolean matches(Object bd) {
        List<Parameter> params = (List<Parameter>) bd;
        return params.stream()
                .anyMatch(this::matchMethodParameter);
    }

    private boolean matchMethodParameter(Parameter parameter) {
        return annotations.matches(parameter.getAnnotations())
                && type.matches(parameter.getType().toString());
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        if (this.matches(bd)) return ViolationCombination.EMPTY;
        // TODO: maybe position here can be interesting
        return new ViolationInfo(null, this.toString());
    }

    @Override
    public String description() {
        Map<String, AggregateCondition> keyValues = new HashMap<>();
        keyValues.put("type", type);
        keyValues.put("annotations", annotations);
        return describe("param", keyValues);
    }
}