package ca.ualberta.smr.model.violationreport;

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

    /**
     * isCompleteError is set to true whenever the complete error message is already provided in missingElement
     * therefore no need for another generated error message
     */
    private final boolean isCompleteError;

    public ViolationInfo(Object treeElement, String missingElement) {
        this.treeElement = treeElement;
        this.missingElement = missingElement;
        this.isCompleteError = false;
    }

    @Override
    public String describe() {
        return missingElement;
    }

    @Override
    public ViolationCombination shallowCopy(Object treeElement) {
        return new ViolationInfo(treeElement, missingElement);
    }
}

