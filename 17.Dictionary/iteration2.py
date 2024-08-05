marks = {
    "history": 65,
    "chemistry": 78,
    "science": 86,
    "english": 92,
    "maths": 100,
}

# Dictonary functions
# print(marks.keys())
# dict_keys(['history', 'chemistry', 'science', 'english', 'maths'])

# for k in marks.keys():
#     print(k, end=" ")  # history chemistry science english maths
#     print(k, marks[k], end=" ")

# for v in marks.values():
#     print(v, end=" ")  # 65 78 86 92 100

print(marks.items())
# dict_items([('history', 65), ('chemistry', 78), ('science', 86), ('english', 92), ('maths', 100)])

result = marks.items()
