class Student:

    def __init__(self,stu_id,stu_name,stu_age):
        self.stu_id=stu_id
        self.stu_name=stu_name
        self.stu_age= stu_age
        
    def stu_details(self):
        return f"self.stu_id,self.stu_name,self.stu_age"
        
obj_stu=Student(1,"gopi",25)
print(obj_stu.stu_id)
print(obj_stu.stu_name)
print(obj_stu.stu_age)


class Cal:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def add(self,x,y):
        x=20
        y=30
        z=x+y
        return z
         

obj=Cal()
res=obj.add(10,10)
print(res)


#single inhertance

class A:

    def ready(self):
        return "please ready"
    def go(self):
        return "please  go "
    def stop(self):
        return "plese stop"
    
class B(A):

    def go(self):
        return "please go"
    def stop(self):
        return "please stop"
    

#obj=A()
#res= obj.ready()
#obj2=B()
#res1=obj2.stop()
#print(res)
#print(res1)


obj=B()
res=obj.stop()
res1=obj.go()
#print(res)
#print(res1)



#multilevel inhertanace

class A:

    def ready(self):
        return "please ready"
    def go(self):
        return "please  go "
    def stop(self):
        return "plese stop"
    
class B(A):

    def go(self):
        return "please go"
    def stop(self):
        return "please stop"

class C(B):

    def stop(self):
        return "Please stop"



obj=C()
res=obj.stop()
res1=obj.ready()
res2=obj.go()

#print(res)
#print(res1)
#print(res2)

#mutliple inheritance
class A:

    def ready(self):
        return "please ready"
    def go(self):
        return "please  go0"
    def stop(self):
        return "plese stop"
    
class B():

    def go(self):
        return "please go"
    def stop(self):
        return "please stop"

class C(B,A):

    def stop(self):
        return "Please stopppp"

obj=C()
res=obj.go()
res1=obj.stop()
res2=obj.ready()

print(res)
print(res1)
print(res2)


#ploymophrisam

class Ind:

    def capital(self):
        return "india capital is delhi"
    def lanuagae(self):
        return "hindi is frist language of india"
    def country_type(self):
        return "india is a developing country"
    
class Usa:
    
    def capital(self):
        return "Usa capital is Washington"
    def lanuagae(self):
        return "English is frist language of india"
    def country_type(self):
        return "Usa is a developed country"

obj_ind=Ind()
obj_usa=Usa()

for i in (obj_ind,obj_usa):
    print(i.capital())
    print(i.lanuagae())
    print(i.country_type())


#function overloading:function overloading is defined as same fucntion name with diffrent sigunatres(variable,arguments).python doesnot support the function overloading 
#beacuse latest function overrides the previous function.

def add(a,b):
    c=a+b
    return c

def add(a,b,c):
    c=a+b+c
    return c

res=add(10,20,30)
print(res)

#function overriding:function overiding defined as same function name with same sigunatres(variable,arguments)

def add(a,b):
    c=a+b
    return c

def add(a,b):
    c=a+b
    return c

res=add(10,20)
print(res)













    


















    




















