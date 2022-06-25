import antlr4 from 'antlr4';
import { onelineify } from './formatter';
import RulepadGrammarLexer from './generated/RulepadGrammarLexer'
import RulepadGrammarParser from './generated/RulepadGrammarParser'
import VisualizerListener from './VisualizerListener';

const ANTECEDENT_SIGN_START = `<span class="antecedent" title="Antecedent">`
const ANTECEDENT_SIGN_END = "</span>"
const CONSEQUENT_SIGN_START = `<span class="consequent" title="Consequent">`
const CONSEQUENT_SIGN_END = "</span>"

const TEMPLATE = `
<ClassAnnotations>
class Foo <ExtendsTemplate><ImplementsTemplate> {
<FieldDeclaration>
<MethodDeclaration>
<OverriddenMethodDeclaration>
}`

// Type -> str
function shortenTypeName(type, defaultVal=null) {
    if (type == null || type.name == null) {
        return defaultVal
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
    const negated = obj.negated ? obj.negated : false;
    const [start, end] = obj.isAntecedent ? [ANTECEDENT_SIGN_START, ANTECEDENT_SIGN_END] : [CONSEQUENT_SIGN_START, CONSEQUENT_SIGN_END]
    const result = `${start}${str}${end}`
    if (negated) {
        return `<span class="negated">${result}</span>`
    } 
    return result;
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
        const typeName = shortenTypeName(param.type, "?")
        const name = param.name ? param.name : `p${ix + 1}`
        return addSigns(param, `${annoStr.trim()} ${typeName.trim()} ${name.trim()}`)
    }

    return method.parameters.map(functionParameter).join(", ")
}

// Method -> str
function method(method, accessModifiedStr = "public ") {
    if (method) {
        const t = `\t<MethodAnnotations>\n\t${accessModifiedStr}<ReturnType> <MethodName>(<FunctionParameters>) {}`
        const annos = handleAnnotations(method.annotations, "\t").trim()
        const params = functionParameters(method)
        return t
            .replace("<MethodAnnotations>", annos)
            .replace("<ReturnType>", addSigns(method.returnType, shortenTypeName(method.returnType)))
            .replace("<FunctionParameters>", params)
            .replace("<MethodName>", method.name == null ? "foo" : addSigns(method, method.name))
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

    return ` implements ${interfaces.map(interfaceStr).join(", ")}`
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
            // result = `${result}(${params})`
            return addSigns(a, result+"(") + params + addSigns(a, ")")
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

    const lines = cf.properties.map(p => addSigns(p, paramToString(p))).join("\n")
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
        .replace("<OverriddenMethodDeclaration>", method(clazz.overriddenMethod, "@Override\n\tpublic "))
        .replace("<ExtendsTemplate>", extendz(clazz.extendedClass))
        .replace("<ImplementsTemplate>", implementz(clazz.implementedInterfaces)).trim()
}

function stringifyClass(clazz) {
    const lines = javaClassToString(clazz).split(/\r?\n/)

    const newLines = []

    let prevWasEmpty = false;

    for (let line of lines) {
        const lineIsEmpty = line.trim().length === 0
        if (!(lineIsEmpty && prevWasEmpty)) {
            newLines.push(line)
        }
        prevWasEmpty = lineIsEmpty;
    }

    return [newLines.join("\n"), configurationFiles(clazz)]
}

function resultWrapper(data) {
    if (data == null) {
        return {
            status: "failure",
            data: null
        }
    }
    return {
        status: "success",
        data: data
    }
}

export function visualize(input) {
    try {
        const chars = new antlr4.InputStream(onelineify(input));
        const lexer = new RulepadGrammarLexer(chars);
        const tokens = new antlr4.CommonTokenStream(lexer);
        const parser = new RulepadGrammarParser(tokens);
        parser.buildParseTrees = true;

        const tree = parser.start();
        const visualizer = new VisualizerListener();
        antlr4.tree.ParseTreeWalker.DEFAULT.walk(visualizer, tree);
        const jc = visualizer.getJavaClass()
        return resultWrapper(stringifyClass(jc))
    } catch (error) {
        console.error(error)
        return resultWrapper(null)
    }
}