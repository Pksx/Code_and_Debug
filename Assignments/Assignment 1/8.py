"""
Ask a number from user. Print if the number is ODD or EVEN.
"""

number = int(input("Enter your Number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
