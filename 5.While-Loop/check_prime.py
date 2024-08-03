def count_factors(num: int) -> int:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count = count + 1
        i += 1
    return count


def check_prime(n: int) -> bool:
    factors = count_factors(n)
    if factors == 2:  # ( Factors of prime will 2,ie 7 will be divided by 1 and itself)
        return True
    return False


print(check_prime(7))
