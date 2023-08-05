def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

# print(return_greeting('Adam'))

print(return_greeting)

print(return_greeting.__name__)

help(return_greeting)

'''However, after being decorated, say_whee() has gotten very confused about its identity. 
It now reports being the wrapper_do_twice() inner function inside the do_twice() decorator. 
Although technically true, this is not very useful information.'''