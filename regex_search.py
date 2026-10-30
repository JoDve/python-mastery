# Write a program that opens all .txt files in a folder and searches 
# for any line that matches a user-supplied regular expression, 
# then prints the results to the screen.

from pathlib import Path # Import Path module
import re # Import re module

# Create the regular expression that user supplied

print('Enter the words that you want to match\n')
words = input()
pattern = re.compile(words)

# Open all files and print the results
print('\nAll matches on the all files are: \n')

for name in Path('/home/useless/Desktop/python-mastery').glob('*.txt'):
    with open(name, encoding='utf-8') as file:
        for line in file:
            if pattern.search(line):
                print(f'{name}:{line.rstrip()}')

