#  It's not uncommon for a fer unneeded but humongous files or folders to take up the bulk 
# of the space on your hard drive. If you're trying to free up room on your computer
# , it's more effective to indetify the largest unneeded files first
# 
# Write a program that walk through a folder tree and searches for exceptionally large files 
# or folders-say, ones that have a file size of more than 100mb. (Remember that, to get a file's size,
# you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.

from pathlib import Path
import os
import sys

# Ask the user enter the path of folder
path_folder = Path(input('\nEnter the path of folder that you want to analyzed for largers files or subfolder\n>')).absolute()

MB = 1024 ** 2
THRESHOLD_MB = 100.0

if not path_folder.exists():
    print('\nPath doesn\'t exists')
    sys.exit()

list_files = []
list_folders = []
# Walk through a folder tree
for folder_name, subfolder, filenames in os.walk(path_folder):
    current_dir = Path(folder_name)
    folder_size = 0.0
    # Searches for exceptionally large files or folders-say > 100mb
    for filename in filenames:
        file_path = (current_dir / filename)
        try:
            file_size = os.path.getsize(file_path) / MB
        except OSError:
            # Skip broken Linux symlinks or restricted files without creashing
            continue
        folder_size += file_size
        # Add files if its size is grather than 100
        if file_size >= THRESHOLD_MB:
            list_files.append(f'- {filename} ({file_size:.2f} MB) in {file_path}')

    # Add folder if its size is grather than 100
    if folder_size >= THRESHOLD_MB:
        list_folders.append(f'{folder_name} ({folder_size:.2f} MB)')

# Print results.
print('=========================================')
print('   The folders larger than 100 MB are:   ')
print('=========================================')
print('\n'.join(list_folders))
print('=========================================')
print('    The files larger than 100 MB are:    ')
print('=========================================')
print('\n'.join(list_files))