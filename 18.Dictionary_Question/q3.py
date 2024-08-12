"""
Print
A as scored total marks
b as scored total marks
c as scored total marks
"""

from typing import Dict, List


# Method 1:
# def DisplayDetails(my_dict: Dict[str, List[int]]) -> None:
#     for name, marks in my_dict.items():
#         print(f"{name} has scored {sum(marks)}")


# details = {
#     "Anirudh": [45, 65, 78, 99, 12],
#     "Lokesh": [54, 68, 74, 98, 70],
#     "Ravi": [50, 69, 78, 36, 25],
#     "Tejas": [85, 65, 87, 91, 99],
#     "Rakesh": [96, 69, 78, 89, 99],
# }

# DisplayDetails(details)


# Method 2:
# def DisplayDetails(my_dict: Dict[str, List[int]]) -> None:
#     for name, marks in my_dict.items():
#         total = 0
#         for mark in marks:
#             total = total + mark
#         print(f"{name} has scored {total} marks")


# details = {
#     "Anirudh": [45, 65, 78, 99, 12],
#     "Lokesh": [54, 68, 74, 98, 70],
#     "Ravi": [50, 69, 78, 36, 25],
#     "Tejas": [85, 65, 87, 91, 99],
#     "Rakesh": [96, 69, 78, 89, 99],
# }

# DisplayDetails(details)
# # Output
# Anirudh has scored 299 marks
# Lokesh has scored 364 marks
# Ravi has scored 258 marks
# Tejas has scored 427 marks
# Rakesh has scored 431 marks


# Method 3:
def DisplayDetails(my_dict: Dict[str, List[int]]) -> None:
    for name, marks in my_dict.items():
        total = 0
        for mark in marks:
            total = total + mark
        print(f"{name} has scored {total} marks")


details = {
    "Anirudh": [45, 65, 78],
    "Lokesh": [54, 68, 74, 98, 70, 89],
    "Ravi": [50, 69, 78, 36],
    "Tejas": [85, 65, 87, 91, 99],
    "Rakesh": [96, 69],
}

DisplayDetails(details)
# Output
# Anirudh has scored 188 marks
# Lokesh has scored 453 marks
# Ravi has scored 233 marks
# Tejas has scored 427 marks
# Rakesh has scored 165 marks


# Method 4:
# By Index and items Method
def DisplayDetails(my_dict: Dict[str, List[int]]) -> None:
    for name, marks in my_dict.items():
        total = 0
        for i in range(0, len(marks)):
            total = total + marks[i]
        print(f"{name} has scored {total} marks")


details = {
    "Anirudh": [45, 65, 78],
    "Lokesh": [54, 68, 74, 98, 70, 89],
    "Ravi": [50, 69, 78, 36],
    "Tejas": [85, 65, 87, 91, 99],
    "Rakesh": [96, 69],
}

DisplayDetails(details)
# Output
# Anirudh has scored 188 marks
# Lokesh has scored 453 marks
# Ravi has scored 233 marks
# Tejas has scored 427 marks
# Rakesh has scored 165 marks


# Method 5:
# Without .items method
def DisplayDetails(my_dict: Dict[str, List[int]]) -> None:
    for key in my_dict:
        total = 0
        for i in range(0, len(my_dict[key])):
            total = total + my_dict[key][i]
        print(f"{key} has scored {total} marks")


details = {
    "Anirudh": [45, 65, 78],
    "Lokesh": [54, 68, 74, 98, 70, 89],
    "Ravi": [50, 69, 78, 36],
    "Tejas": [85, 65, 87, 91, 99],
    "Rakesh": [96, 69],
}

DisplayDetails(details)
# Output
# Anirudh has scored 188 marks
# Lokesh has scored 453 marks
# Ravi has scored 233 marks
# Tejas has scored 427 marks
# Rakesh has scored 165 marks
