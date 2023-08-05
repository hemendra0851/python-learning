
#####  Passing function as an argument ############

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc,3))
# >>> 4
print(operate(dec,3))
# >>> 2

#### Return another function from a function #####

def is_called():
    def is_returned():
        print("Hello")
    return is_returned

new = is_called()

# Outputs "Hello"
new()

#### Return another function from a function #####

def is_called():
    def is_returned():
        return "Hello"
    return is_returned

new = is_called()

# Outputs "Hello"
print(new())

