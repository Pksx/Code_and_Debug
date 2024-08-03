name = "John"
age = 55
gender = "Male"

# Method 1
# print("My Name is", name)
# print("My Age is", age)
# print("My gender is", gender)
# print("My Name is", name, "My Age is", age, "My Gender is", gender)


# Method 2(F-Strings/Formatted Strings)
# print(f"My Name is {name}")
# print(f"My Age is {age}")
# print(f"My Gender is {gender}")
# print(f"My Name is {name} and My Age is {age} and My Gender is {gender}")
# print(f"My Name is {name} My Age is {age} My Gender is {gender}")


# Method 3 (Identifiers)
"""
%s = String
%d = Integer
%f = Float
"""
# print("My Name is %s" % name)
# print("My Age is %d" % age)
# print("My Gender is %s and done." % gender)
# print("My Name is %s and Age is %d, Gender is %s" % (name, age, gender))

# Method 4
# print(f"name = {name}")
print(f"{name = }")
print(f"{age = }")
print(f"{gender = }")
print(f"{name = } {age = } {gender = }")


# Method 5
print(f"My Name is {} and Age is {} and Gender is {}")
