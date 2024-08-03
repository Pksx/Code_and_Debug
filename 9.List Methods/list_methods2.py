"Insert"
# my_list = [5, 6, 7, "John", 77.67, True, False]
# print(my_list)  # [5, 6, 7, 'John', 77.67, True, False]
# my_list.insert(
#     3, 10
# )  #  Insert object before index (3 will be index and 100 will value of that index)

# my_list.insert(0, 100)

# # my_list.insert(50, 100)  # If more than index value it will be inserted at last

# my_list.insert(7, 100)

# my_list.insert(-2, 50)  # [5, 6, 7, 'John', 77.67, 50, True, False]
# print(my_list)  # [5, 6, 7, 10, 'John', 77.67, True, False]

"Pop"
# my_list = [5, 6, 7, "John", 77.67, True, False]
# print(my_list)  # [5, 6, 7, 'John', 77.67, True, False]
# x = my_list.pop()  # Remove and return item at index (default last).
# print(x)  # False
# my_list.pop(2)
# print(my_list)  # [5, 6, 'John', 77.67, True]


"del"
# my_list = [5, 6, 7, "John", 77.67, True, False]
# del my_list[0]
# print(my_list)  # [6, 7, 'John', 77.67, True, False]

# a = 5
# print(a)
# del a  # We delete any element it is not dedicated to list
# print(a)  # NameError: name 'a' is not defined

"Remove"
# my_list = [5, 6, 7, "John", 77.67, 7, 8, 7, True, False]
# print(my_list)
# my_list.remove(7)  # Remove first occurrence of value.
# print(my_list)  # [5, 6, 'John', 77.67, 7, 8, 7, True, False]
# Remove will delete first of its duplicate value

"Clear"
# my_list = [5, 6, 7, "John", 77.67, 7, 8, 7, True, False]
# my_list.clear()
# print(my_list)  # []

"Extend"
# my_list: list = [77.67, 7, 8, 7]
# print(my_list)
# my_list.append([1, 2, 3, 4])
# my_list.append([1, 2])
# print(my_list)  # [77.67, 7, 8, 7, [1, 2, 3, 4]]

# my_list.extend([4, 5, 6])
# print(my_list)  # [77.67, 7, 8, 7, 4, 5, 6]

"Count"
# my_list: list = [77.67, 7, 8, 7]
# print(my_list.count(7))  # 7 Will 2 times and Return number of occurrences of value.


"Index"
# my_list: list = [1, 7, 8, 7]
# x = my_list.index(1)  # 1 will be 0th index
# print(x)

"Sort"
# my_list: list = [1, 7, 8, 7, 8, 9, 6, 7]
# print(my_list)  # [1, 7, 8, 7, 8, 9, 6, 7]
# my_list.sort()  # Sort the list in ascending order and return None.
# print(my_list)  # [1, 6, 7, 7, 7, 8, 8, 9]
# my_list.sort(reverse=True)
# print(my_list)  # [9, 8, 8, 7, 7, 7, 6, 1] (Descending Value)


"Reverse"
my_list: list = [1, 7, 8, 7, 8, 9, 6, 7]
print(my_list)
my_list.reverse()  # Just Reverse the values
print(my_list)  # [7, 6, 9, 8, 7, 8, 7, 1]
