# Convert American-style dates (MM-DD-YYYY) to Eruropean-style (DD-MM-YYYY)

# 1. Seraches all filenames in the current working directory and subdirectories. use the os.walk() functions
# 2. Uses regex to identify filenames with the MM-DD-YYYY. asume the months and days use 2 digits
# (You won't find files named somenthing like 99-99-9999.txt)
# 3. When a filename is found, renames the file with the month and days swapped to make it European-style
# Use the shutil.move() function to do the renaming

from pathlib import Path
import re
import os
import shutil

cwd = Path.cwd() # Current working directory

# create the regex with the MM-DD-YYYY format
re_date = re.compile(r'''(
(.*)?#prefix
(\d{2})# Months
(-|/|\.)# Separator
(\d{2})# Days
(-|/|\.)# Separator
(\d{4})# Years
(.*)?#suffix
)''', re.VERBOSE)

manual_rev = []
# Searches all filenames in the current working directory and subdirectories with os.walk() function.

for folder_name, subfolders, filenames in os.walk(cwd):
    cur_folder = Path(folder_name) # Set the cur_folder variable with its path object
    for filename in filenames: # Walk through files
        match_o = re_date.search(rf'{filename}') 
        if match_o: # If filename matches with the regex, change the name
            file_path = cur_folder / filename
            group = match_o.groups()
            if int(group[2]) <= 12 and int(group[4]) <= 12:
                manual_rev.append(file_path)
                continue
            if int(group[2]) <= 12 and int(group[4]) > int(group[2]):
            
                try:
                    # Rename file with the month an days swapped. use shutil.move() function
                    shutil.move(file_path, cur_folder / rf'{group[1]}{group[4]}-{group[2]}-{group[6]}{group[7]}')
                except OSError:
                    # Skip the OS error.
                    continue

if manual_rev:
    print('\nFiles requiring manual review (ambiguos MM/DD <= 12):')
    for path in manual_rev:
        print(f'- {path}')