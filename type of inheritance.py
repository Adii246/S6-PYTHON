#TYPES OF INHERITANCE
#1.SINGLE INHERTANCE
'''
class parent:
    def f1(s):
        print("hlo")

class child(parent):
    def f2(self):
        print("hai")

c=child()
c.f1()
c.f2()

#2.MULTIPLE INHERTANCE
class parent1:
    def f1(s):
        print("I am function1")

class parent2:
    def f2(s):
        print("I am function2")


class child(parent1,parent2):
    def f3(self):
        print("I am the child")

c=child()
c.f1()
c.f2()       
c.f3()

# multiple inheritance

class Mother:
	def mother(self):
		print("Mother :", self.mothername)
class Father:
	def father(self):
		print("Father :", self.fathername)
class Son(Mother, Father):
    def parents(self):
        super().mother()
        super().father()
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()

#3.MULTILEVEL INHERITANCE
class summ:
    def __init__(s):
        print("2+3:",2+3)
        
class mull(summ):
    def __init__(s):
        super().__init__()
        print("2*3:",2*3)
class both(mull):
    def __init__(s):
        super().__init__()
        print("finished")
x=both()


#*****Heirarchical inheritance

class parent():
    def __init__(self,name):
        self.name=name
        print("My name is ",self.name)
class child1(parent):
    def __init__(self,name,age):
        self.age=age
        print("Age:",self.age)
        super().__init__(name)
class child2(parent):
    def __init__(self,name,year):
        self.year=year
        print("Year:",self.year)
        super().__init__(name)
c1=child1("Adi",20)
print("*******")
c1=child2("Adhi",2004)

'''
#*******HYBRID INHERITANCE*****

class parent:
    def func1(s):
        print("My name is adi")
class parent1:
    def func4(s):
        print("I work hard")
class child1(parent):
    def func2(s):
        print("I am 20")
class child3(parent,parent1):
    def func3(s):
        print("I am from Kerala")

c=child3()
c.func3()
c.func1()
c.func4()
#c.func2()//this is not possivle bcs child3 do not refer to child1        
