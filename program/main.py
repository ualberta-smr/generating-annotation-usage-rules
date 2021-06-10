import sys
import subprocess
import os
import json

RESULTS_FILE = "results.json"
RULES_FILE = "rules.json"
VIOLATIONS_FILE = "violations.json"

def cleanup():
    os.remove(RESULTS_FILE)
    os.remove(RULES_FILE)

def run(args):
    return subprocess.run(args, capture_output=True)


def print_violation_stats():
    with open(VIOLATIONS_FILE) as f:
        violations = json.load(f)
        count = len(violations)
        print("Found %d violations" % count)


# python main.py ..\rules-to-grammar\candidate-rules.json C:\Users\mensu\Downloads\broker
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("There should be 2 args: <candidate rules path> <project path>", file=sys.stderr)
        exit(2)

    _, candidateRulesFile, projectFolder = sys.argv

    # given candidate rules, convert them to grammar
    print("Converting candidate rules to RulePad grammar...", end='')
    run(["python", "../rules-to-grammar/main.py", candidateRulesFile, RESULTS_FILE])
    print("Done")

    # given grammar, convert them to xpath
    print("Converting RulePad grammar to XPath queries...", end='')
    run(["node", "../grammar-to-xpath/index.js", RESULTS_FILE, RULES_FILE])
    print("Done")

    # given xpath rules and a project, detect violations
    print("Detecting violations...", end='')
    run(["python", "../violation-detector/main.py", RULES_FILE, projectFolder, VIOLATIONS_FILE])
    print("Done")

    print_violation_stats()

    cleanup()