package com.apimisuse;

import com.github.javaparser.StaticJavaParser;
import com.github.javaparser.ast.*;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.symbolsolver.JavaSymbolSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.*;

import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.util.function.Consumer;

public class TypeResolver {

    /**
     * Need to resolve:
     * Annotations:
     * - annotations on top of any class
     * - annotations on top of any interface [Optional]
     * - annotations on top of any method
     * - annotations on top of any field
     * <p>
     * Types:
     * - data types of field declarations
     * - data types of method parameters
     * - data types of method returns
     */
    public static void main(String[] args) throws IOException {
        if (args.length != 2) {
            System.err.println("2 argument is required: <Java file> <Lib folder>");
            System.exit(2);
        }
        final String filePath = args[0];
        final String libFolder = args[1];

        configureParser(libFolder);

        final CompilationUnit cu = StaticJavaParser.parse(new File(filePath));

        final Map<String, String> imports = ClassNameCollector.getImports(cu);

        convertMethodDeclarations(cu, imports);
        convertFieldDeclarations(cu, imports);
        convertClassInterfaceDeclarations(cu, imports);

        System.out.print(cu);
    }

    private static void convertClassInterfaceDeclarations(CompilationUnit cu, Map<String, String> imports) {
        cu.findAll(ClassOrInterfaceDeclaration.class)
                .forEach(e -> {
                    convertAnnotations(imports, e.getAnnotations());

                    for (ClassOrInterfaceType extendedType : e.getExtendedTypes()) {
                        final String simple = extendedType.getName().asString();
                        setIfExists(imports, simple, extendedType::setName);
                    }

                    for (ClassOrInterfaceType extendedType : e.getImplementedTypes()) {
                        final String simple = extendedType.getName().asString();
                        setIfExists(imports, simple, extendedType::setName);
                    }
                });
    }

    private static void convertFieldDeclarations(CompilationUnit cu, Map<String, String> imports) {
        cu.findAll(FieldDeclaration.class)
                .forEach(e -> {
                    for (VariableDeclarator variable : e.getVariables()) {
                        final String simple = variable.getType().asString();
                        setIfExists(imports, simple, variable::setType);
                    }

                    convertAnnotations(imports, e.getAnnotations());
                });
    }

    private static void convertMethodDeclarations(CompilationUnit cu, Map<String, String> imports) {
        cu.findAll(MethodDeclaration.class)
                .forEach(e -> {
                    for (Parameter param : e.getParameters()) {
                        final String simple = param.getType().asString();
                        setIfExists(imports, simple, param::setType);
                    }

                    final String simpleName = e.getType().asString();
                    setIfExists(imports, simpleName, e::setType);

                    convertAnnotations(imports, e.getAnnotations());
                });
    }

    private static void convertAnnotations(Map<String, String> imports, NodeList<AnnotationExpr> annotations) {
        for (AnnotationExpr annotation : annotations) {
            final String simple = annotation.getName().asString();
            setIfExists(imports, simple, annotation::setName);
        }
    }

    private static void setIfExists(Map<String, String> imports, String key, Consumer<String> setter) {
        final String value = imports.get(key);
        if (value != null) {
            setter.accept(value);
        }
    }

    private static void configureParser(String libFolder) throws IOException {
        CombinedTypeSolver cts = new CombinedTypeSolver(new ReflectionTypeSolver());

        Files.list(new File(libFolder).toPath())
                .forEach(e -> {
                    try {
                        cts.add(new JarTypeSolver(e));
                    } catch (IOException ioException) {
                        ioException.printStackTrace();
                    }
                });

        StaticJavaParser
                .getConfiguration()
                .setSymbolResolver(new JavaSymbolSolver(cts));
    }

}
