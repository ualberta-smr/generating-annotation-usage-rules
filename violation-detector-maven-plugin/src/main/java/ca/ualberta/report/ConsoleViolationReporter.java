package ca.ualberta.report;

import ca.ualberta.FileStaticAnalysisRulePair;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.*;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.expr.AnnotationExpr;
import lombok.val;
import org.codehaus.plexus.logging.AbstractLogEnabled;

import javax.inject.Named;
import javax.inject.Singleton;
import java.util.Arrays;
import java.util.Collection;
import java.util.Objects;
import java.util.function.Consumer;
import java.util.stream.Stream;

import static java.util.stream.Collectors.joining;

@Named
@Singleton
public class ConsoleViolationReporter extends AbstractLogEnabled implements ViolationReporter {

    @Override
    public void report(StaticAnalysisRule rule, Collection<FileStaticAnalysisRulePair> violations, Consumer<String> logger) {
        logger.accept("------------------------------------------------------------------------");
        logger.accept("For rule: " + rule.name());
        logger.accept("\t" + rule.description());
        logger.accept("\t---");
        int i = 1;
        for (val violation : violations) {
            logger.accept("\tIn: " + violation.path);
            for (ViolationCombination misuse : violation.misuses) {
                logger.accept(getMessage(misuse, i++));
            }
            logger.accept("");
        }
        logger.accept("------------------------------------------------------------------------");
    }

    private String getMessage(ViolationCombination violation, int order) {
        if (violation instanceof ViolationInfo) {
            val location = violation.getLocation().map(ViolationRange::printStart).orElse("--");
            val message = handleViolationInfo(((ViolationInfo) violation), true);
            return String.format("\t%d. at: %s => %s", order, location, message);
        }

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

        return String.format("%d. %s %s has following problems: \n%s", order, elementType, name, describe(violation));
    }

    private String describe(ViolationCombination v) {
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

    private String handleViolationInfo(ViolationInfo info, boolean fullyResolveClassName) {
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
            val fullyQualifiedName = getParentClassName(m, fullyResolveClassName);
            name = String.format("%s#%s", fullyQualifiedName, m.getSignature().toString());
            elementType = "Method";
        } else if (treeElement instanceof FieldDeclaration) {
            val f = (FieldDeclaration) treeElement;
            val fullyQualifiedName = getParentClassName(f, fullyResolveClassName);
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

    private Stream<String> getString(ViolationCombination v, ViolationCombination vv) {
        val description = describe(vv);

        if (vv instanceof ViolationInfo) {
            val locationString = vv.getLocation()
                    .map(ViolationRange::printStart)
                    .orElseGet(() -> v.getLocation().map(ViolationRange::printStart).orElse(""));
            return Stream.of("\tat: " + locationString + " => " + description);
        }

        return Arrays.stream(description.split(System.lineSeparator())).map(s -> "\t" + s);
    }

    private String getParentClassName(Node node) {
        val clazz = (ClassOrInterfaceDeclaration) node.getParentNode()
                .orElseThrow(() -> new RuntimeException("Node does not have a parent class"));
        return clazz.getFullyQualifiedName().orElseGet(clazz::getNameAsString);
    }

    private String getParentClassName(Node node, boolean fullyResolve) {
        val clazz = (ClassOrInterfaceDeclaration) node.getParentNode()
                .orElseThrow(() -> new RuntimeException("Node does not have a parent class"));
        if (fullyResolve) return clazz.getFullyQualifiedName().orElseGet(clazz::getNameAsString);
        return clazz.getNameAsString();
    }

}
