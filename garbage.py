import gc
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student", self.name, "created.")


s = Student("Bob", 22)
s2 = s
print("Student exists:", s.name, "Age:", s.age)
del s
print("Student still exists:", s2.name, "Age:", s2.age)
gc.collect()
