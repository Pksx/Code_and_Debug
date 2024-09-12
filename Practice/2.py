# import math

# print(math.sqrt(55))

# i = 0
# while i <= 5:
#     print(i)
#     if i == 4:
#         print("Breaking Loop")
#         break
#     i += 1

# i = 0
# while i <= 5:
#     print(i)
#     if i == 3:
#         print("Continuing Loop")
#         i += 1  # Increment i before continuing
#         continue
#     i += 1


# for index, item in enumerate(["zero", "one", "two", "three", "four", "five"]):
#     print(index, ":", item)


def v_upper(str_inp):
    output = ""
    y = "aeiou"
    for ch in str_inp:
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            ch = chr(ord(ch) - 32)
            print(ch)
    return ch


resp = v_upper("hyderbadaa")
print(resp)
