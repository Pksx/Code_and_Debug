from copy import deepcopy

a = [1, 2, 3, [100, 200, 300], 7, 9]
b = deepcopy(a)

print(f"id(A)={id(a)}")
print(f"id(B)={id(b)}")
print(f"a = {a}")
print(f"b = {b}")

b[0] = 100  # Shallow Copy Value
b[3][0] = 1
print(f"a = {a}")
print(f"b = {b}")
