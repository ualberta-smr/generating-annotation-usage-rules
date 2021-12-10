package ca.ualberta.report;

import ca.ualberta.smr.model.*;
import com.github.javaparser.Range;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.*;
import lombok.val;
import org.codehaus.plexus.logging.AbstractLogEnabled;

import javax.inject.Named;
import javax.inject.Singleton;
import java.util.Collection;
import java.util.Optional;
import java.util.stream.Collectors;

import static java.util.Optional.empty;

@Named
@Singleton
public class ConsoleViolationReporter extends AbstractLogEnabled implements ViolationReporter {

    @Override
    public void report(StaticAnalysisRule rule, Collection<ViolationInfo> violations) {
        getLogger().warn("------------------------------------------------------------------------");
        getLogger().warn("For rule: " + rule.name());
        getLogger().warn("\t" + rule.description());
        for (val violation : violations) {
            report(violation);
        }
        getLogger().warn("------------------------------------------------------------------------");
    }

    public void report(ViolationInfo violation) {
        val message = getMessage(violation);
        val location = getLocation(violation);

        // printing
        getLogger().warn(message);
        location.ifPresent(l -> getLogger().warn(String.format("\tLocation: %s", l)));
    }

    private String getMessage(ViolationInfo violation) {
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
        return String.format("%s %s is missing the following element(s): %s", elementType, name, violation.missingElements().toString());
    }

    private String getParentClassName(Node node) {
        val clazz = (ClassOrInterfaceDeclaration) node.getParentNode()
                .orElseThrow(() -> new RuntimeException("Node does not have a parent class"));
        return clazz.getFullyQualifiedName().orElseGet(clazz::getNameAsString);
    }

    private Optional<ViolationRange> getLocation(ViolationInfo violation) {
        val treeElement = violation.treeElement();
        if (treeElement instanceof Node) {
            Optional<Range> range = ((Node) treeElement).getRange();
            return range.map(ViolationRange::new);
        }
        return empty();
    }

}
