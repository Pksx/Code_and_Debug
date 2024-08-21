# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n - 2) + fibo(n - 1)


# res = fibo(9)
# print(res)


# class Parent:

#     def greet(self):
#         print("hello from parent")

#     def greet(self):
#         print("hello from parent")


# class Child(Parent):

#     def greet(self):
#         super().greet()
#         print("hello from child")


# obj = Child()
# obj.greet()


def nums():
    yield 1

    yield 2
    yield 3


generator = nums()
next(generator, None)  # 1
next(generator, None)  # 2
next(generator, None)  # 3
next(generator, None)  # None
next(generator, None)
