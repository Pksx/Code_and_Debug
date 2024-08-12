my_string = "ahbhsjdretoqqaaraaaaaaa"

my_dict = {}
for num in my_string:
    my_dict[num] = my_dict.get(num, 0) + 1
print(my_dict)  # {4: 4, 5: 1, 1: 1, 3: 1, 7: 6, 8: 4, 9: 4}

max_freq = 0
max_element = 0
for key in my_dict:
    if my_dict[key] > max_freq:
        max_freq = my_dict[key]
        max_element = key
print(f"Max elemet= {max_element} Max Frequency = {max_freq}")
#
# Try Minimum Frequency
