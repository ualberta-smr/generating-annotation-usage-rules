import RulepadGrammarListener from "./generated/RulepadGrammarListener";
import clone from 'just-clone'
import RulepadGrammarParser from "./generated/RulepadGrammarParser";

class AntecedentOrConsequent {
    constructor() {
        this.isAntecedent = null;
    }
}

class Type extends AntecedentOrConsequent {
    constructor(name) {
        super()
        this.name = name;
    }
}

class ConfigurationProperty extends AntecedentOrConsequent {
    constructor(name, type, value) {
        super()
        this.name = name
        this.type = type
        this.value = value
    }
}

class ConfigurationFile extends AntecedentOrConsequent {
    constructor(name, properties) {
        super()
        this.name = name
        this.properties = properties == undefined ? [] : properties
    }
}

class BeanDeclaration extends AntecedentOrConsequent {
    constructor(name, declared) {
        super()
        this.name = name
        this.declared = declared == undefined ? false : declared;
    }
}

class MethodParam extends AntecedentOrConsequent {
    constructor(type, name, annotations) {
        super()
        this.name = name
        this.type = type
        this.annotations = annotations == undefined ? [] : annotations
    }
}

class AnnotationParam extends AntecedentOrConsequent {
    constructor(type, name, value) {
        super()
        this.name = name
        this.type = type
        this.annotations = value
    }
}

class Annotation extends AntecedentOrConsequent {
    constructor(type, parameters) {
        super()
        this.type = type
        this.parameters = parameters == undefined ? [] : parameters
    }
}

class Field extends AntecedentOrConsequent {
    constructor(type, annotations, configurationFile) {
        super()
        this.type = type == undefined ? new Type("Object") : type
        this.annotations = annotations == undefined ? [] : annotations
        this.configurationFile = configurationFile
    }
}

class Method extends AntecedentOrConsequent {
    constructor(returnType, parameters, annotations, configurationFile, name = null) {
        super()
        this.name = name;
        this.returnType = returnType == undefined ? new Type("void") : returnType
        this.parameters = parameters == undefined ? [] : parameters
        this.annotations = annotations == undefined ? [] : annotations
        this.configurationFile = configurationFile
    }
}

class JavaClass extends AntecedentOrConsequent {
    constructor(annotations, extendedClass, implementedInterfaces, field, method, configurationFile, declaredInBeans, overriddenMethod) {
        super()
        this.extendedClass = extendedClass
        this.annotations = annotations
        this.implementedInterfaces = implementedInterfaces
        this.method = method
        this.overriddenMethod = overriddenMethod
        this.field = field
        this.configurationFile = configurationFile
        this.declaredInBeans = declaredInBeans
    }
}

export default class VisualizerListener extends RulepadGrammarListener {

    constructor() {
        super();
        this.__stack = []
        this.__is_antecedent = true
        this.__initial = {
            'node': null,
            'type': null
        }
    }

    __groupBy = (list, keyGetter) => {
        const map = new Map();
        list.forEach((item) => {
            const key = keyGetter(item);
            if (!map.has(key)) {
                map.set(key, [item]);
            } else {
                map.get(key).push(item);
            }
        });
        return map;
    }

    // (Annotation, Annotation) -> Annotation
    __mergeAnnotations(a, b) {
        const allParams = [...a.parameters, ...b.parameters];
        const an = new Annotation(a.type, allParams);
        an.isAntecedent = a.isAntecedent || b.isAntecedent
        an.negated = a.negated && b.negated
        return an
    }

    // (MethodParam, MethodParam) -> MethodParam
    __mergeParameters(a, b) {
        const p = new MethodParam(
            a.type, a.name, this.__mergeDuplicateAnnotations([
                ...a.annotations, ...b.annotations
            ])
        )
        p.isAntecedent = a.isAntecedent || b.isAntecedent
        return p
    }

    // [MethodParam] -> [MethodParam]
    __mergeDuplicateParameters(oldParams) {
        if (oldParams == null || oldParams == undefined) {
            return oldParams
        }

        oldParams = oldParams.sort((a, b) => {
            // (MethodParam, MethodParam) -> int
            const aTypeName = a.type ? a.type.name : ""
            const aName = a.name ? a.name : ""
            const bTypeName = b.type ? b.type.name : ""
            const bName = b.name ? b.name : ""
            
            const typeComp = aTypeName.localeCompare(bTypeName)

            if (typeComp === 0) {
                return aName.localeCompare(bName)
            }
            return typeComp
        })

        oldParams = this.__groupBy(oldParams, (mp) => {
            const typeName = mp.type ? mp.type.name : ""
            const name = mp.name ? mp.name : ""
            return typeName+"."+name
        })

        const newParameters = []
        for (let [_, params] of oldParams) {
            newParameters.push(params.reduce(this.__mergeParameters))
        }
        return newParameters
    }

    // (str) -> [str...]
    __unfoldWildcard(inp) {
        let prefix = ""

        for (let i = 0; i < inp.length; i++) {
            const ch = inp[i]
            if (ch === "[") {
                const closing = inp.indexOf("]", i);
                if (closing === -1) {
                    return [inp]
                }
                const newInp = inp.slice(i + 1, closing)
                return newInp.split("|").map(e => e.trim())
                    .filter(e => e !== "")
                    .map(e => `${prefix}${e}`)
            } else {
                prefix += ch
            }
        }
        return [inp]
    }

    // [Annotation] -> [Annotation] 
    __mergeDuplicateAnnotations(oldAnnotations) {
        if (oldAnnotations == null || oldAnnotations.length === 0) {
            return oldAnnotations
        }

        // str -> [str]
        const unfold = (a) => this.__unfoldWildcard(a.type.name)
            .map(s => {
                const newAnnotation = clone(a);
                newAnnotation.type.name = s
                return newAnnotation
            })

        for (let sublist of oldAnnotations.map(unfold)) {
            for (let item of sublist) {
                // item
            }
        }

        oldAnnotations = oldAnnotations.map(unfold).flat()
        const compare = (a, b) => {
            return a.type.name.localeCompare(b.type.name)
        }

        const typeToAnnotationsMap = this.__groupBy(oldAnnotations.sort(compare), ann => ann.type.name)
        const newAnnotations = []
        for (let [_, annotations] of typeToAnnotationsMap) {
            newAnnotations.push(annotations.reduce(this.__mergeAnnotations))
        }

        return newAnnotations;
    }

    __isNegated(ctx) {
        const isNegated = ctx.parentCtx.constructor.name.endsWith("ExpressionNoContext")
        if (isNegated) return true;

        let temp = ctx
        while (temp.parentCtx.constructor.name.endsWith("ExpressionAggregateContentsContext") === true) {
            temp = temp.parentCtx
        }

        return temp.parentCtx.constructor.name.endsWith("ExpressionNoneOfContext")
    }

    getJavaClass() {
        const type = this.__initial.type
        const node = this.__initial.node
        if (type === 'class') {
            node.annotations = this.__mergeDuplicateAnnotations(node.annotations)
            if (node.method) {
                node.method.annotations = this.__mergeDuplicateAnnotations(node.method.annotations)
                node.method.parameters = this.__mergeDuplicateParameters(node.method.parameters)
            }
            if (node.field) {
                node.field.annotations = this.__mergeDuplicateAnnotations(node.field.annotations)
            }
            return node;
        } else if (type === 'function') {
            node.annotations = this.__mergeDuplicateAnnotations(node.annotations)
            node.parameters = this.__mergeDuplicateParameters(node.parameters)
            return new JavaClass([], null, [], null, node, null, null, null)
        } else if (type === 'field') {
            node.annotations = this.__mergeDuplicateAnnotations(node.annotations)
            return new JavaClass([], null, [], node, null, null, null, null)
        }
        return null;
    }

    enterMust(ctx) {
        this.__is_antecedent = false
        this.__stack.push({
            'comingFrom': this.__initial['type'],
            'node': this.__initial['node']
        })
    }

    enterClasses(ctx) {
        if (this.__stack.length === 0) {
            this.__initial = {
                'node': new JavaClass([], null, [], null, null, null, null),
                'type': 'class'
            }
            this.__stack.push({
                'comingFrom': 'class',
                'node': this.__initial['node']
            })
        } else { }
    }

    exitClasses(ctx) { this.__stack.pop() }

    enterAnnotations(ctx) {
        let negated = this.__isNegated(ctx)

        let annotationType = null;
        try {
            annotationType = this.initObj(
                new Type(ctx.annotationCondition().combinatorialWords().getText().replaceAll('"', ""))
            )
            annotationType.negated = negated
        } catch (error) { }

        const annotation = this.initObj(new Annotation(annotationType, []))

        const prev = this.peekStack()
        if (['class', 'function', 'field', 'parameter'].includes(prev.comingFrom)) {
            prev.node.annotations.push(annotation)
            // we    parent->result
            // T     T -> F
            // F     F -> F
            // T     F -> T
            // F     T -> T
            // basic idea is that if there are 2 negations, then they cancel each other out
            annotation.negated = prev.node.negated ^ negated
        }

        this.__stack.push({
            comingFrom: 'annotation',
            node: annotation
        })
    }

    exitAnnotations(ctx) { this.__stack.pop() }

    enterExtensions(ctx) {
        let negated = this.__isNegated(ctx)
        const prev = this.peekStack()

        if (prev.comingFrom === 'class') {
            const extendedClass = ctx.extensionCondition().combinatorialWords().getText().replaceAll('"', "")
            prev.node.extendedClass = this.initObj(new Type(extendedClass))
            prev.node.extendedClass.negated = prev.node.negated ^ negated;
        }
    }

    enterImplementations(ctx) {
        let negated = this.__isNegated(ctx)
        const prev = this.peekStack()

        if (prev.comingFrom === 'class') {
            const implementedInterface = ctx.implementationCondition().combinatorialWords().getText().replaceAll('"', "")
            const interfaceClazz = this.initObj(new Type(implementedInterface));
            interfaceClazz.negated  = prev.node.negated ^ negated
            prev.node.implementedInterfaces.push(interfaceClazz)
            
        }
    }

    enterTypes(ctx) {
        let negated = this.__isNegated(ctx)

        let type = ctx.typeCondition().combinatorialWords()
        type = this.initObj(new Type(type.getText().replaceAll('"', "")))

        const prev = this.peekStack()
        if (['parameter', 'field', 'property'].includes(prev.comingFrom)) {
            prev.node.type = type
            type.negated = prev.node.negated ^ negated
        }
    }

    enterReturnTypes(ctx) {
        let negated = this.__isNegated(ctx)
        let type = ctx.returnTypeCondition().combinatorialWords()
        type = this.initObj(new Type(type.getText().replaceAll('"', "")))

        const prev = this.peekStack()
        if (prev.comingFrom === 'function') {
            prev.node.returnType = type
            type.negated = prev.node.negated ^ negated
        }
    }

    enterAnnotationParameters(ctx) {
        let negated = this.__isNegated(ctx)
        let words = ctx.annotationParameterCondition().combinatorialWords()
        let param = new AnnotationParam(null, null, null)
        if (words != null || words != undefined) {
            const elements = words.getText().replaceAll('"', "").split(" ")
            const len = elements.length
            let type_ = null;
            let name_ = null;
            if (len >= 2) {
                type_ = elements[0]
                name_ = elements[1]
            } else if (len === 1) {
                name_ = elements[0]
            }

            type_ = type_ != null ? this.initObj(new Type(type_)) : null
            param = new AnnotationParam(type_, name_, null)
        }

        param = this.initObj(param)
        param.negated = negated;
        const prev = this.peekStack()

        if (prev.comingFrom === 'annotation') {
            prev.node.parameters.push(param)
            param.negated = prev.node.negated ^ negated
        }

        this.__stack.push({
            'comingFrom': 'parameter',
            'node': param
        })
    }

    exitAnnotationParameters(ctx) { this.__stack.pop(); }

    enterFunctionParameters(ctx) {
        let negated = this.__isNegated(ctx)
        const words = ctx.functionParameterCondition().combinatorialWords()
        let param = new MethodParam(null, null, [])
        if (words != null || words != undefined) {
            const elements = words.getText().replaceAll('"', "").split(" ")
            const len = elements.length
            let type_ = '?'
            let name_ = null
            if (len >= 2) {
                type_ = elements[0]
                name_ = elements[1]
            } else if (len == 1) {
                type_ = elements[0]
            }

            type_ = this.initObj(new Type(type_))
            param = new MethodParam(type_, name_, [])
        }

        param = this.initObj(param)
        param.negated = negated;
        const prev = this.peekStack()

        if (prev.comingFrom === 'function') {
            prev.node.parameters.push(param)
            param.negated = prev.node.negated ^ negated
        }

        this.__stack.push({
            'comingFrom': 'parameter',
            'node': param
        })
    }

    exitFunctionParameters(ctx) { this.__stack.pop(); }

    enterFunctions(ctx) {
        let negated = this.__isNegated(ctx)
        let method = null;
        if (this.__stack.length > 0) {
            const prev = this.peekStack()
            if (prev.comingFrom === 'class') {
                const classMethod = prev.node.method
                if (classMethod == null) {
                    method = this.initObj(
                        new Method(new Type("void"), [], [], null)
                    )
                } else {
                    method = classMethod
                }
                prev.node.method = method
                method.negated = prev.node.negated ^ negated
            }
        } else {
            if (this.__is_antecedent) {
                // if the rule starts with 'function'
                this.__initial = {
                    'node': new Method(new Type("void"), [], [], null),
                    'type': 'function'
                }
            }
            method = this.__initial.node
        }

        if (method != null) {
            if (method.negated == undefined) {
                method.negated = negated;
            }
            this.__stack.push({
                'comingFrom': 'function',
                'node': method
            })
        }
    }

    exitFunctions(ctx) { this.__stack.pop(); }

    enterDeclarationStatements(ctx) {
        let negated = this.__isNegated(ctx)
        let field = null;
        if (this.__stack.length > 0) {
            const prev = this.peekStack()
            if (prev.comingFrom === 'class') {
                const classField = prev.node.field
                if (classField == null) {
                    field = new Field(new Type("Object"), [], null)
                } else {
                    field = classField
                }
                prev.node.field = field
                field.negated = prev.node.negated ^ negated
            }
        } else {
            if (this.__is_antecedent) {
                // if the rule starts with 'field'
                this.__initial = {
                    'node': this.initObj(new Field(new Type("Object"), [], null)),
                    'type': 'field'
                }
            }
            field = this.__initial.node
        }

        if (field != null) {
            field.negated = negated;
            this.__stack.push({
                'comingFrom': 'field',
                'node': field
            })
        }
    }

    exitDeclarationStatements(ctx) { this.__stack.pop(); }

    enterNames(ctx) {
        const name = ctx.nameCondition().combinatorialWords().getText().replaceAll('"', "")
        const prev = this.peekStack()
        if (['parameter', 'property'].includes(prev.comingFrom)) {
            prev.node.name = name
        }
    }

    enterValues(ctx) {
        const value = ctx.valueCondition().combinatorialWords().getText().replaceAll('"', "")
        const prev = this.peekStack()
        if (['parameter', 'property'].includes(prev.comingFrom)) {
            prev.node.value = value
        }
    }

    enterConfigurationFiles(ctx) {
        const negated = this.__isNegated(ctx);

        const configFile = this.initObj(new ConfigurationFile("microprofile-config.properties", []))
        const prev = this.peekStack()

        if (['class', 'field', 'function'].includes(prev.comingFrom)) {
            prev.node.configurationFile = configFile;
            configFile.negated = prev.node.negated ^ negated
        }
        this.__stack.push({
            'comingFrom': 'config-file',
            'node': configFile
        })
    }

    exitConfigurationFiles(ctx) { this.__stack.pop(); }

    enterConfigurationProperties(ctx) {
        let negated = this.__isNegated(ctx)
        const prop = this.initObj(new ConfigurationProperty(null, null, null))
        prop.negated =  negated
        const text = ctx.configurationPropertyCondition().combinatorialWords()

        if (text != null || text != undefined) {
            const elements = text.getText().replaceAll('"', "").split(" ")
            const len = elements.length
            let type_ = null;
            let name_ = null;
            if (len >= 2) {
                type_ = elements[0]
                name_ = elements[1]
            } else if (len == 1) {
                name_ = elements[0]
            }
            prop.name = name_
            prop.type = this.initObj(new Type(type_))
            prop.type = negated;
        }

        const prev = this.peekStack()
        if (prev.comingFrom === 'config-file') {
            prev.node.properties.push(prop)
            prop.negated = prev.node.negated ^ negated
        }

        this.__stack.push({
            'comingFrom': 'property',
            'node': prop
        })
    }

    exitConfigurationProperties(ctx) { this.__stack.pop(); }

    enterBeans(ctx) {
        const negated = this.__isNegated(ctx)
        const beanDecl = this.initObj(new BeanDeclaration("beans.xml", true))

        const prev = this.peekStack()
        if (prev.comingFrom === 'class') {
            prev.node.declaredInBeans = beanDecl
            beanDecl.negated = prev.node.negated ^ negated
        }
    }

    enterBeansFile(ctx) {
        const negated = this.__isNegated(ctx);
        const beanDecl = this.initObj(new BeanDeclaration("beans.xml", false))

        const prev = this.peekStack()
        if (prev.comingFrom === 'class') {
            prev.node.declaredInBeans = beanDecl
            beanDecl.negated = prev.node.negated ^ negated
        }
    }

    enterOverriddenFunctions(ctx) {
        let negated = this.__isNegated(ctx)
        const methodSignature = ctx.combinatorialWords().getText().replaceAll('"', "")
        // Example: foobar(String, int, double, Custom)
        // Example: foobar(String)
        // Example: foobar()
        const lparenPos = methodSignature.indexOf("(");
        const rparenPos = methodSignature.lastIndexOf(")");
        if (lparenPos === -1 || rparenPos === -1) {
            // error
        } else {
            const methodName = methodSignature.slice(0, lparenPos);
            const parameters = methodSignature
                                    .slice(lparenPos + 1, rparenPos)
                                    .split(",")
                                    .map(e => e.trim())
                                    .filter(e => e.length > 0)
                                    .map(p => this.initObj(new MethodParam(this.initObj(new Type(p)), null, [])))
                                    .map(mp => {
                                        mp.negated = negated; // TODO: I do not like mutations inside maps
                                        return mp
                                    })

            const prev = this.peekStack()
            if (prev.comingFrom === 'class') {
                prev.node.overriddenMethod = this.initObj(new Method(new Type("T"), parameters, [], [], methodName))
                prev.node.overriddenMethod.negated = prev.node.negated ^ negated
            }
        }
    }

    initObj(obj) {
        obj.isAntecedent = this.__is_antecedent
        return obj;
    }

    peekStack() {
        return this.__stack[this.__stack.length - 1]
    }


}
