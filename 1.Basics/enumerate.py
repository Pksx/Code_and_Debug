# Enumerate
# It will print the element in list,tuple and its index

# Method 1:
my_list = ["Zero", "One", "Two", "Three", "Four", "Five"]
for index, item in enumerate(my_list):
    print(f"The item in position {index} is: {item}")


# Method 2:for index, item in enumerate(my_list):
for index, item in enumerate(["Zero", "One", "Two", "Three", "Four", "Five"]):
    print(f"The item in position {index} is: {item}")
"""
Output:
The item in position 0 is: Zero
The item in position 1 is: One
The item in position 2 is: Two
The item in position 3 is: Three
The item in position 4 is: Four
The item in position 5 is: Five
"""
