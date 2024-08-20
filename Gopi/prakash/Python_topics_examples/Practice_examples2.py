x=[1,2,"gopi",2.5,"bh"]
for i in x:
    if type(i)== str:
        print(i)
print("--------------------------------------------------")
x="BAMPAM"
y=""
for i in x:
    if x.count(i)>1:
        pass
    else:
        y=y+i
print(y)
print("--------------------------------------------------")
#reverse string
x="gopib"
y=""
for i in x:
    y=i+y
print(y)

print("--------------------------------------------------")

#reverse list
x=[1,2,3,4,5]
y=[]
for i in range(len(x)-1,-1,-1):
    y.append(x[i])
print(y)
print("--------------------------------------------------")

#count the special character in string
s=a=0
x="aBbcd%**$"
s=a=0

for i in range(len(x)):
    if x[i].isalpha():
        a=a+1
    else:
        s=s+1
#print(a)
print(s)

print("-------------------------------------------------------------------")

#find the most repeTED Value
x=[1,2,3,4,1,2,3,4,1,2,3,4,4,4,4,4]
c=0
for i in x:
    total_count=x.count(i)
    if total_count>c:
        c=total_count
        repete_ele=i
print(repete_ele)
        
res=max(x,key=x.count)
print(res)

print("-------------------------------------------------------------")
#count the digits and alphabet and special character in string
string="abcdesefg1234%$&@%#^"

sp=alpha=digits=0

for i in range(len(string)):
    if string[i].isalpha():
        alpha=alpha+1
    elif string[i].isdigit():
        digits=digits+1
    else:
        sp=sp+1
print("number of alphabets in string : ",alpha)
print("number of digits in string : ",digits)
print("number of special characters in string: ",sp)

print("----------------------------------------------------------------")

# remove duplicate in list
#ex1 
x=[1,2,3,4,5,1,2,3,4,5,1,2,3,45,4,5]
print(set(x))
#print(set(x))
y=[]
for i in x:
    if i not in y:
        y.append(i)
print(y)

print("--------------------------------------------------")

# remove the duplicates in string
s="gopiiiibhagam"
r=""
for i in s:
    if i not in r:
        r=r+i
print(r)

print("--------------------------------------------------")
        
# count the duplicates
s="gopiiiibhaaagggggamm"
a=""
c=0
for i in s:
    if i not in a:
        a=a+i
    else:
        c=c+1
print(c)


print("--------------------------------------------------")
# count the  duplicate in list
#ex1 
x=[1,2,3,4,5,1,2,3,4,5,1,2,3,45,4,5]
y=[]
z=[]
c=0
for i in x:
    if i not in y:
        y.append(i)
    else:
        z.append(i)
        c=c+i
print(c)
    
print("--------------------------------------------------")

#count the duplicates in string
s="gopiiiibhaaagggggamm"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)

print("--------------------------------------------------")

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

print("-----------------------------------------------------------")

#palindrom
str="malayalam"
str_out=""
for i in str:
    str_out=i+str_out
print(str_out)
if str == str_out:
    print("it is palindrome")
else:
    print("it is not plindrom")
print("--------------------------------------------------")
       
#factorial on recurivse function
def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)
print(fact(5))

print("--------------------------------------------------")

#fabonacci
def febo(n):
    if n<=1:
        return n
    else:
        return febo(n-1)+febo(n-2)
print(febo(9))

fib=[0,1]
res=[fib.append(fib[-2]+fib[-1]) for i in range(8)]
print(fib)

print("--------------------------------------------------")

#prime number
num=29
flag =False
if num>1:
    for i in range(2,num):
        if num%i == 0:
            flag=True
            break        
if flag:
    print("is not prime num")
else:
    print("is prime num")
print("--------------------------------------------------")
x="Gopi n"
y=""
for i in x.split(' '):
    y=y+i[::-1]+" "
    print(y)
    
print("--------------------------------------------------")
#reverse the sentence
sen="python very popular language"
sp=sen.split()
rev_sen=""
for i in sp:
    re=i[::-1]
    rev_sen=rev_sen+re+" "
print(rev_sen)

#method2
import re

rev_senn=""
sen='geeks quiz practice code'
#words = re.findall('\w+', sen)
words=sen.split()
res=' '.join(words[i]for i in range(len(words)-1,-1,-1))
print(res)

print("--------------------------------------------------")
sen="python very popular language"
s=""
for i in sen.split():
    if i == "very":
        i=i[::-1]
        r=sen.replace("very",i)
        s=s+" "+ i
print(r)
print("--------------------------------------------------")
#wap to lowercase to uppercase
x="gopiiiaaaeeuui"
#print(x.upper())
for i in x:
    if ord(i)>97 and ord(i)<122:
        res=chr(ord(i)-32)
        pass
        print(res)
print("--------------------------------------------------")
#wap to alphabet uppercase
x="gopiiiaaaeeuui"
v="aeiou"
for i in x:
    if v in i:
        if ord(i)>97 or ord(i)<122:
            res=chr(ord(i)-32)
            print(res)

strn="abcdefghiioeu"
#print(strn.upper())
v=['a','e','i','o','u']

for i in strn:
    if i in v:
        if ord(i)>97 or ord(i)<122:
            res=chr(ord(i)-32)
            print(res)

print("--------------------------------------------------")
#sum the num
x=[1,2,3,4]
sum=0
for i in x:
    sum=sum+i
    print(sum)
print("--------------------------------------------------")

#sum the digit
n=1234
s=str(n)
c=0
for i in s:
    c=c+int(i)
print(c)


n=12345
c=0
while n>0:
    n=n//10
    c=c+1
print(c)
print("--------------------------------------------------")

# join the "-"without build in fun
s="python"
output=""
for i in range(0,len(s)-1):
    output=output+s[i]+"-"
output=output+s[-1]
print(output)
print("--------------------------------------------------")

#reverse ip address

ip="192.16.15.2"
sp=ip.split()
for i in sp:
    a=i[::-1]
    print(a)
print("--------------------------------------------------")
ip="192.16.15.2"
s=ip.split(".")
a=""
for i in s:
    r=i[::-1]
    a=a+r+"."
    res=a[:len(a)-1]
print(res)

print("--------------------------------------------------")

x=[3,4,8,5,56,58,99,34,666,777]
mx_num=max(x[0],x[1])
sec_max=min(x[0],x[1])
n=len(x)
for i in range(2,n):
    if x[i]>mx_num:
        sec_max=mx_num
        mx_num=x[i]
    else:
        x[i]>sec_max
        mx_num!=x[i]
        sec_max=x[i]
print(sec_max)

print("--------------------------------------------------")
print("****************patterns**********
****************************")
# patterns
"""
#1.
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
n=5
for i in range(1,n):
    for j in range(1,i+1):
        print(j, end="")
    print("\r")
print("--------------------------------------------------")

"""
*
* *
* * *
* * * *
"""
n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")
    
n=5
for row in range(1, n+ 1):
    print(" " * (n - row) +"*" * row)
print("--------------------------------------------------")
"""
    * 
   * * 
  * * * 
 * * * * 
* * * * *
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
print("--------------------------------------------------")

#print the largest string
s="python automation nhd"

sp=s.split()
m=sp[0]

for i in range(len(sp)):
    if len(sp[i])>len(m):
        m=sp[i]
print(m)
print("="*50)
#find the max number
x=[3,4,52,3,4,10,1121]
mx=x[0]
for i in x:
    if i>mx:
        mx=i
print(mx)
---------------------------------------------------------------------
interview questions in mirafra
1.how to achieve the method over riding
ANS: by using super method 
2.what is the polymophrisam
3.what is the diff between the 





























        

    

        
            
        














    



    
    

    
    
        
