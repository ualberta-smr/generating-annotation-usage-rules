package visitors;


import graph.nodes.*;

public interface NodeVisitor<R> {
    // Actions
    R visit(ClassOrInterfaceNode classOrInterfaceNode);
    R visit(MethodNode methodNode);
    R visit(AnnotationNode annotationNode);
    R visit(ReturnNode typeNode);
    R visit(ParamNode paramNode);
    R visit(ConfigFileNode configFileNode);
    R visit(FieldNode fieldNode);
    R visit(ConstructorNode constructorNode);
    R visit(BeansFileNode beansFileNode);
    R visit(FieldTypeDeclNode fieldTypeDeclNode);
    R visit(ParamTypeDeclNode paramTypeDeclNode);
}
