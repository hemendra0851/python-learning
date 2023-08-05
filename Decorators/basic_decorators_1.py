
#### Basic decorator #####

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

# def ordinary():
#     print("I am ordinary")  # Option 1

@make_pretty
def ordinary():
    print("I am ordinary") # Option 2
    

ordinary()
# let's decorate this ordinary function
pretty = make_pretty(ordinary)



