"""
        5 
      4 5 
    3 4 5 
  2 3 4 5 
1 2 3 4 5 
"""

n = int(input("Enter number of lines = "))
for i in range(n, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(i, n + 1):
        print(k, end=" ")
    print()
