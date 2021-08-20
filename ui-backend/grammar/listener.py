from dataclasses import *
from antlr4 import *
import itertools
from functools import reduce

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

def mergeDuplicateAnnotations(oldAnnotations):
    if oldAnnotations is None or oldAnnotations == []:
        return oldAnnotations
    tuples = itertools.groupby(oldAnnotations, lambda a: a.type.name)
    newAnnotations = []
    for t, annotations in tuples:
        newAnnotations.append(reduce(mergeAnnotations, annotations))
    return newAnnotations

class ConcreteRulepadGrammarListener(RulepadGrammarListener):
    def __init__(self) -> None:
        super().__init__()
        self.__stack = []
        self.__is_antecedent = True
        self.__initial = {
            'node': None,
            'type': None
        }

    def getJavaClass(self) -> JavaClass:
        type_ = self.__initial["type"]
        node_ = self.__initial["node"]
        if type_ == 'class':
            node_.annotations = mergeDuplicateAnnotations(node_.annotations)
            if node_.method:
                node_.method.annotations = mergeDuplicateAnnotations(node_.method.annotations)
            if node_.field:
                node_.field.annotations = mergeDuplicateAnnotations(node_.field.annotations)
            return node_
        elif type_ == 'function':
            node_.annotations = mergeDuplicateAnnotations(node_.annotations)
            return JavaClass([], None, [], None, node_, None)
        elif type_ == 'field':
            node_.annotations = mergeDuplicateAnnotations(node_.annotations)
            return JavaClass([], None, [], node_, None, None)
        else:
            return None


    # Enter a parse tree produced by RulepadGrammarParser#must.
    def enterMust(self, ctx: RulepadGrammarParser.MustContext):
        self.__is_antecedent = False
        self.__stack.append({
            'comingFrom': self.__initial['type'],
            'node': self.__initial['node']
        })

    # Enter a parse tree produced by RulepadGrammarParser#classes.
    def enterClasses(self, ctx: RulepadGrammarParser.ClassesContext):
        if len(self.__stack) == 0:
            self.__initial = {
                'node': JavaClass([], None, [], None, None, None),
                'type': 'class'
            }
            self.__stack.append({
                'comingFrom': 'class',
                'node': self.__initial['node']
            })
        else:
            # there's actually no other case when a rule can use class (for now)
            pass

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
            prev = self.__stack[-1]
            if prev['comingFrom'] == 'class':
                classMethod = prev['node'].method
                if classMethod is None:
                    method = self.initObj(
                        Method(self.initObj(Type("void")), [], []))
                else:
                    method = classMethod
                prev['node'].method = method
        else:
            if self.__is_antecedent:
                # if the rule starts with 'function'
                self.__initial = {
                    'node': self.initObj(Method(self.initObj(Type("void")), [], [])),
                    'type': 'function'
                }
            method = self.__initial['node']

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
                self.__initial = {
                    'node': self.initObj(Field(Type("Object"), [])),
                    'type': 'field'
                }
            field = self.__initial['node']

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
            prop.type = self.initObj(Type(type_))
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
