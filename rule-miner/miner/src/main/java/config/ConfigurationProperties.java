package config;

import com.google.gson.Gson;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class ConfigurationProperties {

    private String targetProjectsDir;
    private ApiConfiguration api;
    private Collection<String> libSources;

    public static ConfigurationProperties readConfigJson(String contents) {
        return new Gson().fromJson(contents, ConfigurationProperties.class);
    }

    public String targetProjectsDir() {
        return targetProjectsDir;
    }

    public ApiConfiguration api() {
        return api;
    }

    public Collection<String> libSources() {
        Collection<String> jarFiles = new ArrayList<>();
        for (String libSource : libSources) {
            try(Stream<Path> stream = Files.walk(Paths.get(libSource))) {
                List<String> jarFilesForSource = stream
                        .map(Path::normalize)
                        .filter(Files::isRegularFile)
                        .filter(e -> e.getFileName().toString().endsWith(".jar"))
                        .map(e -> e.toAbsolutePath().toString())
                        .collect(Collectors.toList());
                jarFiles.addAll(jarFilesForSource);
            } catch (Exception ex) {
                throw new RuntimeException(ex);
            }
        }
        return jarFiles;
    }

}
