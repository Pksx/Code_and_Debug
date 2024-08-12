"""
Take 2 numbers from user input and check fisrt number is divisible by the sceond
"""

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# if num1 % num2 == 0:
#     print("num1 is divisible by num2")
# else:
#     print("num1 is not divisible by num2")


# or
num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))
if num2 != 0 and num1 % num2 == 0:
    print(f"{num1} is divisible by {num2}")
else:
    print(f"{num1} is not divisible by {num2}")
