'''
define a base class shape with attributes width and height and a method to
calculate the area .create two subclass rectangle and triangle inheriting from
the shape class .demonstrate polymorphism by calling the area calculation
method or instances of both the classes in Python
'''
class shape:
    def __init__(s,w,h):
        s.width=w
        s.height=h
    def area(s):
        return undefined
class rectangle(shape):
    def __init__(s,length,breadth):
        s.l=length
        s.b=breadth
    def area(s):
        return s.l*s.b

class triangle(shape):
    def __init__(s,height,base):
        s.h=height
        s.base=base
    def area(s):
        return 0.5*s.h*s.base

r=rectangle(5,2)
print(f"Area of rectangle: {r.area()}")
c=triangle(2,9)
print(f"Area of triangle: {c.area()}")
