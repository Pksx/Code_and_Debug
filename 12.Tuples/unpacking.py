# Unpack its values to a,b,c
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)

# x, y, z = [10, 20, 30]

# print(x, y, z)  # 10 20 30

a = (10, 25, 69, 78, 45)  # We can use tuples with and without brackets
b = 10, 26, 69, 78, 45  # We can use tuples with and without brackets
print(type(a))  # <class 'tuple'>
print(type(b))  # <class 'tuple'>

# If we assign single value to variable without brackets it will become int
c = 10
c = (56,)  # <class 'tuple'>
print(type(c))  # <class 'int'>


# Spread/Splat Operator
a, *b, c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)  # 1
print(b)  # [2, 3, 4, 5, 6, 7, 8]
print(c)  # 9
