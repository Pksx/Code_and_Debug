"""
Take values of length and breadth of a rectangle from user 
and check if it is square or not.
"""

# Taking the values from the User
length = int(input("Enter the Length: "))
breadth = int(input("Enter the breadth: "))

# Checking if the rectangle is a square or not
if length == breadth:
    print("It is a square")
else:
    print("It is a rectangle")
