# WhiteSpace - Spaces,Enter,Tab
# my_string = "Python is a good language\nThanks\nand\ngoodbye"

# ans = my_string.split()
# print(ans)  # ['Python', 'is', 'a', 'good', 'language', 'Thanks', 'and', 'goodbye']

# Example 2:
# my_string = "Python is a good language\nThanks\nand\ngoodbye"

# ans = my_string.split(" ")
# print(ans)  # ['Python', 'is', 'a', 'good', 'language\nThanks\nand\ngoodbye']

# Example 3:
my_string = "Python is a good language\nThanks\nand\ngoodbye"

ans = my_string.split("g")
print(ans)  # ['Python is a ', 'ood lan', 'ua', 'e\nThanks\nand\n', 'oodbye']
