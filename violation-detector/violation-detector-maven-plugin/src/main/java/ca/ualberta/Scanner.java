package ca.ualberta;

import ca.ualberta.report.ViolationReporter;
import ca.ualberta.smr.model.*;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import lombok.AllArgsConstructor;
import lombok.val;
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

import static java.util.stream.Collectors.*;
import static java.util.stream.Stream.concat;

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
            val currentDir = System.getProperty("user.dir");
            val allViolations = FileUtils.getFiles(targetDirectory, includes, excludes).stream()
                    .filter(this::isJavaFile)
                    .flatMap(f -> this.violationDetector.analyze(f)
                            .entrySet()
                            .stream()
                            .filter(e -> !e.getValue().isEmpty())
                            .map(e -> new FileStaticAnalysisRulePair(
                                    f.getPath().replace(currentDir, ""),
                                    e.getKey(),
                                    e.getValue()
                            )))
                    .collect(toMap(e -> e.rule, Collections::singletonList,
                            (v1, v2) ->
                                    concat(
                                            v1.stream(),
                                            v2.stream()
                                    ).collect(toList()))
                    );

            report(allViolations);
        } catch (IOException e) {
            throw new MojoExecutionException("Exception occurred while processing the directory", e);
        }
    }

    private void report(Map<StaticAnalysisRule, List<FileStaticAnalysisRulePair>> allViolations) throws MojoFailureException {
        if (!allViolations.isEmpty()) {
            // basically if it needs to fail on violation, the log level should be error
            // otherwise warn
            val logger = new DetectorLogger(failOnViolation);
            allViolations.forEach((rule, violations) ->
                    reporter.report(rule, violations, logger));
            if (failOnViolation) {
                long count = allViolations.values().stream().mapToLong(Collection::size).sum();
                throw new MojoFailureException(String.format("There were %d violations found in the project", count));
            }
        }
    }

    private class DetectorLogger implements Consumer<String> {
        private final Consumer<String> logger;

        private DetectorLogger(boolean failOnViolation) {
            this.logger = failOnViolation ? getLog()::error : getLog()::warn;
        }


        @Override
        public void accept(String input) {
            val lines = input.split(System.lineSeparator());
            for (val line : lines) {
                logger.accept(line);
            }
        }
    }

    private boolean isJavaFile(File file) {
        return file.isFile() && file.getName().endsWith(".java");
    }

    private static final String JAVA_FILES_PATTERN = "**\\/*.java";
}

