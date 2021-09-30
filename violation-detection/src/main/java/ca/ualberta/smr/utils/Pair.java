package ca.ualberta.smr.utils;

public record Pair<K, V>(K key, V value) {
    public boolean hasValue() {
        return this.value != null;
    }

    public static <K, V> Pair<K, V> empty() {
        return new Pair<>(null, null);
    }
}
