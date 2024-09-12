# Method 1
my_dict = {x: x * x for x in (1, 2, 3, 4)}
print(my_dict)  # {1: 1, 2: 4, 3: 9, 4: 16}

# Method 2:
my_dict = dict((x, x * x) for x in (1, 2, 3, 4))
print(my_dict)  # {1: 1, 2: 4, 3: 9, 4: 16}
