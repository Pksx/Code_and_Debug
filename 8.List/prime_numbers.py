def is_prime_number(num: int) -> bool:
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False


my_list = [45, 31, 7, 5, 3, 100, 17, 19, 25, 65, 92]

n = len(my_list)
for index in range(0, n):
    if is_prime_number(my_list[index]) == True:
        print(my_list[index], end=" ")  # 31 7 5 3 17 19
