#!/usr/bin/python3
import sys                                  # mustn't name python file as the module you're importing inside it!!
from random import randint as rand          # 'as' keyword gives imported name an alias in our code

for i in range (2, 0, -1):      # start, stop and(optionaly) step values (can go both ways)
    print(rand(1, 10) ** 2)     # randint (alias rand) incudes both 1 and 10         ** power    // int(floor) division

# Keyword arguments (must come after all 'positional' parameters):
print('Hello', end = '')        # at the end of the line empty string (instead of new line)
print('uno', 'duo', 'tres', 'cuatro', sep = ', ')   # separate with ', ' instead of space
print('Add this: %s number and this: %s char.' % (545.56, 'j'))
num = input('Enter a number: ')
print(str(int(num) + 1))
print(round(3434.4342, 0))      # rounds number to n decimals, returns float
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))
# Unpack tuple or dictionary into a series of individual parameters with *args(for tuples) and **kwargs(for dictionarys)

# Lambda functions:
add = lambda x, y: x + y
print('X + Y = %s' % add(2, 3))

# yield generator function:
def genFunction(n):             # functions that contain yield will return generator
    i = 0
    while i < n:                # when generator executes the entire function without encountering yield (when i becomes equal to n) - StopIteration exception
        yield i                 # like 'return i', but function keeps executing normally
        i += 1                  # Python doesn't support ++
for x in genFunction(3):        # for loop will automatically handle StopIteration exception for us
    print(x)

# Decorator functions:
def withNamePrint(originalFunction):                # takes a function object(functions are objects in Python) as a parameter and returns a new, modified function
    def newFunction(*args, **kwargs):
        print('Function name: %s, args: %s, keyword args: %s.' % (originalFunction.__name__, args, kwargs))
        return originalFunction(*args, **kwargs)
    return newFunction

# Variable scopes and optional parameter:
@withNamePrint      # exactly the same as: spam = withNamePrint(spam) - assigns the new function to the old function's name
def spam(optParam = True):      # if we leave this param out - the default will be used, otherwise it will override the default value (don't use mutable types here!!)
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

# Python uses references whenever variables must store values of mutable data types
