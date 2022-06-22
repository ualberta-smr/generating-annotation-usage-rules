package ca.ualberta.smr.model.violationreport;

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
}
