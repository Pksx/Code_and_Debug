#wap  for cube number
#num=int(input("Enter a number: "))
num=5
cube_res=num*num*num
print(cube_res)

#cube by float value
def cube_num(num):
    return num**3
#num=float(input("Enter a float value: "))
num=5.0
res=cube_num(num)
print(res)
print("-----------------------------------------------------------------")
#wap for perfect number
#num=int(input("Enter a number: "))
num=6
sum_num=0
for i in range(1,num):
    if num%i==0:
        sum_num=sum_num+i
if sum_num==num:
    print("this number is perfect number")
else:
    print("this number is not perfect number")
print("--------------------------------------------------------------------")
"""
#wap two large num
num1=int(input("Enter a number: "))
num2=int(input("ENter a number2:"))

if num1>num2:
    print("a is greaterthan b")
else:
    print("b is greater than a")
"""

print("--------------------------------------------------------------")
#wap large three number
"""
a=int(input("Enter a number1:"))
b=int(input("ENter a number2: "))
c=int(input("Enter a nuymber3:"))

if a>b and a>c:
    print("a is greaterthan b and c")
elif b>c and b>a:
    print("b is greaterthan a and c")
elif c>a and c>a:
    print("c is graterthan c and a")

else:
    print(" and b and c number are equal")
"""
print("-------------------------------------------------------------------")
#natural number
num=10
i=0
while i<=num:
    print(i,end="")
    i=i+1

for i in range(1,num+1):
    print(i,end="")
print("---------------------------------------------------------------------")
#wap for leap year
#year=int(input("Enter a year : "))
year=1200

if ((year%400 == 0) or (year%4==0) and (year%100!=0)):
    print("This year is  leap year")

else:
    print("this year is not leap year")

print("-----------------------------------------------------------------------")
    
#square of numbers
x=[1,2,3,4]

for i in x:
    res=i*i
    print(res)
    
res=[i*i for i in x]
print(res)
    
print("--------------------------------------------------------------")
num=153

s=0

tp=num
while tp>0:
    digit=tp%10
    s=s+digit**3
    tp=tp//10

if num==s:
    print("armstromg")
else:
    print("not a armst")


"""
#armstrong number
num=153

Sum=0
times=0

temp=num
while temp>0:
    times=times+1
    temp=temp//10

temp=num
while temp>0:
    reminder=temp%10
    Sum=Sum+(reminder**times)
    temp//10

if num==Sum:
    print("%d is armstrong."%num)
else:
    print("%d is not."%num)
"""

print("--------------------------------------------------------------------------")
#count the number in digits
num=987666
count=0
while(num>0):
    num=num//10
    count=count+1
    
print(count)

print("------------------------------------------------------------")
#factor of number
v=126

for i in range(1,v+1):
    if (v%i==0):
        print("{0}".format(i))

print("---------------------------------------------------------------------------------")


#wap count the alphabet and digits in stirng
strn="goapiiaeio182994565&@$^%$#"
alpha=digits=special=0

for i in range(len(strn)):
    if strn[i].isalpha():
        alpha=alpha+1

    elif strn[i].isdigit():
        digits=digits+1

    else:
        special=special+1
        
print(f"count of  alphabet {alpha} ".format(alpha))
print(f"count of digits {digits}".format(digits))
print(f"count of special {special}".format(special))

#withou using built in function
strn="goapiiaeio182994565&@$^%$#"
alpha=digits=special=0

for i in range(len(strn)):

    if ((strn[i]>='a' and  strn[i]<='z') or (strn[i]>='A' and strn[i]<='Z')):
        alpha=alpha+1

    elif (strn[i]>='0' and strn[i]<='9'):
        digits=digits+1

    else:
        special=special+1

print(f"count of  alphabet {alpha} ".format(alpha))
print(f"count of digits {digits}".format(digits))
print(f"count of special {special}".format(special))

print("---------------------------------------------------------------------")
#wap for stromg number
num=145
s=0
t=num

while t>0:
    f=1
    i=1
    r=t%10

    while i<=r:
        f=f*i
        i=i+1

    s=s+f
    t=t//10

if s==num:
    print("%d is strong number"%num)
else:
    print("%d is not strong number"%num)

print("--------------------------------------------------------------")
#sum of digits

num=4567
s=str(num)

c=0
for i in s:
    c=c+int(i)
print(c)

su=0

while(num>0):
    r=num%10
    su=su+r
    num=num//10
print(su)
print("----------------------------------------------------------")

#swap num
a=10
b=20

t=a
a=b
b=t

print(a)
print(b)
print("----------------------------------------------------------------")
#count vowels
x="aeioueibcdfeao"
v=["a","e","i","o","u"]
vo=0
for i in x:
    if i == "a" or i =="e" or i =="i" or i=="o" or i=="u":
        vo=vo+1
print(vo)


x="aeioueibcdfhdghdheao"
v=["a","e","i","o","u"]
vow=0

for i in x:

    if i in v:
        vow=vow+1
print(vow)
print("-------------------------------------------------------------------")
#count string
s="stringghii22w "
c=0
for i in s:
    c=c+1
print(c)
print("------------------------------------------------------------------")
#sum of dict values
myDict = {'x': 250, 'y':500, 'z':410}
print(sum(myDict.values()))

y=[]
for v in myDict.values():
    y.append(v)
s=0
for i in y:
    s=s+i
print(s)
print("-----------------------------------------------------------")
myDict = {'x': 20, 'y':5, 'z':60}

del myDict['x']
#myDict.pop('y')
#myDict.popitem()

print(myDict)

print("-----------------------------------------------------------------------")  




        




        




















































        



