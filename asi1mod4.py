'''
#ASSIGNMENT

Simple Real-World Inheritance Example: School Management System You're
developing a School Management System to manage different types of people
in a school.

Requirements:

Create a base class Person with attributes:

name
age
A method display_info() to print person details.
Create a derived class Teacher that inherits from Person, with additional
attributes:

subject (the subject they teach)
Override display_info() to include the subject.
Create another derived class Student that inherits from Person, with additional attributes:
grade (e.g., 10th Grade)
Override display_info() to include the grade.
'''
class Person:
    def __init__(s,name,age):
        s.n=name
        s.a=age
    def display_info(s):
        print("Name:",s.n,"\nAge:",s.a)
       
class Teacher(Person):
    def __init__(s,name,age,subject):
        Person.__init__(s,name,age)
        s.subject=subject
    def display_info(s):
        print("****DETAILS OF TEACHER****")
        super().display_info()
        print("Subject:",s.subject)
        print("\n")

class student(Person):
    def __init__(s,name,age,grade):
        s.grade=grade
        Person.__init__(s,name,age)
    def display_info(s):
        print("****DETAILS OF STUDENT****")
        print("Name:",s.n,"\nAge:",s.a)
        print("Grade:",s.grade)

t1=Teacher("Adi",50,"maths")
t1.display_info()
s1=student("Akhi",20,"PASS")
s1.display_info()
    
    
