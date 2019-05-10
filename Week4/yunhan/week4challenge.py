import os
import shutil
import sys
sys.path.insert(0, 'C:\\Users\\ychen22\\Documents\\python101\\Python-101-2019\\Week4')
import extention_finder
from extention_finder import extention_dict

class customObject():
    def __init__(self, name1, type1):
        self.name1 = name1
        self.type1 = type1
directory = 'C:\\Users\\ychen22\\Documents\\python101\\Python-101-2019\\Database\\Database'
maindirectory = 'C:\\Users\\ychen22\\Documents\\python101\\Python-101-2019\\Week4\\yunhan\\Newdatabase'
if os.path.isdir(maindirectory):
    print("exist:",maindirectory)
else:
    os.mkdir(maindirectory)
files = os.listdir(directory)
print(files)
f = open('C:\\Users\\ychen22\\Documents\\python101\\Python-101-2019\\Week4\\extention_finder.py', 'r')
for key in extention_dict.keys():
    newdir = os.path.join(maindirectory,key)
    if os.path.isdir(newdir):
        print("dir exist: ", newdir)
    else:
        os.mkdir(newdir)
    key1 = "." + key
    for i in files:
        if key1 in i :
            origfile = os.path.join(directory,i)
            newfile = os.path.join(newdir,i)
            shutil.copy(origfile, newfile)
            print("The file ", origfile,"copied to", newfile )
dirlist = os.listdir(maindirectory)
for i in dirlist:
    files1 = os.listdir(os.path.join(maindirectory, i))
    files1.sort()
    print(files1)
