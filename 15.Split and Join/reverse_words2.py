# language good a is Python
# egaugnal doog a si nothyp

my_string = "Python is a good language"

words = my_string.split()
print(words)

# Method 1:
# words.reverse()
# print(" ".join(word[::-1] for word in words))  # egaugnal doog a si nohtyP

# Method 1 of 2:
# print(" ".join(word[::-1] for word in words[::-1]))  # egaugnal doog a si nohtyP

# Method 2:
# words = words[::-1]
# print(" ".join(word[::-1] for word in words))  # nohtyP si a doog egaugnal

# Method 3:
words = words[::-1]
print(" ".join(word for word in words))  # nohtyP si a doog egaugnal
