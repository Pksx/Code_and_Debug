my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
n = len(my_list)

for i in range(0, n):
    if my_list[i] % 2 != 0:
        result.append(my_list[i])

print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(result)  # [1, 3, 5, 7, 9]
