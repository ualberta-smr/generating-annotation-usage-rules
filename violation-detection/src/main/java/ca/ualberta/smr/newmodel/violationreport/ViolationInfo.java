package ca.ualberta.smr.newmodel.violationreport;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
public class ViolationInfo implements ViolationCombination {

    /**
     * treeElement is the element that the violation is occurring in
     */
    private final Object treeElement;
    /**
     * missingElements are the elements that are missing from the treeElement
     */
    private final String missingElement;

    @Override
    public String describe() {
        return "{" + missingElement + "}";
    }
}

