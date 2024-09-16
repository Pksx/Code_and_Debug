############TRY WITH MULTIPLE EXCEPT EXAMPLE################
import sys

def linux_interaction():
    assert ('win32' in sys.platform), "Function can only run on Linux systems."
    print('After assert statement')

try:
    linux_interaction()
    print("after function")
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')

print("I am printed after above try except block")