package util.labeler;

import com.google.common.reflect.TypeToken;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
//import miner.AssociationRule;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class RulesFromExcelReader {
    // Just to get hashcodes of labeled rules. Used to semi-automatically convert rules from Excel to JSON.
    public static void main(String[] args) {
        String jsonFileName = "rules_v0.0.0.json";

        Gson gson = new Gson();
        List<RulesDatabase.LabeledRule> rules = new ArrayList<>();
        try (Reader reader = new FileReader(jsonFileName)) {
            Type rulesListType = new TypeToken<ArrayList<RulesDatabase.LabeledRule>>(){}.getType();

            rules = gson.fromJson(reader, rulesListType);
            if (rules == null) {
                System.out.println("[static StatsCalculator] JSON file is empty!");
                rules = new ArrayList<>();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Convert rules to JSON
        try (Writer writer = new FileWriter(jsonFileName)) {
            gson = new GsonBuilder()
                .disableHtmlEscaping()
                .setPrettyPrinting()
                .create();

//            gson.toJson(rulesWithCorrectCodes, writer);
        } catch (IOException e) {
            System.err.println("Could not write rules to the JSON file");
        }

    }
}

