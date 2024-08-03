a = [1, 2, 3, 4, 5, 6]
b = a.copy()  # Shallow Copy

print(f"id(A)={id(a)}")
print(f"id(B)={id(b)}")
print(f"a = {a}")
print(f"b = {b}")

# Output
# a = [1, 2, 3, 4, 5, 6]
# b = [1, 2, 3, 4, 5, 6]

b[0] = 100
print(f"a = {a}")
print(f"b = {b}")
# # Output
# a = [100, 2, 3, 4, 5, 6]
# b = [100, 2, 3, 4, 5, 6]
