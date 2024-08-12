details = {
    "John": {
        "age": 56,
        "gender": "Male",
        "marks": [55, 78, 68],
        "adult": True,
    },
    "Jaya": {
        "age": 36,
        "gender": "Female",
        "marks": [55, 78, 45, 68],
        "adult": True,
    },
    "Jafar": {
        "age": 28,
        "gender": "Male",
        "marks": [55, 78],
        "adult": True,
    },
}

# print(details["Jaya"])
# {'age': 36, 'gender': 'Female', 'marks': [55, 78, 45, 68], 'adult': True}

print(details["Jaya"]["gender"])  # Female
print(details["Jaya"]["marks"])  # [55, 78, 45, 68]
print(details["Jaya"]["marks"][-1])  # 68
