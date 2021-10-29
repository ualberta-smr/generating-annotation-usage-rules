package ca.ualberta.smr.consequent;

import ca.ualberta.smr.model.javaelements.Annotation;
import ca.ualberta.smr.model.javaelements.Condition;
import ca.ualberta.smr.model.javaelements.Field;
import ca.ualberta.smr.model.javaelements.Type;

import java.util.List;

import static ca.ualberta.smr.model.javaelements.Annotation.annotation;
import static ca.ualberta.smr.model.javaelements.Condition.any;
import static ca.ualberta.smr.model.javaelements.Condition.single;

public class AndOrTest {

    void test1() {
        // field with (annotation "A" or annotation "B") and type "C"
        final Field field = new Field();
        field.annotations().add(
                any(
                        annotation("A"),
                        annotation("B"))
        );
        field.annotations().add(single(annotation("D")));
        field.type(Type.type("C"));
        // field with type "C" and type "D"
    }

//    void test2() {
//        // field with (annotation "A" or annotation "B") and type "C"
//
//        final Field field = new Field();
//
//        final Annotation a = annotation("A");
//
//        field.annotations().add(single(a));
//
//        // OR
//
//        List<Condition<Annotation>> annotations = (List<Condition<Annotation>>) field.annotations();
//        Condition<Annotation> lastAnnotation = annotations.get(annotations.size() - 1);
//        lastAnnotation.merge("OR"); // -> changes lastAnnotation from Single/AND to OR
//
//        // annotation "B"
//        final Annotation b = annotation("B");
//        // TODO: we have to know that we're coming from OR
//        annotations = (List<Condition<Annotation>>) field.annotations();
//        lastAnnotation = annotations.get(annotations.size() - 1);
//        lastAnnotation.merge(b);
//
//
//    }

}
