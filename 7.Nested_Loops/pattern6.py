def pattern(n: int, m: int):

    for n in range(1, n + 1):
        for m in range(1, m + 1):
            print(m, end=" ")
        print()


n = int(input("Enter Number= "))
m = int(input("Enter Number= "))

pattern(n, m)
