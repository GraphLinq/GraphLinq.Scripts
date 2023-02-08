import os
import git
import subprocess

directory = '.'
repositories = ''
changes=''
branches=''
gitst=''

def is_git_repo(path):
    try:
        _ = git.Repo(path).git_dir
        return True
    except git.exc.InvalidGitRepositoryError:
        return False

def has_git_diff(path):
    try:
        r = git.Repo(path).diff
        print("HIIIII")
        print(r)
        return r
    except git.exc.InvalidGitRepositoryError:
        print("never")
        return False

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        print()
    else:
        print("directory")
        print(f)
        print()
        s = is_git_repo(f)
        if (s):
            #diff = has_git_diff(f)
            #changes = changes + "Repo: {}\n{}\n\n" .format(f, diff)
            repositories = repositories + f + "\n"
            #st = os.system("cd {} && git status" .format(f))
            cmd = "cd {} && git status" .format(f)
            st = subprocess.check_output(cmd, shell=True)
            print("OUT", st)
            #clean = (st.find('nothing to commit'))
            #print(clean)
            #if (clean):
            #    print("clean")
            #else:
            #    print("else")
            #    #gitst = str(gitst) + str(f) + "\n" + str(st) + "\n\n"
        else:
            print("No a git repo")
        print("DONE")
        print()

if (repositories):
    print("Repositories found:")
    print(repositories)
    print()
    print("Changes found:")
    print(changes)
    print()
    print("git st:")
    print(gitst)
    print()

