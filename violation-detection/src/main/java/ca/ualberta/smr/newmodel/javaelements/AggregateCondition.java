package ca.ualberta.smr.newmodel.javaelements;

import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@EqualsAndHashCode
@Getter
public final class AggregateCondition implements ProgramElement {

    private final ProgramElement left;
    private final ProgramElement right;
    private final AggregateConditionOperation operation;

    public static AggregateCondition not(AggregateCondition agg) {
        return new AggregateCondition(
                agg, NoOp.INSTANCE, AggregateConditionOperation.NOT
        );
    }

    public static AggregateCondition not(ProgramElement pe) {
        return new AggregateCondition(
                pe, NoOp.INSTANCE, AggregateConditionOperation.NOT
        );
    }

    public boolean isSingle() {
        return this.left == this.right && operation == AggregateConditionOperation.AND;
    }

    @Override
    public String toString() {
        if (left == right && left == NoOp.INSTANCE) {
            return "[empty]";
        }

        if (left == right) {
            return "AggregateCondition{" +
                    "value=" + left.toString() +
                    '}';
        }
        return "AggregateCondition{" +
                "left=" + left.toString() +
                ", right=" + right.toString() +
                ", operation=" + operation +
                '}';
    }

    //    private final Class<T> type;

//    public boolean test(Predicate<T> condition) {
//        switch (operation) {
//            case OR:
//                return elements.stream().anyMatch(condition);
//            case AND:
//                return elements.stream().allMatch(condition);
//            case EMPTY:
//                return true;
//        };
//        throw new RuntimeException("Illegal ConditionOperation : " + operation);
//    }
//
//    public boolean isNotEmpty() {
//        return !isEmpty();
//    }
//
//    public boolean isEmpty() {
//        return operation == ConditionOperation.EMPTY;
//    }
//
//    public boolean isSingle() {
//        return elements.size() == 1 && operation == ConditionOperation.AND;
//    }
//
//    public <R> Collection<R> map(Function<T, R> fieldExtractor) {
//        return elements.stream()
//                .map(fieldExtractor)
//                .collect(Collectors.toList());
//    }
//
//    public <R> Collection<R> flatMap(Function<T, ? extends Collection<? extends R>> fieldExtractor) {
//        return elements.stream()
//                .map(fieldExtractor)
//                .flatMap(Collection::stream)
//                .collect(Collectors.toList());
//    }
//
//    public <R> Collection<R> select(Function<T, Collection<R>> selectionFunction) {
//        return elements.stream()
//                .map(selectionFunction)
//                .reduce((a, b) -> {
//                    switch (operation) {
//                        case OR:
//                            return Stream.concat(a.stream(), b.stream()).distinct().collect(Collectors.toList());
//                        case AND:
//                            return a.stream().filter(b::contains).collect(Collectors.toList());
//                        default:
//                            return emptyList();
//                    }
//                }).orElseGet(Collections::emptyList);
//    }
//
//    public Collection<ViolationInfo> evaluate(Function<T, ? extends Collection<ViolationInfo>> fieldExtractor) {
//        switch (operation) {
//            case OR:
//                return handleOr(fieldExtractor);
//            case AND:
//                return flatMap(fieldExtractor);
//            case EMPTY:
//                return emptyList();
//        };
//        throw new RuntimeException("Illegal ConditionOperation : " + operation);
//    }
//
//    private Collection<ViolationInfo> handleOr(Function<T, ? extends Collection<ViolationInfo>> fieldExtractor) {
//        final Collection<Collection<ViolationInfo>> violations = this.elements
//                .stream()
//                .map(fieldExtractor)
//                .collect(Collectors.toList());
//
//        final boolean atLeastOneConditionSatisfies = violations.stream().anyMatch(Collection::isEmpty);
//        final boolean doesMissingElementConditionSatisfy = violations.stream().flatMap(Collection::stream).anyMatch(ViolationInfo::isMissingElement);
//        if (atLeastOneConditionSatisfies && !doesMissingElementConditionSatisfy) {
//            // No violation is present (one of the conditions hold)
//            return emptyList();
//        }
//
//        var maybeViolations = violations.stream()
//                .filter(vc -> !vc.isEmpty())
//                .filter(vc -> vc.stream().noneMatch(ViolationInfo::isMissingElement))
//                .findAny();
//
//        return maybeViolations.orElse(emptyList());
//    }

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
//
//    @SafeVarargs
//    @SuppressWarnings("unchecked")
//    public static <T extends ProgramElement> AggregateCondition<T> any(T element, T... elements) {
//        final ArrayList<T> nodes = new ArrayList<>();
//        nodes.add(element);
//        nodes.addAll(listOf(elements));
//
//        return new AggregateCondition<T>(nodes, ConditionOperation.OR, (Class<T>) element.getClass());
//    }
//
//    @SuppressWarnings("unchecked")
//    public static <T extends ProgramElement> AggregateCondition<T> any(Class<T> type) {
//        return new AggregateCondition<T>(new ArrayList<>(), ConditionOperation.OR, type);
//    }
//
//    @SafeVarargs
//    @SuppressWarnings("unchecked")
//    public static <T extends ProgramElement> AggregateCondition<T> all(T element, T... elements) {
//        final ArrayList<T> nodes = new ArrayList<>();
//        nodes.add(element);
//        nodes.addAll(listOf(elements));
//
//        return new AggregateCondition<T>(nodes, ConditionOperation.AND, (Class<T>) element.getClass());
//    }
//
//    @SuppressWarnings("unchecked")
//    public static <T extends ProgramElement> AggregateCondition<T> all(Class<T> type) {
//        return new AggregateCondition<T>(new ArrayList<>(), ConditionOperation.AND, type);
//    }

//    @Override
//    public String toString() {
//        if (elements.size() == 1) {
//            return elements.stream().findFirst().get().toString();
//        } else {
//            return elements
//                    .stream()
//                    .map(Objects::toString)
//                    .collect(Collectors.joining(String.format(" %s ", operation.name())));
//        }
//    }
//
//    @Deprecated
//    public T getFirst() {
//        return elements.stream().findFirst().get();
//    }

    private static class NoOp implements ProgramElement {
        public static final NoOp INSTANCE = new NoOp();
    }
}
