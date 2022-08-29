package ca.ualberta.smr.parsing.annotation;

import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.Type;
import lombok.val;
import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.model.javaelements.AggregateCondition.empty;
import static ca.ualberta.smr.model.javaelements.AggregateConditionOperation.OR;
import static ca.ualberta.smr.model.javaelements.AggregateConditionOperation.XOR;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;
import static org.junit.jupiter.api.Assertions.*;

class AnnotationParsingUtilsTest {

    @Test
    void createDisjunctionCondition_no_type() {
        val expectedCondition = empty();
        val actualCondition = AnnotationParsingUtils.createDisjunctionCondition(listOf());
        assertEquals(expectedCondition, actualCondition);
    }

    @Test
    void createDisjunctionCondition_one_type() {
        val expectedCondition = Type.of("Foo");
        val actualCondition = AnnotationParsingUtils.createDisjunctionCondition(listOf("Foo"));
        assertEquals(expectedCondition, actualCondition);
    }

    @Test
    void createDisjunctionCondition_multiple_types() {
        val expectedCondition = new AggregateCondition(new AggregateCondition(
                new AggregateCondition(
                        new Type("Foo"), new Type("Bar"), OR
                ), new Type("Baz"), OR
        ), new Type("Qux"), OR);

        val actualCondition = AnnotationParsingUtils.createDisjunctionCondition(listOf(
                "Foo", "Bar", "Baz", "Qux"
        ));

        assertEquals(expectedCondition, actualCondition);
    }

    @Test
    void createMutualExclusiveCondition_no_type() {
        val expectedCondition = empty();
        val actualCondition = AnnotationParsingUtils.createMutualExclusiveCondition(listOf());
        assertEquals(expectedCondition, actualCondition);
    }

    @Test
    void createMutualExclusiveCondition_one_type() {
        val expectedCondition = Type.of("Foo");
        val actualCondition = AnnotationParsingUtils.createMutualExclusiveCondition(listOf("Foo"));
        assertEquals(expectedCondition, actualCondition);
    }

    @Test
    void createMutualExclusiveCondition_multiple_types() {
        val expectedCondition = new AggregateCondition(new AggregateCondition(
                new AggregateCondition(
                        new Type("Foo"), new Type("Bar"), XOR
                ), new Type("Baz"), XOR
        ), new Type("Qux"), XOR);

        val actualCondition = AnnotationParsingUtils.createMutualExclusiveCondition(listOf(
                "Foo", "Bar", "Baz", "Qux"
        ));

        assertEquals(expectedCondition, actualCondition);
    }
}