"""
Ask start number from user=6
Ask a end number from user=15

start to end 
6,7,8,9,....14 and 15


Ask start number from user=15
Ask a end number from user=8

start to end 
8,...14.15
"""

# Method 1:

# start = int(input("Enter a Start Number="))
# end = int(input("Enter a End Number="))
# i = start
# j = end

# while i <= j:
#     print(i, end=" ")
#     i += 1
# print()
# print(i)

# while j <= i:
#     print(j, end=" ")
#     j += 1


# Method 2:
# If both values are same (start and end),it will go to else and execute
start = int(input("Enter a Start Number="))
end = int(input("Enter a End Number="))
if start < end:
    i = start
    j = end
    while i <= j:
        print(i, end=" ")
        i += 1
else:
    i = end
    j = start
    while i <= j:
        print(i, end=" ")
        i += 1
