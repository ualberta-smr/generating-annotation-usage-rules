package ca.ualberta.smr;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.utils.ViolationReporting;

import java.io.IOException;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        final DefaultViolationDetector defaultDetector = new DefaultViolationDetector();

        final Map<StaticAnalysisRule, Collection<ViolationInfo>> strings =
                defaultDetector.analyze("D:\\Projects\\CodeQL\\sample_projects\\java_code_ql_samples\\src\\main\\java\\io\\code\\annotations\\OrAndExample.java");

        for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : strings.entrySet()) {
            if (!entry.getValue().isEmpty()) {
                System.out.println("For rule: " + entry.getKey().toString());
                for (ViolationInfo violationInfo : entry.getValue()) {
                    ViolationReporting.report(violationInfo);
                }
            }
        }
    }

}