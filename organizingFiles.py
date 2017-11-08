#!/usr/bin/python3
import os, send2trash, zipfile, shutil       # shell utilities

shutil.copy('./capitalsquiz1.txt', '../..')                 # returns the path of newly copied file
shutil.copy('./capitalsquiz1.txt', '../..newName.txt')      # the same, but gives the copied file new name
#shutil.copytree('../atbswp', '../atbswp_backup')           # copyes entire folder and names it atbswp_backup
#shutil.move('./files.py', './FILES.py')                    # if the destination folder doesn't exsist, Python will assume it's new filename

spamFile = open('spam.txt', 'a')    # creates a file
spamFile.write('File to be removed.')
spamFile.close()
os.unlink('spam.txt')               # will delete the file at path
#send2trash.send2trash('spam.txt')  # will send the file to trash
#os.rmdir(path)                     # will delete empty folder at path
#shutil.rmtree(path)                # will delete folder at path

# Walking a directory tree:
for folderName, subfolders, filenames in os.walk('../'):    # walk a directory tree (every file and subfolder in it)
    print('The current floder is: ' + folderName)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
    print('')

# Compressing files:
exampleZip = zipfile.ZipFile('hello.txt.zip')
print(exampleZip.namelist())        # list of all files and folders contained in the ZIP file
exampleInfo = exampleZip.getinfo('hello2.txt')              # returns ZipInfo object
print('Original size: ' + str(exampleInfo.file_size) + ', compressed size: ' + str(exampleInfo.compress_size))
exampleZip.extractall()             # into cwd (or arg path - if path doesn't exists, it will be created)
#exampleZip.extract('hello2.txt')   # extracts single file
exampleZip.close()

newZip = zipfile.ZipFile('new.zip', 'w')    # or 'a'
newZip.write('hello.txt', compress_type = zipfile.ZIP_DEFLATED)
newZip.close()
