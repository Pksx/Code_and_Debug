class StudentDetails:
    # Methods
    def setDetails(self):
        self.idd = int(input("Enter ID = "))
        self.name = input("Enter Name = ")
        self.age = int(input("Enter Age = "))
        self.gender = input("Enter Gender = ")
        self.address = "Surat"

    def display(self):  # (Inside self obj will go)
        # print(self)
        print(f"idd={self.idd}")
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Gender={self.gender}")


obj1 = StudentDetails()
obj1.setDetails()
obj1.display()
