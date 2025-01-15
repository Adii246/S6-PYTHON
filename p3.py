'''Practice Questions

Write a Python program that asks the user for their age and whether they are a student.
The program should determine if the user is eligible for a discount based on the following conditions:
The user must be under 25 years old (age < 25).
The user must be a student (is_student is True).
The program should:

Take the user's age as an integer input.
Ask the user if they are a student, entering "yes" or "no".
Print "You are eligible for a discount." if both conditions are met.
Print "You are not eligible for a discount." if the conditions are not met.
Note: Avoid using if-else statements for decision making. Instead, use a direct conditional expression in the print statement.
'''

o=input("are u a student").lower().strip()
age=int(input("Tell me your age"))      
print("eligible" if o=='yes' and age <25 else " not eligible")
