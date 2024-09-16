"""
SYntax for reduce:
from functools import reduce
reduce(function, iterable[, initializer])

reduce(): This function is used to apply a function to an iterable and reduce it to a single value.
function: The function to apply to the iterable. It should take two arguments.
iterable: The sequence of elements to apply the function to.
initializer: This is an optional argument. If provided, it is used as the first argument to the function.
"""

from functools import reduce

total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
print(total)

# Example 2:

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)
# DRY Run for

# numbers = [1, 2, 3, 4, 5]: A list named numbers is created and assigned the values 1, 2, 3, 4, and 5.
# Reduce Function

# reduce(lambda x, y: x + y, numbers): The reduce function is called with two arguments:

# lambda x, y: x + y: This is a lambda function that takes two arguments (x and y) and returns their sum.
# numbers: This is the list that the lambda function will be applied to.
# The reduce() function works as follows:

# Step 1: The first two elements of the list (1 and 2) are passed to the lambda function. The lambda function returns their sum (3).
# Step 2: The result from Step 1 (3) and the next element in the list (3) are passed to the lambda function. The lambda function returns their sum (6).
# Step 3: The result from Step 2 (6) and the next element in the list (4) are passed to the lambda function. The lambda function returns their sum (10).
# Step 4: The result from Step 3 (10) and the next element in the list (5) are passed to the lambda function. The lambda function returns their sum (15).
# The final result of the reduce() function is 15.

# Output

# print(sum_of_numbers): The value of sum_of_numbers (which is 15) is printed to the console.
