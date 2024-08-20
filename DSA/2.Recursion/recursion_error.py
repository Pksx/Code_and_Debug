# def greet():
#     print("Greetings")
#     greet()
#     print("Done")


# greet()
# RecursionError: maximum recursion depth exceeded while calling a Python object
# It will run upto 999 lines
# This is Stack Space


# from selenium import *
def func():
    global count
    print(count)
    count += 1
    func()


count = 1
func()
# RecursionError: maximum recursion depth exceeded while calling a Python object
