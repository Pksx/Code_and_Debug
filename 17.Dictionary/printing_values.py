my_dict = {
    "name": "John",
    "age": 18,
    "gender": "male",
    100: 200,
}
print(my_dict["name"])  # For Key is name and value is xyz
print(my_dict[100])  # For Key is 100 and value is 200
print(my_dict["100"])  # KeyError

my_dict = {
    "name": "John",
    "age": 18,
    "gender": "male",
    100: 200,
    "marks": [1, 2, 3, 4, 5],
}
print(my_dict["marks"])  # [1, 2, 3, 4, 5]
