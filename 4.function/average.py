# Function named average
# 3 num from users and calculate average


def average():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    num3 = int(input("Enter num3: "))

    average = (num1 + num2 + num3) / 3
    print("The average is: ", average)


average()
