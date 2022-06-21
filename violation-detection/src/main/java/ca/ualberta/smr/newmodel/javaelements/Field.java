package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombinationAnd;
import com.github.javaparser.ast.body.FieldDeclaration;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

import java.util.HashMap;
import java.util.Map;

import static ca.ualberta.smr.utils.Utils.*;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
public final class Field extends ProgramElement implements AnalysisItem {
    private final AggregateCondition type;
    private final AggregateCondition annotations;

    @Override
    public boolean matches(Object bd) {
        val fd = (FieldDeclaration) bd;
        return type.matches(fd.getElementType().asString())
                && annotations.matches(fd.getAnnotations());
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        val fd = (FieldDeclaration) bd;

        val missingType = type.getMissing(fd.getElementType().asString(), rule);
        val missingAnnotations = annotations.getMissing(fd.getAnnotations(), rule);

        return new ViolationCombinationAnd(fd, listOf(missingType, missingAnnotations));
    }

    @Override
    public String description() {
        Map<String, AggregateCondition> keyValues = new HashMap<>();
        keyValues.put("type", type);
        keyValues.put("annotations", annotations);
        return describe("field", keyValues);
    }
}