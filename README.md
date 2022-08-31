# Generating Annotation Usage Rules

The artifact repo for the paper:

> A Human-in-the-loop Approach to Generate Annotation Usage Rules: A Case Study with MicroProfile. Mansur Gulami, Ajay Kumar Jha, Sarah Nadi, Karim Ali, Yee-Kang Chang, Emily Jiang. CASCONxEVOKE '22.

In this work, we create a human-in-the-loop pipeline to produce accurate annotation usage rules. The pipeline includes the following steps:
1. Mining candidate annotation usage rules (see [this repo](https://github.com/ualberta-smr/MiningAnnotationUsageRules) for more details)
2. Validating the candidate usage rules to produce confirmed usage rules (using the Rule Validation Tool)
3. Using confirmed usage rules for misuse detection purposes (using the Violation Detector)

The last two tools are developed and maintained by [Mansur Gulami](https://github.com/MensurOwary).

# Repo structure 
The repository consists of 2 projects:

1. [Rule Validation Tool](./ui)
    1. [frontend](./ui/frontend/)
    2. [backend](./ui/backend)
2. [Violation Detector](./violation-detector/)
    1. [violation detection core library](./violation-detector/violation-detection): the main violation detection component that uses JavaParser to find violations of the rules
    2. [the maven plugin](./violation-detector/violation-detector-maven-plugin): the Maven plugin that uses the violation detection core library

To get started with these tools, please read the README files present in the relevant folders.

# User study materials

During the user study, we presented 18 total rules to four API experts. The [presented_candidate_rules](./artifacts/presented_candidate_rules/) directory shows all the mined candidate rules we presented to the user study participants. Initially, we planned the user study around six people, but ended up only finding four API experts. You can find the unused rulesets in the same directory as well. Rules are tagged by the MicroProfile APIs that the rule is related to. This information was manually added later, so that we could distribute rules based on the expertise of our participants.

You can find the confirmed rules [here](./artifacts/confirmed_rules.txt). You can also find the analysis of each confirmed rule [here](./artifacts/confirmed_rules_analysis.md)

# Misuse Detection Experiment

We used the following [12 rules](./artifacts/misuse_detector_experiment_confirmed_rules_in_rulepad.json). You can also find the original JSON format of those rules [here](./artifacts/misuse_detector_experiment_confirmed_rules.json). Simply putting the rules into the `src/main/resources` folder of the [Maven plugin](./violation-detector/violation-detector-maven-plugin/src/main/resources/) and building using `mvn clean package` equips the plugin with these rules.

# Credit
All credit related to RulePad goes to [Sahar Mehrpour](https://github.com/SaharMehrpour)