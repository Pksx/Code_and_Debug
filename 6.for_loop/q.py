"""
start is big number 5
end is small number 26

1.start to end,total of all numbers
1.start to end,total of all numbers and divivsible by 7
"""

# Ex:1
# start = int(input("Enter Number= "))
# end = int(input("Enter Number= "))
# total = 0
# sum = 0
# for i in range(start, end + 1):
#     sum = sum + i
#     if i % 7 == 0:
#         total = total + i
#     print(i, end=" ")
# print()
# print(f"sum is {sum}")
# print(f"Total divisible 7 is {total}")


# Ex:2
start = int(input("Enter Number= "))
end = int(input("Enter Number= "))
total = 0
for i in range(start, end + 1):
    if i % 7 == 0:
        total = total + i
print(total)
