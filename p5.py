#Assignment
'''
Write a Python program that iterates through the numbers from 0 to 9. For each number:

  If the number is even, print that it is even.

  If the number is odd, skip the rest of the loop for that iteration.

  If the number equals 6, stop the loop before it finishes.
  
'''
for i in range(10):
    
    if i%2==0:
        print(f"{i} is even")
    else:
        continue
    if i==6:
        break;

#**********
#formatting
print("my name is %s and my age is %d" %('adi',24))

s='adi','is','a','good','girl'
print(" ".join(s))

eg = """
hloo
I am studying Btech
I love python
"""
print(eg)

import pprint
a={
    'name':'adi',
    'age':20,
    'course':'CSE'
    }
pprint.pprint(a)

from tabulate import tabulate
data=[['adi',30],['akhi',35]]
print(tabulate(data,headers=['NAME','AGE'],tablefmt='fancy_grid'))

















      
