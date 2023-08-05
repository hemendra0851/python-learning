# Positional Arguments
def positional(a, b):
    print(a+b)

# Default Arguments
def deafult(a, b, c=0, d=0):
    print(a+b+c+d)

# *args - Passed as a tuple
def multiargs(*args):
    print(sum(args))
    
# **kwargs - Keyword Arguments - Passed as a Dictionary
def keywordArgs(**kwargs):
    if 'a' in kwargs: print('True')
    else: print('False')
    
# Combination
def myfunc(*args, **kwargs):
    print(args)
    print (kwargs)
    print(f"I would like {args [0]} {kwargs[ 'food']}")


# positional(3,4)          # 7
# deafult(3,4))            # 7
# deafult(3,4,1,2))        # 10
# multiargs(1,2,3,4,6)       # 16 
# keywordArgs(a = 2, b = 3)    # True
# keywordArgs(c = 2, b = 3)    # False
myfunc (10, 20, 30, fruit='orange', food='eggs' ,animal='dog')