from typing import Dict, Union
from format.model import *
from dataclasses import dataclass

def removeNones(iter):
    return filter(lambda x: x is not None, iter)


@dataclass
class JsonRule:
    id: int
    antecedent: List[str]
    consequent: List[str]


def typeToRulePad(t: Type) -> str:
    return f"type \"{t.name}\""


def paramToRulePad(p: Union[Param, AnnotationParam, ConfigurationProperty]) -> str:
    keyword = "parameter" if isinstance(p, Param) else "property"
    name = f"{p.name}" if p.name else ""
    form = " ".join(removeNones(
        [p.type.name if p.type else None, name])).strip()

    withAnnotation = ""
    if isinstance(p, Param) and p.annotations:
        anno_str = " and ".join(map(annotationToRulePad, p.annotations))
        if len(p.annotations) > 1:
            anno_str = "(" + anno_str + " )"

        withAnnotation = f" with {anno_str}"

    return f"{keyword} \"{form}\"{withAnnotation}"


def annotationToRulePad(a: Annotation):
    res = f"annotation \"{a.type.name}\""
    if a.parameters:
        param_str = " and ".join(map(paramToRulePad, a.parameters))
        res = res + " with " + param_str
    return res


def fieldToRulePad(f: Field) -> str:
    anno_str, type_str = None, None
    if f.annotations:
        anno_str = " and ".join(map(annotationToRulePad, f.annotations))
        if len(f.annotations) > 1:
            anno_str = "(" + anno_str + " )"
    if f.type:
        type_str = typeToRulePad(f.type)
    field_pieces = " and ".join(removeNones([anno_str, type_str]))
    return f"(field with {field_pieces} )"


def methodToRulePad(f: Method) -> str:
    anno_str, type_str, param_str = None, None, None
    if f.annotations:
        anno_str = " and ".join(map(annotationToRulePad, f.annotations))
        if len(f.annotations) > 1:
            anno_str = "(" + anno_str + " )"
    if f.returnType:
        type_str = f"return {typeToRulePad(f.returnType)}"
    if f.parameters:
        param_str = (" and ".join(map(paramToRulePad, f.parameters)))
        if len(f.parameters) > 1:
            param_str = "(" + param_str + " )"
    method_pieces = list(removeNones([anno_str, type_str, param_str]))
    tmp = " and ".join(method_pieces)
    return f"(method with {tmp} )"


def configToRulePad(cf: ConfigurationFile) -> str:
    # TODO: add name support
    prop_str = None
    if cf.properties:
        prop_str = " and ".join(map(paramToRulePad, cf.properties))
        if len(cf.properties) > 1:
            prop_str = "(" + prop_str + " )"
    if prop_str:
        return f"configuration file with {prop_str}"


def classToRulePad(clazz: JavaClass) -> str:
    extends, implements, field, method, cf, anno = [None] * 6
    # extension
    if clazz.extendedClass:
        extends = f"extension of \"{clazz.extendedClass.name}\""
    # implementation
    if clazz.implementedInterfaces:
        implements = " and ".join(map(lambda x: f"implementation of \"{x.name}\"",
                                      clazz.implementedInterfaces))
        if len(clazz.implementedInterfaces) > 1:
            implements = f"({implements} )"
    # field
    if clazz.field:
        field = fieldToRulePad(clazz.field)
    # method
    if clazz.method:
        method = methodToRulePad(clazz.method)
    # config
    if clazz.configurationFile:
        cf = configToRulePad(clazz.configurationFile)
    # annotation
    if clazz.annotations:
        anno = " and ".join(map(annotationToRulePad, clazz.annotations))
        if len(clazz.annotations) > 1:
            anno = "(" + anno + " )"
    class_pieces = list(removeNones(
        [extends, implements, field, method, cf, anno]))
    if len(class_pieces) >= 2:
        tmp = " and ".join(class_pieces)
        return f"class with {tmp}"
    else:
        for v in class_pieces:
            if v is not None:
                return f"class with {v}"


def toRulePad(element: Union[JavaClass, Field, Method, ConfigurationFile]):
    types = {
        JavaClass: classToRulePad,
        Field: fieldToRulePad,
        Method: methodToRulePad,
        ConfigurationFile: configToRulePad
    }

    for type, func in types.items():
        if isinstance(element, type):
            return func(element)


def removeParenthesis(st):
    tmp = st.strip()
    if tmp[0] == "(" and tmp[-1] == ")":
        return tmp[1:-1]
    return st


def toJavaConstruct(facts: List[str], antecedentConstruct: Union[JavaClass, Field, Method]) -> Union[JavaClass, Field, Method, ConfigurationFile]:
    field = Field(type=None, annotations=[], configurationFile=None)
    method = Method(returnType=None, parameters=[],
                    annotations=[], configurationFile=None)
    clazz = JavaClass(
        annotations=[], extendedClass=None, implementedInterfaces=[], field=None,
        method=None, configurationFile=None, declaredInBeans=None
    )
    configFile = ConfigurationFile(None, [])

    has_class, has_method, has_field, has_config = [False] * 4

    # 'annotation_name': Annotation() object
    all_annotations: Dict[str, Annotation] = dict()

    # 'annotation_name': List[Param] object
    all_annotation_params: Dict[str, List[Param]] = dict()

    def extractAnnotation(annotation_str):
        annotation_type = annotation_str.split("_")[1]
        if annotation_type not in all_annotations:
            all_annotations[annotation_type] = Annotation(
                Type(annotation_type), parameters=[])
        return all_annotations[annotation_type]

    # 'param_type': Param() object
    method_parameters: Dict[str, Param] = dict()

    # 'param_type': List[Annotation] object
    method_parameter_annotations: Dict[str, List[Annotation]] = dict()

    for fact in facts:
        str_target, str_operation, str_related = fact.strip().split()
        if str_target == "Class":
            has_class = True
            if "annotatedWith" in str_operation:
                clazz.annotations.append(extractAnnotation(str_related))
            elif "extends" in str_operation or "implements" in str_operation:
                class_name = str_related.split("_")[1]
                t = Type(class_name)
                if "extends" in str_operation:
                    clazz.extendedClass = t
                else:
                    clazz.implementedInterfaces.append(t)
        elif str_target in ["Field", "FieldTypeDecl"]:
            has_field = True
            if "annotatedWith" in str_operation:
                field.annotations.append(extractAnnotation(str_related))
            elif "hasType" in str_operation:
                field.type = Type(str_related)
        elif str_target == "Method":
            has_method = True
            if "annotatedWith" in str_operation:
                method.annotations.append(extractAnnotation(str_related))
            elif "hasType" in str_operation or "hasReturnType" in str_operation:
                method.returnType = Type(str_related)
            elif "hasParam" in str_operation:
                _type = str_related.split("_")[1]
                p = Param(Type(_type), None, [])
                method_parameters[_type] = p
                method.parameters.append(p)
        elif str_target.startswith("Annotation_") and "hasParam" in str_operation:
            annotation_type = str_target.strip().split("_")[1]
            if annotation_type not in all_annotation_params:
                all_annotation_params[annotation_type] = []
            _name, _typeStr = str_related.split("_")[1].split(":")
            _type = Type(_typeStr.strip()) if _typeStr.strip() else None
            all_annotation_params[annotation_type].append(
                Param(_type, _name, []))
        elif "definedIn" in str_operation and str_related.startswith("ConfigFile"):
            has_config = True
            _name, _type = str_target.split("_")[1].split(":")
            cp = ConfigurationProperty(_name, Type(_type), None)
            configFile.properties.append(cp)
            configFile.name = str_related.split("_")[1]
        elif "annotatedWith" in str_operation and str_target.startswith("Param"):
            has_method = True
            param_type = str_target.split("_")[1]
            annotation_type = Annotation(Type(str_related.split("_")[1]), [])
            if param_type not in method_parameter_annotations:
                method_parameter_annotations[param_type] = []
            method_parameter_annotations[param_type].append(annotation_type)

    # Handling Dangling Annotations
    danglingAnnotations: List[Annotation] = []

    for annotation_str, params in all_annotation_params.items():
        if annotation_str in all_annotations:
            all_annotations[annotation_str].parameters = params
        else:
            danglingAnnotation = Annotation(Type(annotation_str), params)
            danglingAnnotations.append(danglingAnnotation)

    for da in danglingAnnotations:
        t = findAnnotationParentType(antecedentConstruct, da.type.name)
        if t is JavaClass:
            has_class = True
            clazz.annotations.append(da)
        elif t is Method:
            has_method = True
            method.annotations.append(da)
        elif t is Field:
            has_field = True
            field.annotations.append(da)

    # Handling method parameter annotations
    danglingParametersWithAnnotations = []
    for param_type, __annotations in method_parameter_annotations.items():
        if param_type in method_parameters:
            method_parameters[param_type].annotations.extend(__annotations)
        else:
            danglingParametersWithAnnotations.append(
                Param(Type(param_type), None, __annotations))

    if danglingParametersWithAnnotations and has_method:
        method.parameters.append(danglingParametersWithAnnotations)

    # determine what to return based on the input
    if has_class or (has_field and has_method):
        # when class is present or more than 2 elements which need to be in a class are present
        if has_method:
            clazz.method = method
        if has_field:
            clazz.field = field
        if has_config:
            clazz.configurationFile = configFile
        return clazz
    elif has_method:
        # when only a method is available
        if has_config:
            clazz.configurationFile = configFile
        return method
    elif has_field:
        # when only a field is available
        if has_config:
            clazz.configurationFile = configFile
        return field
    elif has_config:
        # when only a configuration file is available
        return configFile


def findAnnotationParentType(container, annotation_str):
    if type(container) in [Method, Field]:
        for a in container.annotations:
            if a.type.name == annotation_str:
                return type(container)
    elif type(container) is JavaClass:
        for a in container.annotations:
            if a.type.name == annotation_str:
                return JavaClass
        if container.field:
            for a in container.field.annotations:
                if a.type.name == annotation_str:
                    return Field
        if container.method:
            for a in container.method.annotations:
                if a.type.name == annotation_str:
                    return Method


def toShortRulePad(jsonRule: JsonRule) -> str:
    ant = toJavaConstruct(jsonRule.antecedent, None)
    con = toJavaConstruct(jsonRule.consequent, ant)

    ant_str = removeParenthesis(toRulePad(ant))
    con_str = removeParenthesis(toRulePad(con))
    dependent_types = [Field, Method, ConfigurationFile]
    if type(ant) == type(con):
        con_str = con_str[con_str.index("with")+4+1:]
    elif isinstance(ant, JavaClass) and type(con) in dependent_types:
        con_str = con_str
    elif isinstance(con, JavaClass) and type(ant) in dependent_types:
        ant_str = f"class with {ant_str}"
        con_str = con_str[con_str.index("with")+4+1:]
    elif type(ant) in dependent_types and type(con) in dependent_types:
        if isinstance(ant, Field) and isinstance(con, ConfigurationFile) or \
                isinstance(ant, Method) and isinstance(con, ConfigurationFile):
            pass
        else:
            ant_str = f"class with {ant_str}"
    result = f"{ant_str} must have {con_str} "
    return result