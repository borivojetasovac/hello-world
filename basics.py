#!/usr/bin/python3
import sys
from random import randint

for i in range (2, 0, -1):      # start, stop and(optionaly) step values (can go both ways)
    print(randint(1, 10) ** 2)  # randint incudes both 1 and 10         ** power    // int(floor) division

# Keyword arguments: end, sep
print('Hello', end = '')        # at the end of the line empty string (instead of new line)
print('uno', 'duo', 'tres', 'cuatro', sep = ', ')   # separate with ', ' instead of space
print('Add this: %s number and this: %s char.' % (545.56, 'j'))
num = input('Enter a number: ')
print(str(int(num) + 1))
print(round(3434.4342, 0))      # rounds number to n decimals, returns float
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))

# Variable scopes:
def spam():
    print(eggs)     # no parameter named eggs, so it is considered as a reference to the global variable eggs
def bacon():
    global eggs     # this is how to change global variable within the function ("global statement")
    eggs = 50
eggs = 20
spam()
bacon()
print(eggs)

if len(sys.argv) > 2:           # program started with at least 2 arguments: python3 basic.py firstArgument secondArgument
    print(sys.argv[0])          # basic.py
    print(sys.argv[1])          # firstArgument
    print(sys.argv[2])          # secondArgument

sys.exit()                      # raises SystemExit exception
