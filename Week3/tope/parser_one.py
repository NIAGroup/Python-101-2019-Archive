import os

file_path = "/Users/temitope/Documents/Database/Database/"

files = os.listdir(file_path)

dir_items = []

for file in files:
    dir_items.append(file)
    if ".doc" in file:
        print ("Word documents:\n", file)
    elif ".xlsx" in file:
        print ("Excel Files:\n", file)
    elif ".java" in file:
        print ("Java Files:\n", file)
    else:
        print ("Python Files:\n", file)


