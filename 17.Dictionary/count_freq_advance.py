# my_list = [1, 2, 3, 1, 2, 2, 2, 4, 5, 6, 7, 8, 8, 9, 9, 9, 9, 9]

# my_dict = {}

# for num in my_list:
#     my_dict[num] = my_dict.get(num, 0) + 1

# print(my_dict)
# {1: 2, 2: 4, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 2, 9: 5}

my_list = "House of the dragon"

my_dict = {}

for num in my_list:
    my_dict[num] = my_dict.get(num, 0) + 1

print(my_dict)
# {'H': 1, 'o': 3, 'u': 1, 's': 1, 'e': 2, ' ': 3, 'f': 1, 't': 1, 'h': 1, 'd': 1, 'r': 1, 'a': 1, 'g': 1, 'n': 1}
