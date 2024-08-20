""" A generator-function is defined like a normal function, but whenever it needs to generate a value,
it does so with the yield keyword rather than return. If the body of a def contains yield,
the function automatically becomes a generator function.
def gen():
    yield 1
    yield 2
for i in gen():
    print(i)
import sys
a = [i**2 for i in range(100)]
print(sys.getsizeof(a))
b = (i**2 for i in range(100))
print(sys.getsizeof(b))

def a():
    yield 1
    yield 2
    yield 3
for value in a():
    print(value)

list methods :- append,insert,pop,extend,index,delete
tuplemethods :- count(),index()
set :- add(),clear(),copy(),difference(),difference_update(),pop(),update()
dict :- pair of elements 

Program to display the Fibonacci sequence up to n-th term

n,n1=0,1
nth=0
while True:
    
    nth=n+n1
    if nth <= 100:
        print(nth)
        n1=n
        n=nth
    else:
        break
       
reverse string
     
a = "abcd"
print(a[::-1])
aa =''.join(reversed(a))
print(aa)

number prime or not

for i in range(1,100):
    for j in range(2,i//2):
        if i%j==0:
            #print("not a prime number",i)
            break
    else:
        if i!=1:
            print("prime number",i)


oops:-
class is A Class is like an object constructor, or a "blueprint" for creating objects.

inheritance


class A:
    def __init__(self):
        print("self")
    def print(self):
        print("print")
        
class B(A):
    def abc(self):
        print("aaaaaa")
        super().print()
    def ccc(self):
        print('ssss')
b=B()
b.print()
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.


class a:
    def __init__(self,name,age):
        self.fname = name
        self.fage = age
aa = a("shivu",18)
print(aa.fname)


Class :-The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods.
For example: if you have an employee class, then it should contain an attribute and method, i.e. an email id, name, age, salary, etc.

Object:-The object is an entity that has state and behavior. It may be any real-world object like the mouse, keyboard, chair, table, pen, etc.


Method:-The method is a function that is associated with an object. In Python, a method is not unique to class instances. Any object type can have methods

Inheritance :-Inheritance is the most important aspect of object-oriented programming,
which simulates the real-world concept of inheritance. It specifies that the child object acquires all the properties and behaviors of the parent object.

Polymorphism :- Polymorphism contains two words "poly" and "morphs". Poly means many, and morph means shape. By polymorphism, we understand that one task can be performed in different ways.

Data Abstraction :- Encapsulation is also an essential aspect of object-oriented programming. It is used to restrict access to methods and variables.
In encapsulation, code and data are wrapped together within a single unit from being modified by accident.

Encapsulation :-Abstraction is used to hide internal details and show only functionalities.
Abstracting something means to give names to things so that the name captures the core of what a function or a whole program does.

Decorator :- These are used to modify the behavior of the function. Decorators provide the flexibility to wrap another function to expand the working of wrapped function,
without permanently modifying it.
1)Syntactic Decorator :- here we are used to do symbol '@' for calling the decorator
def outer(func):
    def inner(name):
        return func(name.upper())
    return inner

@outer
def upper(name):
    print(name)

def outer(func):
    
    
    def wapper(name):
        return func(name.lower())
    return wapper
                    

@outer
def upper(name):
     print(name)
upper("shiVu")

"""
   
