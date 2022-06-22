package ca.ualberta.smr.model.violationreport;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

import java.util.Collection;
import java.util.Objects;
import java.util.stream.Collectors;

@RequiredArgsConstructor
@Getter
@Accessors(fluent = true)
public class ViolationCombinationOr implements ViolationCombination {
    private final Object treeElement;
    private final Collection<ViolationCombination> violations;

    @Override
    public String describe() {
        if (!this.isEmpty()) {
            return violations.stream()
                    .map(ViolationCombination::describe)
                    .filter(Objects::nonNull)
                    .collect(Collectors.joining(" OR ", "Missing elements: [", "]"));
        }
        return "";
    }

    @Override
    public boolean isEmpty() {
        return violations.isEmpty() || violations.stream().allMatch(ViolationCombination::isEmpty);
    }
}
