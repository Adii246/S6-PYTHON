
'''
#******LAZY EVALUATION******
x = 10
y = 1
if y != 0 and (x / y > 1):  
    print("Condition met")
else:
    print("Division skipped due to lazy evaluation")
if x > 5 or y == 0:  
   print("First condition is True, so no need to check the second condition")
   
#*****GENERATORS******
gen=(x+2 for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#******RANGE()****

import time
for i in range(5):
    print(i)
    time.sleep(0.5)

#*******ZIP FUNCTION****

l1=1,2,3,4,5
l2='a','b','c','d'
z=zip(l1,l2)
print(list(z))
'''
#******TOOLS****

from itertools import count
for i in count(2,3):
    if i>8:
        break
    print(i)

from itertools import cycle
colors = cycle(['red', 'green'])
for _ in range(5):
    print(next(colors))
    
from itertools import repeat
print(list(repeat('hello', 3)))
