"""
John has score total marks
Jaya has score total marks
Jafar has score total marks
"""

details = {
    "John": {
        "age": 56,
        "gender": "Male",
        "marks": [55, 78, 68],
        "adult": True,
    },
    "Jaya": {
        "age": 16,
        "gender": "Female",
        "marks": [55, 78, 45, 68],
        "adult": False,
    },
    "Jafar": {
        "age": 28,
        "gender": "Male",
        "marks": [55, 78],
        "adult": True,
    },
}

# Method 1:
# for name, info in details.items():
#     print(f"{name} has scored {sum(info['marks'])}")
# John has scored 201
# Jaya has scored 246
# Jafar has scored 133

# Method 2:
# for name, info in details.items():
#     total = 0
#     for mark in info["marks"]:
#         total = total + mark
#     print(f"{name} has scord {total} marks")
"""
#Output
# John has scored 201
# Jaya has scored 246
# Jafar has scored 133  
"""

# Method 3 By Indeing:
for key in details:
    total = 0
    for mark in details[key]["marks"]:
        total += mark
    print(f"{key} has scored {total} marks")
"""
#Output
# John has scored 201
# Jaya has scored 246
# Jafar has scored 133  
"""
