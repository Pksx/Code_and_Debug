"""
18 above - Adult
13-17 - Teenager
1-12- Child 
"""

age = int(input("Ebter Your AGe: "))
if age >= 18:
    print("Adult")
elif age >= 13 and age <= 17:
    print("Teenager")
else:
    print("Child")
