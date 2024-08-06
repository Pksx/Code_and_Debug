from typing import Dict

marks: Dict[str, int] = {
    "history": 65,
    "chemistry": 78,
    "science": 86,
    "english": 92,
    "maths": 100,
}
print(marks)

# Adding new key and value
# marks.update({"kannada": 99})
# print(marks)
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 100}
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 100, 'kannada': 99}

marks["kannada"] = 87
print(marks)
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 100}
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 100, 'kannada': 87}


# Change key and value to exisiting
# marks.update({"maths": 55})
# print(marks)
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 100}
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 55}

# marks["maths"] = 87
# print(marks)
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 100}
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 87}
