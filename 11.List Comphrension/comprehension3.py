"""
i-> 1 to 10

1,3,5,7,9->ODD
2,4,6,8-> Even
"""

# my_list = ["even" if i % 2 == 0 else "odd" for i in range(1, 11)]
# print(my_list)
# # ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

# my_list = ["even" if i % 2 == 0 else i for i in range(1, 11)]
# print(my_list)
# # [1, 'even', 3, 'even', 5, 'even', 7, 'even', 9, 'even']

# my_list = [f"even - {i}" if i % 2 == 0 else f"odd - {i}" for i in range(1, 11)]
# print(my_list)
# # ['odd - 1', 'even - 2', 'odd - 3', 'even - 4', 'odd - 5', 'even - 6', 'odd - 7', 'even - 8', 'odd - 9', 'even - 10']

# my_list = [f"{i}" if i % 2 == 0 else f" {i}" for i in range(1, 11)]
# print(my_list)
# [' 1', '2', ' 3', '4', ' 5', '6', ' 7', '8', ' 9', '10']

"By Value"
my_list = [14, 25, 36, 69, 58, 47]
ans = [num for num in my_list if num % 2 == 0]
print(ans)  # [14, 36, 58]

"By Index"
my_list = [14, 25, 36, 69, 58, 47]
ans = [my_list[i] for i in range(0, len(my_list)) if my_list[i] % 2 == 0]
print(ans)  # [14, 36, 58]
