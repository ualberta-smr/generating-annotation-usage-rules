package ca.ualberta.smr.utils;

import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.ProgramElement;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Stream;

import static java.util.stream.Collectors.toList;

public class Utils {

    @SafeVarargs
    public static <T> Stream<T> concat(Stream<T>...streams) {
        return Arrays.stream(streams)
                .reduce(Stream.of(), Stream::concat);
    }

    public static <T extends ProgramElement> Collection<String> collectionToString(Collection<Condition<T>> elements) {
        return elements.stream().filter(Condition::isNotEmpty).map(Condition::toString).collect(toList());
    }

    @SafeVarargs
    public static <T> List<T> listOf(T...args) {
        return Arrays.asList(args);
    }

}
