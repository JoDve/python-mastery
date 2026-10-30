# Write a program that walks through a folder tree and searches for files with a certain file extension 
# (such as .pdf or .jpg). Copy these files from their current location to a new folder.

from pathlib import Path
import os, shutil, re

# Ask the user to enter the path of the directory that want to copy and type of file
path_folder = Path(input('\nEnter the path of the folder that you want to analize: \n>'))
extension_file = input('\nEnter the extension (.txt, .pdf) of type of file you want to copy. \n>').lower()
print('')
if extension_file[0] != '.':
    extension_file = '.' + extension_file

# Create the new folder (directory) and copy all files into the path to the new folder
if path_folder.exists(): # Failfast to confirm if the path exists

    num = 1 # Set number to add the version of folder

    # Create the new folder
    while True:
        # If the folder doesn't exist create a base folder
        if not (path_folder / f'{extension_file[1:]}_folder').exists():
            (path_folder / f'{extension_file[1:]}_folder').mkdir(parents=True)
            name_directory = f'{extension_file[1:]}_folder' # Store the base-name of folder in name_directory variable
            break
        # If base folder exists add a new version folder
        elif not (path_folder / f'{extension_file[1:]}_folder{num}').exists():
            (path_folder / f'{extension_file[1:]}_folder{num}').mkdir(parents=True)
            name_directory = f'{extension_file[1:]}_folder{num}' # Store the version-name of folder in name_directory variabler
            break
        num += 1 # Add new versions if they exists
    
    # Create a regex to find based folder or old versions
    pattern_name = re.compile(rf'{extension_file[1:]}_folder\d*')

    # Walks through of folder tree and searches for files with extension
    for folder_name, subfolders, filenames in os.walk(path_folder):
        # valuate if the pattern is into folder_name
        if pattern_name.search(folder_name) is None:
            for file in filenames:
                if (path_folder / file).suffix == extension_file:
                    # Copy the file to the new folder in the path directory
                    print(f'Copying {file} from {folder_name} in {name_directory}')
                    shutil.copy(Path(folder_name) / file, path_folder / name_directory)
    print('\nDone')
else:
    print(f"{path_folder} doesn't exists\n")