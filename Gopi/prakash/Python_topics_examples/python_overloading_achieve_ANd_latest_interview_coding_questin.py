#how to achieve the python overloading
#by using the multipledispatch decorator method

from multipledispatch import dispatch

@dispatch(int,int)
def product(a,b):
    c=a+b
    return c

@dispatch(int,int,int)
def product(a,b,c):
    c=a+b+c
    return c

@dispatch(float,float,float,float)
def product(a,b,c,d):
    c=a+b+c+d
    return c

x=product(1,2)
print(x)
y=product(1,2,3)
print(y)
z=product(1.2,3.4,2.5,1.4)
print(z)

print("---------------------------------------------------------------------------")

#We can achieve method overloading in python by user defined function using “None”
#keyword as default parameter.
#by using the if /else statement .we can achieve the the overloading by checking
#each parameter as single statement

def add(a=None,b=None):

    if a!=None and b==None:
        print(a)
    else:
        print(a+b)
add(2)
add(5,5)

print("-------------------------------------------------------------------------------")
"""
Write a program to calculate the sum of a list of numbers. list2 = [23, 45, 32, 8, 2, 4]
Without using built in functions
Without using any kind of loops
Without using indexing
"""
#ans:we can do by iterator 

list2 = [1,2,3,4,5]
#converting list to iterator
x=iter(list2)
print(type(x))
a=next(x)
b=next(x)
c=next(x)
d=next(x)
e=next(x)
print(a+b+c+d+e)

print("--------------------------------------------------------------------------------------")

#find the common element in three lists
l1=[3,4,10,9,1,0]
l2=[0,5,7,8,1]
l3=[8,1,4,6,8]

l4=set(l1)and set(l2) and set(l3)
print(l4)


def intersectionofset(ar1,ar2,ar3):

    s1 = set(arr1)
    s2 = set(arr2)
    s3 = set(arr3)

    set1=s1.intersection(s2)
    result_set=set1.intersection(s3)

    final_list=list(result_set)
    return final_list


arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

ar4=intersectionofset(arr1,arr2,arr3)
print(ar4)


#2method
def common_ele(arr1,arr2,arr3):

    common=set()
    for ele in arr1:
        if ele in arr2 and ele in arr3:
            common.add(ele)
    return common

    
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

arr4=common_ele(arr1,arr2,arr3)
print(arr4)



arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]


#3.method

def common_elee(ar1,ar2,ar3):

    set1=set(ar1)
    set2=set(ar2)
    set3=set(ar3)

    return[ele for ele in set1 if ele in set2 and ele in set3]
    
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

ar4=common_elee(arr1,arr2,arr3)
print(ar4)
print("--------------------------------------------------------------------------------------")

"""
#count the special characters in given stirn
x="aabdb cgdje ^$%3HHdj #*&^%@$#^**"
s=a=0

for i in range(len(x)):
    if x[i].isalpha():
        a=a+1
    else:
        s=s+1
print(s)

#count the repeate string
strn="abcdefghiioeu"
#print(strn.upper())
v=['a','e','i','o','u']
for i in strn:
    if i in v:
        if ord(i)>97 or ord(i)<122:
            res=chr(ord(i)-32)
            print(res)


list2 = [1,2,3,4,5]
res=list(map(lambda i:i+i,list2))
print(res)
#print(list2)

print("------------------------------------------------------------------------------------------")
#tech mahindra interview question

#megre two dict
d={"A":1,"b":2,"c":3}
d2={"D":4,"E":5,"r":6}

d.update(d2)
print(d)

print("**d,**d2")

print("="*50)

print("------------------------------------------------------------------------")
#wap for the list of prime numbers
l=[2,21,17,42,47,1,4,7]
print(id(l))

res=list(filter(lambda l:all(l%y!=0 for y in range(2,l)),l))
l=res
print(l)

print(id(l))

for i in l:
    if i == 0 or i ==1:
        continue
    for j in range(2,i):
        print(j)
        if i%j==0:
            break
    else:
        print(f"prime number {i}")

print("-------------------------------------------------------------------------------------------------")

s="gopi tech mech"
#op="mech tech gopi"

sp=s.split()
a=""
for i in sp:
    r=i[::-1]
    print(r)
    a=a+r+" "
    print(a)
print(a[::-1])

print("---------------------------------------------------------------------------------------------")

import re
s="gopibhagamtechetch tech mech"
res=re.findall("mech",s)
print(res)

print("--------------------------------------------------------------------")

#find the file
#log.txt


f=open("filepath","r")
r=f.read()
sp=r.split()
word="out"
for i in sp:
    if word in i:
    print(word)
"""
print("-------------------------------------------------------------------------------------")
"""
#wap for decorators
def outer_str(func):

    def inner_fun():
        str1=func()
        return str1.upper()
    return inner_fun
    
@outer_str
def print_srt():
    return "hello world"

res=print_srt()
print(res)

print("----------------------------------------------------------------------------------")
#multiple inhertence

class A:

    def go(self):
        print("please go0000")
    def stop(self):
        print("please stopii")

    def ready(self):
        print("please reeadygg")

class B():

    def stop(self):
        print("Please stoppp")

    def ready(self):
        print("please ready")

class C(B,A):

    def ready(self):
        print("please ready")

obj=C()
obj.ready()
obj.stop()
obj.go()
"""
print("-------------------------------------------------------------------------")

#
import threading
import time

def cube(num):
    print( "cube:{}".format(num*num*num))
def square(num):
    print( "square:{}".format(num*num))

#t1=threading.Thread(target=cube,args=(10,))
#t2=threading.Thread(target=square,args=(10,))

#t1.start()
#t2.start()

#t1.join()
#t2.join()
threads = []
for i in range(100):
    t1 = threading.Thread(target=cube, args=(10,))
    threads.append(t1)
    t1.start()
    #t2.start()
    #time.sleep(5)
    #t1.join()
    #t2.join()

print("-------------------------------------------------------------------------------")

#wap for square function by using decorators
def squre_fun(n):

    def inner_fuc():
        s=n()
        for i in s:
            print (i*i)
    return inner_fuc

@squre_fun
def print_square():
    return [2,3,4]

print_square()

print("-------------------------------------------------------------------------------------")

#count the each and every letter
str="my name is maheshbabu"
d={}
for i in str:
    if  i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
"""
"""
print("-------------------------------------------------------------------")

#count the vowles
list=["apple","banana","grapes","oreange"]
v=["a","e","i","o","u"]
vo=[]
for i in list:
    for j in i:
        if j in v:
            vo.append(j)
    print(vo)
    print(len(vo))

print("--------------------------------------------------------------")
#find the max number without using builtin module
x=[2,3,4,7,9,1,2,10,14]

for i in range(len(x)):
    for j in range(len(x)):
        if x[i]>x[j-1]:
            x[i],x[j-1]=x[j-1],x[i]
            print(x[i])

print("-----------------------------------------------------------------------------")

#wap for common letters
s="gopi"
s2="topi"
res=set(s)&set(s2)
print(' '.join(res))
s3=s+s2
print(s3)

y=""
z=""
for i in s3:
    if i not in y:
        y=y+i
    else:
        z=z+i
        
#print(y)
print(z)

print("---------------------------------------------------------------------------")

x="gopimahesh"
#output "GoPiMaHeSh"
y=""

for i in range(len(x)):
    if i%2==0:
        y=y+x[i].upper()
    else:
        y=y+x[i].lower()
print(y)

x="gopimahesh"
l=[]
for i in range(len(x)):

    if i%2==0:
        l.append(x[i].upper())
    else:
        l.append(x[i])
#print(l)
print(''.join(l))

print("---------------------------------------------------------------------------")

#count the vowels
x="pythoniaeiouieaoa"

c=0
for i in x:
    for j in v:
        if i==j:
            c=c+1
print(c)

#find the vowels

x="pythoniaeiouieaoa"
y=""
v=["a","e","i","u","o"]

for i in x:
    if i in v:       
        y=y+i
print(y)
print(len(y))

print("--------------------------------------------------------------------------")      
"""
"""
#count the repate value
x="pythoniaeiouieaoa"

y=""
for i in x:
    for j in v:
        if i==j:
            if i =="i":
                y=y+i
print(len(y))
                
print(c)

print("----------------------------------------------------------------------------------------------------")

#wap for print the duplicate value in tuple
t=(1,2,3,4,3,4,5,3)
print(set(t))

y=[]

for i in t:
    if i not in y:
        y.append(i)
print(y)
print(tuple(y))

print("---------------------------------------------------------------------------------------------------------")

d={"com":"ust","name":{"ust":"gopi"}}


x=d["name"]["ust"]
print(x)

print("------------------------------------------------------------------------------------------------")
"""
x="malayalam"
y=""
for i in x:
    y=y+i
if x==y:
    print("palindrom")
else:
    print("it is not palindrom")

print("-----------------------------------------------------------------------------------------------")
"""    
def fun(vl,l=[]):
    l.append(vl)
    return l

l1=fun(1)
l2=fun(20,[])
#l3=fun(3)

print(l1)#l=[1]
print(l2)#l=[1,20]
#print(l3)#l=[1,20,3]

print("-------------------------------------------------------------------------------------------")
"""

def fun2(a=1,b):#when we run the program we will get the error bec we have to mention default arguments at the end of like (a,b=2) not like that (a=1,b)
    print(a+b)

fun2(10,20)#30
fun2(50)#51
fun2()#error
"""
"""
def fun(arg):
    for i in arg:
        return i
arg = [1,2,3,4,5,6]
print(fun(arg))
"""
print("---------------------------------------------------------------------------------")

#max number     
x=[1,2,3,4,5,6,70,100]

m=x[0]
for i in x:
    if i>m:
        m=i
print(m)

#find the max word
s="python automation testing interviewuuuuuuu test"
sp=s.split()
m=sp[0]
for i in range(len(sp)):
    if len(sp[i])>len(m):
        m=sp[i]
print(m)

print("-------------------------------------------------------------------------")
"""
""" 
#count the each letter(ex: t:8)
s="python automation testing interview test"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
    
print("--------------------------------------------------------------")

class A:

    def go(a):
        
        print("please go")

    def stoap(b):
        print("please stopoooooooooooooooooooooooooooooooo")
        
class B(A):
    
    def stop(self):
        print("please stopppppppppp")

obj=B()
obj.stop()
obj.go()
obj.stoap()

print("------------------------------------------------------------------")
"""
"""
s="python automation testing interview test"
a=""
for i in s.split():
    r=i[::-1]
    a=a+r+" "
print(a[::-1])

word = s.split()
print('  '.join(word[-1::-1]))

#withod reverse and double semicolom  do sentence reverse
s="python automation testing interview test"
sp=s.split()
res=' '.join(sp[i] for i in range(len(sp)-1,-1,-1))
print(res)

print("----------------------------------------------------")

#find the max num without built in functions
x=[6,5,7,4,3,45,3]

for i in range(len(x)):
    for j in range(len(x)):
        if x[i]<x[j-1]:
            x[i],x[j-1]=x[j-1],x[i]
print(x[i],end="")

print("-------------------------------------------------")

#sort the list ascending order
l = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i ] > l[j]:
            l[i],l[j]=l[j],l[i]
print(l)

print("--------------------------------------------------------")
#decending order

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] <l[j]:
            l[i], l[j] = l[j],l[i]

print(l)      
"""
print("-------------------------------------------")
"""
#print even numbers in generators    
def even():
    for i in range(100):
        yield i
r=even()
for i in r:
    if i%2==0:
        
        print(i,end="")

print("-------------------------------------------------------")
"""

""" 
#find the sum of num
def findsum(str1):
    temp="0"   
    Sum=0
    for ch in str1:
        if (ch.isdigit()):
            temp=temp+ch
        else:
            Sum=Sum+int(temp)
            temp="0"
    return Sum+int(temp)

str1="12abc20yz68"
print(findsum(str1))

print("----------------------------------------------------------------------")
"""

"""
from functool import reduce
#x=[1,2,3,4,5]
a=10
b=20
res=reduce(lambda a,b :a+b)
print(res(a,b))
"""
print("---------------------------------------------------------")


#amadeus
"""
#Given a dictionary and a character array, print all valid words that are possible using characters from the array. 
#Note: Repetitions of characters is not allowed.


Dict = ["go","bat","me","eat","goal","boy", "run"]
arr = ['e','o','b', 'a','m','g', 'l']
#Output : go, me, goal. 

for i in Dict:
    for j in arr:
        if j in i:
            pass
            #print(j)
            
print("-------------------------------------------------------------")
"""
"""
#input2="out"
x=[2, 3, 5, 7, 11, 13, 17, 19,0,-5]

#x=int(input("Enter a prime number:-"))

try:
    for i in x:
        if i ==0 or i == 1  :
            continue
        for j in range(2,i):
            if i%j==0:
                break
        print("list of prime numbers",i)
        
except Exception as ae:
    print("unable to prine the prime numner ! please provide the postive number or any values",i)
"""
print("----------------------------------------------------------------------------------")
"""
#wap find the word in line 
#read the file into a list of lines
with open("D:\\Gopi_all_python\\Interview_questions_all\\prnt_word_of_line.txt",'r') as f:
    lines = f.read().split("\n")
    print(lines)
print("Number of lines is {}".format(len(lines)))

word = 'evaluating' # dummy word. you take it from input

# iterate over lines, and print out line numbers which contain
# the word of interest.
for i,line in enumerate(lines):
    if word in line: # or word in line.split() to search for full words
        print("Word \"{}\" found in line {}".format(word, i+1))

"""
print("-------------------------------------------------------------------------------------")
"""
#reverse the integer
x=364758
re=0

while x!=0:
    n=x%10
    re=re*10+n
    x//=10
print(re)
"""
print("----------------------------------------------------------------------------")

"""
s="abccdefffghhhhi"
output=""
for ele in s:
    c=s.count(ele)

    if c==1:
        output=output+ele
    elif c>1 and output.count(ele)<(c-1):
        output=output+ele
    else:
        output=output+str(c)
print(output)
"""
#cumulative 

"""
list=[1, 2, 3, 4, 5, 6, 7, 8, 9,10]  
cum_list=[]   
y = 0  
for x in range(0,len(list)):  
    y+=list[x]  
    cum_list.append(y)   
      
print(cum_list)
"""
#
"""
x="aaabbbccddbb"
#Output:"a3b3c2a2b2"

d={}

for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
out=""
for k,v in d.items():
    out=out+k+str(v)
print(out)
"""

print("-----------------------------------------------------------------")
"""
x="aaabbbccddbb"
#Output:"a3b3c2a2b2"

message="ABBBBCCCCCCCCAB"
encoded_message = ""
i = 0
while (i <= len(message)-1):
    count = 1
    ch = message[i]
    j = i
    while (j < len(message)-1):
        if (message[j] == message[j+1]):
            count = count+1
            j = j+1
        else:
            break
        encoded_message=encoded_message+str(count)+ch
        i = j+1
print(encoded_message)
"""

print("-------------------------------------------------------------------")
"""
from collections import OrderedDict

dict=OrderedDict.fromkeys(x,0)

for ch in x:
    dict[ch]=dict[ch]+1

output=''
for k,v in dict.items():
    output=output+k+str(v)
print(output)
"""
print("---------------------------------------------------------------------")
"""
#find the largets third num in the list
import sys

def find_largets_num(nums,num_size):

    if (num_size <3):
        print("invalied")
        
    #intilize the f,s,t elements
    frist_num=nums[0]
    sec_num= -sys.maxsize
    third_num= -sys.maxsize

    #traversing the elements
    for i in range(1,num_size):

        if nums[i] >frist_num:

            third_num=sec_num
            sec_num=frist_num
            frist_num=nums[i]

        elif nums[i]>sec_num:
            third_num=sec_num
            sec_num=nums[i]

        elif nums[i]>third_num:
            third_num=nums[i]

    return third_num


        #print("print the third element",third_num)
            
            
nums=[34,56,2,57,98,2,7]
num_size=(len(nums))

res=find_largets_num(nums,num_size)

print(res)
"""
print("--------------------------------------------------------------------")
    
s="sp pyth woe id pro hdh "
sp=s.split(' ')
for i in s:
    print(i)


    





        
        
    
    







			
	



        
        
    











      



        











    

















































        
        



























































    

    






























