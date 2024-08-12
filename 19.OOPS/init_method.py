class StudentDetails:
    # Magic/Dunder Method
    def __init__(self) -> None:  # Constructor
        self.idd = int(input("Enter ID = "))
        self.name = input("Enter Name = ")
        self.age = int(input("Enter Age = "))
        self.gender = input("Enter Gender = ")
        self.address = "Surat"

    # Methods
    def updateNAme(self):
        self.name = input("Enter update name = ")

    def display(self):  # (Inside self obj will go)
        # print(self)
        print(f"idd={self.idd}")
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Gender={self.gender}")
        print(f"Address={self.address}")


obj1 = StudentDetails()  # This is a init method
print("----------------")
obj1.display()
obj1.updateNAme()
print("----------------")
obj1.display()


"""
Enter ID = 1
Enter Name = Ani
Enter Age = 18
Enter Gender = M
----------------
idd=1
Name=Ani
Age=18
Gender=M
Address=Surat
Enter update name = John
----------------
idd=1
Name=John
Age=18
Gender=M
Address=Surat
"""
