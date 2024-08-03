# Membership -in/not in
# my_list = [3, 4, 5, 8, 9]

# print(7 not in my_list)  # False
# print(7 not in my_list)  # True
# print(3 in my_list)  # True

my_list = [3, 4, 5, 8, 9, 1, 1, 2, 3, 4, 5, 6]
result = []

for num in my_list:
    # if num not in result:
    #     result.append(num) # [3, 4, 5, 8, 9, 1, 2, 6]
    if result.count(num) == 0:  # [3, 4, 5, 8, 9, 1, 2, 6]
        result.append(num)

print(result)
