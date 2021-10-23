package ca.ualberta.smr.utils;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.experimental.Accessors;

@RequiredArgsConstructor
@Accessors(fluent = true)
@Getter
public class Pair<K, V> {
    private final K key;
    private final V value;

    public boolean hasValue() {
        return this.value != null;
    }

    public static <K, V> Pair<K, V> empty() {
        return new Pair<>(null, null);
    }
}
