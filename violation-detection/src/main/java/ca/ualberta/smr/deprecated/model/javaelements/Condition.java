package ca.ualberta.smr.deprecated.model.javaelements;

import ca.ualberta.smr.deprecated.model.ViolationInfo;
import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.var;

import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static ca.ualberta.smr.deprecated.utils.Utils.concat;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;
import static java.util.Collections.emptyList;

@AllArgsConstructor
@EqualsAndHashCode
@Getter
public final class Condition<T extends ProgramElement> {

    private final Collection<T> elements;
    private ConditionOperation operation;
    private final Class<T> type;

    // TODO: going with mutating value for now, but change later
    public void update(T item, ConditionOperation operation) {
        this.elements.add(item);
        this.operation = operation;
    }

    // TODO: going with mutating value for now, but change later
    public void update(T item) {
        update(item, operation);
    }

    /**
     * Merges the condition with another condition, and sets the operation to a new one
     * @param o other condition
     * @param operation OR/AND/EMPTY operation
     */
    public void update(Condition<T> o, ConditionOperation operation) {
        final Condition<T> plus = this.plus(o, operation);
        this.operation = operation;
        this.elements.clear();
        this.elements.addAll(plus.elements);
    }

    /**
     * Adds 2 conditions and returns a new one without modifying the original ones
     * @param o other condition
     * @param operation OR/AND/EMPTY operation
     * @return a condition that's the combination of 2 conditions
     */
    public Condition<T> plus(Condition<T> o, ConditionOperation operation) {
        final Collection<T> newElements = concat(this.getElements(), o.getElements())
                .collect(Collectors.toList());
        return new Condition<>(newElements, operation, this.getType());
    }

    public boolean test(Predicate<T> condition) {
        switch (operation) {
            case OR:
                return elements.stream().anyMatch(condition);
            case AND:
                return elements.stream().allMatch(condition);
            case EMPTY:
                return true;
        }
        throw new RuntimeException("Illegal ConditionOperation : " + operation);
    }

    public boolean isNotEmpty() {
        return !isEmpty();
    }

    public boolean isEmpty() {
        return operation == ConditionOperation.EMPTY;
    }

    public boolean isSingle() {
        return elements.size() == 1 && operation == ConditionOperation.AND;
    }

    public <R> Collection<R> map(Function<T, R> fieldExtractor) {
        return elements.stream()
                .map(fieldExtractor)
                .collect(Collectors.toList());
    }

    public <R> Collection<R> flatMap(Function<T, ? extends Collection<? extends R>> fieldExtractor) {
        return elements.stream()
                .map(fieldExtractor)
                .flatMap(Collection::stream)
                .collect(Collectors.toList());
    }

    public <R> Collection<R> select(Function<T, Collection<R>> selectionFunction) {
        return elements.stream()
                .map(selectionFunction)
                .reduce((a, b) -> {
                    switch (operation) {
                        case OR:
                            return Stream.concat(a.stream(), b.stream()).distinct().collect(Collectors.toList());
                        case AND:
                            return a.stream().filter(b::contains).collect(Collectors.toList());
                        default:
                            return emptyList();
                    }
                }).orElseGet(Collections::emptyList);
    }

    public Collection<ViolationInfo> evaluate(Function<T, ? extends Collection<ViolationInfo>> fieldExtractor) {
        switch (operation) {
            case OR:
                return handleOr(fieldExtractor);
            case AND:
                return flatMap(fieldExtractor);
            case EMPTY:
                return emptyList();
        }
        throw new RuntimeException("Illegal ConditionOperation : " + operation);
    }

    private Collection<ViolationInfo> handleOr(Function<T, ? extends Collection<ViolationInfo>> fieldExtractor) {
        final Collection<Collection<ViolationInfo>> violations = this.elements
                .stream()
                .map(fieldExtractor)
                .collect(Collectors.toList());

        final boolean atLeastOneConditionSatisfies = violations.stream().anyMatch(Collection::isEmpty);
        final boolean doesMissingElementConditionSatisfy = violations.stream().flatMap(Collection::stream).anyMatch(ViolationInfo::isMissingElement);
        if (atLeastOneConditionSatisfies && !doesMissingElementConditionSatisfy) {
            // No violation is present (one of the conditions hold)
            return emptyList();
        }

        var maybeViolations = violations.stream()
                .filter(vc -> !vc.isEmpty())
                .filter(vc -> vc.stream().noneMatch(ViolationInfo::isMissingElement))
                .findAny();

        return maybeViolations.orElse(emptyList());
    }

    @SuppressWarnings("unchecked")
    public static <T extends ProgramElement> Condition<T> single(T element) {
        return new Condition<>(listOf(element), ConditionOperation.AND, (Class<T>) element.getClass());
    }

    public static <T extends ProgramElement> Condition<T> empty(Class<T> clazz) {
        return new Condition<>(listOf(), ConditionOperation.EMPTY, clazz);
    }

    @SafeVarargs
    @SuppressWarnings("unchecked")
    public static <T extends ProgramElement> Condition<T> any(T element, T... elements) {
        final ArrayList<T> nodes = new ArrayList<>();
        nodes.add(element);
        nodes.addAll(listOf(elements));

        return new Condition<>(nodes, ConditionOperation.OR, (Class<T>) element.getClass());
    }

    public static <T extends ProgramElement> Condition<T> any(Class<T> type) {
        return new Condition<>(new ArrayList<>(), ConditionOperation.OR, type);
    }

    @SafeVarargs
    @SuppressWarnings("unchecked")
    public static <T extends ProgramElement> Condition<T> all(T element, T... elements) {
        final ArrayList<T> nodes = new ArrayList<>();
        nodes.add(element);
        nodes.addAll(listOf(elements));

        return new Condition<>(nodes, ConditionOperation.AND, (Class<T>) element.getClass());
    }

    public static <T extends ProgramElement> Condition<T> all(Class<T> type) {
        return new Condition<>(new ArrayList<>(), ConditionOperation.AND, type);
    }

    @Override
    public String toString() {
        if (elements.size() == 1) {
            return elements.stream().findFirst().get().toString();
        } else {
            return elements
                    .stream()
                    .map(Objects::toString)
                    .collect(Collectors.joining(String.format(" %s ", operation.name())));
        }
    }

    @Deprecated
    public T getFirst() {
        return elements.stream().findFirst().get();
    }

    public enum ConditionOperation {
        OR, AND, EMPTY
    }

}
