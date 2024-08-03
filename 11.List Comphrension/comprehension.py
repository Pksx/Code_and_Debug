# Basic Methods
# Ex:1
# my_list = []

# for i in range(1, 11):
#     my_list.append(i)
# print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"To print Even Numbers"
# my_list = []

# for i in range(1, 11):
#     if i % 2 == 0:
#         my_list.append(i)
# print(my_list)  # [2, 4, 6, 8, 10]

"List Comprehension"

my_list = [i for i in range(1, 11)]
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = [i for i in range(10, 0, -1)]
print(my_list)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
my_list = [i for i in range(1, 11, 2)]
print(my_list)  # [1, 3, 5, 7, 9]

my_list = [-1 for i in range(1, 6)]
print(my_list)  # [-1, -1, -1, -1, -1]

my_list = [i for i in range(1, 6)]
print(my_list)  # [1, 2, 3, 4, 5]

my_list = [-1 for _ in range(1, 6)]
print(my_list)  # [-1, -1, -1, -1, -1]
