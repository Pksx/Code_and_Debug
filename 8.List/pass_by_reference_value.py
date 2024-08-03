# Pass by reference/address
# Ex:1
# def printing_list(lst: list) -> None:
#     print(lst)


# my_list = [1, 2, 3, 4, 5, 6]
# printing_list(my_list)  # [1, 2, 3, 4, 5, 6]

# Ex: 2


def printing_list(lst: list) -> None:
    lst[0] = 100


my_list = [1, 2, 3, 4, 5, 6]
print(my_list)  # [1, 2, 3, 4, 5, 6]
printing_list(my_list)  # [1, 2, 3, 4, 5, 6]
print(my_list)  # 100, 2, 3, 4, 5, 6]
