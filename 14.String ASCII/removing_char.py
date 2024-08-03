"""
Remove all the symbols,digits,spaces from a string.
my_string="a!b@c9d_e.f"
result:
abcdef
"""

# Method 1:
# my_string = "a!b@c9d_e.f"
# result = ""
# for ch in my_string:
#     ascii_code = ord(ch)
#     if ascii_code >= 97 and ascii_code <= 122:
#         result = result + chr(ascii_code)

# print(result) # abcdef

# Method 2
# my_string = "a!b@c9d_e.f"
# result = ""
# for ch in my_string:
#     if "a" <= ch <= "z":
#         result += ch

# print(result) # abcdef

# Method 3
my_string = "a!b@c9d_e.f"
result = ""
for ch in my_string:
    if ord("a") <= ord(ch) <= ord("z"):
        result += ch

print(result)  # abcdef
