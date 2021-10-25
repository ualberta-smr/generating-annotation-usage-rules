package ca.ualberta.smr.testing;

import ca.ualberta.smr.model.*;
import ca.ualberta.smr.utils.ViolationReporting;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        final DefaultViolationDetector defaultDetector = new DefaultViolationDetector();

        final String path = "C:\\Users\\mensu\\Downloads\\projects\\trellis-main\\trellis-main";
        Files.walk(Paths.get(path))
                .filter(Files::isRegularFile)
                .filter(f -> f.toAbsolutePath().toString().endsWith(".java"))
                .forEach(e -> {
                    final String filename = e.toAbsolutePath().toString();
                    final Map<StaticAnalysisRule, Collection<ViolationInfo>> strings = defaultDetector.analyze(filename);

                    for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : strings.entrySet()) {
                        if (!entry.getValue().isEmpty()) {
                            System.out.println("================================================");
                            System.out.println("For rule: " + entry.getKey().toString());
                            System.out.println("File: " + filename);
                            for (ViolationInfo violationInfo : entry.getValue()) {
                                ViolationReporting.report(violationInfo);
                            }
                            System.out.println("================================================");
                        }
                    }
                });


    }

}