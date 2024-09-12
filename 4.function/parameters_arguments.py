# Parameters and Arguments
# If we pass Parameters compulsory we need to pass arguments

Ex: 1


def average(n1, n2, n3):  # Parameters
    total = n1 + n2 + n3
    print(f"Total is {total}")


average(10, 10, 10)  # Argumnets
average(20, 20, 20)
# average(100)  # TypeError: average() missing 2 required positional arguments: 'n2' and 'n3'

average("Hello", "Python", "John")  # average is HelloPythonJohn


Ex: 2


def average(n1: int, n2: int, n3: int):  # Parameters
    total = n1 + n2 + n3
    print(f"Total is {total}")


average(10, 10, 10)  # Argumnets
average(20, 20, 20)
average("Hello", "Python", "John")
