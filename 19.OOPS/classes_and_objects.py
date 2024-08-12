# Example 1:
# class StudentDetails:
#     id = 0
#     name = ""
#     age = 0
#     gender = ""


# obj1 = StudentDetails()
# obj1.id = 1
# obj1.name = "Anirudh"
# obj1.age = 18
# obj1.gender = "Male"
# print(obj1)  # <__main__.StudentDetails object at 0x00000152CE16BFA0>
# print(obj1.id)  # 1
# print(obj1.name)  # Anirudh
# print(obj1.age)  # 18
# print(obj1.gender)  # Male


# Example 2:
class StudentDetails:
    id = 0
    name = ""
    age = 0
    gender = ""


x = int()  # xis object and int is class
obj1 = StudentDetails()
obj2 = StudentDetails()
obj1.id = 1
obj1.name = "Anirudh"
obj1.age = 18
obj1.gender = "Male"

# Object 1
print(obj1)  # <__main__.StudentDetails object at 0x00000152CE16BFA0>
print(f"obj1.id={obj1.id}")
print(f"obj1.name={obj1.name}")  # Anirudh
print(f"obj1.age={obj1.age}")  # 18
print(f"obj1.gender={obj1.gender}")  # Male
"""
Output for obj1
<__main__.StudentDetails object at 0x0000028F4D9EBFD0>
obj1.id=1
obj1.name=Anirudh
obj1.age=18
obj1.gender=Male
"""
# Object 2
print(obj2)  # <__main__.StudentDetails object at 0x00000152CE16BFA0>
print(f"obj2.id={obj2.id}")
print(f"obj2.name={obj2.name}")
print(f"obj2.age={obj2.age}")
print(f"obj2.gender={obj2.gender}")
"""
Output for obj2
<__main__.StudentDetails object at 0x00000226B346BF40>
obj2.id=0
obj2.name=
obj2.age=0
obj2.gender=
"""
