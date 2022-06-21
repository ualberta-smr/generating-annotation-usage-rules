package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.ViolationCombination;
import ca.ualberta.smr.newmodel.ViolationCombinationAnd;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.val;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

import static ca.ualberta.smr.utils.Utils.describe;
import static ca.ualberta.smr.utils.Utils.listOf;

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
        val md = (MethodDeclaration) bd;
        return returnType.matches(md.getTypeAsString())
                && annotations.matches(md.getAnnotations())
                && parameters.matches(md.findAll(Parameter.class));
    }

    @Override
    public ViolationCombination getMissing(Object bd) {
        val md = (MethodDeclaration) bd;

        val missingReturnType = returnType.getMissing(md.getTypeAsString());
        val missingAnnotations = annotations.getMissing(md.getAnnotations());
        val missingParameters = parameters.getMissing(md.findAll(Parameter.class));

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