package ca.ualberta;

import ca.ualberta.report.ViolationReporter;
import ca.ualberta.smr.model.*;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.*;
import org.apache.maven.project.MavenProject;
import org.codehaus.plexus.util.FileUtils;

import javax.inject.Inject;
import java.io.File;
import java.io.IOException;
import java.util.*;
import java.util.function.Consumer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

@Mojo(name = "scan", defaultPhase = LifecyclePhase.VERIFY)
public class Scanner extends AbstractMojo {

    @Parameter(property = "project", readonly = true)
    private MavenProject project;

    @Parameter(property = "targetDirectory", defaultValue = "${project.basedir}/src/main/java", required = true)
    private File targetDirectory;

    @Parameter(property = "excludes")
    private String excludes;

    @Parameter(property = "includes", defaultValue = JAVA_FILES_PATTERN, required = true)
    private String includes;

    @Parameter(property = "failOnViolation", defaultValue = "false", required = true)
    private boolean failOnViolation;

    @Inject
    private ViolationReporter reporter;

    @Inject
    private DefaultViolationDetector violationDetector;

    @Override
    public void execute() throws MojoFailureException, MojoExecutionException {
        try {
            Map<StaticAnalysisRule, Collection<ViolationInfo>> allViolations = new HashMap<>();
            FileUtils.getFiles(targetDirectory, includes, excludes)
                    .stream()
                    .filter(this::isJavaFile)
                    .map(this.violationDetector::analyze)
                    .forEach(e -> {
                        for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : e.entrySet()) {
                            if (!entry.getValue().isEmpty()) {
                                allViolations.putIfAbsent(entry.getKey(), entry.getValue());
                                allViolations.computeIfPresent(entry.getKey(),
                                        (key, oldViolations) ->
                                                Stream.concat(oldViolations.stream(), entry.getValue().stream())
                                                        .collect(Collectors.toSet()));
                            }
                        }
                    });
            if (!allViolations.isEmpty()) {
                // basically if it needs to fail on violation, the log level should be error
                // otherwise warn
                final Consumer<String> logger = failOnViolation ? getLog()::error : getLog()::warn;
                allViolations.forEach((rule, violations) ->
                        reporter.report(rule, violations, logger));
                if (failOnViolation) {
                    long count = allViolations.values().stream().mapToLong(Collection::size).sum();
                    throw new MojoFailureException(String.format("There were %d violations found in the project", count));
                }
            }
        } catch (IOException e) {
            throw new MojoExecutionException("Exception occurred while processing the directory", e);
        }
    }

    private boolean isJavaFile(File file) {
        return file.isFile() && file.getName().endsWith(".java");
    }

    private static final String JAVA_FILES_PATTERN = "**\\/*.java";
}
