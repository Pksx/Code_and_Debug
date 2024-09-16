############TRY EXCEPT################

import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except AssertionError as error:
    print("Error obtained due to assertion-->", error)
    print('The linux_interaction() function was not executed')

print("I am printed after try except")


