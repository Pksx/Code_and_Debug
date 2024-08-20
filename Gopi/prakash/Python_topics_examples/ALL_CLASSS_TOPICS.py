class Stu:

    def __init__(self,name,age,no):#instance class
        self.name=name #instance variable of class
        self.age=age
        self.no=no

    def stu_details(self):
        return {self.name,self.age,self.no}

#obj of class
obj=Stu("gopi",25,39)
print(obj.stu_details())

#Super method
class Parent:
    def __init__(self,txt):
        self.txt=txt
    def print_msg(self):
        return(self.txt)
class Child(Parent):
    def __init__(self,txt):
        super().__init__(txt)

obj=Child("hello world")
print(obj.print_msg())

#class variable

class Animal:
    x=7#class variable
    y=9
    z=4
obj=Animal()
print(obj.x)
print(obj.y)
print(obj.z)

#instance variable

class Stu:

    def __init__(self,name,age):

        self.name=name#instance variable
        self.age=age# instance variable
        
ob_stu=Stu("gopi",25)
print(ob_stu.name)
print(ob_stu.age)


#What is d/w  class and static method.
"""
method Class:class method is decoratpr method .which is bounds to the class
rather than object or instance of that class.

class method can be created using @classmethod"

it is takes the frist parameter of "cls" any variable name which is
pointsto itself

"""

class ClassExample:

    x=2#intilize the class variable

    @classmethod
    def modify(cls):
        cls.x=5
        return cls.x

print(ClassExample.x)#output will be 2
obj=ClassExample
print(obj.x)#op is 2

print(obj.modify())#5

"""
here intial value is x=2 but when we use modify value of x using method
modify value chnaged to 5 so which means we can access and modify the
stateof class
"""

"""
#static method: static is also decorateor methdo whic is also like classmethod
whic is bound to the class rather than object oor instance of that class

we can be cretaed using @staticmethod
it doesnot take frist parametrer like classmethod

it can not access and modify the state of the class.
"""

class StaticExample:
    #intilize the class variable
    x=3
    @staticmethod
    def modify():
        x=6
        return x

print(StaticExample.x)#this is class value 3

obj=StaticExample
print(obj.modify())#6

print(StaticExample.x)#3

#example of class and static method:

class Emp:
    c=0#class variable

    def __init__(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
        Emp.c=Emp.c+1
        
    @staticmethod
    def Upper_name(str1):
        strn=str1.upper()
        return strn

    
    def display(self):
        return {f"name:{self.name} , contact:{self.phone_no}"}

    @classmethod
    def get_count(cls):
        return {"Total employess:{}".format(cls.c)}

obj_emp=Emp("gopi",939259)
obj_emp2=Emp("mam",85495)
res=obj_emp.display()
res2=obj_emp2.display()
print(res)
print(res2)
print(obj_emp.Upper_name(obj_emp.name))
print(Emp.get_count())

# single inheritance

class A:

    def ready(self):
        print("please be ready")
    def go(self):
        print("please go")
    def stop():
        print("please stop")
class B(A):

    def go(self):
        print("please go")
    def stop(self):
        print("please stop")

obj=B()
#obj.ready()
#obj.go()
#obj.stop()

#multilevel inheritance
class A:

    def ready(self):
        print("please be ready")
    def go1(self):
        print("please gooo")
    def stop1(self):
        print("please stopppp")
        
class b(A):
    def go(self):
        print("please go")
    def stop(self):
        print("please stopff")

class c(b):
    def stop3(self):
        print("please stop")

class d(c):
    pass

obj=d()
#obj.ready()
#obj.stop()


#multiple inheritance
class A:

    def ready(self):
        print("please be ready")
    def go(self):
        print("please gooo")
    def stop(self):
        print("please stopppp")
        
class B:
    def go(self):
        print("please go")
    def stop(self):
        print("please stopff")

class C(A,B):#mro method is to tell which frist should be excute.
    def stop(self):
        print("please stop")

obj=C()
obj.stop()
obj.go()
obj.ready()


#polymohisam

class india():
    
    def language(self):
        print("hindi is frist language of india")
    def captial(self):
        print("Delhi is capital of india")
    def country_type(self):
        print("india is developing country")
        
class usa():
    def language(self):
        print("english is frist langauge")
    def captial(self):
        print("washington dc is capital of america ")
    def country_type(self):
        print("america is developed country")

"""
obj=india()
obj.country_type()
obj2=usa()
obj2.captial()
"""
obj_ind=india()
obj_usa=usa()

for country in (obj_ind,obj_usa):
    country.language()
    country.captial()
    country.country_type()
    
"""
class Encapsulation:
    __var = 10
    
    def __func1(self):
        print("this is private method")
    def func(self,var):
        self.__var = var
        self.__func1()
        print(self.__var)
        
obj = Encapsulation()
obj.func(20)'''

## AbstrACTION : SHOWING THE FUNCTIONALITY AND HIDING THE ESSENTIAL DATA.

from abc import ABC,abstactmethod
class Gopi(ABC):    
    @abstractmethod
    def method():
        None
    @abstractmethod
    def method2():
        pass
class Subclass(Gopi):
    def method():
        print("implementing the methods from abstract class")
obj1 = Subclass()
obj1.method()
"""

"""
abstraction:abstaction is one the opps concept is process of hiding the internal
details or unneccesary data from the user or real world in order to reduce the
complixity and increase the effincy.

by default ,python does not provide abstact class.we can use the abc module in python
which provide the base class(abc) for defining abstact class.

AN abstract class can not be instanatiate this means that we can not created the
object abstract class
"""
from abc import ABC ,abstractmethod

class stu(ABC):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @abstractmethod
    def display(self):
        return {f"name:{self.name},age:{self.age}"}
    
class emp(stu):
    def __init__(self,name,age):
        super().__init__(name,age)

    
    #@abstractmethod
    def display(self):
        return {f"name:{self.name},age:{self.age}"}

obj=emp("john",29)
print(obj.display())

#obj2=stu("gopi",25)
#print(obj2.display())#TypeError: Can't instantiate abstract class stu with abstract method display
        


#decorator
def outer_fun(func):

    def inner_fun():
        str1=func()
        return str1.upper()
    return inner_fun

@outer_fun
def print_str():
    return "hello world"

print(print_str())

#normal function
def fun():
    for i in range(20):
        return i
x=fun()
print(x)

#generator
def fun():
    for i in range(20):
        yield i
x=fun()
print(next(x))
print(next(x))

for i in x:
    print(i,end=" ")

#lambda and map
x=range(10)
res=list(map(lambda i : i*i,x))
print(res)

#lambda & filter
y=range(20)
res=tuple(filter(lambda i:i%2==0,y))
print(res)

#list comprehsions
x=range(5)
res=[i*i for i in x]
print(res)

y=range(10)
res=[i for i in x if i%2==0]
print(res)

#iterator
x=[1,2,3,4,5]

y=iter(x)
print(y)
print(next(y))
print(next(y))
print(next(y))


"""
Encapsulation:
"""

class Emp:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        return (f'Name:{self.name} ,age:{self.age}:')

obj=Emp('gopi','25')
res=obj.display()
print(res)

#Protacted data

class Stu:

    def __init__(self,name,age):

        self.name=name
        self._age=age

class Emp(Stu):

    def __init__(self,name,age):
        super().__init__(name,age)

    def display(self):
        print(f"protected data from student class ,age:{self._age}")
        self._age=29

        print(f"protected data from emp in calss ,age:{self._age}")

obj=Emp('gopi',28)
obj.display()





















    

    


