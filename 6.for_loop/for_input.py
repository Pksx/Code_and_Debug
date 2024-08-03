start = int(input("Enter a number="))
end = int(input("Enter a number="))

for i in range(start, end):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9 10

# EX:2
start = int(input("Enter a number="))
end = int(input("Enter a number="))

for i in range(start, end + 1):
    print(i, end=" ")  # 0 1 2 3 4 5 6 7 8 9 10 11
