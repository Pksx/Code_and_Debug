class StudentDetails:

    # Magic/Dunder Method
    def __init__(
        self,
        idd: int,
        name: str,
        age: int,
        gender: str,
        address="",
        school="SDJ",
    ):
        self.idd = idd
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.school = school

    # def __init__(self) -> None:
    #     self.idd = int(input("Enter ID = "))
    #     self.name = input("Enter Name = ")
    #     self.age = int(input("Enter Age = "))
    #     self.gender = input("Enter Gender = ")
    #     self.address = "Surat"

    # Methods
    def updateNAme(self, new_name: str) -> None:
        self.name = new_name

    def display(self):
        # print(self)
        print(f"idd={self.idd}")
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Gender={self.gender}")
        print(f"Address={self.address}")


obj1 = StudentDetails(1, "Ani", 18, "Male", "Surat")
# obj1.StudentDetails(age=18, name="ANi", gender=18, idd=1)
print("----------------")
obj1.display()
obj1.updateNAme("John")
print("----------------")
obj1.display()
"""
Output
idd=1
Name=Ani
Age=18
Gender=Male
Address=Surat
----------------
idd=1
Name=John
Age=18
Gender=Male
Address=Surat
"""
