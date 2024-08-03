"""
Ask a number from user
Enter Element =1
Enter Element =5
Enter Element =4
Enter Element =3
Enter Element =2
Print result in [1,5,4,3,2]
"""

# Method 1
# a = int(input("Enter number= "))
# b = int(input("Enter number= "))
# c = int(input("Enter number= "))
# d = int(input("Enter number= "))
# e = int(input("Enter number= "))
# f = int(input("Enter number= "))

# print(f"abcdef in {[a,b,c,d,e,f]}") #abcdef in [1, 2, 3, 4, 5, 6]

# Method 2
my_list = []
num = int(input("Enter number= "))
#
for i in range(num):
    x = int(input("element: "))
    my_list.append(x)
print(my_list)

# Method 3
from typing import List


def create_list(length: int) -> List[int]:
    my_list = []
    for i in range(length):
        x = int(input(f"Enter Element {i+1}= "))
        my_list.append(x)
    return my_list


ls = create_list(6)
print(ls)  # [5, 6, 6, 7, 8, 9]
