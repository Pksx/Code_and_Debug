#reverse string
x="gopi"
y=""
for i in x:
    y=i+y
print(y)

#reverse list
y=[]
x=[1,2,3,4,5]
for i in range(len(x)-1,-1,-1):
    y.append(x[i])
print(y)


#prime number
num=29
flag = False
if num >1:
    for i in range (2,num):
        if (num%i)==0:
            flag =True
            break
if flag:
    print(num,"is not prime number")
else:
    print(num," is prime number")

#prime number
"""
for i in range(1,30):
    for j in range(2,i//2):
        if i%j==0:
            #print("not prime numbers",i)
            break
        else:
            if i!=1:
                print("prime number",i)
"""

#recursive function:--> recursive function which means a function name calling itself.

#factorial num

def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)

res=fact(5)
print(res)



#fibonacci series
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-2) + fibo(n-1)
res=fibo(9)
print(res)


#how to achieve the method overriding
class Parent:

    def greet(self):
        print("hello from parent")

    def greet(self):
        print("hello from parent")

class Child(Parent):

    def greet(self):
        super().greet()
        print("hello from child")

obj=Child()
obj.greet()

#how to achive the method overloading

from multipledispatch import dispatch

class A:
    @dispatch(int,int)
    def add(self,a,b):
        return a+b
    
class B(A):
    @dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c
    
class C(B):
    @dispatch(float,float,float,float)
    def add(self,a,b,c,d):
        return a+b+c+d

obj=C()
res=obj.add(10,20)
print(res)
res2=obj.add(20,30,40)
print(res2)
res3=obj.add(34.5,45.3,45.2,87.5)
print(res3)

















                



    
