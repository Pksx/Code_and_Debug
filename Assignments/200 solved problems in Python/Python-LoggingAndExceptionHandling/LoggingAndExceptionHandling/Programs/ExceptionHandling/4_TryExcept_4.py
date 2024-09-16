############TRY EXCEPT EXAMPLE2################
"""
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')

print("I am printed after try except")

"""
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)

print("I am printed after try except")

