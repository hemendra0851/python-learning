from collections import namedtuple

Dog = namedtuple('Dog', ['name', 'age', 'breed'])

sammy = Dog(name='Sammy', age=2, breed='Lab')

print(sammy)
print(sammy.name)