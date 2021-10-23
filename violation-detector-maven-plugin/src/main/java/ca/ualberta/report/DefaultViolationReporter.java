package ca.ualberta.report;

import ca.ualberta.smr.model.ViolationInfo;
import ca.ualberta.smr.model.ViolationRange;
import com.github.javaparser.Range;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import lombok.val;

import javax.inject.Named;
import javax.inject.Singleton;
import java.util.Optional;
import java.util.stream.Collectors;

import static java.util.Optional.empty;

@Named
@Singleton
public class DefaultViolationReporter implements ViolationReporter {

    @Override
    public void report(ViolationInfo violation) {
        val message = getMessage(violation);
        val location = getLocation(violation);

        // printing
        System.out.println(message);
        location.ifPresent(l -> System.out.printf("\tLocation: %s\n", l));
    }

    private String getMessage(ViolationInfo violation) {
        val treeElement = violation.treeElement();

        final String name;
        if (treeElement instanceof ClassOrInterfaceDeclaration) {
            val c = (ClassOrInterfaceDeclaration) treeElement;
            name = c.getFullyQualifiedName().orElseGet(c::getNameAsString);
        } else if (treeElement instanceof MethodDeclaration) {
            val m = (MethodDeclaration) treeElement;
            val fullyQualifiedName = getParentClassName(m);
            name = String.format("%s#%s", fullyQualifiedName, m.getSignature().toString());
        } else if (treeElement instanceof FieldDeclaration) {
            val f = (FieldDeclaration) treeElement;
            val fullyQualifiedName = getParentClassName(f);
            name = f.getVariables()
                    .stream()
                    .map(v -> v.getName().asString())
                    .map(varName -> String.format("%s#%s", fullyQualifiedName, varName))
                    .collect(Collectors.joining("; "));
        } else {
            name = treeElement.getClass().toString();
        }
        return String.format("%s is missing the following element(s): %s", name, violation.missingElements().toString());
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
