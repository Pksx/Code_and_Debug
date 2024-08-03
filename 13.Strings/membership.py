my_string = "aeghbioudh"

# Method 1:
# result = 0
# for ch in my_string.lower():
#     if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
#         result += 1
# print(result)  # 5

# Method 2
result = 0
for ch in my_string.lower():
    if ch in "aeiouAEIOU":
        result += 1
print(result)  # 5
