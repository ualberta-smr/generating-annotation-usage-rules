package ca.ualberta.smr.newmodel;

import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.utils.Utils.listOf;
import static org.junit.jupiter.api.Assertions.*;

class ViolationCombinationAndTest {

    @Test
    void test() {
        assertTrue(new ViolationCombinationAnd(null, listOf(
                ViolationCombination.EMPTY, ViolationCombination.EMPTY
        )).isEmpty());
    }

    @Test
    void test2() {
        assertTrue(ViolationCombination.EMPTY.isEmpty());
        assertNotEquals(ViolationCombination.EMPTY, new ViolationCombinationAnd(null, listOf()));
    }


}