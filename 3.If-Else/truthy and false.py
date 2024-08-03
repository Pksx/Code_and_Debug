# Type Casting(Implicit and Explicit)
"""
Int
1,5,7,-9,100 -> Truthy
0 -> Falsy

Float
1.1, 5.6, 7, -9, 100, 0.0002 -> Truthy
0.0 -> Falsy

String
"abc" , "123", " ", "." -> Truthy
"" -> Falsy
"""

# Implicit Type Casting
# Ex:1 Truthy for str
# name = "John"

# if name:
#     print("Yes")
# else:
#     print("No")

# Implicit Type Casting
# Ex:2 Falsy for String
name = ""

if name:
    print("Yes")
else:
    print("No")
