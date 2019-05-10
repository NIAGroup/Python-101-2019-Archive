#This program will reading a set of files and printout their file types
from os import listdir

import os
path = "C:\\Users\\sdarnell\\python101\\Python-101-2019\\Week3\\files"
files = os.listdir(path)
for file in files:
    if "doc" in file:
        print(file + " is a document")
    elif "java" in file:
        print(file + " is a java file")
    elif "py" in file:
        print(file + " is a python file")
    elif "xlsx" in file:
        print(file + " is an Execl file")
    else:
        print("unknown file type")





