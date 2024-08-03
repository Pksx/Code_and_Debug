"""
Keep asking characters from user
stop it untill he/she presses  "q"
Enter char = r
Enter char = a
Enter char = v
Enter char = 1
Enter char = q
Output="rav1"
"""

# my_str = ""
# while True:
#     char = input("Enter a char= ")
#     if char == "q" or char == "Q":
#         break
#     my_str += char

# print(my_str)  # abcdef


# Using Function
def aschar() -> str:
    my_string = ""
    while True:
        char = input("Enter a char= ")
        if char == "q" or char == "Q":
            break
        my_string += char
    return my_string  # abcdef
