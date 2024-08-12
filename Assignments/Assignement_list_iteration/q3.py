"""Create a list and print the total even and odd nubers """

my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]

n = len(my_list)

factors = 0
for i in range(0, n):
    if my_list[i] % 2 == 0:
        factors += 1
    if factors ==2:
    