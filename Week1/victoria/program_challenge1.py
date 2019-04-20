
from os import listdir


directory = 'C:\\Users\\vcampbel\\Downloads\\Database\\Database'


filenames = listdir(directory)

for name in filenames:
    print(name)

