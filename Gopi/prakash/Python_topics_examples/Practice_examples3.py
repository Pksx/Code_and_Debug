#frist Print only and b after count duplicates of a and b
a="maheshbabuacbb"
c = 0
y=""
d={}
for i in a:
    if i=='a' or i=='b':
        print(i)
        for j in i:
            if j not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
print(d)
       

#count the duplicates in dict
s="gopiiiibhaaagggggamm"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
        
       
x="suresh"

y=""
for i in x[0::2].upper():
    print(i,end="")

    
#count the duplicate
x=[1,2,4,5,1,2,3,4,1,5,3,4]
y=[]
z=[]
c=0
for i in x:
    if i not in y:
        y.append(i)
    else:
        z.append(i)
        c=c+1
print(c)

#count the duplicte in string
x="gopigopigopi"
y={}
for i in x:
    if i not in y:
        y[i]=1
    else:
        y[i]=y[i]+1
print(y)

#factoril by using recursive

def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))

n=5
res=[n if n<=1 else n*fact(n-1)]
print(res)

#fab by uisng recursive
def  fib(n):
    if n<=1:
        return n
    else:
        return fib(-2)+fib(-1)
print(fib(5))

#fibnocci
fib=[0,1]
[fib.append(fib[-2]+fib[-1]) for i in range(8)]
print(fib)
#prime number

n=5
flag=False
if n>1:
    for i in range(2,n):
        if n%2==0:
            flag=True
            break
if flag:
    print("is not prime number")
else:
    print("prime number")

#list of prime number
prime=list(filter(lambda x:all(x&i !=0 for i in range(2,x)),range(2,10)))
print(prime)


#ip address

#op=1.0.81.291
x="192.18.0.1"
y=""
for i in x.split(' '):
    y=i[::-1]
    print(y)

y="192.183.98.9"
s=y.split('.')
a=''
for i in s:
    y=i[::-1]
    a=a+y+'.'
    z=a[:len(a)-1]
print(z)#291.381.89.9.

s="hello world python"
z=""
sp=s.split()
for i in sp:
    y=i[::-1]
    z=z+y+' '
print(z)

s="hello world python"
#op="hello dlrow python"
op=""
for i in s.split():
    if i =="world":
        i=i[::-1]
    op=op+' '+i
print(op)
"""
#allupercase
x="gopiiiaaaeeuui"
for i in x:
    if ord(i)>97 and ord(i)<122:
        y=chr(ord(i)-32)
        pass
        #print(y,end='')

"""
#only vowel uppercsae
x="gopiiiaaaeeuui"
v="aeiou"
for i in x:
    if v in i:
        if ord(i)>97 or ord(i)<122:
            res=chr(ord(i)-32)
print(res)


x="python"
print("-".join(x))
y=""
for i in x:
    y=y+i+'-'
print(y)

z=""
for i in range(0,len(x)-1):
    z=z+x[i]+'-'
z=z+x[-1]
print(z)


x=[1,3,45,67,4,5,6,7,100,90]
mx=max(x[0],x[1])
sec_mx=min(x[0],x[1])
n=len(x)
for i in range(2,n):
    if x[i]>mx:
        sec_max=mx
        mx=x[i]
    else:
        x[i]>sec_max
        mx!=x[i]
        sec_max=x[i]
print(sec_max)

"""
#patterns
n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end="")
    print("\r")

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")
"""

def tri(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
n=5
tri(n)




x="abbcddefzzzq"
y=""
for i in x:
    if x.count(i)>1:
        continue
    else:
        y=y+i
print(y)

s="abccdeffghhhhi"
output=""
for i in s:
    c=s.count(i)
    if c==1:
        output=output+i
    elif c>1 and output.count(i)<(c-1):
        output=output+i
    else:
        output=output+str(c)
print(output)


import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

x=[0,1,1,1,0,0,0,1,0,1]
l=[]

le=0
for i in x:
    if i==1:
        l.append(i)
    elif(i==0 and le<len(l)):
        le=len(l)
        l=[]
if(le<=2):
    pass
else:
    print(le)





    
    
    


        
        
        


      




    
    










    













    
    




        







    
    
