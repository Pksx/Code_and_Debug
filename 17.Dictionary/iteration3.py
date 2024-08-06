marks = {
    "history": 65,
    "chemistry": 78,
    "science": 86,
    "english": 92,
    "maths": 100,
}

result = marks.items()

# for i in result:
#     print(i, end=" ")
# ('history', 65) ('chemistry', 78) ('science', 86) ('english', 92) ('maths', 100)

for k, v in result:
    print(f"Key = {k}, Value = {v}")
# #Key = history, Value = 65
# Key = chemistry, Value = 78
# Key = science, Value = 86
# Key = english, Value = 92
# Key = maths, Value = 100
