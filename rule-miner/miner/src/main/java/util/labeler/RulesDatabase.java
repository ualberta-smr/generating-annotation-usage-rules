package util.labeler;

import com.google.common.reflect.TypeToken;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.annotations.SerializedName;
//import miner.AssociationRule;
import miner.AssociationRule;
import miner.config.Configuration;

import java.io.*;
import java.lang.reflect.Type;
import java.util.*;
import java.util.stream.Collectors;

// Implemented as an interface to a JSON file
public class RulesDatabase {

    private static Map<String, List<LabeledRule>> rules;

    public static class LabeledRule {
        @SerializedName("id")
        private int id; // hashcode

        @SerializedName("antecedent")
        private Set<String> antecedent;

        @SerializedName("consequent")
        private Set<String> consequent;

        @SerializedName("label")
        public String label;

        @SerializedName("sameAs")
        private int sameAs;

        public LabeledRule(int id, Set<String> antecedent, Set<String> consequent, String label) {
            this.id = id;
            this.antecedent = antecedent;
            this.consequent = consequent;
            this.label = label;
        }

        public String label() {
            return label;
        }

        public Set<String> antecedent() {
            return antecedent;
        }

        public Set<String> consequent() {
            return consequent;
        }

        public int id() {
            return id;
        }

        public int sameAs() {
            return sameAs;
        }

        @Override
        public String toString() {
            return "LabeledRule{" + "\n" +
                    "\tid = " + id + "\n" +
                    "\tantecedent = " + antecedent + "\n" +
                    "\tconsequent = " + consequent + "\n" +
                    "\tlabel = '" + label + '\'' + "\n" +
                    '}';
        }

        public static LabeledRule toLabeledRule(AssociationRule r) {
            return new LabeledRule(r.hashCode(), r.antecedent(), r.consequentAsSingletonSet(), r.status());
        }
    }


    // Static initialization for the rules
    static {
        Gson gson = new Gson();

        rules = new HashMap<>();

        File dir = new File(".");
        File[] foundFiles = dir.listFiles((dir1, name) -> name.startsWith("rules_v"));

        assert foundFiles != null;
        for (File file : foundFiles) {
            String fileName = file.getName();

            // skip rules_v and extract version
            String version = fileName.substring(7, fileName.lastIndexOf("."));

            // read rules
            List<LabeledRule> rulesForAVersion = new ArrayList<>();

            try (Reader reader = new FileReader(fileName)) {
                Type rulesListType = new TypeToken<ArrayList<LabeledRule>>() {
                }.getType();

                rulesForAVersion = gson.fromJson(reader, rulesListType);
                if (rulesForAVersion == null) {
                    System.out.println("[static RulesDatabase] JSON file is empty!");
                    rulesForAVersion = new ArrayList<>();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }

            // put them into map (rules from each specific version of the tool)
            rules.put(version, rulesForAVersion);
        }
    }

    public static String getLabel(AssociationRule rule) {
        LabeledRule r = getLabeledRule(rule.hashCode());
        if (r != null) {
            return r.label();
        } else {
            return "unknown";
        }
    }

    public static String getVersion(AssociationRule rule) {
        String v = getVersion(rule.hashCode());
        if (v != null) {
            return v;
        } else {
            return Configuration.version;
        }
    }

    public static void writeToJSON(List<AssociationRule> rules) {
        // Gotta make sure this is called after we process all final rules, s.t. we put new rules into JSON.
        String filename = String.format("%s/candidate_rules_%d.json", Configuration.properties.exportDir(), System.currentTimeMillis());
        File outputFile = new File(filename);

        // Convert association rules to labeled rules (basically, label them)
        // In case of frequent itemsets, just put all in antecedent and make consequent empty.
        List<LabeledRule> labeledRules = rules.stream()
                .map(LabeledRule::toLabeledRule)
                .collect(Collectors.toList());

        // Write current version rules to a new JSON file
        try (Writer writer = new FileWriter(outputFile)) {
            new GsonBuilder()
                    .disableHtmlEscaping()
                    .setPrettyPrinting()
                    .create()
                    .toJson(labeledRules, writer);
            System.out.println("Saved the candidate rules to: " + filename);
        } catch (IOException e) {
            System.err.println("Could not write rules to the JSON file");
            e.printStackTrace();
        }

    }

    private static String getVersion(int hashcode) {
        for (Map.Entry<String, List<LabeledRule>> prevRules : rules.entrySet()) {
            // Check if a rule exists for a given version
            Optional<LabeledRule> labeledRule = prevRules.getValue().stream()
                    .filter(rule -> hashcode == rule.id())
                    .findAny();

            if (labeledRule.isPresent()) {
                return prevRules.getKey();
            }
        }
        return null;
    }

    private static LabeledRule getLabeledRule(int hashcode) {
        for (Map.Entry<String, List<LabeledRule>> prevRules : rules.entrySet()) {
            // Check if a rule exists for a given version
            Optional<LabeledRule> labeledRule = prevRules.getValue().stream()
                    .filter(rule -> hashcode == rule.id())
                    .findAny();

            if (labeledRule.isPresent()) {
                return labeledRule.get();
            }
        }
        return null;
    }
}
