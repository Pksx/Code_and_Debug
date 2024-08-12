a = int(input("Enter a number= "))
b = int(input("Enter a number= "))

count1 = 0
count2 = 0
if a > b:
    while a <= b:
        if a % 3 == 0 and a % 5 == 0:
            count1 += 1
        # if a % 3 == 0:
        #     count2 += 1
    a += 1
print(count2)
print(count1)
