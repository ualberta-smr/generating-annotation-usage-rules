package config;

import java.util.Collection;

public class SubApiConfiguration {
    private String subApiRegex;
    private Collection<String> prefixes;

    public String subApiRegex() {
        return subApiRegex;
    }

    public Collection<String> prefixes() {
        return prefixes;
    }
}
