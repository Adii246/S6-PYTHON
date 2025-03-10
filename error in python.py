n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
try:
    result=n1/n2
    print(f"{n1}/{n2}={result}")
except (ZeroDivisionError,ValueError) as e:
    print(f"error by {e}")
    
#***OR method***
'''
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
'''
