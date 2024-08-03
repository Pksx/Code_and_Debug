# Method 1:

# my_list = [14, 25, 36, 87, 95, 25, 74]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])
# print(my_list[6])

# Method 2:
# Length = 7
my_list = [14, 25, 36, 87, 95, 25, 74]
n = len(my_list)

# Iterate by Index
# for i in range(0, n):
#     # print(i, end=" ") # 0 1 2 3 4 5 6
#     print(my_list[i], end=" ")  # 14 25 36 87 95 25 74

# Reverse Index
for i in range(n - 1, -1, -1):
    # print(i, end=" ")  # 6 5 4 3 2 1 0
    print(my_list[i], end=" ")  # 74 25 95 87 36 25 14
