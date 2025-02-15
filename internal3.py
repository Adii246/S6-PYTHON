#count the occurence of a given character
s=input("Enter the string")
dict={}
for i in s:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
