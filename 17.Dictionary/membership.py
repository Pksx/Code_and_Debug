from typing import Dict

marks: Dict[str, int] = {
    "history": 65,
    "chemistry": 78,
    "science": 86,
    "english": 92,
    "maths": 100,
}
print(100 in marks)  # False
print("maths" in marks)  # True
