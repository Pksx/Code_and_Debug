s = "JohnWick"

# By Index
# n = len(s)
# for i in range(n):
#     print(s[i], end=" ")  # J o h n W i c k

# for i in range(n - 1, -1, -1):
#     print(s[i], end=" ")  # k c i W n h o J

# By Value
for ch in s:
    print(ch, end=" ")  # J o h n W i c k

"""Time Complexity:
First s will reverse the length of n and n will run in for loop here timcomplexity will n+n=2n"""
for ch in s[::-1]:
    print(ch, end=" ")  # k c i W n h o J
