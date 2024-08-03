# Method 1:
# my_list = [4, 5, 3, 1, 7, 6, 59, 100]
# n = len(my_list)

# for i in range(n):
#     if my_list[i] % 2 == 0:
#         my_list[i] = my_list[i] + 1
#     elif my_list[i] % 2 != 0:
#         my_list[i] = my_list[i] - 1
# print(my_list)

# Method 2:
my_list = [4, 5, 3, 1, 7, 6, 59, 100]
n = len(my_list)

for i in range(n):
    if my_list[i] % 2 == 0:
        my_list[i] = my_list[i] + 1
    else:
        my_list[i] = my_list[i] - 1
print(my_list)
