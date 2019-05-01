# files is a list
# for each item in the list, search for a period
# add the string after period into a list that is called filesuffixes
# create a dictionary with the file suffixes as the key for the key:value pair
# grab the collection of files under each key and order alphabetically

from os import listdir

#from os.path import isfile, join

directory = 'C:\\Users\\bascott\\Documents\\Python\\Database'

files = listdir(directory)

number_files = len(files)

print("There are %s" % number_files + " files in the directory.")

microsoft_word_doc = []   # .doc
java_doc = []             # .java
python_doc = []           # .py
text_doc = []             # .txt
excel_doc = []            # .xlsx
c_plus_plus_doc = []      # .cpp

for i in range(number_files):
    # print(files[i])
    current_file = files[i]
    delimiter_position = current_file.find('.')
    # print(current_file[delimiter_position:])

    if(current_file[delimiter_position:]) == ".doc":
        microsoft_word_doc.append(current_file)
    #    print(current_file)

    if(current_file[delimiter_position:]) == ".java":
        java_doc.append(current_file)
    #    print(current_file)

    if(current_file[delimiter_position:]) == ".py":
        python_doc.append(current_file)
    #    print(current_file)

    if (current_file[delimiter_position:]) == ".txt":
        text_doc.append(current_file)
    #    print(current_file)

    if (current_file[delimiter_position:]) == ".xlsx":
        excel_doc.append(current_file)
    #    print(current_file)

    if (current_file[delimiter_position:]) == ".cpp":
        c_plus_plus_doc.append(current_file)
    #    print(current_file)

print(excel_doc)

f_doc = open("C:\\Users\\bascott\\Documents\\Python\\Database\\Microsoft_Word_Docs.txt", "a")
print(microsoft_word_doc)
for i in range(len(microsoft_word_doc)):
    f_doc.write(microsoft_word_doc[i] + "\n")

f_doc.close()

f_doc = open("C:\\Users\\bascott\\Documents\\Python\\Database\\Java_Docs.txt", "a")
print(java_doc)
for i in range(len(java_doc)):
    f_doc.write(java_doc[i] + "\n")

f_doc.close()

f_doc = open("C:\\Users\\bascott\\Documents\\Python\\Database\\Python_Docs.txt", "a")
print(python_doc)
for i in range(len(python_doc)):
    f_doc.write(python_doc[i] + "\n")

f_doc.close()

f_doc = open("C:\\Users\\bascott\\Documents\\Python\\Database\\Text_Docs.txt", "a")
print(text_doc)
for i in range(len(text_doc)):
    f_doc.write(text_doc[i] + "\n")

f_doc.close()

f_doc = open("C:\\Users\\bascott\\Documents\\Python\\Database\\Excel_Docs.txt", "a")
print(excel_doc)
for i in range(len(excel_doc)):
    f_doc.write(excel_doc[i] + "\n")

f_doc.close()

f_doc = open("C:\\Users\\bascott\\Documents\\Python\\Database\\C_Plus_Plus_Docs.txt", "a")
print(c_plus_plus_doc)
for i in range(len(c_plus_plus_doc)):
    f_doc.write(c_plus_plus_doc[i] + "\n")

f_doc.close()
