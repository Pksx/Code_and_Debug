my_list = [4, 5, 3, 1, 7, 6, 59, 100]

# By Index

n = len(my_list)
for i in range(n):
    if my_list[i] % 2 == 0:
        my_list[i] = my_list[i] + 5

print(my_list)  # [9, 5, 3, 1, 7, 11, 59, 105]
