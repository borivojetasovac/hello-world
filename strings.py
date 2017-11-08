#!/usr/bin/python3
import pyperclip

print(r'That is Carol\'s cat.')             # raw string - ignores all escape characters
print('''Dear Alice,

Eva's cat has been arrested for catnapping, cat burglary and extortion.

Bob''')     # multiline string (also raw); block indentation rules doesn't apply

spam = 'Hello world!'
print(spam[:5])                             # 'Hello'
print(spam[:5].isupper())                   # False     islower(), isalpha(), isalnum(), isdecimal(), isspace(), istitle()
print(spam.upper())                         # 'HELLO WORLD!'      contrary: lower()
print('cats' not in 'cats and dogs')        # False
print('\t'.join(['cats', 'rats', 'bats']))  # inserts separator between each list argument
print('My name is Simon'.split('name'))
print('Hello'.rjust(10, '*'))               # ljust(), center()         default: space
print('  12345SSSSSkkkkk '.strip('Sk '))    # trims S, k and ' ' from both ends        lstrip(), rstrip()
print(pyperclip.paste())                    # pastes whatever was on clipboard
pyperclip.copy('pyperclip clipboard')       # send 'pyperclip clipboard' to clipboard

try:                                        # Strings are immutable data types
    spam[2] = 'd'
except TypeError:
    print('Strings are immutable data types!!!')
