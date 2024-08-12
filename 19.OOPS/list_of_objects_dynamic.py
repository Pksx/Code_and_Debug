class StudentDetails:

    # Magic/Dunder Method
    def __init__(self, roll_no: int, name: str, age: int, gender: str, marks=[]):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.marks = marks

    # Methods
    def updateNAme(self, new_name: str) -> None:
        self.name = new_name

    def total(self) -> int:
        # return sum(self.marks)
        t = 0
        for m in self.marks:
            t = t + m
        return t

    def display(self):
        # print(self)
        print(f"roll_no={self.roll_no}")
        print(f"Name={self.name}")
        print(f"Age={self.age}")
        print(f"Gender={self.gender}")
        print(f"Marks={self.marks}\n")


# s1 = StudentDetails(1, "Anirudh", 55, "Male", [46, 38, 55, 99])
# s2 = StudentDetails(2, "Naveen", 33, "Male", [89, 28, 78, 100])

student_data = [
    StudentDetails(1, "Anirudh", 55, "Male", [46, 38, 55, 99]),
    StudentDetails(2, "Naveen", 33, "Male", [89, 28, 78, 100]),
]

student_details = []
while True:
    print("1) Add a Student")
    print("2) Remove a Student")
    print("3) Display all Student Details")
    print("4) update Student Details")
    print("5) Display a Student Details")
    print("6) Exit")
    choice = int(input("Enter Your Choice = "))
    if choice == 1:
        roll_no = int(input("Enter roll_no = "))
        name = input("Enter Name = ")
        age = int(input("Enter Age = "))
        gender = input("Enter gender = ")
        no_of_s = int(input("Enter no of Subject = "))
        marks = []
        for _ in range(no_of_s):
            m = int(input("Enter Your marks"))
            marks.append(m)

        x = StudentDetails(roll_no, name, age, gender, marks)
        student_details.append(x)
        # print(student_details)
        # [<__main__.StudentDetails object at 0x000001C5EBDF3E20>, <__main__.StudentDetails object at 0x000001C5EBDF3D90>]
    elif choice == 2:
        pass
    elif choice == 3:
        if len(student_details) == 0:
            print("No Student Found")
        else:
            for stu in student_details:
                stu.display()
    elif choice == 4:
        pass
    elif choice == 5:
        rno = int(input("Enter Student roll no you want to search = "))
        for stu in student_details:
            if stu.roll_no == rno:
                roll_no.display()
                break
            else:
                print("No Student found with that roll no")
        pass
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
