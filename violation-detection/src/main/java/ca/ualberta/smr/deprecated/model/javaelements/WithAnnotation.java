package ca.ualberta.smr.deprecated.model.javaelements;

import java.util.Collection;

public interface WithAnnotation {
    Collection<Condition<Annotation>> annotations();
}
