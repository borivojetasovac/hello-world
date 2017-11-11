#!/usr/bin/python3
import copy

spam = [['cat', 'bat'],
    'rat',
    'elephant',
    [10, 20, 30, 40, 50]]

print(spam)
bacon = spam[0:2]
print(len(bacon))

del spam[1]     # delete values at index
print(spam)

# List concatenation:
catNames = []
while True:
    name = input('Enter the name of the cat(or just type Enter): ')
    if name == '':
        break
    catNames += [name]
print('Cat names are: ' + str(catNames))

# The Multiple Assignment Trick - the number of variables and the lenght of the list must be exactly equal
cat = ['fat', 'black', 'loud']
catSize, catColor, catDisposition = cat
print('Cat size: ' + catSize + ', color: ' + \
    catColor + ', disposition: ' + catDisposition)  # split up a single instruction with \      the indentation on the line after \ does not matter

print(cat.index('black'))   # if the passed value isn't in the list, ValueError; in case of duplicates - it returns the first index
cat.append('ugly')
cat.insert(1, 'Lukas')      # adds the argument at given index
cat.remove('Lukas')         # delete a value that doesn't exist: ValueError; in case of duplicates - only the first one is removed
# del when you know the index and remove when you know the value
cat.sort(reverse = True)    # cannot sort lists that have both number and string values
print(cat)

# TUPLES:
tupleExample = ('hello', 32, 3)         # tuples are immutable lists
try:
    tupleExample[0] = 3
except TypeError:
    print('Tuples are immutable!!!')
print(type(('hello',)))     # indicate Python that it's a tuple with only one value, otherwise it's a string

# List variables don't actually contain lists - they contain references:
cheese = cat                # this is why lists passed as function arguments will be changed (side effect)
cheese[1] = 'Hello!'        # it actually changes 'both' lists, since there is only one list in memory
print(str(cat) + '\t' + str(cheese))
# To make 2 different lists use copy modul (copy and deepcopy functions)
cheese = copy.copy(cat)    # if the list you need to copy contains lists, use copy.deepcopy()
cheese[1] = 'Goodby!'
print(str(cat) + '\t' + str(cheese))
