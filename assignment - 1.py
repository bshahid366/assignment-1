# 2. Write a Python program to get the Python version you are using
print("Version")
import sys
print(sys.version)


# 3. Write a Python program to display the current date and time.
print("\n\nDate & Time")
import datetime
print(datetime.datetime.now())

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
print("\n\nRadius and Area")
radius = int(input('Enter Radius: '))
Area = (22/7)*radius**2
print(Area)

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
print("\n\nInverted Name")
x = input('Enter First Name: ')
y = input('Enter Last Name: ')
print(y, x)

# 6. Write a python program which takes two inputs from user and print them addition
print("\n\nSum of two inputs")
x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
total = x + y
print('Total= ', total)