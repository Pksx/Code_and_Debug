class StudentDetails:
    # Class Variables / Attributes
    idd = 0
    name = ""
    age = 0
    gender = ""

    # Methods
    def display(self):  # (Inside self obj will go)
        print(self)
        print(f"idd={self.idd}")
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Gender={self.gender}")


obj1 = StudentDetails()
obj2 = StudentDetails()

obj1.id = 1
obj1.name = "Anirudh"
obj1.age = 18
obj1.gender = "Male"
print(obj1)

# Call Method
obj1.display()
obj2.display()

"""
# Output of obj1
<__main__.StudentDetails object at 0x0000015B1784BFD0>
<__main__.StudentDetails object at 0x0000015B1784BFD0>
idd=0
Name=Anirudh
Age=18
Gender=Male
"""
"""
#Output of obj2
<__main__.StudentDetails object at 0x00000283D543BFA0>
idd=0
Name=
Age=0
Gender=
"""
