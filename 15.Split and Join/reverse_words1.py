# nothyp si a doog egaugnal

my_string = "Python is a good language"
words = my_string.split()
# print(words)

# print(" ".join(word for word in words))  # Python is a good language
# print(" ".join(word[::-1] for word in words))  # nohtyP si a doog egaugnal

result = ""
for i in words:
    result = result + i[::-1]
    result += "-"  # nohtyP-si-a-doog-egaugnal-
print(result)  # There will be an extra - in last
print(result[:-1])  # nohtyP-si-a-doog-egaugnal
