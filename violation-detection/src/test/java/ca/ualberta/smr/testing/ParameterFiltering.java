package ca.ualberta.smr.testing;

import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.util.Collection;
import java.util.Map;

public class ParameterFiltering {

    @Test
    void test1() throws IOException {
        final DefaultViolationDetector detector = new DefaultViolationDetector();
        String filename = "C:\\Users\\mensu\\Downloads\\projects\\capstone-ccp\\client-api\\src\\main\\java\\jaxrs\\resources\\DebrisBidResource.java";

        for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : detector.analyze(filename).entrySet()) {
            if (!entry.getValue().isEmpty()) {
                System.out.println("================================================");
                System.out.println("For rule: " + entry.getKey().toString());
                System.out.println("File: " + filename);
                for (ViolationInfo violationInfo : entry.getValue()) {
                    Reporter.report(violationInfo);
                }
                System.out.println("================================================");
            }
        }
    }

}
