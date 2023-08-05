
def function_decorator(func):
    def wrapped_func():
        # Do something before the function is executed
        func()
        # Do something after the function has been executed
    return wrapped_func

@function_decorator
def func():
    pass

# function call
func()