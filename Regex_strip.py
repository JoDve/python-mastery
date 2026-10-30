# Regex Version of the strip() Method
import re


def stripmethod(string, side):

    if side == '':
        print(WHITESPACE.search(string).group(2))
        
    else:
        print(STRING_RE.search(string).group(2))
        
    



phrase = input('Insert your phrase\n>')

words = input('Enter the characters you want to strip off \n>')

if words != '':
    STRING_RE = re.compile(f'^([{words}]+)(.*?)([{words}]+)$')
    
WHITESPACE = re.compile(f'^( *)(.*?)( *)$')

stripmethod(phrase, words)
