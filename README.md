# API misuse detection process

Developed and maintained by [Mansur Gulami](https://github.com/MensurOwary).

The repository consists of 2 projects:

1. Rule authoring UI
    1. [ui](./ui): it allows users to edit, confirm, discard rules
    2. [ui-backend](./ui-backend): handles the backend needs (e.g. retrieving the next rule to label) of the UI
2. Violation Detection
    1. [violation detection library](./violation-detection): main violation detection component that uses JavaParser to find violations of the rules
    2. [maven plugin](./violation-detector-maven-plugin): the Maven plugin that uses the violation detection library


# Credit

All credit related to RulePad goes to [Sahar Mehrpour](https://github.com/SaharMehrpour)