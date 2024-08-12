"""
Print total maximum marks
print name with total maximum marks 
"""

from typing import Dict, List


def max_marks(my_dict: Dict[str, List[int]]) -> None:
    max_marks = 0
    maxi_student = None
    for name, marks in my_dict.items():
        total = 0
        for i in range(0, len(marks)):
            total = total + marks[i]
        if total > max_marks:
            max_marks = total
            maxi_student = name
    print(max_marks, maxi_student)


details = {
    "Anirudh": [45, 65, 78],
    "Lokesh": [54, 68, 74, 98, 70, 89],
    "Ravi": [50, 69, 78, 36],
    "Tejas": [85, 65, 87, 91, 99],
    "Rakesh": [96, 69],
}

max_marks(details)
