#Challenge: Randomly break up a list of names into groups of three.  The total number of names must not be a multiple of three

import secrets

#create initial list of all names - must not be a multiple of three
names = ["Jose", "Injoh", "Felicia", "Adonay", "Stephen", "Chuey", "Biance", "Scott", "Johnny", "Tope", "Ken", "Sushma", "Frank", "Rowena"]

"""
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(names[0:2])
print(names[1:2])
print(names[1:3])
print(names[0:3])

output:     #huh???, why when i use multiple indexes they don't represent the order of elements in the list?
Jose
Injoh
Felicia
Adonay
['Jose', 'Injoh']
['Injoh']
['Injoh', 'Felicia']
['Jose', 'Injoh', 'Felicia']

"""

#determine the number of groups needed
no_of_groups = int(len(names) / 3)
if len(names)/3 != 0:
    no_of_groups += 1

#print(no_of_groups)

# randomize original list by using the random.shuffle command and then
# store the first three names from the list into a list and
# remove those first three names from the original list so that they cannot be selected again
groups = []
for i in range(no_of_groups):
    secrets.SystemRandom().shuffle(names)
    groups.append([names[0:3]])
    print(groups)
    del names[0:3]

print(groups)

"""
output:
[[['Frank', 'Felicia', 'Adonay']]]
[[['Frank', 'Felicia', 'Adonay']], [['Stephen', 'Johnny', 'Jose']]]
[[['Frank', 'Felicia', 'Adonay']], [['Stephen', 'Johnny', 'Jose']], [['Sushma', 'Biance', 'Chuey']]]
[[['Frank', 'Felicia', 'Adonay']], [['Stephen', 'Johnny', 'Jose']], [['Sushma', 'Biance', 'Chuey']], [['Tope', 'Scott', 'Injoh']]]
[[['Frank', 'Felicia', 'Adonay']], [['Stephen', 'Johnny', 'Jose']], [['Sushma', 'Biance', 'Chuey']], [['Tope', 'Scott', 'Injoh']], [['Rowena', 'Ken']]]
[[['Frank', 'Felicia', 'Adonay']], [['Stephen', 'Johnny', 'Jose']], [['Sushma', 'Biance', 'Chuey']], [['Tope', 'Scott', 'Injoh']], [['Rowena', 'Ken']]]
"""
