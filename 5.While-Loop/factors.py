# Ex:1
# For this loop will run 20times
# def print_factors(num: int) -> None:
#     """Prints all factors of a number."""
#     i = 1
#     while i <= num:
#         if num % i == 0:
#             print(i, end=" ")
#         i += 1


# print_factors(20)  # 1 2 4 5 10 20


def print_factors_2(num: int) -> None:
    """Prints all factors of a number."""
    i = 1
    while i <= num // 2:
        if num % i == 0:
            print(i, end=" ")
        i += 1
    print(num)


print_factors_2(20000000)  # 1 2 4 5 10 20
