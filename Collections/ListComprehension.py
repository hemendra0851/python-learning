
nums = [1,4,7,3,8,6]

my_list = [x for x in nums]
my_list = [x*2 for x in nums]
my_list = [x for x in nums if x%2==0]
my_list = [x if x%2==0 else 'ODD' for x in nums]

fileList = [file.name for file in files if 'DU' in file.name or 'HU' in file.name and '(' not in file.name]

# Nested For Loop
mylist = []

for x in [2,4,6]:
    for y in [10,100,1000]:
        mylist.append(x*y)
        

my_list = [x*y for x in [2,4,6] for y in [10,100,1000]]