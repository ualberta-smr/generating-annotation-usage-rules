package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.detection.method.MethodAntecedentScanner;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
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
public final class Method extends ProgramElement implements AnalysisItem {
    private final AggregateCondition returnType;
    private final AggregateCondition annotations;
    private final AggregateCondition parameters;
    private final AggregateCondition enclosingClass;

    // TODO: should be deleted
    public Method(AggregateCondition returnType, AggregateCondition annotations, AggregateCondition parameters) {
        this.returnType = returnType;
        this.annotations = annotations;
        this.parameters = parameters;
        this.enclosingClass = AggregateCondition.empty();
    }

    @Override
    public boolean matches(Object bd) {
        if (bd instanceof MethodDeclaration) {
            val md = (MethodDeclaration) bd;
            return returnType.matches(md.getTypeAsString())
                    && annotations.matches(md.getAnnotations())
                    && parameters.matches(md.getParameters())
                    && enclosingClassMatches(md);
        } else if (bd instanceof Parameter) {
            return parameters.matches(listOf(((Parameter) bd)));
        }
        return false;
    }

    private boolean enclosingClassMatches(MethodDeclaration md) {
        return md.getParentNode()
                .map(enclosingClass::matches)// if parent exists, check if it matches with the rule
                .orElseGet(enclosingClass::isEmpty); // if it does not exist, check if the rule is empty
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        val md = (MethodDeclaration) bd;

        val missingReturnType = returnType.getMissing(md.getTypeAsString(), rule);
        val missingAnnotations = annotations.getMissing(md.getAnnotations(), rule);
        val missingParameters = parameters.getMissing(MethodAntecedentScanner.findMethodParametersFromMethodDeclaration(md, rule.antecedent()), rule);
        val missingEnclosingClass = getMissingEnclosingClass(md, rule);

        val violations = listOf(missingReturnType, missingAnnotations, missingParameters, missingEnclosingClass);

        return handleViolationCombinationCreation(md, violations);
    }

    private ViolationCombination getMissingEnclosingClass(MethodDeclaration md, StaticAnalysisRule rule) {
        return md.getParentNode()
                .map(p -> enclosingClass.getMissing(p, rule))
                .orElse(ViolationCombination.EMPTY);
    }

    @Override
    public String description() {
        Map<String, AggregateCondition> keyValues = new HashMap<>();
        keyValues.put("annotations", annotations);
        keyValues.put("params", parameters);
        keyValues.put("returnType", returnType);
        return describe("method", keyValues);
    }
}