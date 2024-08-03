"""
Count alphabets,digits,spaces and symbols
a-z,A-Z,0-9,spaces and symbols
"""


def count_char(user_string: str):
    alphabets = 0
    digits = 0
    spaces = 0
    symbols = 0
    for ch in user_string:
        ascii_code = ord(ch)
        # if 97 <= ascii_code <= 122:
        #     alphabets += 1
        if (97 <= ascii_code <= 122) and (65 <= ascii_code <= 90):
            alphabets += 1
        # elif 65 <= ascii_code <= 90:
        #     alphabets += 1
        # elif 48 <= ascii_code <= 57:
        #     digits += 1
        elif ord(ch) >= ord("0") and ord(ch) >= ord("9"):
            digits += 1
        # elif ascii_code == 32:
        #     spaces += 1
        elif ord(ch) == (ord(" ")):
            spaces += 1
        else:
            symbols += 1

    print(
        f"Alphabes =  {alphabets}, digits = {digits}, spaces = {spaces}, symbols = {symbols}"
    )


my_string = "dhaw43789HGDSAK&*(#$  HDK486/*-+daw)"
count_char(my_string)
