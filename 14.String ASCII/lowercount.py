# Method 1:
# my_string = "abcdABCD1234"

# count = 0
# count2 = 0
# for ch in my_string:
#     ascii_code = ord(ch)
#     if ascii_code >= 97 and ascii_code <= 122:
#         count += 1
#     elif ascii_code >= 65 and ascii_code <= 90:
#         count2 += 1

# print(f"Total lowercase letters= {count}")  # Total lowercase letters= 4
# print(f"Total Uppercase letters= {count2}")  # Total Uppercase letters= 4


# Method 2
my_string = "abcdABCD1234"

count = 0
count2 = 0
for ch in my_string:
    if "a" <= ch <= "z":
        count += 1
    elif "A" <= ch <= "Z":
        count2 += 1

print(f"Total lowercase letters= {count}")  # Total lowercase letters= 4
print(f"Total Uppercase letters= {count2}")  # Total Uppercase letters= 4

# Method 3
my_string = "abcdABCD1234"

count = 0
count2 = 0
for ch in my_string:
    if ord("a") <= ord(ch) <= ord("z"):
        count += 1
    if ord("A") <= ord(ch) <= ord("Z"):
        count2 += 1

print(f"Total lowercase letters= {count}")  # Total lowercase letters= 4
print(f"Total Uppercase letters= {count2}")  # Total Uppercase letters= 4
