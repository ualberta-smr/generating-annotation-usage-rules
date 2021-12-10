package ca.ualberta.smr.model;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;
import lombok.var;

import java.util.Collection;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
public class ViolationInfo {

    /**
     * treeElement is the element that the violation is occurring in
     */
    private final Object treeElement;
    /**
     * missingElements are the elements that are missing from the treeElement
     */
    private final Collection<String> missingElements;
    /**
     * isMissingElement specifies that the element is missing altogether
     */
    private final boolean isMissingElement;

    /**
     * @param treeElement is the element that the violation is occurring in
     * @param missingElements are the elements that are missing from the treeElement
     * @apiNote isMissingElement is set to false by default in this constructor
     */
    public ViolationInfo(Object treeElement, Collection<String> missingElements) {
        this(treeElement, missingElements, false);
    }

    /**
     * Merges to 2 violations and produces a new one. It concatenates their missing elements, keeps the tree element the same, and performs OR on isMissingElement
     *
     * @param other the ViolationInfo object to add to the current one
     * @return a new instance of ViolationInfo that contains the merged information about both objects
     */
    public ViolationInfo merge(ViolationInfo other) {
        var missingElements = Stream.concat(
                        this.missingElements().stream(), other.missingElements().stream())
                .collect(toList());
        var isMissingElementValue = isMissingElement || other.isMissingElement;
        return new ViolationInfo(treeElement(), missingElements, isMissingElementValue);
    }

    public boolean isNotEmpty() {
        return !missingElements.isEmpty();
    }

    @Override
    public String toString() {
        return "ViolationInfo{" +
                "missingElements=" + missingElements +
                '}';
    }
}