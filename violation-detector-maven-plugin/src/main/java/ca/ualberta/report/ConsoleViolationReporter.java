package ca.ualberta.report;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import lombok.val;
import org.codehaus.plexus.logging.AbstractLogEnabled;

import javax.inject.Named;
import javax.inject.Singleton;
import java.util.Collection;
import java.util.function.Consumer;
import java.util.stream.Collectors;

@Named
@Singleton
public class ConsoleViolationReporter extends AbstractLogEnabled implements ViolationReporter {

    @Override
    public void report(StaticAnalysisRule rule, Collection<ViolationCombination> violations, Consumer<String> logger) {
        logger.accept("------------------------------------------------------------------------");
        logger.accept("For rule: " + rule.name());
        logger.accept("\t" + rule.description());
        for (val violation : violations) {
            report(violation, logger);
        }
        logger.accept("------------------------------------------------------------------------");
    }

    public void report(ViolationCombination violation, Consumer<String> logger) {
        val message = getMessage(violation);
        val location = violation.getLocation();

        // printing
        logger.accept(message);
        location.ifPresent(l -> logger.accept(String.format("\tLocation: %s", l)));
    }

    private String getMessage(ViolationCombination violation) {
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
                    .collect(Collectors.joining("; "));
            elementType = "Field";
        } else {
            name = treeElement.getClass().toString();
            elementType = "Element";
        }
        return String.format("%s %s is missing the following element(s): %s", elementType, name, violation.describe());
    }

    private String getParentClassName(Node node) {
        val clazz = (ClassOrInterfaceDeclaration) node.getParentNode()
                .orElseThrow(() -> new RuntimeException("Node does not have a parent class"));
        return clazz.getFullyQualifiedName().orElseGet(clazz::getNameAsString);
    }

}
