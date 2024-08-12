"""
Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order
"""

my_list = []
n = int(input("Enter Number= "))

for i in range(n):
    num = int(input("Enter input= "))
    my_list.append(num)
print(my_list)

result = []
for i in range(n - 1, -1, -1):
    result.append(my_list[i])
print(result)
