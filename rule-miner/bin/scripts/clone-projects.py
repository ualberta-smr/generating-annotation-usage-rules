import os
import sys
import git
from common import extractParameterFromCommandLineArgs, getEnv

def readProjectsList(filename):
    """
    Read the file that contains a list of projects to clone from.
    """
    projs = []

    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        lines = list(filter(lambda x: len(x) > 0, lines))
        
        i = 0
        while i < len(lines):
            url = lines[i]
            if lines[i + 1].startswith("--"):
                commit = None
                i += 2
            else:
                commit = lines[i + 1]
                i += 3

            if '.git' in url:
                if 'git@github.com:' in url:
                    projs.append((url.split(':')[1], commit))
                else:
                    projs.append(('/'.join(url.split('/')[-2:]), commit))
    return projs

if __name__ == "__main__":
    if extractParameterFromCommandLineArgs("--help", True):
        print("clone-projects --file [file_path]")
        print("     --file      - path to the file that contains GitHub links of the projects that need to be downloaded")
        print()
        sys.exit(0)

    file_path = extractParameterFromCommandLineArgs("--file")
    if file_path is None:
        print("ERROR: expected --file parameter")
        print("help:")
        print("clone-projects --file [file_path]")
        print("     --file      - path to the file that contains GitHub links of the projects that need to be downloaded")
        print()
        sys.exit(1)

    target_dir = getEnv("TARGET_PROJECTS_DIR")

    # Read rules from TXT
    projects = readProjectsList(file_path)
    size = len(projects)
    # Clone each repo and checkout the target commit
    for i, (proj, commit) in enumerate(projects):
        try:
            print(f"[{i + 1}/{size}] Cloning the repo {proj}...", end='', flush=True)
            # Reference: https://stackoverflow.com/a/44483212
            url = "https://:@github.com/{0}".format(proj)
            where = target_dir + "/{0}".format('#'.join(proj.split('/')))

            if os.path.exists(where):
                print("Already exists!", flush=True)
                commit = None # to skip the commit checkout at the end of the loop
                continue

            repo = git.Repo.clone_from(
                url, 
                where, 
                no_checkout=True
            )
            print("Done!", flush=True)

            for submodule in repo.submodules:
                print(f"    Cloning the submodule...", end='', flush=True)
                submodule.update(init=True)
                print(f"Done!", flush=True)
        except git.exc.InvalidGitRepositoryError:
            print("-" * 50)
            print("Could not clone " + proj)
            print("-" * 50)
            continue
        except git.exc.GitCommandError as e:
            print("-" * 50)
            print(e)
            print("Could not clone " + proj)
            print("Check if it exists (i.e., public)?")
            print("-" * 50)
            continue
        
        if commit:
            try: 
                repo.git.checkout(commit)
            except git.exc.GitCommandError:
                print("-" * 50)
                print("Could not check out commit {0} for {1}".format(commit, proj))
                print("-" * 50)
                continue

