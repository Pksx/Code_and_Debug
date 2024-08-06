marks = {
    "history": 65,
    "chemistry": 78,
    "science": 86,
    "english": 92,
    "maths": 100,
}
# print(marks)

# marks.clear()
# print(marks)  # {}

# print(marks.get("history"))  # 65
# # print(marks["history"])  # 65 if we enter key it will giv value
# print(marks.get("historyy"))  # None if we enter wrong key it will giv none
# print(marks.get("historyy", 0))  # 0
# None if we enter wrong key and enter a value is "0" instead of none

# marks.pop("maths")
# print(marks)
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92, 'maths': 100}
# {'history': 65, 'chemistry': 78, 'science': 86, 'english': 92}

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 1, "d": 4}

dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2, 'c': 1, 'd': 4}
