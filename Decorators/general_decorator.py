
def works_for_all(func):
    def inner(*args, **kwargs):
        print("|"*30)
        func(*args, **kwargs)
        print("|"*30)
    return inner

@works_for_all
def ordinary(*args, **kwargs):
    print(args)
    print(kwargs)
    

ordinary(1,2,3,4, a=1, b=2)