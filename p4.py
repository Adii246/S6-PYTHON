'''
print(2**3)
a=5
b=5
c=5
print("equal" if a==b and c==b else "notequal" )


a=[1,2,3]
b=[1,2,3]
c=a
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)

#INBUILT FUNCTIONS

'''
s='adithya'
a=10,20,300,20,20,10
b=20
c=4

print(len(s))
print(max(a))
print(min(a))
print(sum(a))

import random
import math
import datetime
import json
from collections import Counter
import os

print(random.randint(5,200))
print(math.sqrt(c))
print(math.factorial(c))
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
data_dict = {"name": "Alice", "age": 30, "city": "New York"}
json_data = json.dumps(data_dict)
print(f"JSON string: {json_data}")
parsed_data = json.loads(json_data)
print(f"Parsed JSON data: {parsed_data}")
print("Element counts in the list:",Counter(a) )
current_dir = os.getcwd()
print(f"Current working directory: {current_dir}")
files_in_dir = os.listdir(current_dir)
print(f"Files and directories in the current directory: {files_in_dir}")
