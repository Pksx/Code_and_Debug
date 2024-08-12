class Rectangle:
    def __init__(self, length: float, breadth: float) -> None:
        self.length = length
        self.breadth = breadth

    # def __str__(self) -> str:
    #     return "A rectangle object"

    def __str__(self) -> str:
        return f"Length = {self.length} Breadth = {self.breadth}"

    def area(self) -> float:
        return self.length * self.breadth

    def perimeter(self) -> float:
        return 2 * (self.length + self.breadth)

    def is_square(self) -> bool:
        return self.length == self.breadth


x = Rectangle(5, 10)
# print(x)
# # <__main__.Rectangle object at 0x000002313F5FBFD0>(without __str__ it will print address)
# print(x)  # A rectangle object(with __str__ it will return string)
print(x)  # Length = 5 Breadth = 10
