
''' We have a closure in Python when a nested function references a value in its enclosing scope.

The criteria that must be met to create closure in Python are summarized in the following points.

We must have a nested function (function inside a function).
The nested function must refer to a value defined in the enclosing function.
The enclosing function must return the nested function.'''

def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)

    return printer  # returns the nested function instead of calling printer()


# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")    # Output is now attached to another object.
another()

del print_msg
another()
print_msg("Hello")  # Does not exist now. Will throw NameError

