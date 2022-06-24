from dataclasses import *
from antlr4 import *
import itertools
from functools import reduce
from copy import deepcopy

from .RulepadGrammarParser import RulepadGrammarParser
from .RulepadGrammarListener import RulepadGrammarListener
from .model import *

def mergeParameters(a: Param, b: Param) -> Param:
    p = Param(a.type, a.name, mergeDuplicateAnnotations(a.annotations + b.annotations))
    p.is_antecedent = a.is_antecedent or b.is_antecedent
    return p

def mergeDuplicateParameters(oldParameters: List[Param]):
    if oldParameters is None or oldParameters == []:
        return oldParameters
    def key(p: Param):
        type_name = p.type.name if p.type else ""
        name = p.name if p.name else ""
        return (type_name, name)
    tuples = itertools.groupby(sorted(oldParameters, key=key), key=key)

    newParameters = []
    for _, annotations in tuples:
        newParameters.append(reduce(mergeParameters, annotations))
    
    return newParameters

def mergeAnnotations(a: Annotation, b: Annotation) -> Annotation:
    parameters = a.parameters + b.parameters
    an = Annotation(a.type, parameters)
    an.is_antecedent = a.is_antecedent or b.is_antecedent
    return an

def unfoldWildcard(inp: str) -> List[str]:
    """
        TODO: this method needs to report when 
        there's a violation in the input string
    """
    prefix = ""
    for i, ch in enumerate(inp):
        if ch == "[":
            closing = inp.find("]", i)
            if closing == -1:
                return [inp]
            newInp = inp[i+1:closing]
            return list(map(lambda x: f"{prefix}{x}", filter(lambda x: x != "", map(str.strip, newInp.split("|")))))
        else:
            prefix += ch
    return [inp]

def mergeDuplicateAnnotations(oldAnnotations: List[Annotation]):
    if oldAnnotations is None or oldAnnotations == []:
        return oldAnnotations

    def unfold(a: Annotation) -> List[Annotation]:
        unfolded = unfoldWildcard(a.type.name)
        all = []
        for s in unfolded:
            newAnnotation:Annotation = deepcopy(a)
            newAnnotation.type.name = s
            all.append(newAnnotation)
        return all
       

    oldAnnotations = [item for sublist in map(unfold, oldAnnotations) for item in sublist]

    key = lambda anno: anno.type.name
    tuples = itertools.groupby(sorted(oldAnnotations, key=key), key=key)

    newAnnotations = []
    for _, annotations in tuples:
        newAnnotations.append(reduce(mergeAnnotations, annotations))
    
    return newAnnotations

class ConcreteRulepadGrammarListener(RulepadGrammarListener):
    """
        The purpose of this class is to construct a JavaClass object that contains
        all the elements and the fact that if they are antecedent or consequent 
    """
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
                node_.method.parameters = mergeDuplicateParameters(node_.method.parameters)
            if node_.field:
                node_.field.annotations = mergeDuplicateAnnotations(node_.field.annotations)
            return node_
        elif type_ == 'function':
            node_.annotations = mergeDuplicateAnnotations(node_.annotations)
            node_.parameters = mergeDuplicateParameters(node_.parameters)
            return JavaClass([], None, [], None, node_, None, None)
        elif type_ == 'field':
            node_.annotations = mergeDuplicateAnnotations(node_.annotations)
            return JavaClass([], None, [], node_, None, None, None)
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
        if prev['comingFrom'] in ['class', 'function', 'field', 'parameter']:
            prev['node'].annotations.append(annotation)

        self.__stack.append({
            'comingFrom': 'annotation',
            'node': annotation
        })

    def exitAnnotations(self, ctx: RulepadGrammarParser.AnnotationsContext):
        self.__stack.pop()

    def enterExtensions(self, ctx: RulepadGrammarParser.ExtensionsContext):
        # TODO: there can be multiple extensions, currently not supported
        extendedClass = ctx.extensionCondition().combinatorialWords().getText().replace('"', "")

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].extendedClass = self.initObj(Type(extendedClass))

    def enterImplementations(self, ctx: RulepadGrammarParser.ImplementationsContext):
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            className = ctx.implementationCondition().combinatorialWords().getText().replace('"', "")
            prev['node'].implementedInterfaces.append(
                self.initObj(Type(className)))

    def enterTypes(self, ctx: RulepadGrammarParser.TypesContext):
        type = ctx.typeCondition().combinatorialWords()
        type = self.initObj(Type(type.getText().replace("\"", "")))

        prev = self.__stack[-1]
        if prev['comingFrom'] in ['parameter', 'field', 'property']:
            prev['node'].type = type

    def enterReturnTypes(self, ctx: RulepadGrammarParser.ReturnTypesContext):
        type = ctx.returnTypeCondition().combinatorialWords()
        type = self.initObj(Type(type.getText().replace("\"", "")))

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'function':
            prev['node'].returnType = type

    def enterAnnotationParameters(self, ctx: RulepadGrammarParser.AnnotationParametersContext):
        words = ctx.annotationParameterCondition().combinatorialWords()
        if words:
            elements = words.getText().replace("\"", "").split()
            if len(elements) >= 2:
                type_, name_ = elements[0], elements[1]
            elif len(elements) == 1:
                type_, name_ = None, elements[0] 
            else:
                type_, name_ = None, None 
            type_ = self.initObj(Type(type_)) if type_ else None
            param = AnnotationParam(type_, name_, None)
        else:
            param = AnnotationParam(None, None, None)
        param = self.initObj(param)
        prev = self.__stack[-1]
        if prev['comingFrom'] in ['annotation']:
            prev['node'].parameters.append(param)
        self.__stack.append({
            'comingFrom': 'parameter',
            'node': param
        })

    def exitAnnotationParameters(self, ctx: RulepadGrammarParser.AnnotationParametersContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#functionParameters.
    def enterFunctionParameters(self, ctx:RulepadGrammarParser.FunctionParametersContext):
        words = ctx.functionParameterCondition().combinatorialWords()
        if words:
            elements = words.getText().replace("\"", "").split()
            if len(elements) >= 2:
                type_, name_ = elements[0], elements[1]
            elif len(elements) == 1:
                type_, name_ = elements[0], None
            else:
                type_, name_ = '?', None
            type_ = self.initObj(Type(type_))
            param = self.initObj(Param(type_, name_, []))
        else:
            param = self.initObj(Param(None, None, []))
        prev = self.__stack[-1]
        if prev['comingFrom'] in ['function']:
            prev['node'].parameters.append(param)
        self.__stack.append({
            'comingFrom': 'parameter',
            'node': param
        })

    # Exit a parse tree produced by RulepadGrammarParser#functionParameters.
    def exitFunctionParameters(self, ctx:RulepadGrammarParser.FunctionParametersContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#functions.
    def enterFunctions(self, ctx: RulepadGrammarParser.FunctionsContext):
        if len(self.__stack) > 0:
            prev = self.__stack[-1]
            if prev['comingFrom'] == 'class':
                classMethod = prev['node'].method
                if classMethod is None:
                    method = self.initObj(
                        Method(Type("void"), [], [], None))
                else:
                    method = classMethod
                prev['node'].method = method
        else:
            if self.__is_antecedent:
                # if the rule starts with 'function'
                self.__initial = {
                    'node': self.initObj(Method(Type("void"), [], [], None)),
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
            prev = self.__stack[-1]
            if prev['comingFrom'] == 'class':
                classField = prev['node'].field
                if classField is None:
                    field = self.initObj(Field(Type("Object"), [], None))
                else:
                    field = classField
                prev['node'].field = field
        else:
            if self.__is_antecedent:
                self.__initial = {
                    'node': self.initObj(Field(Type("Object"), [], None)),
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
        name = ctx.nameCondition().combinatorialWords().getText().replace("\"", "")
        prev = self.__stack[-1]
        if prev['comingFrom'] in ['parameter', 'property']:
            prev['node'].name = name

    # Enter a parse tree produced by RulepadGrammarParser#values.
    def enterValues(self, ctx:RulepadGrammarParser.ValuesContext):
        value = ctx.valueCondition().combinatorialWords().getText().replace("\"", "")
        prev = self.__stack[-1]
        if prev['comingFrom'] in ['parameter', 'property']:
            prev['node'].value = value

    # Enter a parse tree produced by RulepadGrammarParser#configurationFiles.
    def enterConfigurationFiles(self, ctx: RulepadGrammarParser.ConfigurationFilesContext):
        configFile = self.initObj(ConfigurationFile("microprofile-config.properties", []))

        prev = self.__stack[-1]
        if prev['comingFrom'] in ['class', 'field', 'function']:
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
        prop = self.initObj(ConfigurationProperty(None, None, None))

        text = ctx.configurationPropertyCondition().combinatorialWords()
        if text:
            elements = text.getText().replace("\"", "").split()
            if len(elements) >= 2:
                type_, name_ = elements[0], elements[1]
            elif len(elements) == 1:
                type_, name_ = None, elements[0]
            else:
                type_, name_ = None, None
            prop.name = name_
            prop.type = self.initObj(Type(type_))
        
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'config-file':
            prev['node'].properties.append(prop)

        self.__stack.append({
            'comingFrom': 'property',
            'node': prop
        })


    def exitConfigurationProperties(self, ctx: RulepadGrammarParser.ConfigurationPropertiesContext):
        self.__stack.pop()


    # Enter a parse tree produced by RulepadGrammarParser#beans.
    def enterBeans(self, ctx:RulepadGrammarParser.BeansContext):
        beanDecl = self.initObj(BeanDeclaration("beans.xml", True))

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].declaredInBeans = beanDecl

    # Enter a parse tree produced by RulepadGrammarParser#beansFile.
    def enterBeansFile(self, ctx:RulepadGrammarParser.BeansFileContext):
        beanDecl = self.initObj(BeanDeclaration("beans.xml", False))

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].declaredInBeans = beanDecl


    def initObj(self, obj):
        obj.is_antecedent = self.__is_antecedent
        return obj
