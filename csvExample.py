#!/usr/bin/python3
import csv, os

# read CSV file:
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)     # makes Reader object from CSV file

exampleDate = list(exampleReader)
print(exampleDate)
exampleFile.seek(0)                         # rewind the CSV file
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

# write to CSV file:
outputFile = open('output.csv', 'w')        # creates new file       if we use delimiter = '\t', we should name the file 'output.tsv' (tab separated value)
outputWriter = csv.writer(outputFile)       # makes Writer object
#outputWriter = csv.writer(outputFile, delimiter = '\t', lineterminator = '\n\n')

outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])             # returns num of characters written
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.141592, 4])
outputFile.close()

# Removing the Header from CSV files:
os.makedirs('headerRemoved', exist_ok = True)                       # all headerless CSV files will be written here

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue

    print('Removing header from ' + csvFilename + '...')

    csvFile = open(csvFilename)
    reader = csv.reader(csvFile)
    data = list(reader)
    del data[0]     # remove first line of CSV files
    csvFile.close()

    outputFile = open(os.path.join('headerRemoved', csvFilename), 'w')
    writer = csv.writer(outputFile)
    for row in data:
        writer.writerow(row)
    outputFile.close()

''' example.csv:
4/5/2015 13:34,Apples,73
4/5/2015 3:41,Cherries,85
4/6/2015 12:46,Pears,14
4/8/2015 8:59,Oranges,52
4/10/2015 2:07,Apples,152
4/10/2015 18:10,Bananas,23
4/10/2015 2:40,Strawberries,98
'''
