# Write a program that lists all the files and directories in the current directories, as well as all files
# and directories in its sub-directories and so on.

import os

def list_files_and_directories(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
        for dir in dirs:
            print(os.path.join(root, dir))

if __name__ == "__main__":
    current_directory = os.getcwd()
    list_files_and_directories(current_directory)