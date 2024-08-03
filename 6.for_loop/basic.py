"""
print 1 to 20
2,4,6,8....18,20
"""

for abc in range(1, 21, 2):
    print(
        abc, end=" "
    )  # 1 3 5 7 9 11 13 15 17 19  (2 will be the step index,By default step index value is 1)


# for abc in range(1, 21):
#     if abc % 2 == 0:
#         print(abc, end=" ")  # 2 4 6 8 10 12 14 16 18 20
