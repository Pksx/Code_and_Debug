# To print
# Python is a good language
# language good a is Python

my_string = "Python is a good language"
words = my_string.split()
print(words)  # ['Python', 'is', 'a', 'good', 'language']

# Reverse Methods
# words.reverse()
# print(words)  # ['language', 'good', 'a', 'is', 'Python']

words = words[::-1]
print(words)  # ['language', 'good', 'a', 'is', 'Python']

ans = " ".join(word for word in words)
print(ans)  # language good a is Python
