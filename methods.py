
#******METHODS*****
class car:
    def s(self):
        print("i have car")
c=car()
c.s()


#*****class variable****
class car:
    wheels=4
    def __init__(s,name,yr):
        s.n=name
        s.y=yr
c1=car("swift",2004)
print(c1.wheels)
car.wheels=6
print(c1.wheels)
        

