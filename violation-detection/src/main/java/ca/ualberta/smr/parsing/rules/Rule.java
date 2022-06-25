package ca.ualberta.smr.parsing.rules;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
public class Rule {

    /**
     * id of the rule
     */
    private String id;
    /**
     * The actual rule string that's specified in RulePad format
     */
    private String specification;

}