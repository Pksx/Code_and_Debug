# Dictionary is Key and Value
# Unique and Ordered and No Indexing
# my_dict = {
#     "name": "John",
#     "age": 18,
#     "gender": "male",
#     100: 200,
# }
# print(my_dict)
# print(type(my_dict))  # {'name': 'John', 'age': 18, 'gender': 'male', 100: 200}

# If you add key with same name it will take the latest key and value

my_dict = {
    "name": "John",
    "age": 18,
    "gender": "male",
    100: 200,
    "name": "xyz",
}
print(my_dict)  # {'name': 'xyz', 'age': 18, 'gender': 'male', 100: 200}
print(type(my_dict))  # <class 'dict'>
