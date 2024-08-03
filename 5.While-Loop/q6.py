"""
1 to 20,even number Print
2,4,6,8....16 20
"""

# Method 1:
# i = 2
# while i <= 20:
#     print(i, end=" ") # 2 4 6 8 10 12 14 16 18 20
#     i += 2

# Method 2:
i = 2
while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")  # 2 4 6 8 10 12 14 16 18 20
    i += 1
