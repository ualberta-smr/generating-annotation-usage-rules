package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.*;
import ca.ualberta.smr.utils.Utils;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.val;

import java.util.Collection;

import static ca.ualberta.smr.utils.Utils.listOf;
import static java.util.Collections.*;

@RequiredArgsConstructor
@EqualsAndHashCode(callSuper = false)
@Getter
public final class AggregateCondition extends ProgramElement {

    private final ProgramElement left;
    private final ProgramElement right;
    private final AggregateConditionOperation operation;

    @Override
    public ViolationCombination getMissing(Object bd) {
        val missingLeft = left.getMissing(bd);
        val missingRight = right.getMissing(bd);
        switch (operation) {
            case AND:
                return and(missingLeft, missingRight, bd);
            case OR:
                return or(missingLeft, missingRight, bd);
            case XOR:
                return xor(missingLeft, missingRight, bd);
            case EMPTY:
                return ViolationCombination.EMPTY;
            case NOT:
                return mergeNot(missingLeft, bd);
        }
        throw new RuntimeException("Illegal state " + operation);
    }

    @Override
    public String description() {
        if (!(left instanceof AggregateCondition && right instanceof AggregateCondition)) {
            if (left == right) {
                if (left == NoOp.INSTANCE) return "";
                if (operation == AggregateConditionOperation.NOT) {
                    return String.format("(not %s)", left.toString());
                }
                return String.format("%s", left.toString());
            }
        }
        return String.format("(%s %s %s)", left.toString(), operation, right.toString());
    }

    private ViolationCombination mergeNot(ViolationCombination a, Object bd) {
        if (a.isEmpty()) return new ViolationInfo(bd, left.toString());
        return ViolationCombination.EMPTY;
    }

    public ViolationCombination and(ViolationCombination a, ViolationCombination b, Object treeElement) {
        if (left == right) return a;
        return new ViolationCombinationAnd(treeElement, listOf(a, b));
    }

    public ViolationCombination or(ViolationCombination a, ViolationCombination b, Object treeElement) {
        if (!a.isEmpty() && !b.isEmpty()) return new ViolationCombinationOr(treeElement, listOf(a, b));
        return ViolationCombination.EMPTY;
    }

    // TODO: needs optimization
    public ViolationCombination xor(ViolationCombination a, ViolationCombination b, Object treeElement) {
        if (a.isEmpty() ^ b.isEmpty()) return ViolationCombination.EMPTY;
        if (!a.isEmpty() && !b.isEmpty()) {
            return new ViolationCombinationXor(treeElement, listOf(a, b));
        }
        return new ViolationCombinationXor(treeElement, listOf(
                new ViolationInfo(treeElement, left.toString()),
                new ViolationInfo(treeElement, right.toString())
        ));
    }

    @Override
    public boolean matches(Object bd) {
        switch (operation) {
            case AND:
                if (left == right) return left.matches(bd);
                return left.matches(bd) && right.matches(bd);
            case OR:
                return left.matches(bd) || right.matches(bd);
            case EMPTY:
                return true;
            case NOT:
                return !left.matches(bd);
            case XOR:
                return left.matches(bd) ^ right.matches(bd);
            default:
                throw new IllegalStateException("Illegal operation - " + operation);
        }
    }

    public static AggregateCondition not(ProgramElement pe) {
        return new AggregateCondition(
                pe, NoOp.INSTANCE, AggregateConditionOperation.NOT
        );
    }

    public boolean isSingle() {
        return this.left == this.right && operation == AggregateConditionOperation.AND;
    }

    @SuppressWarnings("unchecked")
    public static <T extends ProgramElement> AggregateCondition single(T element) {
        return new AggregateCondition(element, element, AggregateConditionOperation.AND);
    }

    public static AggregateCondition empty() {
        return new AggregateCondition(NoOp.INSTANCE, NoOp.INSTANCE, AggregateConditionOperation.EMPTY);
    }

    public boolean isEmpty() {
        return this.operation == AggregateConditionOperation.EMPTY;
    }

    private static class NoOp extends ProgramElement {
        public static final NoOp INSTANCE = new NoOp();

        @Override
        public boolean matches(Object bd) {
            return true;
        }

        @Override
        public ViolationCombination getMissing(Object bd) {
            return ViolationCombination.EMPTY;
        }

        @Override
        String description() {
            return null;
        }
    }
}
