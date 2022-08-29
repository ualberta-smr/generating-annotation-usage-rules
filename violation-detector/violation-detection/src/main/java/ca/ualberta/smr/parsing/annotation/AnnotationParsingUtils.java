package ca.ualberta.smr.parsing.annotation;

import ca.ualberta.smr.model.javaelements.AggregateCondition;
import ca.ualberta.smr.model.javaelements.AggregateConditionOperation;
import ca.ualberta.smr.model.javaelements.Type;
import lombok.val;

import java.util.List;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.unwrapIfSingle;

public class AnnotationParsingUtils {

    /**
     * Given a list of type names in the string form, this method returns an AggregateCondition that
     * is a disjunction (OR) of all these types
     *
     * @param typeNames list of type names (e.g., ["Foo", "Bar", "Baz"]
     * @return an AggregateCondition that is a disjunction of the provided types (e.g., ["Foo" or "Bar" or "Baz"]
     */
    public static AggregateCondition createDisjunctionCondition(List<String> typeNames) {
        return typeNames
                .stream()
                .map(Type::of)
                .reduce((type1, type2) -> {
                    val t1 = unwrapIfSingle(type1);
                    val t2 = unwrapIfSingle(type2);
                    return new AggregateCondition(t1, t2, AggregateConditionOperation.OR);
                }).orElseGet(AggregateCondition::empty);
    }

    /**
     * Given a list of type names in the string form, this method returns an AggregateCondition that
     * is a mutually exclusive (XOR) condition of all these types
     *
     * @param typeNames list of type names (e.g., ["Foo", "Bar", "Baz"]
     * @return an AggregateCondition that is a disjunction of the provided types (e.g., ["Foo" xor "Bar" xor "Baz"]
     */
    public static AggregateCondition createMutualExclusiveCondition(List<String> typeNames) {
        return typeNames
                .stream()
                .map(Type::of)
                .reduce((type1, type2) -> {
                    val t1 = unwrapIfSingle(type1);
                    val t2 = unwrapIfSingle(type2);
                    return new AggregateCondition(t1, t2, AggregateConditionOperation.XOR);
                }).orElseGet(AggregateCondition::empty);
    }

}
