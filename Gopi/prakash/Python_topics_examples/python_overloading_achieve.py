"""
def product(a,b):
    c=a+b
    return c

def product(a,b,c):
    c=a+b+c
    return c
    
y=product(1,2)
print(y)
x=product(1,2,3)
print(x)
"""

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


#how to convert the muliple integer to single integer

x=[11,33,55]
#outx=113355

s=""
for i in x:
    s=s+str(i)
print(s)

#Write a Python program to split a list into different variables.
l=[4,5,8]
a,b,c=l
print(a)
print(b)
print(c)

print("--------------------------------------------------------------------")
#Write a Python program to change the position of every n-th value with the (n+1)th in a list.
l=[0,5,8,6,1,10]
l2=[]

for i in range(len(l)):
    if i%2==0:
        i=i+1
        l2.append(l[i])
    else:
        i=i-1
        l2.append(l[i])
print(l2)
print("---------------------------------------------------")
#Write a Python program to get the frequency of the elements in a list
l=[6,5,8,1,7,10,1,5,6,5,1,1,1,1,2,2,2,2,2,2,2]
c=0
for i in l:
    t_c=l.count(i)
    if t_c>c:
        c=t_c
        r=i
print(r)

res=max(l,key=l.count)
print(res)

print("-----------------------------------------------------------------")
#print the values of dict
x=[[{"a":1,"b":2,"c":3}]]

res=[ele2 for sublist in x for ele in sublist for ele2 in ele]
print(res)

for i in x:
   print(i)
   for j in i:
       print(j)
       for k in j.values():
           print(k)
print("----------------------------------------------------------------")

#Write a Python program to flatten a shallow list.
nestedlist = [ [1, 2, 3, 4], ["Ten", "Twenty", "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
for i in nestedlist:
    for j in i:
        print(j)

print("-------------------------------------------------------------------------")
#Write a Python program to get the difference between the two lists.
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7,3, 8]

l1=list(set(list1)-set(list2))
l2=list(set(list2)-set(list1))
tot_diff=l1+l2
print(tot_diff)
print("-----------------------------------------------------")
#Write a Python program to count the number of strings where the string length is 2 or more and the first and last 
#character are same from a given list of strings.
l=['abc', 'xyz', 'aba',"jj","lllll","abc"]
c=0
for i in l:
    if len(i)>1 and i[0]==i[-1]:
        c=c+1
print(c)

print("------------------------------------------------------------------------------------------------------")
#Write a Python program to multiply all the items in a list.
l=[2,1,3,4]
print(id(l))
for i in range(len(l)):
    l[i]=l[i]*l[i]
print(l)
print(id(l))

print("--------------------------------------------------------------------")
x=[1,2,3,4,5]
x.append([1,2,2,3,4])
print(len(x))
x.extend(["str",9.0,3])
print(len(x))

print("--------------------------------------------------")

class TE:
    def __init__(self,txt):
        self.txt=txt

    def display(self):
        return self.txt
class tvx(TE):
    def __init__(self,txt):
        super().__init__(txt)

obj=tvx("python")
print(obj.display())
print("-----------------------------------")

class stu:

    c=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        stu.c=stu.c+1

    def display(self):
        return {f"name:{self.name},age:{self.age}"}
    
    @staticmethod
    def str_upper(str1):
        strn=str1.upper()
        return strn
    
    @classmethod
    def get_count(cls):
        return("total count of stu:{}",format(cls.c))


obj=stu("gopi",25)
obj2=stu("mahesh",39)
print(obj.display())

res=obj.str_upper(obj.name)
print(res)
print(stu.get_count())

print("-----------------------------------")
x=[1,4,10,2,3,7,4,5]

for i in range(len(x)):
    for j in range(len(x)):
        if x[i]<x[j]:
            x[i],x[j]=x[j],x[i]
print(x)
print("---------------------------------------")
"""
#Honeywell
#create a module and import this module in another without effecting the things in current module..how to do that?
#How to reduce execution time of a code
Proper Algorithm & Data Structure. Each data structure has a significant effect on runtime. ...
Using Built-in Functions and Libraries. Python's built-in functions are one of the best ways to speed up your code. ...
Use Multiple Assignments. ...
Prefer List Comprehension Over Loops. ...
Proper Import. ...
String Concatenatio
"""
#cube of each num using generator

def cube(x):
    for i in x:
        yield i*i*i
x=[1,2,3,4]
res=cube(x)
print(next(res))
print(next(res))
for i in res:
    print(i)

#same code using lambda function
res=list(map(lambda i:i*i*i,x))
print(res)

print("--------------------------------------------------")
#how to sort a lsit which contains different data types
x=[1,2,3,9.6,3]
x.sort()
print(x)

x = ['banana', 'grapes', 'apple', 'jackfruit']#..how to sort this list
x.sort()
print(x)
for i in range(len(x)):
    for j in range(len(x)):
        if x[i]<x[j]:
            x[i],x[j]=x[j],x[i]
print(x)
print("--------------------------------------------------------------------------")

#how to sort a lsit which contains different data types
def sort_mix(num):

    try:
        ele=int(num)
        return (0, ele, '')
    except ValueError:
        return (1, num, '')

test_list =[4, 'gfg', 2, 'best', 'is', 3,9.0,99.9]
# printing original list
print("The original list : "+ str(test_list))
test_list.sort(key =sort_mix)
print("List after mixed sorting : "+ str(test_list))

"""
test_list = ['4', 'gfg', '2', 'best', 'is', '3',"gd2","1gio4h",3]

num=[]
word=[]

for i in test_list:
    if i.isnumeric():
        num.append(i)

    else:
        word.append(i)
num.sort()
word.sort()
num.extend(word)
print(num)

"""
print("--------------------------------------------------------------------")
#sort the tuple last element
l1 = [(2,3),(5,2),(7,1),(6,7)]

def last(n):
    return n[-1]

def sort_list(t):
    return sorted(t,key=last)

print(sort_list([(2,3),(5,2),(7,1),(6,7)]))

print("--------------------------------------------------------------------------")

#how to validate the emial by using re
import re

# Define a function for
# for validating an Email
def check(s):
	pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
	if re.match(pat,s):
		print("Valid Email")
	else:
		print("Invalid Email")

# Driver Code
if __name__ == '__main__':

	# Enter the email
	email = "ankitrai326@gmail.com"

	# calling run function
	check(email)

	email = "my.ownsite@our-earth.org"
	check(email)

	email = "ankitrai326.com"
	check(email)


#match the url by using re

# Python code to find the URL from an input string
# Using the regular expression
import re


def Find(string):

	# findall() has been used
	# with valid conditions for urls in string
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex, string)
	return [x[0] for x in url]


# Driver Code
string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ", Find(string))



string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
sp=string.split()

res=[]

for i in sp:
    if i.startswith("https:") or i.startswith("http:"):
        res.append(i)
print(res)



X = [1, 2, 3, [6, 7, 8]]

def fun(lst):
    new=[]
    for ele in lst:
        if type(ele) == list:
            new.extend(fun(ele))
        else:
            new.append(ele)
    return new
out=fun(X)
print(out)

X = [1, 2, 3, [6, 7, 8]]

new=[]
for ele in X:
    if type(ele) == list:
        new.extend(ele)
    else:
        new.append(ele)
print(new)


            
        
        






















