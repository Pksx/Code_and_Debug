"""
"""

number_of_class_held = int(input("Enter number held: "))
number_of_class_attended = int(input("Enter number attended: "))
attendance_percentage = (number_of_class_attended / number_of_class_held) * 100
print(f"Percentage is : {number_of_class_attended}% ")
if number_of_class_attended >= 75:
    print("Allowed to sit")
else:
    print("Not Allowed to sit")


# classes_held = int(input("Enter the number of classes held = "))
# classes_attended = int(input("Enter the number of classes attended = "))
# attendance_percentage = (classes_attended / classes_held) * 100
# print(f"Attendance percentage = {attendance_percentage}%")
# if attendance_percentage >= 75:
#     print("Student is allowed to sit in exam")
# else:
#     print("Student is not allowed to sit in exam")
