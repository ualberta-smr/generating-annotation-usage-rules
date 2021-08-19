from dataclasses import *
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .RulepadGrammarParser import RulepadGrammarParser
    from .RulepadGrammarListener import RulepadGrammarListener
    from .model import *
else:
    from RulepadGrammarParser import RulepadGrammarParser
    from RulepadGrammarListener import RulepadGrammarListener
    from model import *


def mergeAnnotations(a: Annotation, b: Annotation) -> Annotation:
    parameters = a.parameters + b.parameters
    an = Annotation(a.type, parameters)
    an.is_antecedent = a.is_antecedent or b.is_antecedent
    return an


class ConcreteRulepadGrammarListener(RulepadGrammarListener):
    def __init__(self) -> None:
        super().__init__()
        self.__clazz = JavaClass([], None, [], None, None, None)
        # self.__stack = [{
        #     'comingFrom': 'class',
        #     'node': self.__clazz
        # }]
        self.__stack = []
        self.__is_antecedent = True
        self.__initial_element = None
        self.__initial_node = None

    def mergeDuplicateAnnotations(self, oldAnnotations):
        if oldAnnotations == []:
            return oldAnnotations
        import itertools
        from functools import reduce

        tuples = itertools.groupby(oldAnnotations, lambda a: a.type.name)
        newAnnotations = []
        for t, annotations in tuples:
            newAnnotations.append(reduce(mergeAnnotations, annotations))
        return newAnnotations

    def getJavaClass(self) -> JavaClass:
        self.__clazz.annotations = self.mergeDuplicateAnnotations(
            self.__clazz.annotations)
        if self.__clazz.method:
            self.__clazz.method.annotations = self.mergeDuplicateAnnotations(
                self.__clazz.method.annotations)
        if self.__clazz.field:
            self.__clazz.field.annotations = self.mergeDuplicateAnnotations(
                self.__clazz.field.annotations)
        return self.__clazz

    # Enter a parse tree produced by RulepadGrammarParser#must.
    def enterMust(self, ctx: RulepadGrammarParser.MustContext):
        self.__is_antecedent = False
        if self.__initial_element == 'class':
            node = self.__clazz
        elif self.__initial_element == 'function':
            node = self.__clazz.method
        elif self.__initial_element == 'field':
            node = self.__clazz.field
        if self.__initial_element in ['class', 'field', 'function']:
            self.__stack.append({
                'comingFrom': self.__initial_element,
                'node': node
            })

    # Enter a parse tree produced by RulepadGrammarParser#classes.
    def enterClasses(self, ctx: RulepadGrammarParser.ClassesContext):
        if len(self.__stack) == 0:
            self.__initial_element = 'class'
        self.__stack.append({
            'comingFrom': 'class',
            'node': self.__clazz
        })

    # Exit a parse tree produced by RulepadGrammarParser#classes.
    def exitClasses(self, ctx: RulepadGrammarParser.ClassesContext):
        self.__stack.pop()

    def enterAnnotations(self, ctx: RulepadGrammarParser.AnnotationsContext):
        try:
            annotationType = self.initObj(
                Type(ctx.annotationCondition().combinatorialWords(
                ).getText().replace("\"", ""))
            )
        except:
            annotationType = None

        annotation = self.initObj(Annotation(annotationType, []))

        prev = self.__stack[-1]
        if prev['comingFrom'] in ['class', 'function', 'field']:
            prev['node'].annotations.append(annotation)

        self.__stack.append({
            'comingFrom': 'annotation',
            'node': annotation
        })

    def exitAnnotations(self, ctx: RulepadGrammarParser.AnnotationsContext):
        self.__stack.pop()

    def enterExtensions(self, ctx: RulepadGrammarParser.ExtensionsContext):
        # TODO: there can be multiple extensions, currently not supported
        extendedClass = ctx.extensionCondition().words().getText().replace('"', "")

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].extendedClass = self.initObj(Type(extendedClass))

    def enterImplementations(self, ctx: RulepadGrammarParser.ImplementationsContext):
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            className = ctx.implementationCondition().words().getText().replace('"', "")
            prev['node'].implementedInterfaces.append(
                self.initObj(Type(className)))

    def enterTypes(self, ctx: RulepadGrammarParser.TypesContext):
        try:
            type = ctx.typeCondition().combinatorialWords()
        except:
            type = ctx.typeCondition().words()

        type = self.initObj(Type(type.getText().replace("\"", "")))

        prev = self.__stack[-1]
        if prev['comingFrom'] in ['parameter', 'field', 'property']:
            prev['node'].type = type
        elif prev['comingFrom'] == 'function':
            prev['node'].returnType = type

    def enterParameters(self, ctx: RulepadGrammarParser.ParametersContext):
        words = ctx.parameterCondition().combinatorialWords()
        if words:
            elements = words.getText().replace("\"", "").split()
            if len(elements) >= 2:
                type_, name_ = elements[0], elements[1]
            else:
                type_ = elements[0]
            type_ = self.initObj(Type(type_))
            param = self.initObj(Param(type_, name_))
        else:
            param = self.initObj(Param(None, None))
        prev = self.__stack[-1]
        if prev['comingFrom'] in ['annotation', 'function']:
            prev['node'].parameters.append(param)
        self.__stack.append({
            'comingFrom': 'parameter',
            'node': param
        })

    def exitParameters(self, ctx: RulepadGrammarParser.ParametersContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#functions.
    def enterFunctions(self, ctx: RulepadGrammarParser.FunctionsContext):
        if len(self.__stack) > 0:
            classMethod = self.__clazz.method
            if classMethod is None:
                method = self.initObj(
                    Method(self.initObj(Type("void")), [], []))
            else:
                method = classMethod

            prev = self.__stack[-1]
            if prev['comingFrom'] == 'class':
                prev['node'].method = method
        else:
            if self.__is_antecedent:
                self.__initial_element = 'function'
                method = self.initObj(
                    Method(self.initObj(Type("void")), [], []))
                self.__clazz.method = method
            else:
                method = self.__clazz.method

        self.__stack.append({
            'comingFrom': 'function',
            'node': method
        })

    # Exit a parse tree produced by RulepadGrammarParser#functions.
    def exitFunctions(self, ctx: RulepadGrammarParser.FunctionsContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#declarationStatements.
    def enterDeclarationStatements(self, ctx: RulepadGrammarParser.DeclarationStatementsContext):
        if len(self.__stack) > 0:
            field = self.initObj(Field(Type("Object"), []))

            prev = self.__stack[-1]
            if prev['comingFrom'] == 'class':
                prev['node'].field = field
        else:
            if self.__is_antecedent:
                self.__initial_element = 'field'
                field = self.initObj(Field(Type("Object"), []))
                self.__clazz.field = field
            else:
                field = self.__clazz.field
                
        self.__stack.append({
            'comingFrom': 'field',
            'node': field
        })

    # Exit a parse tree produced by RulepadGrammarParser#declarationStatements.
    def exitDeclarationStatements(self, ctx: RulepadGrammarParser.DeclarationStatementsContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#names.
    def enterNames(self, ctx: RulepadGrammarParser.NamesContext):
        name = ctx.nameCondition().words().getText().replace("\"", "")
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'parameter':
            prev['node'].name = name
        elif prev['comingFrom'] == 'property':
            prev['node'].name = name

    # Enter a parse tree produced by RulepadGrammarParser#configurationFiles.
    def enterConfigurationFiles(self, ctx: RulepadGrammarParser.ConfigurationFilesContext):
        configFile = self.initObj(ConfigurationFile("config.properties", []))

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].configurationFile = configFile

        self.__stack.append({
            'comingFrom': 'config-file',
            'node': configFile
        })

    # Exit a parse tree produced by RulepadGrammarParser#configurationFiles.
    def exitConfigurationFiles(self, ctx: RulepadGrammarParser.ConfigurationFilesContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#configurationProperties.
    def enterConfigurationProperties(self, ctx: RulepadGrammarParser.ConfigurationPropertiesContext):
        prop = self.initObj(ConfigurationProperty(None, None))

        text = ctx.configurationPropertyCondition().combinatorialWords()
        if text:
            elements = text.getText().replace("\"", "").split()
            if len(elements) >= 2:
                type_, name_ = elements[0], elements[1]
            else:
                type_, name_ = elements[0], None
            prop.name = name_
            prop.type = type_
        else:
            self.__stack.append({
                'comingFrom': 'property',
                'node': prop
            })
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'config-file':
            prev['node'].properties.append(prop)

    def exitConfigurationProperties(self, ctx: RulepadGrammarParser.ConfigurationPropertiesContext):
        self.__stack.pop()

    def initObj(self, obj):
        obj.is_antecedent = self.__is_antecedent
        return obj
