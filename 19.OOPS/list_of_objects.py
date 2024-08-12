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


# s1 = StudentDetails(1, "Anirudh", 55, "Male", [46, 38, 55, 99])
# s2 = StudentDetails(2, "Naveen", 33, "Male", [89, 28, 78, 100])

student_data = [
    StudentDetails(1, "Anirudh", 55, "Male", [46, 38, 55, 99]),
    StudentDetails(2, "Naveen", 33, "Male", [89, 28, 78, 100]),
]

""" 
Output
# roll_no=2
# Name=Naveen
# Age=33
# Gender=Male
"""
# Accessing Elements
print(student_data[0].marks)  # [46, 38, 55, 99]
print(student_data[0].name)  # Anirudh
print(student_data[1].total())  # 295
print(student_data[1].age)  # 33
