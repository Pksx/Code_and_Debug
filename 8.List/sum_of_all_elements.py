my_list = [14, 25, 36, 87, 95, 25, 74]

# Iterate by Index
total = 0
n = len(my_list)
for i in range(0, n):
    total = total + my_list[i]
print(total)  # 356

# Iterate by Value
total2 = 0
for i in my_list:
    total2 = total2 + i
print(total2)  # 356
