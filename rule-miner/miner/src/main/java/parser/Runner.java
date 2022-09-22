package parser;

import miner.config.Configuration;
import miner.config.ConfigurationProperties;
import miner.config.SubApiConfiguration;
import miner.*;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

import util.AggregateData;
import util.ResultPrinter;
import util.labeler.RulesDatabase;

import static java.util.Arrays.asList;
import static java.util.Objects.requireNonNull;
import static java.util.stream.Collectors.toList;

public class Runner {
    private static AnnotationUsageGraphBuilder builder;

    public static void main(String[] args) throws IOException {
        // Get the path to all input user projects that use target library
        parseConfiguration(args);

        // Read in all java files
        long startProcessingTime = System.currentTimeMillis();
        readProjectsFiles();
        long endProcessingTime = System.currentTimeMillis();
        System.out.println("Parsed projects in " + (endProcessingTime - startProcessingTime) + " milliseconds");

        // Parse all annotations
        List<Itemset> allUsages = builder.getAllUsageGraphs();

        System.out.println("*****************************************");
        System.out.println("******** Finish Phase I: Parsing ********");
        System.out.println("*****************************************");
        System.out.println("There are " + allUsages.size() + " usages (in total!)");
        System.out.println("There are " + AnnotationUsageGraphBuilder.projectsWithCrossClassUsage.size() + " projects that have xclass rels");
        System.out.println("There are " + AnnotationUsageGraphBuilder.numOfFieldTypeDecl + " files that have field type decl");
        System.out.println("There are " + AnnotationUsageGraphBuilder.numOfParamTypeDecl + " files that have param type decl");

        // TODO: Comes with v0.0.6
        List<Itemset> usagesWithoutProjectDuplicates = takeOneItemsetFromEachProject(builder.getUsagesAsMap());
        System.out.println("There are " + usagesWithoutProjectDuplicates.size() + " usages (without duplicates in projects!)");
        HashMap<String, List<Itemset>> usagesByAnnotations = divideUsagesByAnnotations(usagesWithoutProjectDuplicates);
        getFrequencyDist(usagesByAnnotations);

        int itemsets = 0;
        for (Map.Entry<String, List<Itemset>> entry : usagesByAnnotations.entrySet()) {
            System.out.println("Annotation " + entry.getKey() + " appears in " + entry.getValue().size() + " transactions (usages).");
            itemsets += entry.getValue().size();
        }
        System.out.println("There are " + itemsets + " itemsets with at least 1 MP element");

        // Association rule mining using FP-Growth algorithm
        mineByAnnotations(usagesByAnnotations);
        System.out.println("It took " + (endProcessingTime - startProcessingTime) + " to parse and mine stuff all projects.");
    }

    private static void getFrequencyDist(HashMap<String, List<Itemset>> usagesBySubApi) {
        PrintStream originalOut = System.out;

        try {
            PrintStream dump = new PrintStream("dump_input_itemsets.txt");
            System.setOut(dump);

            for (Map.Entry<String, List<Itemset>> subApiItemsets : usagesBySubApi.entrySet()) {
                String subApi = subApiItemsets.getKey();
                System.out.println("Printing frequencies for sub-API: " + subApi);

                Map<Itemset, Integer> freqAcrossProjs = new HashMap<>();
                for (Itemset itemset : subApiItemsets.getValue()) {
                    freqAcrossProjs.put(itemset, freqAcrossProjs.getOrDefault(itemset, 0) + 1);
                }

                int i = 1;
                for (Map.Entry<Itemset, Integer> freqOfItemset : freqAcrossProjs.entrySet()) {
                    String items = "{" + String.join(",", freqOfItemset.getKey().getItems()) + "}";
                    // Prints "id_, {...items}, size, freq"
                    System.out.println("id" + i + ","
                            + freqOfItemset.getKey().size() + ","
                            + freqOfItemset.getValue() + ","
                            + items
                    );
                    ++i;
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            System.setOut(originalOut);
        }
    }

    private static List<Itemset> takeOneItemsetFromEachProject(HashMap<String, List<Itemset>> rawProjectUsages) {
        List<Itemset> allUsages = new ArrayList<>();

        Map<String, Integer> subApiProjectFreq = new HashMap<>();
        for (String subApi : Configuration.properties.api().subApi().prefixes()) {
            int freq = 0;

            // For each project
            for (Map.Entry<String, List<Itemset>> usage : rawProjectUsages.entrySet()) {
                if (usage.getValue().size() < 1) {
                    continue;
                }

                Set<Itemset> uniqueItemsetsPerProject = new HashSet<>(usage.getValue());
                boolean found = false;
                for (Itemset itemset : uniqueItemsetsPerProject) {
                    for (String item : itemset.getItems()) {
                        if (item.contains(subApi)) {
                            found = true;
                            break;
                        }
                    }
                    if (found) break;
                }

                // Calculates once per project
                if (found) {
                    ++freq;
                }
            }

            if (subApiProjectFreq.containsKey(subApi)) {
                System.out.println("Oh uh");
                System.exit(1);
            }

            subApiProjectFreq.put(subApi, freq);
        }

        System.out.println("-------------------------");
        for (String subApi : subApiProjectFreq.keySet()) {
            System.out.println("Sub-API " + subApi + " appears in " + subApiProjectFreq.get(subApi) + " projects");
        }
        System.out.println("-------------------------");


        // Obtain frequent itemsets for each project
        int numProjectsSkipped = 0;
        for (Map.Entry<String, List<Itemset>> usage : rawProjectUsages.entrySet()) {
            if (usage.getValue().size() < 1) {
                ++numProjectsSkipped;
                continue;
            }

            Set<Itemset> uniqueItemsetsPerProject = new HashSet<>(usage.getValue());
            allUsages.addAll(uniqueItemsetsPerProject);
        }
        System.out.println("Skipped " + numProjectsSkipped + " projects because they are empty!");

        return allUsages;
    }

    private static void mineByAnnotations(HashMap<String, List<Itemset>> usagesBySubApi) throws FileNotFoundException {
        Miner miner = new Miner(
                Configuration.minSupp,
                Configuration.minConf,
                -1
        );

        // 1. We do not want to mine patterns of usages of annotations that appear very little,
        //    In other words, they should appear in at least X transactions.
        // 2. Remove usages that have non-target sub-APIs.
        HashMap<String, List<Itemset>> relevantUsages = new HashMap<>();
        usagesBySubApi.entrySet()
                .stream()
                .filter(entry -> entry.getValue().size() >= 10)
                .filter(entry -> Configuration.properties.api().subApi().prefixes().stream().anyMatch(subApi -> entry.getKey().contains(subApi)))
                .forEach(entry -> relevantUsages.put(entry.getKey(), entry.getValue()));

        // Mine
        long startMiningTime = System.currentTimeMillis();
        HashMap<String, CombinedResult> results = miner.trainPerAnnotation(relevantUsages);
        long endMiningTime = System.currentTimeMillis();

        // TODO: comes in 0.0.7
        // Remove rules where rule does not contain at least 1 element of sub-API (target sub-API element)
        for (Map.Entry<String, CombinedResult> resultForSubAPI : results.entrySet()) {
            String subApi = resultForSubAPI.getKey();

            // Rules to remove
            List<FrequentItemset> freqItemsetsSubApi = new ArrayList<>(resultForSubAPI.getValue().getFrequentItemsets());
            freqItemsetsSubApi = freqItemsetsSubApi.stream()
                    .filter(r -> Heuristics.containsTargetSubApiPrefix(r, subApi))
                    .collect(toList());

            // Retain only relevant rules
            resultForSubAPI.getValue().getFrequentItemsets().retainAll(freqItemsetsSubApi);
        }

        // Merge all frequent itemsets rules together & run maximality filter over the union
        List<FrequentItemset> allFrequentItemsets = results.values()
                .stream()
                .map(CombinedResult::getFrequentItemsets)
                .flatMap(List::stream)
                .collect(toList());
        allFrequentItemsets = Miner.getMaximalFreqItemsetsLocal(allFrequentItemsets);

        int totalNumOfFreqItemsets = allFrequentItemsets.size();
        System.out.println("... Total number of frequent itemsets -> " + totalNumOfFreqItemsets);

        // Keep only rules with at least 1 MP usage
        long startMpSortTime = System.currentTimeMillis();
        List<FrequentItemset> mpFreqItemsets = allFrequentItemsets.stream().filter(Heuristics::containsTargetAPIPrefix).collect(toList());
        long endMpSortTime = System.currentTimeMillis();
        System.out.println("... Filtered frequent itemsets without target APIs -> " + mpFreqItemsets.size());

        // Remove rules that are semantically incorrect
        long startSemanticSortTime = System.currentTimeMillis();
        List<FrequentItemset> clearFreqItemsets = mpFreqItemsets.stream().filter(Heuristics::isSemanticallyOk).collect(toList());
        long endSemanticSortTime = System.currentTimeMillis();
        System.out.println("... Remove freq. itemsets that are semantically incorrect -> " + clearFreqItemsets.size());

        // Remove required annotation params because compiler can catch these
        long startRemoveRequiredParams = System.currentTimeMillis();
        // TODO: comes in 0.0.8
        List<FrequentItemset> finalFreqItemsets = Heuristics.filterRequiredParams(clearFreqItemsets);
        long endRemoveRequiredParams = System.currentTimeMillis();
        System.out.println("... Removed required annotation parameters");

        // Remove frequent itemsets of size 2
        // TODO: comes in 0.0.9
        finalFreqItemsets = finalFreqItemsets.stream().filter(fi -> fi.size() >= 2).collect(toList());
        System.out.println("... Removed freq. itemsets of size < 2 -> " + finalFreqItemsets.size());

        // Now take one rule per itemset
        List<AssociationRule> uniqueRules = Miner.getOneRulePerFreqItemset(miner.getAllAssociationRules(), finalFreqItemsets);

        //Rearrange consequent
        uniqueRules.forEach(Heuristics::rearrangeConsequent);

        // Check final rules if they have been mined previously and labeled.
        uniqueRules.forEach(r -> {
            String label = RulesDatabase.getLabel(r);
            String version = RulesDatabase.getVersion(r);

            r.setStatus(label);
            r.setVersion(version);
        });

        // Stats on overall mining (all sub-APIs)
        AggregateData data = new AggregateData(
                usagesBySubApi.values().size(), // all input itemsets
                allFrequentItemsets.size(),
                uniqueRules.size(),
                mpFreqItemsets.size(),
                clearFreqItemsets.size(),
                0,
                0,
                finalFreqItemsets.size(),
                0
        );

        // Let's print the stuff
        ResultPrinter printer = new ResultPrinter(data);

        for (Map.Entry<String, CombinedResult> result : results.entrySet()) {
            String subApiShortName = result.getKey().substring(result.getKey().lastIndexOf('.') + 1).trim();

            if (Configuration.dumpInputItemsets) {
                List<Set<String>> inputItemsets = usagesBySubApi.get(result.getKey())
                        .stream()
                        .map(Itemset::getItems)
                        .collect(toList());

                // Dump all input itemsets for the sub-API
                printer.printInputItemsets(
                        subApiShortName,
                        inputItemsets
                );
            }
        }

        // Dump results for all sub-APIs together
        if (Configuration.dumpFrequentItemsets) {
            // TODO: Was just frequent itemsets.
            printer.printFrequentItemsets("all", finalFreqItemsets);
        }
        if (Configuration.dumpCandidateRules) {
            printer.printCandidateRules("all", uniqueRules);
        }

        // Dump all candidate rules from all sub-APIs at once
        System.out.println("Writing " + uniqueRules.size() + " association rules out of "
                + finalFreqItemsets.size() +
                " post-processed freq. itemsets (in total, mined " +
                totalNumOfFreqItemsets + " freq. itemsets)" +
                "to a JSON file!");
        RulesDatabase.writeToJSON(uniqueRules);

        System.out.println("In total, mined: ");
        System.out.println("\tFrequent itemsets (raw) = " + totalNumOfFreqItemsets);
        System.out.println("\tFrequent itemsets (final, post-processed) = " + finalFreqItemsets.size());
        System.out.println("\tAssociation rules = " + uniqueRules.size());
    }

    private static HashMap<String, List<Itemset>> divideUsagesByAnnotations(List<Itemset> allUsages) {
        /*
         * Given list of usages as sets of items, e.g.:
         *     [{ A, B, C }, { A,D }]
         *
         * We want to distribute those into buckets of "@A -> list of usages where @A appears", e.g.:
         *     A : [{ A, B, C }, {A, D}]
         *     B : [{ A, B, C }]
         *     C : [{ A, B, C }]
         *     D : [{ A, D }]
         */
        HashMap<String, List<Itemset>> usagesByAnnotation = new HashMap<>();
        Collection<String> apiPrefixes = Configuration.properties.api().prefixes();
        SubApiConfiguration subApiConfig = Configuration.properties.api().subApi();

        for (Itemset itemset : allUsages) {
            Set<String> items = itemset.getItems();
            Set<String> annotations = new HashSet<>();
            for (String item : items) {
                if (apiPrefixes.stream().anyMatch(item::contains)) {
                    subApiConfig
                            .extractMatchingAnnotation(item)
                            .ifPresent(annotations::add);
                }
            }

            for (String annotation : annotations) {
                List<Itemset> annotationUsages = usagesByAnnotation.computeIfAbsent(annotation, t -> new ArrayList<>());
                annotationUsages.add(itemset);
            }
        }
        return usagesByAnnotation;
    }

    private static void parseConfiguration(String[] args) throws IOException {
        // --config [configPath]
        // --targetProjectsDir [path]
        // --libSources [path]
        // --exportDir [path]

        final Map<String, String> parameters = new HashMap<>();
        // initialize the slots for params
        asList("--config", "--targetProjectsDir", "--libSources", "--exportDir")
                .forEach(param -> parameters.put(param, null));

        if (args.length != parameters.size() * 2) { // *2 because each parameter needs to have a value too
            System.err.println("Expected four parameters: ");
            System.err.println("PROGRAM --config [configPath] --targetProjectsDir [path] --libSources [path] --exportDir [path]");
            System.exit(1);
        }

        for (int i = 0; i < parameters.size() * 2; i += 2) {
            if (args[i].startsWith("--")) {
                String option = args[i].trim();

                if (parameters.containsKey(option)) {
                    parameters.put(option, args[i + 1]);
                } else {
                    throw new RuntimeException("Unexpected option: " + option);
                }
            }
        }

        // all three parameters are required, thus, they all must be non-null
        if (parameters.values().stream().anyMatch(Objects::isNull)) {
            System.err.println("Expected four parameters: ");
            System.err.println("PROGRAM --config [configPath] --targetProjectsDir [path] --libSources [path] --exportDir [path]");
            System.exit(1);
        }

        String contents = Files.lines(Paths.get(parameters.get("--config"))).collect(Collectors.joining("\n"));
        Configuration.properties = ConfigurationProperties.readConfigJson(contents);
        Configuration.properties.targetProjectsDir(parameters.get("--targetProjectsDir"));
        Configuration.properties.libSources(Collections.singletonList(parameters.get("--libSources")));
        Configuration.properties.exportDir(parameters.get("--exportDir"));
    }

    private static void readProjectsFiles() {
        File project = new File(Configuration.properties.targetProjectsDir());

        int projectsWithBeans = 0;
        int projectsSkipped = 0;
        int totalNumOfBeans = 0;
        int numOfBeansConsidered = 0;
        int totalProjects = 0;

        // Parse library sources so we get fully-qualified names
        List<File> libs = Configuration.properties.libSources()
                .stream()
                .map(File::new)
                .collect(toList());

        // Read projects
        builder = new AnnotationUsageGraphBuilder();
        File[] files = requireNonNull(project.listFiles());

        List<File> projectDirectories = Arrays.stream(files).filter(File::isDirectory).collect(toList());
        totalProjects = projectDirectories.size();

        int progress = 1;

        for (File f : projectDirectories) {
            List<File> sourceFiles = new ArrayList<>();
            List<File> configFiles = new ArrayList<>();
            List<File> beans = new ArrayList<>();

            listFilesForFolder(f, sourceFiles, configFiles, beans);
            boolean parsed = false;
            try {
                System.out.printf("[%d/%d] Parsing %s...", progress, totalProjects, f.getName().toLowerCase());
                parsed = builder.generateUsageGraphsPerProject(f, libs, sourceFiles, configFiles, beans);
                System.out.println("Done!");
            } catch (RuntimeException e) {
                System.out.println("\nFailed to parse: " + f.getPath());
            }
            // INFO: To get info on how many projs have beans.xml
            if (!parsed) {
                ++projectsSkipped;
            } else {
                if (beans.size() > 0) {
                    ++projectsWithBeans;
                    numOfBeansConsidered += beans.size();
                }
            }
            progress += 1;

            totalNumOfBeans += beans.size();
        }
        System.out.println("There are " + projectsWithBeans + " projects that we used and that are with beans.xml");
        System.out.println("There are " + totalNumOfBeans + " number of beans.xml files");
        System.out.println("There are " + numOfBeansConsidered + " number of beans.xml files that we take into account");
        System.out.println("Could not parse " + builder.getCountUnparseableFiles() + " beans.xml files");
        System.out.println("Finally, I could parse " + builder.getUsagesAsMap().keySet().size() + " out of " + totalProjects + " projects given.");

        System.out.println("*************************\nDid not parse "
                + projectsSkipped + " projects because they are toy projects."
                + "\n*************************"
        );
    }

    private static void listFilesForFolder(final File folder, List<File> sourceFiles, List<File> configFiles, List<File> beans) {
        if (folder.listFiles() == null) {
            return;
        }

        for (final File file : requireNonNull(folder.listFiles())) {
            if (file.isDirectory()) {
                listFilesForFolder(file, sourceFiles, configFiles, beans);
            } else {
                if (file.getName().endsWith(".java")) {
                    sourceFiles.add(file);
                } else if (Configuration.properties.api().prefixes().contains("org.eclipse.microprofile")
                        && file.getName().endsWith("microprofile-config.properties")) {
                    configFiles.add(file);
                } else if (file.getName().equals("beans.xml") && file.getAbsolutePath().contains("src/main")) {
                    // beans.xml should be inside src/main
                    beans.add(file);
                }
            }
        }
    }
}
