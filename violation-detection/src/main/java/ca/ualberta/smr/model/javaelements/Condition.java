package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.model.ViolationInfo;
import lombok.RequiredArgsConstructor;
import lombok.var;

import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

import static ca.ualberta.smr.utils.Utils.listOf;
import static java.util.Collections.emptyList;
import static java.util.Collections.list;

@RequiredArgsConstructor
public final class Condition<T extends ProgramElement> {

    private final Collection<T> elements;
    private final ConditionOperation operation;
    private final Class<T> type;

    public Class<T> getType() {
        return this.type;
    }

    // TODO: going with mutating value for now, but change later
    public void merge(T item) {
        this.elements.add(item);
    }

    public void merge(String operation) {

    }

    public boolean test(Predicate<T> condition) {
        switch (operation) {
            case OR:
                return elements.stream().anyMatch(condition);
            case AND:
                return elements.stream().allMatch(condition);
            case EMPTY:
                return true;
        };
        throw new RuntimeException("Illegal ConditionOperation : " + operation);
    }

    public boolean isNotEmpty() {
        return operation != ConditionOperation.EMPTY;
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

    public Collection<ViolationInfo> evaluate(Function<T, ? extends Collection<ViolationInfo>> fieldExtractor) {
        switch (operation) {
            case OR:
                return handleOr(fieldExtractor);
            case AND:
                return flatMap(fieldExtractor);
            case EMPTY:
                return emptyList();
        };
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
        return new Condition<T>(Collections.singletonList(element), ConditionOperation.AND, (Class<T>) element.getClass());
    }

    public static <T extends ProgramElement> Condition<T> empty(Class<T> clazz) {
        return new Condition<T>(emptyList(), ConditionOperation.EMPTY, clazz);
    }

    @SafeVarargs
    @SuppressWarnings("unchecked")
    public static <T extends ProgramElement> Condition<T> any(T element, T... elements) {
        final ArrayList<T> nodes = new ArrayList<>();
        nodes.add(element);
        nodes.addAll(listOf(elements));

        return new Condition<T>(nodes, ConditionOperation.OR, (Class<T>) element.getClass());
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

    enum ConditionOperation {
        OR, AND, EMPTY
    }

}
