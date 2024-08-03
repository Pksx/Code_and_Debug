# my_list = [3, 5, 6, 7, 2, 3, 6, 9]
# # print(my_list)
# # print(id(my_list))

# # my_list.sort()  # In Place Sorting
# # print(my_list)  # [2, 3, 3, 5, 6, 6, 7, 9]
# # print(id(my_list))

# # In built function
# print(sorted(my_list))  # [2, 3, 3, 5, 6, 6, 7, 9]
# print(id(my_list))


# print(my_list)
# print(id(my_list))


my_list = [3, 5, 6, 7, 2, 3, 6, 9]

# my_list.sort()  # 2-3-3-5-6-6-7-9 (it will chnage in main my_list)
print("-".join(str(num) for num in my_list))  # 3-5-6-7-2-3-6-9
print("-".join(str(num) for num in (sorted(my_list))))
# Output:
# 2-3-3-5-6-6-7-9 (it will add in new list)
print(my_list)  # [3, 5, 6, 7, 2, 3, 6, 9]

print(sorted("sjbcji13r8u19!@#$%"))
# ['!', '#', '$', '%', '1', '1', '3', '8', '9', '@', 'b', 'c', 'i', 'j', 'j', 'r', 's', 'u']
