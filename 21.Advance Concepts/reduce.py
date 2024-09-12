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


numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)
