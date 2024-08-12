# Task 1:
# Inputs(10,50,30)->(50 Output)


def largest(n1, n2, n3):
    print(f"Total numbers are {n1, n2, n3}")
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


n1 = int(input("Enter Num1= "))
n2 = int(input("Enter Num2= "))
n3 = int(input("Enter Num3= "))
x = largest(n1, n2, n3)
print(f"largest number is {x}")

# Task 2:
# Input =(50,50,50)->(50-Output)
# def largest(n1, n2, n3):
#     print(f"Total numbers are {n1, n2, n3}")
#     if n1 > n2 and n1 > n3:
#         return n1
#     elif n2 > n1 and n2 > n3:
#         return n2
#     else:
#         return n3


# n1 = int(input("Enter Num1= "))
# n2 = int(input("Enter Num2= "))
# n3 = int(input("Enter Num3= "))
# x = largest(n1, n2, n3)
# print(f"largest number is {x}")


# Task 3:
# Input =(-56,-96,-11)->(-11->Output)
def largest(n1, n2, n3):
    print(f"Total numbers are {n1, n2, n3}")
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


n1 = int(input("Enter Num1= "))
n2 = int(input("Enter Num2= "))
n3 = int(input("Enter Num3= "))
x = largest(n1, n2, n3)
print(f"largest number is {x}")


# Main Answer
def find_largest(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


a = int(input())
b = int(input())
c = int(input())

largest = find_largest(a, b, c)

print(largest)
