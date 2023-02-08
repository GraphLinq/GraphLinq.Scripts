import os
import subprocess
directory = '.'
 
for dirname in os.listdir(directory):
    f = os.path.join(directory, dirname)
    # checking if it is a file
    if os.path.isdir(f):
        print("------------------")
        print("Directory")
        print(f)
        print()
        if os.path.isdir(f + "\.git"):
            print("1" + f + "\.git")
            output = subprocess.check_output('git remote -v', shell=True)
            print("2" + output)
            output = output.decode('utf-8')
            print("3" + output)
            output = output.replace('origin', '').replace('(fetch)', '').replace('(push)', '').replace(' ', '')
            print("4" + output)
            output = output.split('\n')[0]
            print("5" + output)
            print("DONE" + output)
        else:
            print('Current directory is not a git repo')
    else:
        print("Not a directory")
        print(f)
        print()

