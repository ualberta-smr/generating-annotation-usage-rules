package miner.config;

import java.util.Collection;

public class ApiConfiguration {

    /**
     * 1. Used to check if frequent item set contains the target api (four times)
     * 2. For dividing the usages based on the annotation: but sub api prefixes already do that
     * 3. To determine if we need to consider the microprofile-config.properties
     */
    private Collection<String> prefixes;
    private SubApiConfiguration subApi;

    public Collection<String> prefixes() {
        return prefixes;
    }

    public SubApiConfiguration subApi() {
        return subApi;
    }
}
