package ca.ualberta.smr.typeresolution;

import com.github.javaparser.JavaParser;
import com.github.javaparser.ParserConfiguration;
import com.github.javaparser.ast.CompilationUnit;
import com.github.javaparser.ast.NodeList;
import com.github.javaparser.ast.body.*;
import com.github.javaparser.ast.expr.AnnotationExpr;
import com.github.javaparser.ast.type.ClassOrInterfaceType;
import com.github.javaparser.symbolsolver.JavaSymbolSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.CombinedTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.JarTypeSolver;
import com.github.javaparser.symbolsolver.resolution.typesolvers.ReflectionTypeSolver;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.util.Collection;
import java.util.Map;
import java.util.Objects;
import java.util.Optional;
import java.util.function.Consumer;

public class TypeResolver {

    /**
     * Stores the location of jar files
     */
    private final JavaParser javaParser;

    private static final Logger LOGGER = LoggerFactory.getLogger(TypeResolver.class);

    public TypeResolver(final String libFolder) throws IOException {
        this.javaParser = configureParser(libFolder);
    }

    public TypeResolver(Collection<InputStream> fileStreams) {
        this.javaParser = configureParser(fileStreams);
    }

    public String resolveTypesInFile(String filePath) {
        return getResolvedCompilationUnit(filePath).map(Objects::toString).orElse("");
    }

    public Optional<CompilationUnit> getResolvedCompilationUnit(String filePath) {
        try {
            final Optional<CompilationUnit> maybeParsed = this.javaParser.parse(new File(filePath)).getResult();
            if (!maybeParsed.isPresent()) return Optional.empty();

            final CompilationUnit cu = maybeParsed.get();

            final Map<String, String> imports = ClassNameCollector.getImports(cu);

            convertMethodDeclarations(cu, imports);
            convertFieldDeclarations(cu, imports);
            convertClassInterfaceDeclarations(cu, imports);

            return Optional.of(cu);
        } catch (Exception exception) {
            LOGGER.warn("Resolving types in file {} resulted in exception {}", filePath, exception);
            return Optional.empty();
        }
    }

    private void convertClassInterfaceDeclarations(CompilationUnit cu, Map<String, String> imports) {
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

    private void convertFieldDeclarations(CompilationUnit cu, Map<String, String> imports) {
        cu.findAll(FieldDeclaration.class)
                .forEach(e -> {
                    for (VariableDeclarator variable : e.getVariables()) {
                        final String simple = variable.getType().asString();
                        setIfExists(imports, simple, variable::setType);
                    }

                    convertAnnotations(imports, e.getAnnotations());
                });
    }

    private void convertMethodDeclarations(CompilationUnit cu, Map<String, String> imports) {
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

    private void convertAnnotations(Map<String, String> imports, NodeList<AnnotationExpr> annotations) {
        for (AnnotationExpr annotation : annotations) {
            final String simple = annotation.getName().asString();
            setIfExists(imports, simple, annotation::setName);
        }
    }

    /**
     * Perform the setter action when given key exists in the map with the value of the key
     * @param imports the map
     * @param key the key
     * @param setter the action to be performed
     */
    private void setIfExists(Map<String, String> imports, String key, Consumer<String> setter) {
        final String value = imports.get(key);
        if (value != null) {
            setter.accept(value);
        }
    }

    private JavaParser configureParser(String libFolder) throws IOException {
        CombinedTypeSolver cts = new CombinedTypeSolver(new ReflectionTypeSolver());

        Files.list(new File(libFolder).toPath())
                .forEach(e -> {
                    try {
                        cts.add(new JarTypeSolver(e));
                    } catch (IOException ioException) {
                        ioException.printStackTrace();
                    }
                });

        return new JavaParser(new ParserConfiguration().setSymbolResolver(new JavaSymbolSolver(cts)));
    }

    private JavaParser configureParser(Collection<InputStream> fileStreams) {
        CombinedTypeSolver cts = new CombinedTypeSolver(new ReflectionTypeSolver());

        fileStreams.forEach(fs -> {
            try {
                cts.add(new JarTypeSolver(fs));
            } catch (IOException e) {
                e.printStackTrace();
            }
        });

        return new JavaParser(new ParserConfiguration().setSymbolResolver(new JavaSymbolSolver(cts)));
    }

}
