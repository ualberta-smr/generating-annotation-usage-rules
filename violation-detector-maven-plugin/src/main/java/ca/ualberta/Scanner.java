package ca.ualberta;

import ca.ualberta.report.ViolationReporter;
import ca.ualberta.smr.model.*;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugins.annotations.*;
import org.apache.maven.project.MavenProject;

import javax.inject.Inject;
import java.io.IOException;
import java.nio.file.*;
import java.util.*;

@Mojo(name = "scan")
public class Scanner extends AbstractMojo {

    @Parameter(property = "project", readonly = true)
    private MavenProject project;

    @Inject
    private ViolationReporter reporter;

    @Inject
    private DefaultViolationDetector violationDetector;

    @Override
    public void execute() {
        final String absolutePath = project.getBasedir().getAbsolutePath();
        // TODO: maybe make this a bit more configurable?
        // INFO: currently only uses to src/main/java for source files
        final Path path = Paths.get(absolutePath, "src", "main", "java");
        try {
            Files.walk(path)
                    .filter(Files::isRegularFile)
                    .map(f -> f.toAbsolutePath().toString())
                    .map(this.violationDetector::analyze)
                    .forEach(e -> {
                        for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : e.entrySet()) {
                            if (!entry.getValue().isEmpty()) {
                                System.out.println("For rule: " + entry.getKey().toString());
                                for (ViolationInfo violationInfo : entry.getValue()) {
                                    reporter.report(violationInfo);
                                }
                            }
                        }
                    });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
