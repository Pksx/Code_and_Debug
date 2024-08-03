# SPlit-> String to List
# Join ->List to String

# my_list = ["J", "o", "h", "n"]

# print(str(my_list))  # ['J', 'o', 'h', 'n']


# Example 2:
# my_list = ["J", "o", "h", "n"]

# result = " ".join(ch for ch in my_list)  # With Space
# print(result)  # J o h n

# Example 3:
my_list = ["J", "o", "h", "n"]

result = "".join(ch for ch in my_list)  # Without Space
print(result)  # John
result = "-".join(ch for ch in my_list)  # Without Space
print(result)  # J-o-h-n

# Example 4:
# my_list = ["a", 4, 5, 6, 7, 8, "John", "a", "b", "C"]
# print("".join(ch for ch in my_list))  # For Join only strings will work

# Example 5:
my_list = ["a", 4, 5, 6, 7, 8, "John", "a", "b", "C"]
print(" ".join(str(ch) for ch in my_list))  # a 4 5 6 7 8 John a b C
