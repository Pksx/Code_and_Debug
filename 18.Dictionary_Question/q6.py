"""
John has score highest marks
Jaya has score highest marks
Jafar has score highest marks
"""

details = {
    "John": {
        "age": 56,
        "gender": "Male",
        "marks": [55, 99, 68],
        "adult": True,
    },
    "Jaya": {
        "age": 16,
        "gender": "Female",
        "marks": [55, 85, 45, 68],
        "adult": False,
    },
    "Jafar": {
        "age": 28,
        "gender": "Male",
        "marks": [55, 100],
        "adult": True,
    },
}

for name, info in details.items():
    for mark in info["marks"]:
        print(name, mark)
