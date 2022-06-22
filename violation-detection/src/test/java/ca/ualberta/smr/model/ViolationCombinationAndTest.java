package ca.ualberta.smr.model;

import ca.ualberta.smr.model.violationreport.ViolationCombination;
import ca.ualberta.smr.model.violationreport.ViolationCombinationAnd;
import org.junit.jupiter.api.Test;

import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;
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