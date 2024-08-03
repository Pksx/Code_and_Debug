my_list = [15, 48, 69, 23, 74, 12, 58, 99, 21]

# x = my_list[0:4]
"It will print all values upto end [0:],[:],[:end value]"
# x = my_list[0:]  # [15, 48, 69, 23, 74, 12, 58, 99, 21]
# x = my_list[:]
# x = my_list[:9]
# x = my_list[:]
"it will be incremented with the value given"
# x = my_list[0:9:2]  # [15, 69, 74, 58, 21]
# x = my_list[::3]
# x = my_list[:n\\2]
# x = my_list[n\\2:]
"Negative Slicing"
# x = my_list[::-1]  # [21, 99, 58, 12, 74, 23, 69, 48, 15]
# x = my_list[5:2:-1]  # [12, 74, 23]
# x = my_list[-3:-8:-1]  # [58, 12, 74, 23, 69]
# x = my_list[-5:]  # [74, 12, 58, 99, 21]
x = my_list[-5::-1]  # [74, 23, 69, 48, 15]


print(x)  # [15, 48, 69, 23]
