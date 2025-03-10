'''
from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def name(s,name):
        pass
class dog(animal):
    def name(s,name):
        s.name=name
        print(s.name)

d=dog()
d.name("MAX")    
'''

#********MULTIPLE INHERITANCE*****
from abc import ABC,abstractmethod
class book(ABC):
    @abstractmethod
    def name(s,name):
        pass
class authorname(ABC):
    @abstractmethod
    def author(s,name):
        pass
class details(book,authorname):
    def name(s,name):
        print("Name of the book:",name)
    def author(s,name):
        print("Name of the author:",name)
d=details()
d.name("HARRY POTTER")
d.author("MARK")


    
