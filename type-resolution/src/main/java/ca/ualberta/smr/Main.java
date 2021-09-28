package ca.ualberta.smr;

import ca.ualberta.smr.TypeResolver;
import com.github.javaparser.ParseProblemException;
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

public class Main {

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

        final TypeResolver typeResolver = new TypeResolver(libFolder);
        System.out.println(typeResolver.resolveTypesInFile(filePath));
    }

}
