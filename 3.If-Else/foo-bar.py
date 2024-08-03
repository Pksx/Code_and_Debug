"""
Ask a number from user

num is divisible by 3 ->foo
num is divisible by 5 ->bar
num is divisible by 3 and 5 ->foobar

else print(Invalid)
"""

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("FOOBAR")
elif num % 3 == 0:
    print("FOO")
elif num % 5 == 0:
    print("BAR")
else:
    print("Invalid")
