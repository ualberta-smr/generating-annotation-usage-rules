package ca.ualberta.smr.typeresolution;

import java.util.Objects;

class Import {
    private final String simpleName;
    private final String fullyQualifiedName;

    public Import(String a, String b) {
        this.simpleName = a;
        this.fullyQualifiedName = b;
    }

    String getSimpleName() {
        return simpleName;
    }

    String getFullyQualifiedName() {
        return fullyQualifiedName;
    }

    @Override
    public String toString() {
        return "(" + "" + simpleName + ", " + fullyQualifiedName + ')';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Import pair = (Import) o;
        return Objects.equals(simpleName, pair.simpleName) && Objects.equals(fullyQualifiedName, pair.fullyQualifiedName);
    }

    @Override
    public int hashCode() {
        return Objects.hash(simpleName, fullyQualifiedName);
    }
}