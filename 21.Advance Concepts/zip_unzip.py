# ZIPPING
a = ("SHIVAM", "SACHIN", "VIKALP", "RAGHAV", "PRANAY")
b = ("SINGLA", "SINGLA", "GARG", "GUPTA", "GUPTA")

x = zip(a, b)

# use the tuple() function to display
#  a readable version of the result:
print(tuple(x))


# ZIPPING AND UNZIPPING
name = ["sachin", "shivam", "vikalp"]
age = [20, 18, 19]

result = zip(name, age)
result_list = list(result)
print(result_list)

n, a = zip(*result_list)

print("name =", n)
print("age =", a)
