import os

# print(os.getcwd())

# print(os.listdir())
# os.unlink('test.txt')
# os.rmdir('test')
# os.mkdir('test')

for folder, sub_folder, files in os.walk(os.pardir(os.getcwd())):
    print(folder)
    print(sub_folder)
    print(files)
    print('\n')