# Default Parameter

# Method 1
# def marks(sci=0, maths=0, hindi=0, english=0, computer=0):
#     print(sci, maths, hindi, english, computer)
#     total = sci + maths + hindi + english + computer
#     print(f"Total is {total}")
#     percentage = total / 5
#     print(f"Percentge is {percentage}%")


# marks()  # 0 0 0 0 0
# marks(15, 10)


# Method 2
# def marks(sci=0, maths=0, hindi=0, english=50, computer: int = 100):
#     print(sci, maths, hindi, english, computer)
#     total = sci + maths + hindi + english + computer
#     print(f"Total is {total}")
#     percentage = total / 5
#     print(f"Percentge is {percentage}%")


# marks(15, 10)  # 15 10 0 50 100


# Required and Optional Parameters:
# Required Parameters need to keep in left side


def intro(name, age="", gender=""):
    print(name, age, gender)


def marks(sci, maths, hindi=0, english=0, computer=0):
    print(sci, maths, hindi, english, computer)
    total = sci + maths + hindi + english + computer
    print(f"Total is {total}")
    percentage = total / 5
    print(f"Percentge is {percentage}%")


# marks(15)  # TypeError: marks() missing 1 required positional argument: 'maths'
