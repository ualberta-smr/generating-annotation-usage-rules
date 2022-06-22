package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.parsing.utils.GeneralUtility;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationCombinationAnd;
import com.github.javaparser.ast.body.FieldDeclaration;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

import java.util.HashMap;
import java.util.Map;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
public final class Field extends ProgramElement implements AnalysisItem {
    private final AggregateCondition type;
    private final AggregateCondition annotations;
    private final AggregateCondition enclosingClass;

    // TODO: should be deleted
    public Field(AggregateCondition type, AggregateCondition annotations) {
        this.type = type;
        this.annotations = annotations;
        this.enclosingClass = AggregateCondition.empty();
    }

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

        return new ViolationCombinationAnd(fd, GeneralUtility.listOf(missingType, missingAnnotations));
    }

    @Override
    public String description() {
        Map<String, AggregateCondition> keyValues = new HashMap<>();
        keyValues.put("type", type);
        keyValues.put("annotations", annotations);
        return GeneralUtility.describe("field", keyValues);
    }
}