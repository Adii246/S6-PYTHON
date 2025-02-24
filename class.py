class car:
    def __init__(self,brand,model,year,mileage=0):
        self.b=brand
        self.m=model
        self.y=year
        self.m=mileage
    def drive(self,km):
        self.m= km+self.m
    def displayinfo(self):
        print(f"{self.b},{self.m},{self.y},{self.m}")

c1=car("TOYOTA","COROLLA",2020,100)
c2=car("VOLKSWAGEN","CURLA",2004)
c1.displayinfo()
c1.drive(100)
c1.displayinfo()

    
