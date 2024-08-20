# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it

x=["gopi bhagam","virat kohli","p t usha"]
#out=["bhagam ,gopi" "kohli, virat"," usha,p t"]
passport_form=[]
for i in x:
    first_name,*middle_name,last_name=i.split()
    full_name=f"{last_name.lower()},{first_name.capitalize()} {' '.join(map(str.capitalize,middle_name))}"
    passport_form.append(full_name)
    
print(passport_form)


def out_fun(func):
    
    def inner_fun():
        str1=func()
        return str1.upper()
    return inner_fun

@out_fun
def print_upper():
    return "hello"
res=print_upper()
print(res)

class cal:

    def add(self):
        return a+b
        

from Cal import  add
import pytest

@pytest.fixture
def cl():
    return Cal()

def test_add(cl):
    assert Cal.add(5,4)==9

driver=find_element_by_partilalink("mob")





"""

class A:
    
    def __init__(self,a):
        self.__a=a
        
class B(A):
    def __init__(self,b):
        self.b = b
        print(self.b)
        super().__init__(self)
        
    def display2(self):
        print(self._A__a)
    
obj_B=B(4)
obj_B.display2()

class A:
    
    def m_soun(self):
        print("sound")
    
class B(A):
    
    def d_sound(self):
        print("d is sound")

obj_A=A()
obj_A.m_soun()

obj_B=B()
obj_B.d_sound()
        
class Parent:
    
    def __init__(self,a):
        self.a =a
    
    def display(self):
        Print(self.a)
        
class Child(Parent):
    def __init__(self,b):
        self.b=b
        super().__init__(self)
    def display2(self):
        print(self.b)

obj_b=Child("hello")
obj_b.display2()
        



"""



        
