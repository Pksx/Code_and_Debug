"""
a=[1,2,3,4,5,6,7]
a.append(8)
a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a.insert(2,6)
>>> a
[1, 2, 6, 3, 4, 5, 6, 7, 8]
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.remove()
TypeError: list.remove() takes exactly one argument (0 given)
>>> a
[1, 2, 6, 3, 4, 5, 6, 7, 8]
>>> a.remove(6)
>>> a
[1, 2, 3, 4, 5, 6, 7, 8]
>>> a.pop()
8
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>> a.pop(2)
3
>>> a.extend([1,2,3,4])
>>> a
[1, 2, 4, 5, 6, 7, 1, 2, 3, 4]
>>> a.copy()
[1, 2, 4, 5, 6, 7, 1, 2, 3, 4]
>>> a
[1, 2, 4, 5, 6, 7, 1, 2, 3, 4]
>>> b.copy()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b.copy()
NameError: name 'b' is not defined
>>> a
[1, 2, 4, 5, 6, 7, 1, 2, 3, 4]
>>> a.count(2)
2
>>> a.index(4)
2
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.index()
TypeError: index expected at least 1 argument, got 0
"""

#combining the two lists
x=[1,2,3,4,5]
y=[2,3,4,8,7]
print(zip(x,y))
for i in zip(x,y):
  print(i)


#if we have list of tuple can we modify tuple?
#yes we can change the tuple of list but we cannot chnage list of tiple
t=([1,2,3],5,6)
t[0][2]=0
print(t)

tup1 = (1,2,3,4,[5,6,7])
tup1[4].append(8)
print(tup1)

#we cannot change the list of tuple
#l=[1,2,(2,3,4,5),5,7]
#l[2][3]=9
#print(l)

#can we change the tuple values?
"""
ANS:tuple is an immutable object.we cannot change values once created tuple.but if
if we want to add value in the existing tuple frist we have to convert the tuple
into list then we can add after that again we have to turn into tuple.
"""
"""
t=(1,2,3,4)
print(type(t))
con_tuple_to_list=list(t)#convert the tuple to list
print(type(con_tuple_to_list))
print(con_tuple_to_list)
con_tuple_to_list.append(9)
print(con_tuple_to_list)
con_list_to_tuple=tuple(con_tuple_to_list)#convert the list to tuple
print(type(con_list_to_tuple))
print(con_list_to_tuple)

string="abdcd[1,2,3,4]"
#print(string[8])
con_sting_to_list=list(string)#convert the stirng to list
print(type(con_sting_to_list))
print(con_sting_to_list)
con_sting_to_tuple=tuple(string)#convert the sting into tuple
print(type(con_sting_to_tuple))
print(con_sting_to_tuple)
print("-------------------------------------------------------------------")

s="python world"
y=s[::-1]
print(y[0:len(y):2])

s="python world"
a=s[::-2]
print(a)
s="python world"
r=s[::-3]
print(r)
"""
"""
print("-----------------------------------------")
x=[1,4,6,7,34,87,-1,-2]
mx=x[0]
for i in x:
  if i<mx:
    mx=i
print(mx)
print("---------------------------------------------------------")
"""
"""
#find the longest string
x="python is high level programikkkkkkknng  languaga "
sp=x.split()
print(sp)
mx=sp[0]
for i in range(len(sp)):
  if len(sp[i])>len(mx):
    mx=sp[i]
print(mx)
"""
"""
print("-------------------------------------------------------------")
#find the longest string
words = ['data', 'science', 'machine', 'learning']

mx=words[0]
print(mx)

for i in range(len(words)):
  if len(words[i])>len(mx):
    mx=words[i]
print(mx)
print("---------------------------------------------------")

"""


x="dffffffffffffffffffffffffhdff"
c=0
y=""
z=""
for i in x:
  if i not in y:
    y=y+i
  else:
    z=z+i
    c=c+1
    
print(c)
print(z)    
print(y)

    
X = "bbccddeerrffffddd"

output = ""
count = 1
prev_char = X[0]

for i in range(1, len(X)):
    if X[i] == prev_char:
        count += 1
    else:
        output += prev_char + str(count)
        prev_char = X[i]
        count = 1

output += prev_char + str(count)

print(output)    
  

#how to change the tuple
#by uisng concatanation and
t1=(1,2,3,4)
t2=(6,7,8,9)
t3=t1+t2
print(t3)

#by using packing and unpacking:we can unpacking the elements of tuple into
#variables.modify the variables and then pack the variable.
t=(1,2,3,5)
a,b,c,d=t
a=9
new_t=(a,b,c,d)
print(new_t)


#how to change th stirng:
# we can change the string by uisng slice.
s="bangalore"
r="m"+s[1:]
print(r)

#by using replace
s="hello  world"
r=s.replace("hello","hi")
print(r)


#x=range(100)
res=list(filter(lambda x:all(x%i !=0 for i in range(2,x)),range(2,100)))
print(res)

b=1000
b2=1000
n1=1
n2=1
print(b==b2)
print(n1==n2)

print(b is b2)# "IS" identify objecct operators 
print(n1 is n2)


from random import randint

def random_num():
    num = randint(100,999)
    return num
res=random_num()
print(res)

import random
def random_list(n):
    numbers = random.sample(range(100,999),n)
    return numbers
    
n = 20
numbers = random_list(n)
print(numbers)

def out_fun(func):
    
    def inn_fun():
        strn=func()
        return strn.upper()
    return inn_fun

@out_fun
def print_str():
    return "hello"
    
res= print_str()
print(res)


    























