#!/usr/bin/python
import os
import commands

print ("PYGR02 - Let there be light!\n")

files = commands.getoutput("ls -l").split("\n")
del files[0] # First line, not useful

filesChanged = [];
for file in files:
    if (file[9] != 'x'):
        data = file.split(" ")
        fileName = data[len(data) - 1]
        if (fileName[len(fileName) - 3:len(fileName)] == '.py'):
            os.system("chmod +x " + fileName)
            filesChanged.append(fileName)

if(len(filesChanged) > 0):
    print ("Checkout a list of changed files:")
    for file in filesChanged:
        print (file)
else:
    print ("Well... there's no file to change.")