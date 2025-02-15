#write a prgrm that accepts a sentence and calculate the number of words, digits,uppercase letter and lowercase letter

s=input("Enter the string")
length=len(s.split())
count,m,k=0,0,0
print("No of words:",length)
for char in s:
    if char.isdigit():
        
        count += 1
    
    elif char.isupper():
        m += 1
    elif char.islower():
        k += 1
    else:
        pass
print("no of digit:",count)
print("Number of uppercase letters:", m)
print("Number of lowercase letters:", k)

