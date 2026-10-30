'''
The BulletPointAdder.py script will get the text from the clipboard,
add a star and space to the beginning of each line, and the paste this new
text to the clipboard .
'''

import pyperclip, copy

# Get text from the clipboard, add a star an space to the beginning of each line,

text = pyperclip.paste().split('\n')

for index in range(len(text)):
    
    text[index] = '* ' + text[index]

text = '\n'.join(text)

pyperclip.copy(text)
