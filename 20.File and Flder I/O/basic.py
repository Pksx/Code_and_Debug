try:
    with open("Multi_threading", "r") as f:
        file_content = f.read()
    # Now you can work with the content of the file, stored in the variable 'file_content'
except FileNotFoundError:
    print("The file 'Multi_threading' was not found.")
