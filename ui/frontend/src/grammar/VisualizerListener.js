import RulepadGrammarListener from "./RulepadGrammarListener";
import clone from 'just-clone'

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
    constructor(returnType, parameters, annotations, configurationFile) {
        super()
        this.returnType = returnType == undefined ? new Type("void") : returnType
        this.parameters = parameters == undefined ? [] : parameters
        this.annotations = annotations == undefined ? [] : annotations
        this.configurationFile = configurationFile
    }
}

class JavaClass extends AntecedentOrConsequent {
    constructor(annotations, extendedClass, implementedInterfaces, field, method, configurationFile, declaredInBeans) {
        super()
        this.extendedClass = extendedClass
        this.annotations = annotations == undefined ? [] : annotations
        this.implementedInterfaces = implementedInterfaces == undefined ? [] : implementedInterfaces
        this.method = method
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
        console.log(oldParams, newParameters)
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
            return new JavaClass([], null, [], null, node, null, null)
        } else if (type === 'field') {
            node.annotations = this.__mergeDuplicateAnnotations(node.annotations)
            return new JavaClass([], null, [], node, null, null, null)
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
                'node': new JavaClass([], null, [], null, null, null),
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
        let annotationType = null;
        try {
            annotationType = this.initObj(
                new Type(ctx.annotationCondition().combinatorialWords().getText().replaceAll('"', ""))
            )
        } catch (error) { }

        const annotation = this.initObj(new Annotation(annotationType, []))

        const prev = this.peekStack()

        if (['class', 'function', 'field', 'parameter'].includes(prev.comingFrom)) {
            prev.node.annotations.push(annotation)
        }

        this.__stack.push({
            'comingFrom': 'annotation',
            'node': annotation
        })
    }

    exitAnnotations(ctx) { this.__stack.pop() }

    enterExtensions(ctx) {
        const prev = this.peekStack()

        if (prev.comingFrom === 'class') {
            const extendedClass = ctx.extensionCondition().combinatorialWords().getText().replaceAll('"', "")
            prev.node.extendedClass = this.initObj(new Type(extendedClass))
        }
    }

    enterImplementations(ctx) {
        const prev = this.peekStack()

        if (prev.comingFrom === 'class') {
            const implementedInterface = ctx.implementationCondition().combinatorialWords().getText().replaceAll('"', "")
            prev.node.implementedInterfaces.push(this.initObj(new Type(implementedInterface)))
        }
    }

    enterTypes(ctx) {
        let type = ctx.typeCondition().combinatorialWords()
        type = this.initObj(new Type(type.getText().replaceAll('"', "")))

        const prev = this.peekStack()
        if (['parameter', 'field', 'property'].includes(prev.comingFrom)) {
            prev.node.type = type
        }
    }

    enterReturnTypes(ctx) {
        let type = ctx.returnTypeCondition().combinatorialWords()
        type = this.initObj(new Type(type.getText().replaceAll('"', "")))

        const prev = this.peekStack()
        if (prev.comingFrom === 'function') {
            prev.node.returnType = type
        }
    }

    enterAnnotationParameters(ctx) {
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
        const prev = this.peekStack()

        if (prev.comingFrom === 'annotation') {
            prev.node.parameters.push(param)
        }

        this.__stack.push({
            'comingFrom': 'parameter',
            'node': param
        })
    }

    exitAnnotationParameters(ctx) { this.__stack.pop(); }

    enterFunctionParameters(ctx) {
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
        const prev = this.peekStack()

        if (prev.comingFrom === 'function') {
            prev.node.parameters.push(param)
        }

        this.__stack.push({
            'comingFrom': 'parameter',
            'node': param
        })
    }

    exitFunctionParameters(ctx) { this.__stack.pop(); }

    enterFunctions(ctx) {
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
            }
        } else {
            if (this.__is_antecedent) {
                // if the rule starts with 'function'
                this.__initial = {
                    'node': this.initObj(new Method(new Type("void"), [], [], null)),
                    'type': 'function'
                }
            }
            method = this.__initial.node
        }

        if (method != null) {
            this.__stack.push({
                'comingFrom': 'function',
                'node': method
            })
        }
    }

    exitFunctions(ctx) { this.__stack.pop(); }

    enterDeclarationStatements(ctx) {
        let field = null;
        if (this.__stack.length > 0) {
            const prev = this.peekStack()
            if (prev.comingFrom === 'class') {
                const classField = prev.node.field
                if (classField == null) {
                    field = this.initObj(
                        new Field(new Type("Object"), [], null)
                    )
                } else {
                    field = classField
                }
                prev.node.field = field
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
        const configFile = this.initObj(new ConfigurationFile("microprofile-config.properties", []))

        const prev = this.peekStack()

        if (['class', 'field', 'function'].includes(prev.comingFrom)) {
            prev.node.configurationFile = configFile;
        }
        this.__stack.push({
            'comingFrom': 'config-file',
            'node': configFile
        })
    }

    exitConfigurationFiles(ctx) { this.__stack.pop(); }

    enterConfigurationProperties(ctx) {
        const prop = this.initObj(new ConfigurationProperty(null, null, null))
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
        }

        const prev = this.peekStack()
        if (prev.comingFrom === 'config-file') {
            prev.node.properties.push(prop)
        }

        this.__stack.push({
            'comingFrom': 'property',
            'node': prop
        })
    }

    exitConfigurationProperties(ctx) { this.__stack.pop(); }

    enterBeans(ctx) {
        const beanDecl = this.initObj(new BeanDeclaration("beans.xml", true))

        const prev = this.peekStack()
        if (prev.comingFrom === 'class') {
            prev.node.declaredInBeans = beanDecl
        }
    }

    enterBeansFile(ctx) {
        const beanDecl = this.initObj(new BeanDeclaration("beans.xml", false))

        const prev = this.peekStack()
        if (prev.comingFrom === 'class') {
            prev.node.declaredInBeans = beanDecl
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

const ANTECEDENT_SIGN_START = `<span class="antecedent" title="Antecedent">`
const ANTECEDENT_SIGN_END = "</span>"
const CONSEQUENT_SIGN_START = `<span class="consequent" title="Consequent">`
const CONSEQUENT_SIGN_END = "</span>"

const TEMPLATE = `
<ClassAnnotations>
class Foo <ExtendsTemplate><ImplementsTemplate> {
<FieldDeclaration><MethodDeclaration>
}`

// Type -> str
function shortenTypeName(type) {
    if (type == null || type.name == null) {
        return null
    }

    const pieces = type.name.split(".")
    if (pieces.length > 1) {
        // simple name
        return pieces.filter(p => p[0] === p[0].toUpperCase()).join(".")
    }
    return type.name
}

// (AntecedentOrConsequent, str) -> str
function addSigns(obj, str) {
    if (obj.isAntecedent == null) {
        return str
    }
    const [start, end] = obj.isAntecedent ? [ANTECEDENT_SIGN_START, ANTECEDENT_SIGN_END] : [CONSEQUENT_SIGN_START, CONSEQUENT_SIGN_END]
    return `${start}${str}${end}`
}

// Field -> str
function field(field) {
    if (field == null) {
        return ""
    }
    const t = "\t<FieldAnnotations>\n\tprivate <ReturnType> field;"
    const annos = handleAnnotations(field.annotations, "\t").trim()
    return t
        .replace("<FieldAnnotations>", annos)
        .replace("<ReturnType>", addSigns(field.type, shortenTypeName(field.type)))
}

// Method -> str
function functionParameters(method) {
    if (method.parameters.length === 0) {
        return ""
    }

    const functionParameter = (param, ix) => {
        const annoStr = param.annotations ? handleAnnotations(param.annotations).split("\n").join(" ") : ""
        const typeName = shortenTypeName(param.type)
        const name = param.name ? param.name : `p${ix + 1}`
        return addSigns(param, `${annoStr}${typeName} ${name}`)
    }

    return method.parameters.map(functionParameter).join(", ")
}

// Method -> str
function method(method) {
    if (method) {
        const t = "\t<MethodAnnotations>\n\tpublic <ReturnType> method(<FunctionParameters>) {}"
        const annos = handleAnnotations(method.annotations, "\t").trim()
        const params = functionParameters(method)
        return t.replace("<MethodAnnotations>", annos)
            .replace("<ReturnType>", addSigns(method.returnType, shortenTypeName(method.returnType)))
            .replace("<FunctionParameters>", params)
    }
    return ""
}


function extendz(extendedClass) {
    if (extendedClass) {
        return `extends ${addSigns(extendedClass, shortenTypeName(extendedClass))}`
    }
    return ""
}

function implementz(interfaces) {
    const interfaceStr = (i) => addSigns(i, shortenTypeName(i))

    if (interfaces.length == 0) {
        return ""
    }

    return `implements ${interfaces.map(interfaceStr).join(", ")}`
}

// ConfigurationProperty|AnnotationParam -> str
function paramToString(p) {
    let name = "?"
    let value;
    if (p.name) {
        name = p.name
    }
    if (p.value == null) {
        if (p.type == null || p.type.name == null) {
            value = "?"
        } else {
            value = shortenTypeName(p.type)
        }
    } else {
        value = p.value.trim()
    }

    return `${name}=${value}`
}

function handleAnnotations(annotations, ch = "") {
    const annotation = (a) => {
        let result = `@${shortenTypeName(a.type)}`
        if (a.parameters.length > 0) {
            const params = a.parameters.map(p => addSigns(p, paramToString(p))).join(",")
            result = `${result}(${params})`
        }
        return addSigns(a, result)
    }

    return annotations.map(annotation).join(`\n${ch}`)
}

// BeanDeclaration -> [str, str]/[name, lines]
function beanDeclaration(bd) {
    if (bd == null) {
        return null
    }

    let body = '&lt;!--empty--&gt;'
    if (bd.declared) {
        body = '&lt;bean id="..." class="Foo" /&gt;'
    }
    const lines = `
&lt;beans&gt;
BODY
&lt;/beans&gt;
    `.trimStart().replace("BODY", body)

    return [bd.name, lines]
}

// ConfigurationFile -> [str, str]/[name, lines]
function configFiles(cf) {
    if (cf == null) return null

    const lines = cf.properties.map(paramToString).join("\n")
    return [cf.name, lines]
}

// JavaClass -> [{str -> str}]/List[{filename, code}]
function configurationFiles(clazz) {
    const extractConfigurationObj = (obj) => {
        // JavaClass ->JavaClass | Method | Field
        if (obj.configurationFile) {
            return obj
        } else if (obj.field && obj.field.configurationFile) {
            return obj.field
        } else if (obj.method && obj.method.configurationFile) {
            return obj.method
        }
        return null
    }

    const confObj = extractConfigurationObj(clazz);
    const bd = beanDeclaration(clazz.declaredInBeans)
    let configs = [bd]
    if (confObj) {
        const cf = configFiles(confObj.configurationFile)
        configs = [cf, bd]
    }

    return configs.filter(x => x != null).map(([filename, code]) => {
        return {
            filename,
            code
        }
    })
}

function javaClassToString(clazz) {
    return TEMPLATE
        .replace("<ClassAnnotations>", handleAnnotations(clazz.annotations))
        .replace("<FieldDeclaration>", field(clazz.field))
        .replace("<MethodDeclaration>", method(clazz.method))
        .replace("<ExtendsTemplate>", extendz(clazz.extendedClass))
        .replace("<ImplementsTemplate>", implementz(clazz.implementedInterfaces))
}

export function stringifyClass(clazz) {
    return [javaClassToString(clazz), configurationFiles(clazz)]
}