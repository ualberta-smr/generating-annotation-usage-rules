# Analysis of the Confirmed Rules

There are a total of 11 confirmed rules. However, some of them are very similar, thus in this page, we merged the similar ones together. You can find all confirmed rules [here](./confirmed_rules.txt).

## Rule 1

```
method with annotation "APIResponses" or annotation "Operation" 
must have annotation "[GET|POST|HEAD|OPTIONS|DELETE|PATCH|PUT]"
```

### Comments
- The official JavaDoc for the APIResponses does not state anything about consequent: https://download.eclipse.org/microprofile/microprofile-open-api-3.0/apidocs/org/eclipse/microprofile/openapi/annotations/responses/APIResponses.html
- However, the JavaDoc for APIResponse does indeed state that the annotation is applied to a JAX-RS method (which is a method that uses GET/POST...): https://download.eclipse.org/microprofile/microprofile-open-api-3.0/apidocs/org/eclipse/microprofile/openapi/annotations/responses/APIResponse.html
- The JavaDoc for Operation does not state anything about the consequent: https://download.eclipse.org/microprofile/microprofile-open-api-3.0/apidocs/index.html?org/eclipse/microprofile/openapi/annotations/responses/APIResponse.html
- In MicroProfile OpenAPI spec, it is clearly stated that the API is used with JAX-RS annotations: https://download.eclipse.org/microprofile/microprofile-open-api-1.0/microprofile-openapi-spec.html#_documentation_mechanisms
- Also, there is not a reason to use OpenAPI annotations if we don't have a REST API already.

### Consequence of violation
    ...

## Rule 2
```
class with annotation "OpenAPIDefinition" must have extension of "Application"
```

### Comments
- The actual JavaDoc does not state anything about this rule: https://download.eclipse.org/microprofile/microprofile-open-api-3.0/apidocs/index.html?org/eclipse/microprofile/openapi/annotations/responses/APIResponse.html
- Not any mention in the MicroProfile OpenAPI spec either: 
    - https://download.eclipse.org/microprofile/microprofile-open-api-1.0/microprofile-openapi-spec.html#_documentation_mechanisms
    - https://stackoverflow.com/questions/59168710/where-to-put-openapidefinition

### Consequence of violation
    ... [see StackOverflow post]

## Rule 3
```
class with method with annotation "[Outgoing|Incoming]" must have bean declaration
```

### Comments
- Directly mentioned in the docs:  
    - https://download.eclipse.org/microprofile/microprofile-reactive-messaging-2.0.1/microprofile-reactive-messaging-spec-2.0.1.html#_message_consumption_with_incoming 
    - https://download.eclipse.org/microprofile/microprofile-reactive-messaging-2.0.1/microprofile-reactive-messaging-spec-2.0.1.html#_message_production_with_outgoing    
- Actually the confirmed rules are slightly incorrect. Because the class cannot be any CDI bean. Only @ApplicationScoped and @Dependent are supported: https://download.eclipse.org/microprofile/microprofile-reactive-messaging-2.0.1/microprofile-reactive-messaging-spec-2.0.1.html#_supported_cdi_scopes
- TCK examples all have @ApplicationScoped or @Dependent: https://github.com/eclipse/microprofile-reactive-messaging/tree/master/tck

### Consequence of violation
The consumer/producer will not be picked by the CDI, therefore the runtime will not have any information about them. This is not a likely case though.

## Rule 4
```
class with annotation "ApplicationScoped" and annotation "[Startup|Readiness|Liveness]" 
must have implementation of "HealthCheck"
```

### Comments
- Mentioned in docs: https://download.eclipse.org/microprofile/microprofile-health-4.0/microprofile-health-spec-4.0.html#_different_kinds_of_health_checks

- As for being a CDI bean: https://download.eclipse.org/microprofile/microprofile-health-4.0/microprofile-health-spec-4.0.html#_integration_with_cdi

### Consequence of violation
- The HealthCheck will be ignored, however, this case is unlikely because one has to 1) implement the `call` method from the HealthCheck interface, and also forget to implement the interface explicitly. Extremely unrealistic case.

## Rule 5
```
class with method with annotation "Gauge" 
must have annotation "ApplicationScoped" and method with annotation "Gauge" with parameter "String unit"
```

**We can rewrite this rule using the new additions made to the DSL**:

```
method with annotation "Gauge" 
must have annotation "Gauge" with parameter "String unit" and enclosing class with annotation "ApplicationScoped"
```

### Comments
- The class being a CDI bean is mentioned: https://download.eclipse.org/microprofile/microprofile-metrics-4.0/microprofile-metrics-spec-4.0.html#cdi_scopes (second paragraph). In addition to "ApplicationScoped", the annotation can also be "Singleton" (see: https://jakarta.ee/specifications/platform/8/apidocs/javax/ejb/Singleton.html)

- "String unit" part is not necessary as it is a parameter with no default value. The compilation will fail if none is supplied. Effectively, the rule is as follows:

```
method with annotation "Gauge" must have enclosing class with annotation "ApplicationScoped" or "Singleton"
```

### Consequence of violation
    ...

## Rule 6
```
field with annotation "RegistryType" with parameter "MetricRegistry.Type type" and annotation "Inject" 
must have type "MetricRegistry"
```

### Comments
- This is actually present in the JavaDoc exactly: https://download.eclipse.org/microprofile/microprofile-metrics-4.0/apidocs/org/eclipse/microprofile/metrics/annotation/RegistryType.html
- This is exactly present in the Spec as well: https://download.eclipse.org/microprofile/microprofile-metrics-4.0/microprofile-metrics-spec-4.0.html#_registrytype (see the next 4 subsections)
- This rule is also unlikely to be violated. A better rule would be:

```
field with type "MetricRegistry" must have annotation "Inject"
```

### Consequence of violation
    ...

## Rule 7
```
field with annotation "Metric" must have annotation "Inject"
```

### Comments
- Available in the spec: https://download.eclipse.org/microprofile/microprofile-metrics-4.0/microprofile-metrics-spec-4.0.html#_metric
- Available in the JavaDoc: https://download.eclipse.org/microprofile/microprofile-metrics-4.0/apidocs/org/eclipse/microprofile/metrics/annotation/Metric.html
- This rule is more useful than the previous one
- In the spec there's another rule:
    - method with parameter with annotation "Metric" must have annotation "Inject"

### Consequence of violation
Since it won't be injected, it will be "null"

## Rule 8
```
class with annotation "ApplicationPath" and annotation "LoginConfig" with parameter "String authMethod" 
must have extension of "Application"
```

### Comments
- `authMethod` is actually a required parameter, the code will not compile without it
    - However, there's an interesting thing here. The value of `authMethod` should be either `MP-JWT` or some known authentication mechanism
- Available in the spec: https://download.eclipse.org/microprofile/microprofile-jwt-auth-2.0/microprofile-jwt-auth-spec-2.0.html#_marking_a_jax_rs_application_as_requiring_mp_jwt_access_control
- The rule can be shortened because of the reasons below:
    - `ApplicationPath` annotation can only be applied to a subclass of Application class (https://docs.oracle.com/javaee/7/api/javax/ws/rs/ApplicationPath.html) thus we do not really need it in this rule. It can form a rule of its own.
    - `authMethod` is actually required, so we can omit that as well
    - Final rule: 
    
    ```
    class with annotation "LoginConfig" must have extension of "Application"
    ```
