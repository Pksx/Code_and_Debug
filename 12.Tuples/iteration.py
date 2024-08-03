my_tuple = (1, 2, 3, "John", True, 45.67, 3, 4, 7)
# By Index
n = len(my_tuple)
for i in range(n):
    print(my_tuple[i], end=" ")  # 1 2 3 John True 45.67 3 4 7
print()

# By Value
for i in my_tuple:
    print(i, end=" ")
