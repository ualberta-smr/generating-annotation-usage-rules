package miner;

import config.ConfigurationProperties;

import java.util.*;

public class Configuration {

    public static ConfigurationProperties properties = null;


    /*------------------- GENERAL CONFIGS ----------------------- */
    /**
     * All projects (collective) strategy configs
     */
    public static double minSupp = 0.8;
    public static double minConf = 0.85;

    /**
     * Version of the tool currently being run (can be any value; used just for convenience)
     */
    public final static String version = "v0.0.10_final";

//    /**
//     * Library prefixes/regexes - uncomment one or the other
//     */
    // Spring
//    public final static String libSubApiRegex = "Annotation_org\\.springframework[\\w,\\.]+";
//    public final static String libPref = "org.springframework";
    // Microprofile
//    public final static String libSubApiRegex = "Annotation_org\\.eclipse\\.microprofile[\\w,\\.]+";
//    public final static String libPref = "org.eclipse.microprofile";

//    /**
//     * Target library (or libraries) directory
//     */
//    // info: may have to adjust the correct paths. If does not work, try absolute paths, e.g., "/a/b/c"
//    public final static String[] librariesPaths = {
//            // spring
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-aop",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-asm",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-beans",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-boot",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-context",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-core",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-expression",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-jdbc",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-jms",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-ldap",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-messaging",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-retry",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-security",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-shell",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-tx",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-web",
//        "/home/owary/Programming/Research/Annotation-Violation-Detector/project/spring/spring-boot/spring-ws",
//
//            // microprofile
////            "../libsources/microprofile/microprofile-config",
////            "../libsources/microprofile/microprofile-jwt-auth",
////            "../libsources/microprofile/microprofile-fault-tolerance",
////            "../libsources/microprofile/microprofile-graphql",
////            "../libsources/microprofile/microprofile-health",
////            "../libsources/microprofile/microprofile-metrics",
////            "../libsources/microprofile/microprofile-open-api",
////            "../libsources/microprofile/microprofile-opentracing",
////            "../libsources/microprofile/microprofile-reactive-streams-operators",
////            "../libsources/microprofile/microprofile-rest-client",
//
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/cdi-api-2.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.annotation-api-2.1.1.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.enterprise.cdi-api-4.0.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.inject-api-2.0.1.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.persistence-api-3.1.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.servlet-api-6.0.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.validation-api-3.0.2.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.ws.rs-api-3.1.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/javax.inject-1.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/javax.ws.rs-api-2.1.1.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-config-api-3.0.1.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-fault-tolerance-api-3.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-graphql-api-1.1.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-health-api-3.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-jwt-auth-api-1.2.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-metrics-api-4.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-openapi-api-2.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-reactive-messaging-api-2.0.jar",
////            "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-rest-client-api-2.0.jar"
//    };

    public final static List<String> subApiLibPrefixes = new ArrayList<String>() {{
        // spring boot
        add("org.springframework.aop");
        add("org.springframework.asm");
        add("org.springframework.boot");
        add("org.springframework.beans");
        add("org.springframework.core");
        add("org.springframework.context");
        add("org.springframework.expression");
        add("org.springframework.jdbc");
        add("org.springframework.jms");
        add("org.springframework.ldap");
        add("org.springframework.messaging");
        add("org.springframework.orm");
        add("org.springframework.retry");
        add("org.springframework.security");
        add("org.springframework.shell");
        add("org.springframework.tx");
        // spring web
        add("org.springframework.remoting");
        add("org.springframework.web");
        add("org.springframework.http");

        // microprofile
//        add("org.eclipse.microprofile.config");
//        add("org.eclipse.microprofile.faulttolerance");
//        add("org.eclipse.microprofile.graphql");
//        add("org.eclipse.microprofile.health");
//        add("org.eclipse.microprofile.jwt");
//        add("org.eclipse.microprofile.metrics");
//        add("org.eclipse.microprofile.openapi");
//        add("org.eclipse.microprofile.opentracing");
//        add("org.eclipse.microprofile.reactive");
//        add("org.eclipse.microprofile.rest");
//        add("org.eclipse.microprofile.auth");
    }};

    /**
     * Library prefix
     */
    // INFO: If you want to get usages for Java EE, then there should not be checkers for it. Unless we look for javax...
    public final static String[] apiLibPrefixes = {
            // Spring
        "org.springframework",

            // Microprofile
//            "javax",
//            "org.eclipse.microprofile",
    };

    /**
     * Invididual project mining strategy configs
     * <p>
     * If false, then combines all itemsets/usages together and mines.
     * Otherwise, this will individually mine from each project, and then combine the mined frequent itemsets.
     */
    public static boolean mineIndividualProjects = true;
    public static int minItemsetSizePerProject = 1;


    /*------------- GROUP BY SUB-API BEFORE MINING -------------- */
    public static boolean mineBySubApi = true;


    /* -------- Additional dumps from intermediate steps (input & freq itemsets) -------- */
    public static boolean dumpFrequentItemsets = false;
    public static boolean dumpCandidateRules = false;
    public static boolean dumpInputItemsets = false;

}
