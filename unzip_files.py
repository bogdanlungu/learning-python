"""This program reads all the zip archives from a folder
and unzips them in a folder with the same name.
You need to give the path to the folder in the folder variable."""
# pylint: disable=C0103

import os
import zipfile
#from pathlib import Path


def count_zips(the_folder):
    """Checks to see if there are zip files inside the folder and returns hoe many"""
    zip_list = os.listdir(the_folder)
    zip_files = []

    for file_name in zip_list:
        if file_name.endswith('.zip'):
            zip_files.append(file_name)

    number_of_archives = len(zip_files)
    if number_of_archives > 0:
        # print(number_of_archives)
        #print("There are " + str(number_of_archives) + " zips in this folder")
        return number_of_archives
    else:
        print("There are no zip files in this folder.")

    return number_of_archives


def unzip_files(the_folder, files_number):
    """Unzip the files from the given folder, received two parameters:
    the folder and the number of zip files inside the folder"""

    if files_number > 0:
        print("There are " + str(files_number) +
              " zips in this folder, starting to unzip ...")
        zip_list = os.listdir(the_folder)
        for file_name in zip_list:
            if file_name.endswith('.zip'):
                path_to_zip_file = os.path.join(the_folder, file_name)
                folder_to_extract = os.path.splitext(path_to_zip_file)[0]

                zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
                zip_ref.extractall(folder_to_extract)
                zip_ref.close()

                # print(os.path.splitext(path_to_zip_file)[0])
                print(file_name + " was unzipped")
                # print(path_to_zip_file)
    else:
        return  # Nothing to do


# Run the program
folder = r"C:\Tmp\folder"
count_files = count_zips(folder)
unzip_files(folder, count_files)
