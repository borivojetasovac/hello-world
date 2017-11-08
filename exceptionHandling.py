#!/usr/bin/python3
import traceback, logging

def spam(number):
    try:
        return 50 / number
    except ZeroDivisionError:
        return 'Error: Invalid argument.'

print(spam(2))
print(spam(0))

# Custom exceptions:
# the code that calls the function (not the function itself) knows how to handle an exception
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width)           # print * width times
    for i in range(height - 2):
        print(symbol + ' ' * (width - 2) + symbol)
    print(symbol * width)
for sym, w, h in(('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:        # how to catch exception message
        print('An exception happened: ' + str(err))

# Write traceback to file:
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())    # returns traceback string (error message, the line num that caused the error, and the call stack)
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')

# Assertions: when a lot of code is written under the assumption that the door is 'open' - we add assertion to make sure we're right to assume that
                        # That's why code shouldn't handle assert statements with try except - if assert fails program SHOULD crash
door = 'open'
assert door == 'open', 'The door need to be "open".'    # start program whit -0 param to disable all assertions
door = 'close'

# Logging:          5 leveles of logging: DEBUG < INFO < WARNING < ERROR < CRITICAL
logging.basicConfig(filename = 'myProgramLog.txt', level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')
# loggs to 'myProgramLog.txt' file (optional)      level: lowest level of logging messages to display (logging.ERROR will display ERROR and CRITICAL)
logging.debug('Start of program')       # .debug() - write to DEBUG level
#logging.disable(logging.CRITICAL)      # suppress all log messages at that level or lower
for i in range(20, 2, -2):
    logging.info('i is ' + str(i))
logging.debug('End of program')
