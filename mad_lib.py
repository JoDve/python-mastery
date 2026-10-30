# Create a Mad Libs program that read in text files
# And lets the user add their own text anywhere 
# the word ADJECTIVE, NOUN, ADVERB, or VERB appears in 
# the text file.

from pathlib import Path
import re

print('''Hi! this is a Mad Libs Program 

Please pay attention to the next text and change the word\n''')

# Open the File and show the content to the User

text_file = open('mad_lib.txt', 'r', encoding='utf-8')
content = text_file.read()
print('>', content)
text_file.close()

# Search patterns  (ADJECTIVE, NOUN, ADVERB, VERB )
patterns = re.compile('ADJECTIVE|NOUN|ADVERB|VERB')

# Calculate how many words (ADJECTIVE, NOUN, ADVERB, VERRB)

WORDS = patterns.findall(content)

# Convert the WORDS in curly brackets '{}' to use format
content = patterns.sub('{}', content)

# Insert a `foor` loop that iterate over each item of WORDS list.
replace = []

for word in WORDS:
    if word[0].lower() in 'aeiou':
        replace = replace + [input(f'Enter a {word}: \n>')] 
         
    else:
        replace = replace + [input(f'Enter a {word}: \n>')]


# Replace the content with the news words

content = content.format(*replace)

# create a new file with `with` statement for WRITE

with open('new_txt.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(content) 


# Print the new text to the user.

print(content)

#for grammar in WORDS:
#   word = re.compile(f'{grammar}?')
   
#   if grammar[0].lower() in 'aeiou':
#        replace = input(f'Enter an {grammar.lower()}:\n>') # Lets the user enter the new word
#        content = word.sub(replace, content)
#    
#    else:
#        replace = input(f'Enter a {grammar.lower()}: \n>') # Lets the user enter the new word
#        content = word.sub(replace, content)
