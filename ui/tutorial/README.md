# Tutorial

## Rulepad

Rulepad DSL resembles English language. It has a IF-THEN structure. 

Here are some Rulepad example statements alongside with their Java code equivalents:

```java
// class with annotation "A" must have method with annotation "B"

@A
@B
class Foo {}
```

```java
// field with type "A" must have annotation "B" or annotation "C"

class Foo {
    @B // or @C
    A dummyField;
}
```

```java
// method with parameter with type "A" must have type "B" and annotation "C"

class Foo {

    @C
    B dummyMethod(A paramFoo) { /*ignored*/ }
}
```

### Syntax

In Rulepad, we describe rules about Java program elements. Each program element can have different properties. When we want to specify different properties for a program element, we use `with` keyword (e.g., `field with type "String"`). Statements consist of 2 parts: (1) IF part that is before _must have_ and (2) THEN part which is after _must have_. There is a general structure for all the statements:

```
programElement with programElementExpression must have programElementExpression
```

Although there are 13 program elements that we can specify, **the actual statements need to describe either a class, a method or a field**. So, in the structure given above `programElement` can be either `class`, `method` or `field`. 

For each program element, `programElementExpression` represents the properties that can belong to that program element. `programElementExpression` can take an aggregate form, meaning we can use `AND`s and `OR`s to combine multiple properties (see [aggregates](#aggregates-and-parenthesis)) 

#### annotation

`annotation` has 2 properties that we can use: `type` and `parameters`. 

- Type is mandatory when it comes to annotations. `@Override` should be written as `annotation "Override"`. 
- Annotations may also have annotation parameters. `@ConfigProperty(name=...)` should be described as `annotation "ConfigProperty" with parameter "name"`

#### annotation parameter

Annotation parameters have 3 properties: `type`, `name` and `value` (basically, `@Type(name=value)`). Examples:
- A _String_ parameter should be described as `parameter with type "String"`
- A parameter with name _maxInterval_ should be described as `parameter with name "maxInterval"`
- A parameter with value _enabled_ should be described as `parameter with value "enabled"`

There're shortcuts available for annotation parameters. These are the following:
- Instead of `parameter with name "maxInterval"`, we can say `parameter "maxInterval"`
    - So, if we want to say `parameter with name "fallback" and value "enabled"`, it can be simplified to `parameter "fallback" with value "enabled"`
- Instead of `parameter with type "long" and name "maxInterval"`, we can say `parameter "long maxInterval"`

#### type

Types only have 1 property and that's the name of the type. For example, _String_ type should be described as `type "String"`

#### name

Names only have 1 property and that's the name string. For example, something with name _maxInterval_ should be written as `name "maxInterval"`.

#### value

Values only have 1 property and that's the value string. For example, something with the value of _enabled_ should be written as `value "enabled"`. By default value string matches the literal value. So, `value "enabled"` is equal to `@Dummy(param="enabled")`.

#### field

Fields can have 3 properties: `annotation`, `type` and `configuration file`. Examples:

- A field with annotation _Inject_ will be `field with annotation "Inject"`
- A field with _String_ type will be `field with type "String"`

Configuration file example is explained [here](#configuration-file-and-configuration-property)

#### method

Methods can have 4 properties: `annotation`, `type` (as return type), `parameter` and `configuration file`. Examples:

- A method with annotation _GET_ will be `method with annotation "GET"`
- A method with a return type of _String_ will be `method with type "String"`
- A method with _String_ parameter will be `method with parameter "String"` 

Configuration file example is explained [here](#configuration-file-and-configuration-property)

#### method parameter

Method parameters can have 3 properties: `type`, `name` and `annotation`. Examples:
- A _String_ parameter should be described as `parameter with type "String"`
- A parameter with annotation _PathParam_ should be described as `parameter with annotation "PathParam"`
- A parameter with name _inputString_ should be described as `parameter with name "inputString"`

There're shortcuts available for method parameters. These are the following:
- Instead of `parameter with type "String"`, we can say `parameter "String"`
- Instead of `parameter with type "long" and name "maxInterval"`, we can say `parameter "long maxInterval"`

#### class
`class` can have 7 different properties: 
- annotation
- field
- method
- extension
- implementation
- bean declaration
- configuration file

Here are some examples:
- A class with the annotation _Path_ should be described as `class with annotation "Path"`
- If a class has a _String_ field, it should be described as `class with field with type "String"`
- If a class has a method that has been annotated with _GET_, it should be described as `class with method with annotation "GET"`
- If we want to specify that a class is extending _HealthCheck_ class, it should be described as `class with extension of "HealthCheck"`
- If we want to specify that a class is implementing _Health_ interface, it should be described as `class with implementation of "HealthCheck"`
- If we want to specify that a class has been declared as a bean in _beans.xml_, it should be described as `class with bean declaration`

`extension of`, `implementation of` and `bean declaration` are exclusive to classes. `bean declaration` does not have any properties. `extension of` and `implementation of` can only specify what class they are referring to (examples given above).

Configuration file example is explained [here](#configuration-file-and-configuration-property)

#### configuration file and configuration property

In our context, configuration file refers to the `microprofile-config.properties`. Configuration file only has 1 program element which is a configuration `property`.

Configuration properties have 3 properties: `type`, `name` and `value`. Examples:
- A _String_ property should be described as `property with type "String"`
- A property with name _maxInterval_ should be described as `property with name "maxInterval"`
- A property with value _enabled_ should be described as `property with value "enabled"`

There're shortcuts available for configuration properties. These are the following:
- Instead of `property with name "maxInterval"`, we can say `property "maxInterval"`
    - So, if we want to say `property with name "fallback" and value "enabled"`, it can be simplified to `property "fallback" with value "enabled"`
- Instead of `property with type "long" and name "maxInterval"`, we can say `property "long maxInterval"`


#### Aggregates and Parenthesis

Properties of program element can be combined as well. We currently have 2 aggregation operation: AND and OR. Examples:

- `class with annotation "A" must have annotation "B" or annotation "C"`
- `field with type "A" must have annotation "B" and annotation "C"`
- `method with type "A" must have annotation "B" or parameter with type "C"`

There's a shortcut available for annotations if one wants to specify multiple annotations from the same package with OR operation. Consider the case when you want to say `@javax.ws.rs.GET or @javax.ws.rs.POST or @javax.ws.rs.DELETE or @javax.ws.rs.PUT`. With the usual Rulepad syntax it would be:

```
annotation "javax.ws.rs.GET" or annotation "javax.ws.rs.POST" or annotation "javax.ws.rs.DELETE" or annotation "javax.ws.rs.PUT"
```

but we can group them together and write it as:

```
annotation "javax.ws.rs.[GET|POST|DELETE|PUT]"
```

This shortcut should only be used to specify different annotations from the same package and not with combination of multiple packages (_e.g., avoid doing something like `"a.b.[c.[X|Y]|M|N]"`_) 

We can also use parenthesis to group things together to avoid ambiguities.

- `class with (field with type "A" and annotation "B") must have ... `
- `class with (field with type "A") and annotation "B" must have ... `