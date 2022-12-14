package ca.ualberta.smr.typeresolution;

import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.type.Type;
import com.github.javaparser.resolution.declarations.ResolvedAnnotationDeclaration;

import java.util.Collection;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.concat;

public class ClassNameCollector {

    public static Map<String, String> getImports(CompilationUnit cu) {
        return concat(
                getAllClassRelatedImports(cu),
                getAllMethodRelatedImports(cu),
                getAllFieldRelatedImports(cu)
        ).filter(Objects::nonNull).collect(Collectors.toMap(
                Import::getSimpleName,
                Import::getFullyQualifiedName,
                (s1, s2) -> s1 // basically, accept the first value
        ));
    }

    private static Stream<Import> getAllClassRelatedImports(CompilationUnit cu) {
        return concat(
                getClassAnnotationMappings(cu),
                getInterfaceImplementationClassExtensions(cu)
        );
    }

    private static Stream<Import> getAllMethodRelatedImports(CompilationUnit cu) {
        return concat(
                getMethodAnnotationMappings(cu),
                getMethodParameterTypeImports(cu),
                getMethodReturnTypeImports(cu)
        );
    }

    private static Stream<Import> getAllFieldRelatedImports(CompilationUnit cu) {
        return concat(
                getFieldAnnotationMappings(cu),
                getFieldTypeImports(cu)
        );
    }

    private static Stream<Import> getInterfaceImplementationClassExtensions(CompilationUnit cu) {
        return cu.findAll(ClassOrInterfaceDeclaration.class)
                .stream()
                .flatMap(c -> concat(
                        c.getImplementedTypes().stream(),
                        c.getExtendedTypes().stream()
                ))
                .map(ClassNameCollector::getImportFromType);
    }

    private static Stream<Import> getFieldAnnotationMappings(CompilationUnit cu) {
        return cu.findAll(FieldDeclaration.class)
                .stream()
                .map(BodyDeclaration::getAnnotations)
                .flatMap(Collection::stream)
                .map(ClassNameCollector::getAnnotationExprPairFunction);
    }

    private static Stream<Import> getMethodAnnotationMappings(CompilationUnit cu) {
        return cu.findAll(MethodDeclaration.class)
                .stream()
                .flatMap(e -> concat(
                        e.getAnnotations().stream(),
                        e.getParameters().stream().flatMap(p -> p.getAnnotations().stream())))
                .map(ClassNameCollector::getAnnotationExprPairFunction);
    }

    private static Stream<Import> getClassAnnotationMappings(CompilationUnit cu) {
        return cu.findAll(ClassOrInterfaceDeclaration.class)
                .stream()
                .map(BodyDeclaration::getAnnotations)
                .flatMap(Collection::stream)
                .map(ClassNameCollector::getAnnotationExprPairFunction);
    }

    private static Stream<Import> getMethodReturnTypeImports(CompilationUnit cu) {
        return cu.findAll(MethodDeclaration.class)
                .stream()
                .map(MethodDeclaration::getType)
                .map(ClassNameCollector::getImportFromType);
    }

    private static Stream<Import> getFieldTypeImports(CompilationUnit cu) {
        return cu.findAll(FieldDeclaration.class)
                .stream()
                .flatMap(fd -> fd.getVariables().stream().map(VariableDeclarator::getType))
                .map(ClassNameCollector::getImportFromType);
    }

    private static Stream<Import> getMethodParameterTypeImports(CompilationUnit cu) {
        return cu.findAll(MethodDeclaration.class)
                .stream()
                .map(MethodDeclaration::getParameters)
                .flatMap(Collection::stream)
                .map(Parameter::getType)
                .map(ClassNameCollector::getImportFromType);
    }

    private static Import getImportFromType(Type type) {
        if (type.isVoidType() || type.isPrimitiveType()) return null;
        try {
            final String qualifiedName = type.resolve().asReferenceType().getQualifiedName();
            final String simple = type.asString();
            return new Import(simple, qualifiedName);
        } catch (Exception e) {
            return null;
        }
    }

    private static Import getAnnotationExprPairFunction(AnnotationExpr a) {
        try {
            final String original = a.getName().toString();

            final ResolvedAnnotationDeclaration resolve = a.resolve();
            final String name = resolve.getName();
            final String qualifiedName = resolve.getQualifiedName();

            final boolean alreadyQualifiedName = Objects.equals(original, qualifiedName);
            if (alreadyQualifiedName) return null;

            return new Import(name, qualifiedName);
        } catch (Exception e) {
            return null;
        }
    }
}
