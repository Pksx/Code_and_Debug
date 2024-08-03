"""
start end /total of all even numbers    
1 to 100

"""

start = 1
end = 10
total = 0
i = start
j = end
while i <= j:
    if i % 2 == 0:
        total = total + i
    i = i + 1
    print(total)
print(total)  # 30
