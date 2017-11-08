#!/usr/bin/python3
import re

# Character Classes:
# \d - any digital character
# \D - any character that is not a numeric digit
# \w - any letter/numeric digit/underscore
# \W - anything that is not letter/numeric digit/underscore
# \s - any space/tab/newline character
# \S - anything but space/tab/new line

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')    # returns a Regex object        always pass raw string!
mo = phoneNumberRegex.search('My number is 415-555-4242.')  # returns None or Match object of the first matched text (through group method)
print('Phone number found: ' + mo.group())

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
listVal = phoneNumberRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # the findall() returns lists of every match (or tuples list for every group)
print('findall() method: ' + str(listVal))

# Grouping with ():
phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')    # first parentheses - group 1, second - group 2
mo = phoneNumberRegex.search('My number is (415) 555-4242.')
print('All regex: ' + mo.group(0))
print('First group found: ' + mo.group(1))
print('Second group found: ' + mo.group(2))
print('All groups: ' + str(mo.groups()))

# Matching multiple groups with the pipe: |
heroRegex = re.compile(r'Batman|Tina Fey')                  # maches one of many expressions ('Batman' or 'Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print('First found: ' + mo1.group())                        # the first occurrence will be returned as the Match object
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')        # matches one of several matches that starts with 'Bat'
mo = batRegex.search('Batmobile lost a wheel')
print("'Bat' regex found: " + mo.group() + ", so the sufix after 'Bat' is " + mo.group(1))

# Optional matching with ?
batRegex2 = re.compile(r'Bat(wo)?man')                      # ? flags the group that precedes it as an optional part of the pattern (0 or 1 times)
mo = batRegex2.search('The Adventures of Batman')
print('Optional matching with ?: ' + mo.group())
mo = batRegex2.search('The Adventures of Batwoman')
print('Optional matching with ?: ' + mo.group())

# (Mutual) optional matching with *
batRegex3 = re.compile(r'Bat(wo)*man')                      # * flags the group that precedes it as an optional part of the pattern (0 or more times)
mo = batRegex3.search('The Adventures of Batwowowoman')
print('Optional matching with *: ' + mo.group())

# One or more matching with +
batRegex4 = re.compile(r'Bat(wo)+man')                      # the same as *, but it HAS to apper at least once

# Matching specific repetitions with {}
haRegex = re.compile(r'(Ha){3}')                            # {n} matches the previous pattern n times
haRegex = re.compile(r'(Ha){3,5}')                          # {n, m} matches the previous pattern n to m times (one can be left out)    no space after comma !!!!
mo = haRegex.search('HaHaHaHa')
print('Matching specific repetitions with {n, m}: ' + mo.group())

# Regexes are greedy by default - in ambiguous situations they will match the longest string possible
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')                # nongreedy regex (? after{})
mo = nongreedyHaRegex.search('HaHaHaHa')
print('Nongreedy specific repetition match: ' + mo.group()) # the smallest possible

# Your own character class:
vowelRegex = re.compile(r'[aeiouAEIOU]')
print('Vowels: ' + str(vowelRegex.findall('RoboCup eats baby food. BABY FOOD.')))
                                                            # [a-zA-Z0-9] - range of characters using a hyphen(-): all letters and numbers
consonantRegex = re.compile(r'[^aeiouAEIOU]')               # negative character class using caret character(^) - matches everything out of the character class
print('Consonants: ' + str(consonantRegex.findall('RoboCup eats baby food. BABY FOOD.')))

beginsWith = re.compile(r'^Hello')                          # a string must begin with this regex pattern
mo = beginsWith.search('Hello world!')
endsWith = re.compile(r'\d$')                               # a string must end with this regex pattern
mo = endsWith.search('Your number is 42')
wholeString = re.compile(r'^\d$')                           # used together, to indicate that the entire string must match the regex
mo = wholeString.search('09848324')

# Wildcard character . match any character except a newline:
atRegex = re.compile(r'.at')                                # passing re.DOTALL as the second argument will match all characters
print('Wildcard example: ' + str(atRegex.findall('The cat in the hat sat on the flat mat.')))

# Matching everything with .*
greedyRegex = re.compile(r'<.*>')                           # wildcard 0 or more times
print('Matching everything with .* : ' + str(greedyRegex.findall('<To serve man> for dinner.>')))
nongreedyWildcard = re.compile(r'<.*?>')
print('Matching everything nongreedy: ' + str(nongreedyWildcard.findall('<To serve man> for dinner.>')))

# For case-insensitive matching pass re.IGNORECASE(or re.I) as the second argument:
nameRegex = re.compile(r'Agent \w+', re.I)
print(nameRegex.sub('CENSORED', 'Agent Alice gave the secret documents to agent Bob.')) # returns a string in wich every match is replaced with fitst argument
agentNamesRegex = re.compile(r'Agent (\w)\w*')  # 2 groups, so \1 in sub() method refer to the first group (wich is only one character - firs letter)
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

# Managing complex regexes (with re.VERBOSE):
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
\d{3}                           # first 3 digits
(\s|-|\.)                       # separator
\d{4}                           # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?    # extension
)''', re.VERBOSE)
for groups in phoneRegex.findall('(111) 111 1111, (222)-222-2222, 333 333 3333, 444-444-4444, 555 5555'):
    print(groups[0])            # because group 0 matches the entire regex

# Combination of re.IGNORECASE, re.DOTALL, and re.VERBOSE
combRegex = re.compile(r'\d', re.IGNORECASE | re.DOTALL | re.VERBOSE)   # the bitwise operator | (re.compile has only 2 arguments)
