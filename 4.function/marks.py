"""
Make a function named marks,it should take 5 integers as a parameter
Print the total
and print the percentage
"""

# Method 1:
# def marks(num1, num2, num3, num4, num5):
#     total = num1 + num2 + num3 + num4 + num5
#     print(f"Total is {total}")
#     percentage = total / 5
#     print(f"Percentge is {percentage}%")


# marks(50, 20, 100, 75, 65)
# marks(100, 100, 100, 100, 100)


# Method 2
def marks(num1: int, num2: int, num3: int, num4: int, num5: int):
    total = num1 + num2 + num3 + num4 + num5
    print(f"Total is {total}")
    percentage = total / 5
    print(f"Percentge is {percentage}%")


m1 = int(input("Enter num1: "))
m2 = int(input("Enter num2: "))
m3 = int(input("Enter num3: "))
m4 = int(input("Enter num4: "))
m5 = int(input("Enter num5: "))

marks(m1, m2, m3, m4, m5)


# Method 3
def marks():
    m1 = int(input("Enter num1: "))
    m2 = int(input("Enter num2: "))
    m3 = int(input("Enter num3: "))
    m4 = int(input("Enter num4: "))
    m5 = int(input("Enter num5: "))
    total = m1 + m2 + m3 + m4 + m5
    print(f"Total is {total}")
    percentage = total / 5
    print(f"Percentge is {percentage}%")


marks()
