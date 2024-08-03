def factors_tota1(num: int) -> int:
    """Return the sum of all factors of a number."""
    i = 1
    total = 0
    while i <= num:
        if num % i == 0:
            total += i
        i += 1
    return total


print(factors_tota1(368))  # 744
