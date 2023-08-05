class Circle():
    
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        
    def area(self):
        return (self.radius**2)*self.pi
    
obj = Circle(10)
print(obj.area())