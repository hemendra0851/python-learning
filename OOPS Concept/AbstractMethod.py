class Animal():
    
    def __init(self, name):
        self.name = name
    
    def eat(self):
        raise NotImplementedError('Method Not Implemented in Child Class')

class Dog(Animal):

    def __init__(self):
        # Animal.init(self)
        print("Dog Created")

    # def eat(self) :
    #     print("I am a dog and eating")
        
    def bark(self) :
        print("WOOF! ")
        
obj = Dog()
# obj.name = 'Hello'
obj.bark()

