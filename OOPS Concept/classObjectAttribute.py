
class Dog():

    # CLASS OBJECT ATTRIBUTE
    # Same for all Child Classes
    pi = 3.14
    
    def __init__(self):
        print("Dog Created")

    def eat(self) :
        print("I am a dog and eating")
        
    def bark(self) :
        print("WOOF! ")