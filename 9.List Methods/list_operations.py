# Operations in List

a = [1, 2, 3]
# b = [4, 5, 6, "John"]
# c = [True, False]

# ans = a + b + c
# print(ans)  # [1, 2, 3, 4, 5, 6, "John", True, False]
# Below wont work
# ans = a - b
# ans = a / b
# ans = a * b
# ans = a + 5
# ans = a + [4]  # [1, 2, 3, 4, 5, 6, 'John', True, False]
ans = a * 5  # It will print 5 times
print(ans)  # [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]

a = [-1] * 5
print(a)  # [-1, -1, -1, -1, -1]
