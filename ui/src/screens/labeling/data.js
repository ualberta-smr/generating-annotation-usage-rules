const data = [
    {
        id: 1144405872,
        grammar:
            'class with (annotation "Path" ) must have (annotation "RegisterRestClient" and declaration statement with (annotation "Inject" and annotation "Claim" ) and function with (annotation "Path" and annotation "Produces" and annotation "GET" and annotation "Traced" ) ) ',
        ruleCode: `@Path(value="dummy-value")
@RegisterRestClient
class DemoClass {

    @Inject
    @Claim
    private Object field;

    @Path
    @Produces
    @GET
    @Traced
    public Object method() {}
}`,
        compliantExamples: [
            `@Path(value="demo")
@RegisterRestClient
public class Correct {

    @Inject
    @Claim
    private String field;

    @Path
    @Produces
    @GET
    @Traced
    public void method(){}

}`,
        ],
        nonCompliantExamples: [
            `@Path(value="demo")
@RegisterRestClient
public class Incorrect {

    @Inject
    @Claim
    private String field;

    @Path
    @Produces
    @GET
    /* Missing: @Traced */
    public void method(){}

}`,
        ],
        label: null
    },
    {
        id: 1530558578,
        grammar:
            'class with (annotation "Path" and declaration statement with (annotation "Claim" ) ) must have (declaration statement with (annotation "Inject" ) ) ',
        ruleCode: `@Path
class Demo {
    @AnnotationA
    @AnnotationB
    private Object field;
}`,
        compliantExamples: [
            `@Path
class Demo {
    @Claim
    @Inject
    private Object field;
}`,
        ],
        nonCompliantExamples: [
            `@Path
class Demo {
    @Inject
    private Object field;
}`,
        ],
        label: null
    },
];

export default data;
