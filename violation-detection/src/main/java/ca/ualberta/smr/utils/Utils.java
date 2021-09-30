package ca.ualberta.smr.utils;

import java.util.Arrays;
import java.util.stream.Stream;

public class Utils {

    @SafeVarargs
    public static <T> Stream<T> concat(Stream<T>...streams) {
        return Arrays.stream(streams)
                .reduce(Stream.of(), Stream::concat);
    }

}
