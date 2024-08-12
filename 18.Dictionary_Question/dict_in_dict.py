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
# To print name in dict
# for name, info in details.items():
#     if info["adult"] == True:
#         print(name)  # John ,Jafar
# To print age
for name, info in details.items():
    if info["adult"] == True:
        print(name, info["age"])  # John 56
