# As an added challenge, write another program that can insert gaps into numbered files 
# (and bump up the numbers in the filenames after the gap) so that a new file can be inserted.

from pathlib import Path
import shutil
import sys

folder_path = Path.home() / 'spam/test'
prefix_file = input('\nEnter the prefix (such spam, filename without suffix) of filename that you want to search\n>')
gap = input('\nEnter the number of you want to add a gap\n>')

gap = gap.zfill(3)

print(gap)

file_list = []

# Find all files with the given prefix
for filename in (folder_path).glob(f'{prefix_file}[0-9][0-9][0-9].*'):
    # If filename is file add to the name_list.
    if filename.is_file():
        file_list.append(filename)
file_list.sort()

num = len(file_list)

if int(gap) > num:
    print('\nThe gap is outside the range of files\n')
    sys.exit()

# Find the gaps and rename the files to close gaps in the numeration
for file_path in reversed(file_list):
    try:
        shutil.move(file_path, folder_path / (file_path.stem[:-3] + str(num + 1).zfill(3) + file_path.suffix))
    except OSError:
        continue
    if str(num).zfill(3) == gap:
        break
    num -= 1
print('\nThe numering of files had been verify and renumering to close gaps')