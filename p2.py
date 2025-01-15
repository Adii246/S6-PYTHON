a,b,c=1,2,3
print(a,b,c)


n=input("name??\n")
print("name is "+n)

a=input("tell me ur age:\n")
a=int(a)
print("my age is "+str(a)+" ...")

name=input("enter ur name:\t")
b=int(input("enter ur birth yr:\t"))
print("My name is "+name+". My age is "+str(2025-b))



x=10
print(f"x is num:{x}")
print("Hloo {}".format("adi"))
print(f"i am {x} years old")

print("******Charater Set-ord and chr******")
print("\n")
a='A'
print("unicode of A is",ord(a))
print("unicode of l is {}".format(ord("l")))
b=97
print("character for 97 is",chr(b))
a="1,2,3,4,5,6"
print(a)
print("Greek Letter: \u03A9") 
print("Hindi: नमस्ते") 

m=10
n=5
print(f"{m} is greater than {n}:{m<n}")
