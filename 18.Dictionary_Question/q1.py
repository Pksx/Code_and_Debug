# my_list = [4, 5, 1, 3, 7, 4, 7, 4, 4, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]

#  find the Maximum Frequency

# my_dict = {}

# for num in my_list:
#     my_dict[num] = my_dict.get(num, 0) + 1
# print(my_dict)  # {4: 4, 5: 1, 1: 1, 3: 1, 7: 6, 8: 4, 9: 4}

# ans = 0
# for key in my_dict:
#     if my_dict[key] > ans:
#         ans = my_dict[key]
# print(ans)  # 6

# Example 2:
# my_list = [4, 5, 1, 3, 7, 4, 7, 4, 4, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]

# # find the Maximum Frequency
# # find the maximum frequency of whose?
# my_dict = {}

# for num in my_list:
#     my_dict[num] = my_dict.get(num, 0) + 1
# print(my_dict)  # {4: 4, 5: 1, 1: 1, 3: 1, 7: 6, 8: 4, 9: 4}

# max_freq = 0
# max_element = 0
# for key in my_dict:
#     if my_dict[key] > max_freq:
#         max_freq = my_dict[key]
#         max_element = key
# print(f"Max elemet= {max_element} Max Frequency = {max_freq}")
# Max elemet= 7 Max Frequency = 6

# Method 2:
my_list = [4, 5, 1, 3, 7, 4, 7, 4, 4, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9]

# find the Maximum Frequency
# find the maximum frequency of whose?
my_dict = {}

for num in my_list:
    my_dict[num] = my_dict.get(num, 0) + 1
print(my_dict)  # {4: 4, 5: 1, 1: 1, 3: 1, 7: 6, 8: 4, 9: 4}

max_freq = 0
max_element = 0
for key, values in my_dict.items():
    if my_dict[key] > max_freq:
        max_freq = my_dict[key]
        max_element = key
print(f"Max elemet= {max_element} Max Frequency = {max_freq}")
