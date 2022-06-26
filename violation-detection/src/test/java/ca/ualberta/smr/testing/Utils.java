package ca.ualberta.smr.testing;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.SneakyThrows;
import lombok.val;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;
import static java.util.stream.Collectors.*;
import static java.util.stream.Stream.concat;

public class Utils {

    public static void main(String[] args) throws IOException {
        val dir = new File("src/test/data/jarfiles");
        Files.walk(dir.toPath())
                .map(Path::toFile)
                .filter(File::isFile)
                .map(Utils::getClassNamesFromJarFile)
                .flatMap(Collection::stream)
                .filter(s -> !s.contains("package-info") || !s.contains("module-info"))
                .map(s -> Arrays.stream(s.split("\\.")).limit(s.split("\\.").length - 1).collect(joining(".")))
                .collect(groupingBy(s -> s))
                .keySet()
                .stream()
                .sorted()
                .forEach(System.out::println);
    }

    private static void generateAllClassNamesAndPackages() throws IOException {
        val dir = new File("src/test/data/jarfiles");
        val result = Files.walk(dir.toPath())
                .map(Path::toFile)
                .filter(File::isFile)
                .map(Utils::getClassNamesFromJarFile)
                .flatMap(Collection::stream)
                .filter(s -> !s.contains("package-info") || !s.contains("module-info"))
                .collect(toMap(
                        str -> str.substring(str.lastIndexOf(".") + 1).replace("$", ".").toLowerCase(),
                        str -> listOf(str.replace("$", ".")),
                        (a, b) -> new ArrayList<>(concat(a.stream(), b.stream()).collect(toSet()))));

        val s = new ObjectMapper().writerWithDefaultPrettyPrinter().writeValueAsString(result);
        System.out.println(s);
    }

    @SneakyThrows
    public static Set<String> getClassNamesFromJarFile(File givenFile) {
        Set<String> classNames = new HashSet<>();
        try (JarFile jarFile = new JarFile(givenFile)) {
            Enumeration<JarEntry> e = jarFile.entries();
            while (e.hasMoreElements()) {
                JarEntry jarEntry = e.nextElement();
                if (jarEntry.getName().endsWith(".class")) {
                    String className = jarEntry.getName()
                            .replace("/", ".")
                            .replace(".class", "");
                    classNames.add(className);
                }
            }
            return classNames;
        }
    }


}
