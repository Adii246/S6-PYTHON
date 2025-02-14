
'''
#TO PRINT THE FOLLOWING PATTERN
    *
  * * *
* * * * *

'''
rows = 3
x=0

for i in range(1, rows + 1):
    print(" " *(rows - i), end=" ")
    print("* "*(i+x),end=" ")
    x+=1
    print("\n")
    
