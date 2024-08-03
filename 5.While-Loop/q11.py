"""
5674
10983

1. How Many numbers are divisible by 7
2. How many numbers are divisible by 2 and 7


"""

# Ex:1
st = int(input("Enter a Number= "))
en = int(input("Enter a Number= "))
count = 0

while st <= en:
    if st % 2 == 0 and st % 7 == 0:
        count += 1
    st += 1  # Increment st to move through the range

print(count)

# while st <= en:
#     if st % 7 == 0:
#         count += 1
#     st += 1  # Increment st to move through the range

# print(count) # 759

# Method 2:
i = 5674
j = 10983
count1 = 0
count2 = 0
while i <= j:
    if i % 7 == 0:
        count1 += 1
    if i % 2 == 0 and i % 7 == 0:
        count2 += 1
    i += 1
print(count1)
print(count2)
