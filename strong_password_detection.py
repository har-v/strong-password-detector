import re
import pyperclip
'''
Strong password checker.
Copies strong passwords to the clipboard.
'''

# At least 1: lowercase letter, uppercase letter, special character and digit.
# Min. 8 character length.
passwordRegex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*?[#?!@$%^&*-])(?=.*[0-9]).{8,}')

def strongPassword():
    password = input('Enter password: ')
    mo = passwordRegex.search(password)
    
    if not mo:
        print('''Password is weak. It must contain:
        - At least 1 lowercase letter.
        - At least 1 uppercase letter.
        - At least 1 special character.
        - At least 1 digit.
        - Have a minimum of 8 characters.
        ''')
    else:
        pyperclip.copy(password)
        print('Your password is strong and has been copied to your clipboard.')
            
strongPassword()
