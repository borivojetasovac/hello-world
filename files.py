#!/usr/bin/python3
import os, shelve, pprint

# hello.txt needed

print('Manually created path: ' + str(os.path.join('home', 'perkan', 'Documents', 'spam'))) # creates string path using the correct path (Win/Linux) formed out of parametars
path = os.getcwd()
print('Current working directory path: ' + os.getcwd())
print('Current working directory name: ' + os.path.basename(path))
print('Cwd path and name: ' + str(os.path.split(path)))
print('Path to cwd (without it): ' + os.path.dirname(path))

os.chdir('..')      # change cwd (relative path)          absolute: os.chdir('/home/perkan/Downloads')
print('Changed cwd: ' + os.getcwd())
#os.makedirs('./test/moreTests/stop')           # makes every subfolder needed

print('\nAbsolute path cwd/../..: ' + os.path.abspath('../..'))
print('Is the path absolute ../..: ' + str(os.path.isabs('../..')))     # checks if the arg is absolute path (False if it is relative)
print('Realtive path: ' + str(os.path.relpath('.', '~/Documents')))     # relative path from first to second arg
print('/usr/bin'.split(os.path.sep))            # will return a list of each part of the path (on any OS if os.path.sep is passed)

print('\nFile size: ' + str(os.path.getsize(os.getcwd())) + ' bytes.')
print('Every file in cwd: ' + str(os.listdir(path)))
print('\nDoes passed path exist? ' + str(os.path.exists(path)))
print('Does passed path exist and is file? ' + str(os.path.isfile(path)))
print('Does passed path exist and is directory? ' + str(os.path.isdir(path)))

# Writing to and reading from files:
helloFile = open('/home/perkan/Documents/pythonExamples/atbswp/hello.txt')  # read mode (or explicitly with 'r' as the second arg)
print(helloFile.read())
helloFile.seek(0)
print(helloFile.readlines())                    # returns list of all lines in file         readline() reads only 1 line
helloFile.close()

helloFile = open('hello.txt', 'w')              # write mode 'w' - overwrite the existing file and start from scratch
print(helloFile.write('Start from scratch!'))   # returns number of characters written
helloFile.close()                               # if the filename doesn't exist ('w', 'a' modes) blank file will be created

helloFile = open('hello.txt', 'a')              # append mode 'a' - append text to the end of the exsisting file
helloFile.write('Now we are here...')
helloFile.close()

# Saving variable with the shelve module:
shelfFile = shelve.open('mydata')
names = ['Alice', 'Bob', 'Carol']
shelfFile['names'] = names
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['names'])
shelfFile['names'] = 5
print(shelfFile['names'])

# Saving variable with the pprint.pformat:
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()     # when the string from pprint.pformat is saved to a .py file, that file is a module that can be imported just like any other
