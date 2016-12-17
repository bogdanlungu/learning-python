"""This program reads all the files and subfolders
inside a folder and writes them in a txt file named content.txt"""
# pylint: disable=C0103

import os
from pathlib import Path

folder = r"C:\Tmp\folder"
content_file = folder + r"\content.txt"

check_file = Path(content_file)
if check_file.is_file():
    os.remove(content_file)

file = open(folder + r"\content.txt", "w")
file_list = os.listdir(folder)
for file_name in file_list:
    print(file_name)
    file.write(file_name + "\n")

file.close()
