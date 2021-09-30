package ca.ualberta.smr.model.javaelements;

import lombok.RequiredArgsConstructor;

import java.util.*;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;

@RequiredArgsConstructor
public class Condition<T> {

    private final Collection<T> elements;
    private final ConditionOperation operation;

    public boolean test(Predicate<T> condition) {
        return switch (operation) {
            case OR -> elements.stream().anyMatch(condition);
            case AND -> elements.stream().allMatch(condition);
            case EMPTY -> true;
        };
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

    public static <T> Condition<T> single(T element) {
        return new Condition<T>(Collections.singletonList(element), ConditionOperation.AND);
    }

    public static <T> Condition<T> empty() {
        return new Condition<T>(List.of(), ConditionOperation.EMPTY);
    }

    @SafeVarargs
    public static <T> Condition<T> any(T... elements) {
        return new Condition<T>(Arrays.asList(elements), ConditionOperation.OR);
    }

    @SafeVarargs
    public static <T> Condition<T> all(T... elements) {
        return new Condition<T>(Arrays.asList(elements), ConditionOperation.AND);
    }

    @Override
    public String toString() {
        if (elements.size() == 1) {
            return elements.stream().findFirst().get().toString();
        } else {
            return elements
                    .stream()
                    .map(Objects::toString)
                    .collect(Collectors.joining(", ", "[", "]"));
        }
    }

    enum ConditionOperation {
        OR, AND, EMPTY
    }

}
