"""
Keep Asking a number from user untill user enters zero(0)
Calculate total
"""

total = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    total += num
print("Total is: ", total)
