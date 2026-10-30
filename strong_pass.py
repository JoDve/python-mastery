import re
NEWLINE_RE = re.compile(r'\s')
UPPER_RE = re.compile(r'[A-Z]')
LOWER_RE = re.compile(r'[a-z]')
DIGIT_RE = re.compile(r'\d')

def strongpass(password):    

    if len(password) < 8:
        return False

    if NEWLINE_RE.search(password):
        return False
            
    if not UPPER_RE.search(password):
        return False
    
    if not LOWER_RE.search(password):
        return False
    
    if not DIGIT_RE.search(password):
        return False


    return True
                        

if strongpass(input('> Insert your password:  \n')):
    print('Your password is strong')

else:
    print('Your password is invalid')
    
