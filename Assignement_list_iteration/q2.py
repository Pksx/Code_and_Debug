"Create a list and print the total even and odd nubers "

my_list = [4, 8, 6, 5, 3, 12, 1, 3, 6]

n = len(my_list)

even_count = 0
odd_count = 0

for i in range(0, n):
    if my_list[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Total even Numbers ={even_count}")
print(f"Total Odd Numbers ={odd_count}")
#
for num in my_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Total even Numbers ={even_count}")
print(f"Total Odd Numbers ={odd_count}")
