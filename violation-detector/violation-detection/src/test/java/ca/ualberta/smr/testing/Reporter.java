package ca.ualberta.smr.testing;

import ca.ualberta.smr.model.violationreport.*;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.AnnotationExpr;
import lombok.val;

import java.util.Arrays;
import java.util.Objects;
import java.util.stream.Stream;

import static java.util.stream.Collectors.joining;

public class Reporter {

    public static final String NL = System.lineSeparator();

    public static void report(ViolationCombination violation) {
        System.out.println(getMessage(violation));
    }

    private static String getMessage(ViolationCombination violation) {
        val treeElement = violation.treeElement();

        final String name;
        final String elementType;
        if (treeElement instanceof ClassOrInterfaceDeclaration) {
            val c = (ClassOrInterfaceDeclaration) treeElement;
            name = c.getFullyQualifiedName().orElseGet(c::getNameAsString);
            elementType = "Class";
        } else if (treeElement instanceof MethodDeclaration) {
            val m = (MethodDeclaration) treeElement;
            val fullyQualifiedName = getParentClassName(m);
            name = String.format("%s#%s", fullyQualifiedName, m.getSignature().toString());
            elementType = "Method";
        } else if (treeElement instanceof FieldDeclaration) {
            val f = (FieldDeclaration) treeElement;
            val fullyQualifiedName = getParentClassName(f);
            name = f.getVariables()
                    .stream()
                    .map(v -> v.getName().asString())
                    .map(varName -> String.format("%s#%s", fullyQualifiedName, varName))
                    .collect(joining("; "));
            elementType = "Field";
        } else {
            name = treeElement.getClass().toString();
            elementType = "Element";
        }

        if (violation instanceof ViolationInfo) {
            val location = violation.getLocation().map(ViolationRange::printStart).orElse("--");
            val message = handleViolationInfo(((ViolationInfo) violation), true);
            return String.format("\tat: %s => %s", location, message);
        }

        return String.format("%s %s has following problems: \n%s", elementType, name, describe(violation));
    }

    private static String describe(ViolationCombination v) {
        if (v.isEmpty()) return "";

        if (v instanceof ViolationCombinationAnd) {
            val and = (ViolationCombinationAnd) v;
            return and.violations().stream()
                    .filter(Objects::nonNull)
                    .filter(vv -> !vv.isEmpty())
                    .flatMap(vv -> getString(v, vv))
                    .collect(joining("\n", "All of these should be resolved:\n", "\n"));
        } else if (v instanceof ViolationCombinationOr) {
            val or = (ViolationCombinationOr) v;
            return or.violations().stream()
                    .filter(Objects::nonNull)
                    .filter(vv -> !vv.isEmpty())
                    .flatMap(vv -> getString(v, vv))
                    .collect(joining("\n", "Fixing any of issues below will resolve the problem:\n", "\n"));
        } else if (v instanceof ViolationCombinationXor) {
            val xor = (ViolationCombinationXor) v;
            return xor.violations().stream()
                    .filter(Objects::nonNull)
                    .filter(vv -> !vv.isEmpty())
                    .flatMap(vv -> getString(v, vv))
                    .collect(joining("\n", xor.violationMessagePrefix() + "\n\t", "\n"));
        } else if (v instanceof ViolationInfo) {
            return handleViolationInfo(((ViolationInfo) v), false);
        }

        return "";
    }

    private static String handleViolationInfo(ViolationInfo info, boolean fullyResolveClassName) {
        if (info.isCompleteError()) return info.describe();

        val treeElement = info.treeElement();

        final String name;
        final String elementType;

        if (treeElement instanceof ClassOrInterfaceDeclaration) {
            val c = (ClassOrInterfaceDeclaration) treeElement;
            name = fullyResolveClassName ? c.getFullyQualifiedName().orElseGet(c::getNameAsString) : c.getNameAsString();
            elementType = "Class";
        } else if (treeElement instanceof MethodDeclaration) {
            val m = (MethodDeclaration) treeElement;
            val fullyQualifiedName = getParentClassSimpleName(m, fullyResolveClassName);
            name = String.format("%s#%s", fullyQualifiedName, m.getSignature().toString());
            elementType = "Method";
        } else if (treeElement instanceof FieldDeclaration) {
            val f = (FieldDeclaration) treeElement;
            val fullyQualifiedName = getParentClassSimpleName(f, fullyResolveClassName);
            name = f.getVariables()
                    .stream()
                    .map(vv -> vv.getName().asString())
                    .map(varName -> String.format("%s#%s", fullyQualifiedName, varName))
                    .collect(joining("; "));
            elementType = "Field";
        } else if (treeElement instanceof AnnotationExpr) {
            return info.describe();
        } else {
            name = treeElement.getClass().toString();
            elementType = "Element";
        }
        return String.format("%s %s is missing %s", elementType, name, info.describe());
    }

    private static Stream<String> getString(ViolationCombination v, ViolationCombination vv) {
        val description = describe(vv);

        if (vv instanceof ViolationInfo) {
            val locationString = vv.getLocation()
                    .map(ViolationRange::printStart)
                    .orElseGet(() -> v.getLocation().map(ViolationRange::printStart).orElse(""));
            return Stream.of("\tat: " + locationString + " => " + description);
        }

        return Arrays.stream(description.split(NL)).map(s -> "\t" + s);
    }

    private static String getParentClassName(Node node) {
        val clazz = (ClassOrInterfaceDeclaration) node.getParentNode()
                .orElseThrow(() -> new RuntimeException("Node does not have a parent class"));
        return clazz.getFullyQualifiedName().orElseGet(clazz::getNameAsString);
    }

    private static String getParentClassSimpleName(Node node, boolean fullyResolve) {
        val clazz = (ClassOrInterfaceDeclaration) node.getParentNode()
                .orElseThrow(() -> new RuntimeException("Node does not have a parent class"));
        if (fullyResolve) return clazz.getFullyQualifiedName().orElseGet(clazz::getNameAsString);
        return clazz.getNameAsString();
    }

}
