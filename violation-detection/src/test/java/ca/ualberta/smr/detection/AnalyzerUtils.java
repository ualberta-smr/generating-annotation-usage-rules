package ca.ualberta.smr.detection;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.parsing.rules.Rule;
import ca.ualberta.smr.parsing.rules.RuleParser;
import com.github.javaparser.JavaParser;
import com.github.javaparser.ast.CompilationUnit;
import lombok.val;

import static org.junit.jupiter.api.Assumptions.assumeTrue;

public class AnalyzerUtils {

    static CompilationUnit parse(String... lines) {
        String javaCode = String.join("\n", lines);
        val parseResult = new JavaParser().parse(javaCode);
        assumeTrue(parseResult.isSuccessful() && parseResult.getResult().isPresent(),
                "Parsing should be successful");
        return parseResult.getResult().get();
    }

    static StaticAnalysisRule getRule(String ruleString) {
        val rule = new Rule();
        rule.setId("id");
        rule.setSpecification(ruleString);
        return RuleParser.parseRule(rule);
    }

}
