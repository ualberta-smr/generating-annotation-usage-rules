package ca.ualberta;

import ca.ualberta.smr.DefaultViolationDetector;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.ViolationInfo;
import ca.ualberta.smr.utils.ViolationReporting;
import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugin.MojoFailureException;
import org.apache.maven.plugins.annotations.Mojo;
import org.apache.maven.plugins.annotations.Parameter;
import org.apache.maven.project.MavenProject;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Collection;
import java.util.Map;

@Mojo(name = "list")
public class Demo extends AbstractMojo {

    @Parameter(property = "project", readonly = true)
    private MavenProject project;

    private final DefaultViolationDetector vd = initVD();

    private DefaultViolationDetector initVD() {
        try {
            return new DefaultViolationDetector();
        } catch (IOException ex) {
            throw new RuntimeException(ex);
        }
    }

    @Override
    public void execute() throws MojoExecutionException, MojoFailureException {
        final String absolutePath = project.getBasedir().getAbsolutePath();
        final Path path = Paths.get(absolutePath, "src", "main", "java");
        try {
            Files.walk(path)
                    .filter(Files::isRegularFile)
                    .map(f -> f.toAbsolutePath().toString())
                    .map(this.vd::analyze)
                    .forEach(e -> {
                        for (Map.Entry<StaticAnalysisRule, Collection<ViolationInfo>> entry : e.entrySet()) {
                            if (!entry.getValue().isEmpty()) {
                                System.out.println("For rule: " + entry.getKey().toString());
                                for (ViolationInfo violationInfo : entry.getValue()) {
                                    ViolationReporting.report(violationInfo);
                                }
                            }
                        }
                    });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
