class StudentDetails:
    # Class Variables / Attributes
    idd = 0
    name = ""
    age = 0
    gender = ""

    # Methods
    def setDetails(self):
        self.idd = int(input("Enter ID = "))
        self.name = input("Enter Name = ")
        self.age = int(input("Enter Age = "))
        self.gender = input("Enter Gender = ")

    def display(self):  # (Inside self obj will go)
        # print(self)
        print(f"idd={self.idd}")
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Gender={self.gender}")


obj1 = StudentDetails()
obj2 = StudentDetails()

# Call Method
obj1.setDetails()
obj1.display()
obj2.setDetails()
obj2.display()

"""
Output of obj 1
# SetDetails Values
Enter ID = 1
Enter Name = Anirudh
Enter Age = 54
Enter Gender = Male

# display values
idd=1
Name=Anirudh
Age=54
Gender=Male
"""
