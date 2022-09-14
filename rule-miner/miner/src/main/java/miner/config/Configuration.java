package miner.config;

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

    /* -------- Additional dumps from intermediate steps (input & freq itemsets) -------- */
    public static boolean dumpFrequentItemsets = false;
    public static boolean dumpCandidateRules = false;
    public static boolean dumpInputItemsets = false;

}
