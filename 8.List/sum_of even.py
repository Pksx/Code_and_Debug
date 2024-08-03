"""
Tell  me the sumof all even numbers
"""

my_list = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]

# Iterate by Index
n = len(my_list)
total = 0
for index in range(0, n):
    if my_list[index] % 2 == 0:
        total = total + my_list[index]
print(total)

# Iterate by value
total2 = 0
for num in my_list:
    if num % 2 == 0:
        total2 = total2 + num
print(total2)
