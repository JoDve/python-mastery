# Write a program that finds all files with a given prefix, such as spam001.txt, 
# spam002.txt, and so on, in a single folder and locates any gaps in the numbering
# (such as if there is a spam001.txt and a spam003.txt but no spam002.txt). 
# Have the program rename all the later files to close this gap.

from pathlib import Path
import shutil

folder_path = Path.home() / 'spam/test'
prefix_file = input('\nEnter the prefix (such spam, filename without suffix) of filename that you want to search\n>')

file_list = []
num = 1

# Find all files with the given prefix
for filename in (folder_path).glob(f'{prefix_file}*.*'):
    # If filename is file add to the name_list.
    if filename.is_file():
        file_list.append(filename)
file_list.sort()


# Find the gaps and rename the files to close gaps in the numeration
for file_path in file_list:
    if str(num).zfill(3) != file_path.stem[-3:]:
        shutil.move(file_path, folder_path / (file_path.stem[:-3] + str(num).zfill(3) + file_path.suffix))
        num += 1
    else:
        num += 1

print('\nThe numering of files had been verify and renumering to close gaps')