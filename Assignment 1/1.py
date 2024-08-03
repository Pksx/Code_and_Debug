a = 5
b = 10

print(a > 5 and b >= 10)  # False
print(a >= 5 or not b > 10)  # True
print(not (a > 5 and b > 5))  # True
print(not (a < 10 or not b < 10))  # False
print(not (not a <= 5 or not b >= 10))  # True
