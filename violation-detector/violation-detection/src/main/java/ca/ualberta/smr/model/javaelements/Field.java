package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.body.FieldDeclaration;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

import java.util.HashMap;
import java.util.Map;

import static ca.ualberta.smr.model.javaelements.JavaElementUtils.handleViolationCombinationCreation;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.*;

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
                && annotations.matches(fd.getAnnotations())
                && enclosingClassMatches(fd);
    }

    private boolean enclosingClassMatches(FieldDeclaration fd) {
        return fd.getParentNode()
                .map(enclosingClass::matches)// if parent exists, check if it matches with the rule
                .orElseGet(enclosingClass::isEmpty); // if it does not exist, check if the rule is empty
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        val fd = (FieldDeclaration) bd;

        val missingType = type.getMissing(fd.getElementType().asString(), rule);
        val missingAnnotations = annotations.getMissing(fd.getAnnotations(), rule);
        val missingEnclosingClass = getMissingEnclosingClass(fd, rule);

        return handleViolationCombinationCreation(fd, listOf(missingType, missingAnnotations, missingEnclosingClass));
    }

    private ViolationCombination getMissingEnclosingClass(FieldDeclaration fd, StaticAnalysisRule rule) {
        return fd.getParentNode()
                .map(p -> enclosingClass.getMissing(p, rule))
                .orElse(ViolationCombination.EMPTY);
    }

    @Override
    public String description() {
        Map<String, AggregateCondition> keyValues = new HashMap<>();
        keyValues.put("type", type);
        keyValues.put("annotations", annotations);
        return describe("field", keyValues);
    }
}