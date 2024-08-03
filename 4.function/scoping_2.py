"""Scoping in Functions"""


def info():
    # Local variables
    num1 = 100
    num2 = 200
    total = num1 + num2
    print(total)
    greet()


def greet():
    name = "John"
    print(f"Hello {name}")
    info()


info()

# RecursionError: maximum recursion depth exceeded while calling a Python object
