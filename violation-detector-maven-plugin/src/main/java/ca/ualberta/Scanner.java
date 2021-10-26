package ca.ualberta;

import ca.ualberta.report.ConsoleViolationReporter;
import ca.ualberta.report.ViolationReporter;
import ca.ualberta.smr.model.*;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugins.annotations.*;
import org.apache.maven.project.MavenProject;
import org.codehaus.plexus.util.FileUtils;

import javax.inject.Inject;
import java.io.File;
import java.io.IOException;
import java.util.*;

@Mojo(name = "scan", defaultPhase = LifecyclePhase.VERIFY, threadSafe = true)
public class Scanner extends AbstractMojo {

    @Parameter(property = "project", readonly = true)
    private MavenProject project;

    @Parameter(property = "targetDirectory", required = true, defaultValue = "${project.basedir}/src/main/java")
    private File targetDirectory;

    @Parameter(property = "excludes")
    private String excludes;

    @Parameter(property = "includes", defaultValue = JAVA_FILES_PATTERN, required = true )
    private String includes;

    @Inject
    private ViolationReporter reporter;

    @Inject
    private DefaultViolationDetector violationDetector;

    @Override
    public void execute() {
        try {
            FileUtils.getFiles(targetDirectory, includes, excludes)
                    .stream()
                    .filter(this::isJavaFile)
                    .map(this.violationDetector::analyze)
                    .forEach(e -> {
                        for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : e.entrySet()) {
                            if (!entry.getValue().isEmpty()) {
                                getLog().info("For rule: " + entry.getKey().toString());
                                for (ViolationInfo violationInfo : entry.getValue()) {
                                    reporter.report(violationInfo);
                                }
                            }
                        }
                    });
        } catch (IOException e) {
            getLog().error("Exception occurred while processing the directory", e);
        }
    }

    private boolean isJavaFile(File file) {
        return file.isFile() && file.getName().endsWith(".java");
    }

    private static final String JAVA_FILES_PATTERN = "**\\/*.java";
}
