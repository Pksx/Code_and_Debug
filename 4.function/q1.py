"""
Make a function which as 5 integer parameter as a subject
return true if pass
else false
"""

# Method 1:

# def marks(s1, s2, s3, s4, s5) -> bool:
#     total = s1 + s2 + s3 + s4 + s5
#     per = (total / 5)
#     print(f"percentage is {per}%")
#     return per


# def result(num):
#     if num > 33:
#         return True
#     else:
#         return False

# x = marks(100, 62, 89, 45, 75)
# result(x)


# Method 2
def marks(s1, s2, s3, s4, s5) -> bool:
    total = s1 + s2 + s3 + s4 + s5
    per = total / 5
    if per < 33:
        return False
    return True


x = marks(100, 62, 89, 45, 75)
print(x)


# Method 3:
def marks(s1, s2, s3, s4, s5) -> bool:
    total = s1 + s2 + s3 + s4 + s5
    per = total / 5
    return per >= 33


x = marks(100, 62, 89, 45, 75)
print(x)
