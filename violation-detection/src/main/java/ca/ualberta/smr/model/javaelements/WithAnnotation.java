package ca.ualberta.smr.model.javaelements;

import java.util.Collection;

public interface WithAnnotation {
    Collection<Condition<Annotation>> annotations();
}
