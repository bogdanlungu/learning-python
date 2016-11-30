"""
Renames all the files from a given directory by removing the numbers from
their names - example boston221.jpg will become boston.jpg
"""

import os
from string import digits

# define the function


def rename_files():


    # get the file names from a folder

    file_list = os.listdir(r"C:\Python\tmp\prank")
    saved_path = os.getcwd()  # get the current working directory

    print("Current working directory is " + saved_path)

    os.chdir(r"C:\Python\tmp\prank")  # the folder that contains the files



    # rename files

    remove_digits = str.maketrans('', '', digits)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(remove_digits))

    os.chdir(saved_path)

rename_files()
