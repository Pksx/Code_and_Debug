"""
Count Factors
 1 to 20
"""


def count_factors(num: int) -> int:
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count = count + 1
        i += 1
    return count


print(count_factors(20))  # 6
