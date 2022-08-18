# Generating Annotation Usage Rules

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

# Credit
All credit related to RulePad goes to [Sahar Mehrpour](https://github.com/SaharMehrpour)