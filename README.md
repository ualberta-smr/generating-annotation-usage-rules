# Rule Validation Tool + Violation Detector

Developed and maintained by [Mansur Gulami](https://github.com/MensurOwary).

The repository consists of 2 projects:

1. Rule Validation Tool
    1. [frontend](./ui/frontend/)
    2. [backend](./ui/backend)
2. Violation Detector
    1. [violation detection core library](./violation-detector/violation-detection): the main violation detection component that uses JavaParser to find violations of the rules
    2. [the maven plugin](./violation-detector/violation-detector-maven-plugin): the Maven plugin that uses the violation detection core library


# Credit
All credit related to RulePad goes to [Sahar Mehrpour](https://github.com/SaharMehrpour)