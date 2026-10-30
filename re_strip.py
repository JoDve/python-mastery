import re

def stripmethod(string, chars=None):
    
    # 1. THE WHITESPACE CONDITION
    if chars is None:
        WHITESPACE = re.compile(r'(^\s+)|(\s+$)')
        return WHITESPACE.sub(r'', string)
        
    # 2. THE CUSTOM CHARACTER CONDITION
    else:
        STRIPWORD = re.compile(f'(^[{chars}]+)|([{chars}]+$)')
        return STRIPWORD.sub(r'', string)
        
# --- MAIN EXECUTION ---
phrase = input('Insert your phrase\n>')

words = input('Enter the characters you want to strip off (or press Enter for whitespace)\n>')

# Handle the default parameter logic cleanly
if words == '':
    result = stripmethod(phrase)
else:
    result = stripmethod(phrase, words)

print(f"Result: '{result}'")
