# Ex:1

# def product(n1, n2):
#     ans = n1 * n2
#     print(ans)
#     if ans % 5 == 0:
#         print("divisible by 5")
#     else:
#         print("not divisible by 5")


# product(10, 15)


# Ex:2
def product(n1, n2):
    ans = n1 * n2
    return ans


def check_divisible_by_5(num):
    if num % 5 == 0:
        print("divisible by 5")
    else:
        print("not divisible by 5")


x = product(10, 20)
print(x)

# ...............
y = product(10, 15)
print(y)
check_divisible_by_5(y)
