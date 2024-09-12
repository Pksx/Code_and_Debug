# Example 1:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# Function that filters out all
# numbers which are multiple of 4
def filter_numbers(num):

    if num % 4 == 0:
        return True
    else:
        return False


filtered_numbers = filter(filter_numbers, numbers)
filters = list(filtered_numbers)
print(filters)

# Example 2:


# To sort all ages which
# are above 20 years
ages = [35, 21, 17, 18, 24, 32, 50, 59, 26, 6, 14]


def Func(x):
    if x < 20:
        return False
    else:
        return True


adults = filter(Func, ages)

for z in adults:
    print(z)
