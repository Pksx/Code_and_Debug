# List Methods are Functions

"Append"
# # Ex:1
# my_list = [5, 6, 7, "John", 77.67, True, False]
# print(my_list)

# my_list.append(100)  # Append object to the end of the list.
# print(my_list)
# Output
# [5, 6, 7, 'John', 77.67, True, False, 100]

# Ex:2
# my_list: list = ["John", 55, 79.05, True]
# my_list.append(500)
# print(my_list)  # ['John', 55, 79.05, True, 500]

# Ex: 3
# my_list: list[int] = ["John", 55, 79.05, True]
# my_list.append(500)
# print(my_list)  # ['John', 55, 79.05, True, 500]

# Ex:4
# my_list: list[int] = [14, 55, 79, 68, 88]
# my_list.append("John")
# print(my_list)  # [14, 55, 79, 68, 88, 'John']

import typing
from typing import List

my_list: List[int] = [
    14,
    55,
    79,
    68,
    88,
]  # List and list are annotation for our reference it wont take part of code
my_list.append(1000)
print(my_list)  # [14, 55, 79, 68, 88, 1000]
