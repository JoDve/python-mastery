import re

def ask_user(match_object):
    # 1. Extract the found word (e.g., 'ADJECTIVE')
    print(match_object)
    word = match_object.group() 

    # 2. Check if it starts with a vowel for "a" vs "an"
    if word[0].lower() in 'aeiou':
        print(f'Enter an {word.lower()}:')
    else:
        print(f'Enter a {word.lower()}:')
    # 3. Ask the user for input
    new_word = input()
    # 4. Return the user's input
    return new_word
    
# --- MAIN EXECUTION ---
# Open the file and read the content
with open('mad_lib.txt', encoding='utf-8') as text_file:
    content = text_file.read()
    print(content)

patterns = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

# re.sub will automatically call ask_user() every time it finds a pattern!
new_content = patterns.sub(ask_user, content)

print(new_content)
# Write new_content to the file