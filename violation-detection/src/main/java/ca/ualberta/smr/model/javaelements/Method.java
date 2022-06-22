package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.detection.method.MethodAntecedentScanner;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationCombinationAnd;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

import java.util.HashMap;
import java.util.Map;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.describe;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
public final class Method extends ProgramElement implements AnalysisItem {
    private final AggregateCondition returnType;
    private final AggregateCondition annotations;
    private final AggregateCondition parameters;

    @Override
    public boolean matches(Object bd) {
        if (bd instanceof MethodDeclaration) {
            val md = (MethodDeclaration) bd;
            return returnType.matches(md.getTypeAsString())
                    && annotations.matches(md.getAnnotations())
                    && parameters.matches(md.findAll(Parameter.class));
        } else if (bd instanceof Parameter) {
            return parameters.matches(listOf(((Parameter) bd)));
        }
        return false;
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        val md = (MethodDeclaration) bd;

        val missingReturnType = returnType.getMissing(md.getTypeAsString(), rule);
        val missingAnnotations = annotations.getMissing(md.getAnnotations(), rule);
        // TODO: make sure the params are the same
        val missingParameters = parameters.getMissing(MethodAntecedentScanner.findMethodParametersFromMethodDeclaration(md, rule.antecedent()), rule);

        return new ViolationCombinationAnd(md, listOf(missingReturnType, missingAnnotations, missingParameters));
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