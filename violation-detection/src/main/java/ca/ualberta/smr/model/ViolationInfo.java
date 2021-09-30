package ca.ualberta.smr.model;

import com.github.javaparser.ast.body.*;

import java.util.Collection;

public record ViolationInfo(Object treeElement, Collection<String> missingElements) {

    public boolean isNotEmpty() {
        return !missingElements.isEmpty();
    }

    @Override
    public String toString() {
        final String name;
        if (treeElement instanceof ClassOrInterfaceDeclaration) {
            name = ((ClassOrInterfaceDeclaration) treeElement).getFullyQualifiedName().get();
        } else if (treeElement instanceof MethodDeclaration) {
            name = ((MethodDeclaration) treeElement).getSignature().toString();
        } else if (treeElement instanceof FieldDeclaration) {
            name = ((FieldDeclaration) treeElement).getElementType().asString();
        } else {
            name = treeElement.getClass().toString();
        }
        return String.format("(%s -> %s)", name, missingElements.toString());
    }
}