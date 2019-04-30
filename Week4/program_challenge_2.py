
import os
import extention_finder

#this is the directory where the files are located:
path = "C:\\Users\\sdarnell\\python101\\Python-101-2019\\Week4\\files\\"

#create folders if they don't already exist
folders = extention_finder.extention_dict

for folder in folders.values():
    if not (os.path.exists(path + "\\" + folder)):
        print("added the " + folder + " folder")
        os.mkdir(path + "\\" + folder)
    else:
        print("the " + folder + " folder already exists")


# moves files into directories which match their file extensions
# store the list of file names
files = os.listdir(path)

for file in files:
    extension = os.path.splitext(file)[1]   #this will return the extension but with the period ".cpp"
    extension = extension[1:]
    for folder in folders.keys():
        if extension == folder:
            print("moved " + file + " to " + path + folders.get(folder) + "\\")
            os.rename(path + "\\" + file, path + folders.get(folder) + "\\" + file)


# print sorted file list for each folder
for folder in folders.keys():
    print("\n" + folders.get(folder) + " documents:")
    files = os.listdir(path + folders.get(folder))
    files.sort()
    for file in files:
        print(file)




