# Example 1:
def my_func():
    n = 1
    print("First Number")
    # Generator function contains yield statements
    yield n

    n += 1
    print("Second Number ")
    yield n

    n += 1
    print("Last Number ")
    yield n


# Using for loop
for number in my_func():
    print(number)


"""
Here's a step-by-step dry run:

def my_func():: This line defines a function named my_func().

n = 1: Inside the function, a variable n is assigned the value 1.

print('First Number'): The string "First Number" is printed to the console.

yield n: The yield keyword is used to return the value of n (which is 1) and pause the execution of the function. The function's state is saved.

for number in my_func():: A for loop is used to iterate over the values yielded by the my_func() generator.

print(number): The first value yielded by my_func() (which is 1) is printed to the console.

n += 1: The execution of my_func() resumes from where it left off (after the first yield). The value of n is incremented to 2.

print('Second Number'): The string "Second Number" is printed to the console.

yield n: The value of n (which is now 2) is yielded and the function's execution is paused again.

print(number): The second value yielded by my_func() (which is 2) is printed to the console.

n += 1: The execution of my_func() resumes. The value of n is incremented to 3.

print('Last Number'): The string "Last Number" is printed to the console.

yield n: The value of n (which is now 3) is yielded.

print(number): The third value yielded by my_func() (which is 3) is printed to the console.


"""
