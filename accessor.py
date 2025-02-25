#****ACCESSOR and MUTATOR*****

class car:
    def __init__(s,name="swift"):
        s.n=name
    def getname(s):
        return s.n
    def setname(s,newname):
        s.n=newname
        return s.n
c1=car()
print(c1.n)
print(c1.setname("toyota"))


