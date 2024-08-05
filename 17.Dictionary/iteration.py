marks = {
    "history": 65,
    "chemistry": 78,
    "science": 86,
    "english": 92,
    "maths": 100,
}

# By value
# for i in marks:
#     print(i, end=" ")  # history chemistry science english maths

# By Keys
for k in marks:
    # print(k, end=" ")  # history chemistry science english maths
    # print(marks[k], end=" ")  # 65 78 86 92 100
    print(f"key = {k}, value = {marks[k]}")

total = 0
for k in marks:
    total = total + marks[k]
print(total)  # 421
