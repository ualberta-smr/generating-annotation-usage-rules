package ca.ualberta.smr.rules;

import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.Collection;

@Getter
@Setter
@NoArgsConstructor
public class Rules {

    @JsonProperty("rules")
    private Collection<Rule> rules;

}
