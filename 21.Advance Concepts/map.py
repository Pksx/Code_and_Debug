# # Example 1:
# def func(n):
#     return len(n)


# a = ("Singla", "Shivam", "Sachin")
# x = map(func, a)
# print(a)

# # convert the map into a list,
# #  for readability:
# print(list(x))

# # Example 2:
# numbers = (1, 2, 3, 4)
# res = map(lambda x: x * x * x, numbers)

# # converting map object to list
# numbersCube = list(res)
# print(numbersCube)

# Example 3:
name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(list(name_lengths))  # [4, 4, 3]

name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(tuple(name_lengths))  # (4, 4, 3)
