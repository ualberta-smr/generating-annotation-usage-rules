package ca.ualberta.smr.model.violationreport;

import com.github.javaparser.Range;
import com.github.javaparser.ast.Node;
import lombok.val;

import java.util.Optional;

import static java.util.Optional.empty;

public interface ViolationCombination {
    Object treeElement();
    String describe();

    ViolationCombination EMPTY = new ViolationCombination() {
        @Override
        public Object treeElement() {
            return null;
        }

        @Override
        public String describe() {
            return null;
        }
    };
    default boolean isEmpty() {
        return this == EMPTY;
    }

    default Optional<ViolationRange> getLocation() {
        val treeElement = this.treeElement();
        if (treeElement instanceof Node) {
            Optional<Range> range = ((Node) treeElement).getRange();
            return range.map(ViolationRange::new);
        }
        return empty();
    }
}
