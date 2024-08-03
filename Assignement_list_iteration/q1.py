"Create a list and print the total count of all odd numbers"

my_list = [4, 8, 6, 5, 3, 12, 1, 3]

# By Index
# n = len(my_list)
# count = 0
# for i in range(0, n):
# if my_list[i] % 2 == 1:
# count += 1
#
# print(f"Total Odd Numbers = {count}")

# By Value
count = 0
for num in my_list:
    if num % 2 == 1:
        count += 1
print(f"Total Odd Numbers = {count}")
