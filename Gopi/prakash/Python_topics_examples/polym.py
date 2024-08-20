"""
from multipledispatch import dispatch
class India:
    

    def language(self):
        return "hindi is lnag"

    def captial(self):
        return "delhi"

class Usa(India):

    def language(self):
        return "english"

    def captial(self):
        return "washington DC"
    
    @staticmethod
    def country_type(self):
        return "developed country"

#obj_usa=Usa()


print(obj_usa.captial())
obj_india=India()
print(obj_india.language())
print(obj_usa.country_type)
"""


#from threading import Thread
"""
from multipledispatch import dispatch
class Cal:

    @dispatch(int,int)
    def add(self,a,b):
        return a+b

class Cal2:
    
    @dispatch(int,int)
    def add(self,a,b,):
        return a+b
    @dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c

obj_cal2=Cal2()
obj_cal=Cal()

print(obj_cal.add(2,3))
print(obj_cal2.add(10,29))
print(obj_cal2.add(10,20,30))

"""


    

"""
class Cal:

    
    def add(self,a,b):
        return a+b
    
    def add2(self,a,b,c):
        return a+b+c

"""
 
"""
obj_cal2=Cal2()
obj_cal=Cal()

print(obj_cal.add(2,3))
print(obj_cal2.add(10,29))
"""

class Animal:

    def make_sound(self):
        return "make animal sound"

class Dog(Animal):

    def make_sound(self):
        return "dog is barks"

#obj_a=Animal()
#print(obj_a.make_sound())

obj_dog=Dog()
print(obj_dog.make_sound())
class Cal:

    def add(self,a,b=0):
        return a+b

    def add(self,a,b):
        return a+b

obj=Cal()
print(obj.add(5,7))
print(obj.add(5,7))


x=[1,2,3]
y=[6,7,8]

print(dict(zip(x,y)))


x=1234

res=[int(i) for i in str(x)]
print(res)

s="gopi"
y=int(x)
print(y)















