for i in range(5, 0, -1):
    for j in range(1, 5 - i + 1):
        print(" ", end=" ")
    for k in range(6, i):
        print(k, end=" ")
    print()
