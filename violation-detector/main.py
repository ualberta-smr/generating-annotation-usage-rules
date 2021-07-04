# idea is the following
# 0. Given a project, generate xml files from the files using srcML
# 1. Take the rules.json file, and check the rules against any project.
# 2. Report on the violations.

import json
import sys
from subprocess import Popen, PIPE, run
from typing import *
from dataclasses import *
from utils import *
from violation_details import *
from position_finder import *


def main(args: List[str]):
    rules_file, path_to_project, violations_output = args
    rules = list(get_rules(rules_file))
    print("Rules available: %d" % len(rules))

    filenames = get_files(path_to_project, 'java')
    print("Files available: %d" % len(filenames))
    
    file_xml_dict = execute_srcml(filenames)

    d = list(find_violations(file_xml_dict, rules, len(filenames)))

    find_positions_of_violations(d)

    execute_srcml_with_position(d)

    with open(violations_output, "w+") as f:
        json.dump(list(d), f, indent=4)


def execute_srcml(filenames):
    for filename in filenames:
        r1 = Popen(f"java -jar ../type-resolution/type-resolver.jar \"{filename}\" ../type-resolution/lib", stdout=PIPE)
        r2 = Popen(f"srcml --language Java --position", stdin=r1.stdout, stdout=PIPE)
        result = r2.communicate()
        if r2.returncode == 0:
            xml = result[0].decode('UTF-8')
            yield (filename, xml)

def execute_srcml_with_position(violations):
    for violation in violations:
        file = violation["file"]
        result = run(["srcml", file, "--position"], capture_output=True)
        if result.returncode == 0:
            for detail in violation["details"]:
                element = detail["element"]
                positions = get_positions(element, result.stdout.decode("UTF-8"))
                if positions:
                    detail["positions"] = positions[0], positions[1]


# 3 args:
# <rules path> <project path> <violations output>
if __name__ == '__main__':
    main(sys.argv[1:])
