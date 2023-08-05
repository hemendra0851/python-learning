import os, sys

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(rootDir)
sys.path.append(rootDir)

from pack1 import file1, file2

file1.one()
file2.two()

def thre():
    print('file 3')