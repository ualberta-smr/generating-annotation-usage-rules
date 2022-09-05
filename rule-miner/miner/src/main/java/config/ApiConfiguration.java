package config;

import java.util.Collection;

public class ApiConfiguration {

    private Collection<String> prefixes;
    private SubApiConfiguration subApi;

    public Collection<String> prefixes() {
        return prefixes;
    }

    public SubApiConfiguration subApi() {
        return subApi;
    }
}
