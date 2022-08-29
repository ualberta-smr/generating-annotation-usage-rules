package ca.ualberta.smr.model.javaelements;

import ca.ualberta.smr.detection.clazz.ClassAntecedentScanner;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationInfo;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import com.github.javaparser.ast.body.FieldDeclaration;
import com.github.javaparser.ast.body.MethodDeclaration;
import com.github.javaparser.ast.body.Parameter;
import com.github.javaparser.ast.nodeTypes.NodeWithSimpleName;
import lombok.*;
import lombok.experimental.Accessors;

import java.util.*;

import static ca.ualberta.smr.model.javaelements.AggregateCondition.empty;
import static ca.ualberta.smr.model.javaelements.AggregateCondition.single;
import static ca.ualberta.smr.model.javaelements.JavaElementUtils.handleViolationCombinationCreation;
import static ca.ualberta.smr.parsing.annotation.AnnotationParsingUtils.createDisjunctionCondition;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.describe;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;
import static java.util.stream.Collectors.toList;

@Getter
@RequiredArgsConstructor
@Accessors(fluent = true)
@EqualsAndHashCode(callSuper = false)
public final class JavaClass extends ProgramElement implements AnalysisItem {
    private final AggregateCondition annotations;
    private final AggregateCondition field;
    private final AggregateCondition method;
    private final AggregateCondition extendedClass;
    private final AggregateCondition implementedInterfaces;
    private final AggregateCondition overriddenMethod;
    private final AggregateCondition beanDeclaration;
    // TODO: support for configuration files
    // TODO: support for constructors (that actually can be treated like methods)

    @Override
    public boolean matches(Object bd) {
        if (bd instanceof ClassOrInterfaceDeclaration) {
            val cd = (ClassOrInterfaceDeclaration) bd;
            boolean annotationMatches = annotations.matches(cd.getAnnotations());
            boolean fieldsMatch = field.isEmpty() || cd.getFields().stream().anyMatch(field::matches);
            boolean methodsMatch = method.isEmpty() || cd.getMethods().stream().anyMatch(method::matches);
            boolean extendMatch = extendedClass.isEmpty() || cd.getExtendedTypes().stream().map(NodeWithSimpleName::getNameAsString).anyMatch(extendedClass::matches);
            boolean implMatch = implementedInterfaces.isEmpty() || cd.getImplementedTypes().stream().map(NodeWithSimpleName::getNameAsString).anyMatch(implementedInterfaces::matches);
            boolean overriddenMatch = overriddenMethod.matches(cd.getMethods());
            boolean isACDIBean = beanDeclaration.matches(cd);

            return annotationMatches
                    && fieldsMatch
                    && methodsMatch
                    && extendMatch
                    && implMatch
                    && overriddenMatch
                    && isACDIBean;
        } else if (bd instanceof MethodDeclaration) {
            val md = (MethodDeclaration) bd;
            return method.matches(md);
        } else if (bd instanceof FieldDeclaration) {
            val fd = (FieldDeclaration) bd;
            return field.matches(fd);
        }

        return false;
    }

    @Override
    public ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
        val cd = (ClassOrInterfaceDeclaration) bd;

        val missingAnnotations = annotations.getMissing(cd.getAnnotations(), rule);
        val missingField = findMissing(field, ClassAntecedentScanner.findFieldsFromClassDeclaration(cd, rule.antecedent()), cd, rule);
        val missingMethod = findMissing(method, ClassAntecedentScanner.findMethodsFromClassDeclaration(cd, rule.antecedent()), cd, rule);
        val missingExtensions = findMissing(extendedClass,
                cd.getExtendedTypes().stream().map(NodeWithSimpleName::getNameAsString).collect(toList()), cd, rule);
        val missingImplementation = findMissing(implementedInterfaces,
                cd.getImplementedTypes().stream().map(NodeWithSimpleName::getNameAsString).collect(toList()), cd, rule);
        val missingOverriddenMethods = overriddenMethod.getMissing(cd.getMethods(), rule);
        val missingCDIBean = beanDeclaration.getMissing(cd, rule);

        val violations = listOf(
                missingField, missingMethod, missingExtensions,
                missingImplementation, listOf(missingAnnotations, missingOverriddenMethods, missingCDIBean)
        ).stream().flatMap(Collection::stream).collect(toList());

        return handleViolationCombinationCreation(cd, violations);
    }

    private Collection<ViolationCombination> findMissing(AggregateCondition prop, Collection<?> elements, ClassOrInterfaceDeclaration cd, StaticAnalysisRule rule) {
        if (prop.isEmpty() || elements.stream().map(e -> prop.getMissing(e, rule)).anyMatch(ViolationCombination::isEmpty)) {
            return listOf(ViolationCombination.EMPTY);
        }

        return elements.stream()
                .map(e -> prop.getMissing(e, rule))
                .filter(v -> !v.isEmpty())
                .map(v -> {
                    if (v.treeElement() != null) return v;
                    return v.shallowCopy(cd);
                })
                .collect(toList());
    }

    @Override
    String description() {
        Map<String, AggregateCondition> map = new HashMap<>();
        map.put("annotations", annotations);
        map.put("field", field);
        map.put("method", method);
        map.put("extends", extendedClass);
        map.put("implements", implementedInterfaces);
        map.put("isCDIBean", beanDeclaration);
        return describe("class", map);
    }

    @RequiredArgsConstructor
    @Getter
    @Accessors(fluent = true)
    @EqualsAndHashCode(callSuper = false)
    public static class OverriddenMethod extends ProgramElement {
        private final String name;
        private final List<MethodParameter> parameters;

        @Override
        @SuppressWarnings("unchecked")
        boolean matches(Object bd) {
            val declarations = (List<MethodDeclaration>) bd;
            return declarations.stream()
                    .anyMatch(md -> name.equals(md.getNameAsString()) && allParamsMatchInOrder(md.getParameters()));
        }

        private boolean allParamsMatchInOrder(NodeList<Parameter> otherParameters) {
            if (this.parameters.size() != otherParameters.size()) return false;

            for (int i = 0; i < this.parameters.size(); i++) {
                boolean paramAtPosMatches = this.parameters.get(i).type().matches(otherParameters.get(i).getTypeAsString());
                if (!paramAtPosMatches) {
                    return false;
                }
            }
            return true;
        }

        @Override
        @SuppressWarnings("unchecked")
        ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
            val declarations = (List<MethodDeclaration>) bd;
            for (val md : declarations) {
                if (name.equals(md.getNameAsString())) {
                    if (allParamsMatchInOrder(md.getParameters())) {
                        return ViolationCombination.EMPTY;
                    }
                    return new ViolationInfo(md, String.format("Method '%s' must have all the parameters: [%s]", name, parameters), true);
                }
            }
            return new ViolationInfo(null, this.toString());
        }

        @Override
        String description() {
            return String.format("method [name = %s, params = %s]", name, parameters);
        }
    }

    /**
     * Bean declaration denotes that a class is a CDI bean. Please note that, there are multiple ways to declare a bean.
     * What we are doing here is partial, and only checking for the bean defining annotations. It is also possible to
     * create beans programmatically, or by mentioning them in the beans.xml file. We currently do not scan for these
     * options as it requires more sophisticated misuse detection techniques.
     */
    @RequiredArgsConstructor
    @Getter
    @Accessors(fluent = true)
    @EqualsAndHashCode(callSuper = false)
    public static class BeanDeclaration extends ProgramElement {

        /**
         * Reference: https://jakarta.ee/specifications/cdi/3.0/jakarta-cdi-spec-3.0.html#bean_defining_annotations
         * <br/>
         * Since, we currently do not scan the annotation definitions, we will not be able to detect if any custom
         * annotation is has a @NormalScope or @Stereotype annotation.
         * <br/>
         * This is also something to keep in mind (excerpt from the previously mentioned link):
         * <blockquote>
         * Note that to ensure compatibility with other JSR-330 implementations, all pseudo-scope annotations
         * except @Dependent are not bean defining annotations.
         * However, a stereotype annotation including a pseudo-scope annotation is a bean defining annotation.
         * </blockquote>
         */
        private static final List<String> beanDeclaringAnnotations = listOf(
                // Jakarta EE annotations
                "jakarta.enterprise.context.ApplicationScoped",
                "jakarta.enterprise.context.SessionScoped",
                "jakarta.enterprise.context.ConversationScoped",
                "jakarta.enterprise.context.RequestScoped",
                // normal scoped?
                "jakarta.enterprise.inject.spi.Interceptor",
                "jakarta.enterprise.inject.spi.Decorator",
                "jakarta.enterprise.inject.Stereotype", // or anything that has been annotated with Stereotype
                "jakarta.enterprise.context.Dependent",

                // Java EE annotations
                "javax.enterprise.context.ApplicationScoped",
                "javax.enterprise.context.SessionScoped",
                "javax.enterprise.context.ConversationScoped",
                "javax.enterprise.context.RequestScoped",
                // normal scoped?
                "javax.enterprise.inject.spi.Interceptor",
                "javax.enterprise.inject.spi.Decorator",
                "javax.enterprise.inject.Stereotype", // or anything that has been annotated with Stereotype
                "javax.enterprise.context.Dependent"
        );

        // create a condition that is simply the disjunction of all the annotations mentioned above
        private final AggregateCondition annotations = single(
                new Annotation(
                        createDisjunctionCondition(beanDeclaringAnnotations),
                        empty()
                )
        );

        @Override
        boolean matches(Object bd) {
            val cd = (ClassOrInterfaceDeclaration) bd;
            return this.annotations.matches(cd.getAnnotations());
        }

        @Override
        ViolationCombination getMissing(Object bd, StaticAnalysisRule rule) {
            val cd = (ClassOrInterfaceDeclaration) bd;
            return annotations.getMissing(cd.getAnnotations(), rule);
        }

        @Override
        String description() {
            return "CDI bean";
        }
    }
}

