# Ask an Integer,print even or odd

# integer = int(input("Enter your number: "))

# if integer % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Divisible by 5
# integer = int(input("Enter your number: "))

# if integer % 5 == 0:
#     print("Divisible")
# else:
#     print("Not divisible")

# Divisible by both 3 and 2
# integer = int(input("Enter your number: "))

# if integer % 2 == 0 and integer % 3 == 0:
#     print("Divisible")
# else:
#     print("Not divisible")

# Divisible by any one 3 or 2
integer = int(input("Enter your number: "))

if integer % 2 == 0 or integer % 3 == 0:
    print("Divisible")
else:
    print("Not divisible")
