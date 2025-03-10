'''
#********ABSTRACT METHOD******
from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(s):
        return null
class dog(animal):
    def sound(s):
        return "Bow Bow"
class cat(animal):
    def sound(s):
        return "Meow Meow"
d=dog()
c=cat()
print(c.sound())
print(d.sound())
'''
#****CONCRETE METHOD******
from abc import ABC,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(s):
        return null
    def colour(s):
        print("BLACK")
class dog(animal):
    def sound(s):
        return "Bow Bow"
class cat(animal):
    def sound(s):
        return "Meow Meow"
d=dog()
c=cat()
d.colour()
print(c.sound())
print(d.sound())
