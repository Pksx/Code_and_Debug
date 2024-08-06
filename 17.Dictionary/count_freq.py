# Output
# {
#     1:2
#     9:4
#     2:3

# }
my_list = [1, 2, 3, 1, 2, 2, 2, 4, 5, 6, 7, 8, 8, 9, 9, 9, 9, 9]

my_dict = {}

for num in my_list:
    if num in my_dict:
        my_dict[num] = my_dict[num] + 1
    else:
        my_dict[num] = 1

print(my_dict)
# {1: 2, 2: 4, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 2, 9: 5}
