package ca.ualberta.smr.testing;

import ca.ualberta.smr.model.*;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

import static ca.ualberta.smr.utils.Utils.listOf;

public class Main {

    public static void main(String[] args) throws IOException {
        final DefaultViolationDetector defaultDetector = new DefaultViolationDetector();

        for (String projectPath : projectsFolder()) {
            System.out.println(">>>>> Scanning the directory: " + projectPath);
            scanProject(defaultDetector, projectPath);
            System.out.println(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n");
        }
    }

    private static void scanProject(DefaultViolationDetector defaultDetector, String projectPath) throws IOException {
        Files.walk(Paths.get(projectPath))
                .filter(Files::isRegularFile)
                .filter(f -> f.toAbsolutePath().toString().endsWith(".java"))
                .map(e -> {
                    final String filename = e.toAbsolutePath().toString();
                    long start = System.nanoTime();
                    final Map<StaticAnalysisRule, Collection<ViolationInfo>> strings = defaultDetector.analyze(filename);
                    long diff = System.nanoTime() - start;

                    for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : strings.entrySet()) {
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

                    return diff;
                }).reduce(Long::sum).ifPresent(t -> System.out.printf("It took : %d seconds\n", (t / 1_000_000_000)));
    }

    private static List<String> projectsFolder() {
        return listOf(
                "C:\\Users\\mensu\\Downloads\\projects\\capstone-ccp",
                "C:\\Users\\mensu\\Downloads\\projects\\guide-microprofile-reactive-messaging\\finish\\food",
                "C:\\Users\\mensu\\Downloads\\projects\\trellis-main\\trellis-main",
                "C:\\Users\\mensu\\Downloads\\projects\\guide-reactive-rest-client",
                "C:\\Users\\mensu\\Downloads\\projects\\guide-microprofile-jwt-a0867bf",
                "C:\\Users\\mensu\\Downloads\\projects\\guide-microprofile-jwt-7d1da9a",
                "C:\\Users\\mensu\\Downloads\\projects\\guide-microprofile-jwt-0e563e8a",
                "C:\\Users\\mensu\\Downloads\\projects\\citi-workshop-20201102\\4.5.6",
                "C:\\Users\\mensu\\Downloads\\projects\\foodOrderRestaurantApp",
                "C:\\Users\\mensu\\Downloads\\projects\\membership"
        );
    }

}