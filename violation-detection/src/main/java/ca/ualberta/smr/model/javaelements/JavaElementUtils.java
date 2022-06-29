package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationCombinationAnd;
import ca.ualberta.smr.model.violationreport.ViolationInfo;
import lombok.val;

import java.util.Collection;

import static java.util.stream.Collectors.toList;

public class JavaElementUtils {

    public static ViolationCombination handleViolationCombinationCreation(Object treeElement, Collection<ViolationCombination> violations) {
        val onlyNonEmptyViolations = violations.stream().filter(e -> !e.isEmpty()).collect(toList());
        if (onlyNonEmptyViolations.size() == 1) {
            val v = onlyNonEmptyViolations.get(0);
            if (v.treeElement() != null) return v;
            return new ViolationInfo(treeElement, v.describe());
        }
        return new ViolationCombinationAnd(treeElement, violations);
    }

}
