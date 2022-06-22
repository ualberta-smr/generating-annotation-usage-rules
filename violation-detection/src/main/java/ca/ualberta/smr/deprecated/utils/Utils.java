package ca.ualberta.smr.deprecated.utils;

import ca.ualberta.smr.deprecated.model.javaelements.Condition;
import ca.ualberta.smr.deprecated.model.javaelements.ProgramElement;
import com.github.javaparser.HasParentNode;
import com.github.javaparser.ast.Node;
import com.github.javaparser.ast.body.ClassOrInterfaceDeclaration;

import java.util.*;
import java.util.stream.Stream;

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

    public static Collection<ClassOrInterfaceDeclaration> getClassDeclarations(Collection<? extends HasParentNode<? extends Node>> declarations) {
        return declarations
                .stream()
                .map(HasParentNode::getParentNode)
                .filter(Optional::isPresent)
                .map(Optional::get)
                .map(node -> ((ClassOrInterfaceDeclaration) node))
                .collect(toSet());
    }

}
