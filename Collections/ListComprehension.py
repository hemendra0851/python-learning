
nums = [1,4,7,3,8,6]

my_list = [x for x in nums]                             # print all items
my_list = [x*2 for x in nums]                           # double all items
my_list = [x for x in nums if x%2==0]                   # filter even number
my_list = [x if x%2==0 else 'ODD' for x in nums]        # item is even, else ODD


import os
files = os.listdir(path= os.path.dirname(__file__))
print(files)

check = lambda file: ('Count' in file or 'HU' in file) and 'ipynb' not in file.split('.')[1]

fileList = list(filter(check, files))
print(fileList)

# Nested For Loop
mylist = []

for x in [2,4,6]:
    for y in [10,100,1000]:
        mylist.append(x*y)
        

my_list = [x*y for x in [2,4,6] for y in [10,100,1000]]

import itertools
s = 'hello'
data = itertools.combinations_with_replacement(s,2)
while data.__next__():
    print(next(data))
