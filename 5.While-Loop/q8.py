# 1 to n and sum it
st = int(input("Enter a number: "))
end = int(input("Enter a number: "))

i = st
total = 0
while i <= end:
    total = total + i
    i += 1
print(total)
