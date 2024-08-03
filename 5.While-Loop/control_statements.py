"""
Loops:
Continue(skips the below partof the code and moves to  next loop)
break(break from the loop)
"""

# Ex:1
# i = 1
# while i <= 10:
#     print("Hello")
#     i += 1
#     print("Good")
#     print("Bye")
#     print("Done")

# Ex:2
# i = 1
# while i <= 5:
#     print("Hello")
#     i += 1
#     if i == 2:
#         continue
#     print("Good")
#     print("Bye")
#     print("Done")

# Ex:3
# i = 1
# while i <= 5:
#     print("Hello")
#     if i == 3:
#         continue
#     i += 1

# Ex:4
# i = 1
# while i <= 5:
#     print("Hello")
#     if i == 3:
#         break
#     i += 1
# print("Done")


# Ex:5
# def func():
#     i = 1
#     while i <= 5:
#         print("Hello")
#         if i == 3:
#             break # break is come out of the loop
#         i += 1
#     print("Done")
# Ex:6
def func():
    i = 1
    while i <= 5:
        print("Hello")
        if i == 3:
            return  # break is come out of the loop
        i += 1
    print("Done")


func()
