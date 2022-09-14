package config;

import miner.config.SubApiConfiguration;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Field;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SubApiConfigurationTest {

    @Test
    void extractMatchingAnnotation() throws NoSuchFieldException, IllegalAccessException {
        SubApiConfiguration subApiConfiguration = new SubApiConfiguration();
        // TODO: this is actually a bad practice, which is why I hate gson for its field injection
        Field prefixes = SubApiConfiguration.class.getDeclaredField("prefixes");
        prefixes.setAccessible(true);
        prefixes.set(subApiConfiguration, Arrays.asList(
                "org.eclipse.microprofile.config",
                "org.eclipse.microprofile.faulttolerance",
                "org.eclipse.microprofile.graphql",
                "org.eclipse.microprofile.health",
                "org.eclipse.microprofile.jwt",
                "org.eclipse.microprofile.metrics",
                "org.eclipse.microprofile.openapi",
                "org.eclipse.microprofile.opentracing",
                "org.eclipse.microprofile.reactive",
                "org.eclipse.microprofile.rest",
                "org.eclipse.microprofile.auth"
        ));

        Map<String, String> input = new HashMap<>();
        input.put("Class --(annotatedWith)--> Annotation_org.eclipse.microprofile.config.ConfigProperty", "Annotation_org.eclipse.microprofile.config.ConfigProperty");
        input.put("Annotation_org.eclipse.microprofile.faulttolerance.CircuitBreaker --(hasParam)--> Param_failureRatio:double", "Annotation_org.eclipse.microprofile.faulttolerance.CircuitBreaker");
        input.put("Class --(implements)--> Interface_org.eclipse.microprofile.health.HealthCheck", null);
        input.put("Annotation_org.eclipse.microprofile.abc.ABC --(hasParam)--> Param_failureRatio:double", null);

        input.forEach((expr, expectedResult) -> {
            Optional<String> maybe = subApiConfiguration.extractMatchingAnnotation(expr);
            if (expectedResult == null) {
                assertFalse(maybe.isPresent(), "Result should be empty");
            } else {
                assertTrue(maybe.isPresent(), "Result should be present for " + expr);
                assertEquals(expectedResult, maybe.get());
            }
        });
    }
}