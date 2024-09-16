#########TRY EXCEPT ELSE EXAMPLE 2################

import sys

def windows_interaction():
    assert ('win32' in sys.platform), "Function can only run on Windows systems."
    print('After assert statement')

try:
    windows_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause as exception dint occur')
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)

