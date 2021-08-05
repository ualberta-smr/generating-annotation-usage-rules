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
        self.__stack = [{
            'comingFrom': 'class',
            'node': self.__clazz
        }]
        self.__is_antecedent = True

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
        self.__clazz.annotations = self.mergeDuplicateAnnotations(self.__clazz.annotations)
        if self.__clazz.method:
            self.__clazz.method.annotations = self.mergeDuplicateAnnotations(self.__clazz.method.annotations)
        if self.__clazz.field:
            self.__clazz.field.annotations = self.mergeDuplicateAnnotations(self.__clazz.field.annotations)
        return self.__clazz

    # Enter a parse tree produced by RulepadGrammarParser#must.
    def enterMust(self, ctx:RulepadGrammarParser.MustContext):
        self.__is_antecedent = False

    def enterAnnotations(self, ctx: RulepadGrammarParser.AnnotationsContext):
        try:
            annotationType = self.initObj(
                Type(ctx.annotationCondition().combinatorialWords().getText().replace("\"", ""))
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
    
    def exitAnnotations(self, ctx:RulepadGrammarParser.AnnotationsContext):
        self.__stack.pop()
    
    def enterExtensions(self, ctx:RulepadGrammarParser.ExtensionsContext):
        # TODO: there can be multiple extensions, currently not supported
        extendedClass = ctx.extensionCondition().words().getText().replace('"', "")

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].extendedClass = self.initObj(Type(extendedClass))
    
    def enterImplementations(self, ctx:RulepadGrammarParser.ImplementationsContext):
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            className = ctx.implementationCondition().words().getText().replace('"', "")
            prev['node'].implementedInterfaces.append(self.initObj(Type(className)))

    def enterTypes(self, ctx:RulepadGrammarParser.TypesContext):
        try:
            type = ctx.typeCondition().combinatorialWords()
        except:
            type = ctx.typeCondition().words()

        type = self.initObj(Type(type.getText().replace("\"", "")))
        print(type)

        prev = self.__stack[-1]
        if prev['comingFrom'] in ['parameter', 'field', 'property']:
            prev['node'].type = type
        elif prev['comingFrom'] == 'function':
            prev['node'].returnType = type
    
    def enterParameters(self, ctx:RulepadGrammarParser.ParametersContext):
        prev = self.__stack[-1]
        param = self.initObj(Param(None, None))
        if prev['comingFrom'] in ['annotation', 'function']:
            prev['node'].parameters.append(param)
        
        self.__stack.append({
            'comingFrom': 'parameter',
            'node': param
        })

    def exitParameters(self, ctx:RulepadGrammarParser.ParametersContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#functions.
    def enterFunctions(self, ctx:RulepadGrammarParser.FunctionsContext):
        classMethod = self.__clazz.method
        if classMethod is None:
            method = self.initObj(Method(self.initObj(Type("void")), [], []))
        else:
            method = classMethod

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].method = method

        self.__stack.append({
            'comingFrom': 'function',
            'node': method
        })


    # Exit a parse tree produced by RulepadGrammarParser#functions.
    def exitFunctions(self, ctx:RulepadGrammarParser.FunctionsContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#declarationStatements.
    def enterDeclarationStatements(self, ctx:RulepadGrammarParser.DeclarationStatementsContext):
        field = self.initObj(Field(Type("Object"), []))
        
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].field = field

        self.__stack.append({
            'comingFrom': 'field',
            'node': field
        })

    # Exit a parse tree produced by RulepadGrammarParser#declarationStatements.
    def exitDeclarationStatements(self, ctx:RulepadGrammarParser.DeclarationStatementsContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#names.
    def enterNames(self, ctx:RulepadGrammarParser.NamesContext):
        name = ctx.nameCondition().words().getText().replace("\"", "")
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'parameter':
            prev['node'].name = name
        elif prev['comingFrom'] == 'property':
            prev['node'].name = name

    # Enter a parse tree produced by RulepadGrammarParser#configurationFiles.
    def enterConfigurationFiles(self, ctx:RulepadGrammarParser.ConfigurationFilesContext):
        configFile = self.initObj(ConfigurationFile("config.properties", []))

        prev = self.__stack[-1]
        if prev['comingFrom'] == 'class':
            prev['node'].configurationFile = configFile

        self.__stack.append({
            'comingFrom': 'config-file',
            'node': configFile
        })

    # Exit a parse tree produced by RulepadGrammarParser#configurationFiles.
    def exitConfigurationFiles(self, ctx:RulepadGrammarParser.ConfigurationFilesContext):
        self.__stack.pop()

    # Enter a parse tree produced by RulepadGrammarParser#configurationProperties.
    def enterConfigurationProperties(self, ctx:RulepadGrammarParser.ConfigurationPropertiesContext):
        prop = self.initObj(ConfigurationProperty(None, None))
        prev = self.__stack[-1]
        if prev['comingFrom'] == 'config-file':
            prev['node'].properties.append(prop)
        
        self.__stack.append({
            'comingFrom': 'property',
            'node': prop
        })

    def exitConfigurationProperties(self, ctx:RulepadGrammarParser.ConfigurationPropertiesContext):
        self.__stack.pop()


    def initObj(self, obj):
        obj.is_antecedent = self.__is_antecedent
        return obj


