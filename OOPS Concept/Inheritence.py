class Animal():
    
    def __init(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):

    def __init__(self):
        # Animal.init(self)
        print("Dog Created")

    def eat(self) :
        print("I am a dog and eating")
        
    def bark(self) :
        print("WOOF! ")
        
obj = Dog()
# obj = Animal()
obj.name = 'Hello'
obj.eat()
obj.eat()

