package ca.ualberta.smr.newmodel.javaelements;

import ca.ualberta.smr.newmodel.StaticAnalysisRule;
import ca.ualberta.smr.newmodel.violationreport.ViolationCombination;

public abstract class ProgramElement {
    abstract boolean matches(Object bd);
    /**
     * @param bd is an object from JavaParser, it can be MethodDeclaration, FieldDeclaration, etc.
     * @return list of violations
     */
    abstract ViolationCombination getMissing(Object bd, StaticAnalysisRule rule);
    abstract String description();

    @Override
    public String toString() {
        return this.description();
    }

    public enum ProgramElementType {
        CLASS, METHOD, FIELD, OTHER
    }
}
