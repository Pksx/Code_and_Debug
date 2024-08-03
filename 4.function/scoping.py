# EX:1

# def info():
#     pass
# print("Start")
# info()
# print("End")

"""Scoping in Functions"""


def info():
    # Local variables
    num1 = 100
    num2 = 200
    total = num1 + num2
    print(total)
    print(num1)  # Inside the function we can call


def greet():
    name = "John"
    print(f"Hello {name}")


info()
# print(num1) # We can't print num1, bcoz num is local variable and it is inside the function.
