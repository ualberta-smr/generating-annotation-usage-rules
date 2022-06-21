package ca.ualberta.smr.utils;

import ca.ualberta.smr.model.javaelements.*;
import ca.ualberta.smr.newmodel.javaelements.AggregateCondition;
import com.github.javaparser.HasParentNode;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;
import lombok.val;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static java.lang.String.format;
import static java.util.stream.Collectors.*;

public class Utils {

    @SafeVarargs
    public static <T> Stream<T> concat(Stream<T>...streams) {
        return Arrays.stream(streams)
                .reduce(Stream.of(), Stream::concat);
    }

    @SafeVarargs
    public static <T> Stream<T> concat(Collection<T>...collections) {
        return Arrays.stream(collections)
                .map(Collection::stream)
                .reduce(Stream.of(), Stream::concat);
    }

    public static <T extends ProgramElement> Collection<String> collectionToString(Collection<Condition<T>> elements) {
        return elements.stream().filter(Condition::isNotEmpty).map(Condition::toString).collect(toList());
    }

    @SafeVarargs
    public static <T> List<T> listOf(T...args) {
        return new ArrayList<>(Arrays.asList(args));
    }

    public static Collection<ClassOrInterfaceDeclaration> getClassDeclarations(Collection<? extends HasParentNode<? extends Node>> declarations) {
        return declarations
                .stream()
                .map(HasParentNode::getParentNode)
                .filter(Optional::isPresent)
                .map(Optional::get)
                .map(node -> ((ClassOrInterfaceDeclaration) node))
                .collect(toSet());
    }

    public static String describe(String prefix, Map<String, AggregateCondition> keyValues) {
        return keyValues.entrySet().stream()
                .filter(entry -> !entry.getValue().isEmpty())
                .map(entry -> format("%s=[%s]", entry.getKey(), entry.getValue()))
                .collect(joining(", ", prefix + " {", "}"));
    }

}
