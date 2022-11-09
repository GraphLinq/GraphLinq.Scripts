# Attempt to execute a `git pull` on all
# subdirectories of the current directory.

import os
directory = '.'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print("-- Ignoring file: {}" .format(filename))
    else:
        print()
        print("++ Processing directory: {}" .format(filename))
        os.system("cd {} && git pull" .format(filename))
        print("++ Completed directory: {}" .format(filename))
        print()
