#"Click Open link on the dialog shown by your browser"
#1.Fetch "browser"
str="Click Open link on the dialog shown by your browser"
for i in str.split():
    if i == "browser":
        print(i)
print("-----------------------------------------")
#2.Fetch "link"
str="Click Open link on the dialog shown by your browser"
for i in str.split():
    if i == "link":
        print(i)
print("-----------------------------------------")
#3.Convert Whole string to uppercase
str="Click Open link on the dialog shown by your browser"
for i in str.split():
    print(i.upper(),end=" ")
    
print("-----------------------------------------")
#4.Convert Whole string to lowercase
str="Click Open link on the dialog shown by your browser"
for i in str.split():
    print(i.lower(),end=" ")
    
print("-----------------------------------------")
#5.Convert "Click" to upper case in string
str="Click Open link on the dialog shown by your browser"
for i in str.split():
    if i == "Click":
        print(i.upper())

print("-----------------------------------------")
#6.Convert "Open" and "browser" to upper case in string
str="Click Open link on the dialog shown by your browser"
for i in str.split():
    if i == "Open" or i == "browser":
        print(i.upper())
print("-----------------------------------------")
7#.Print "Open link: in reverse order
str="Click Open link on the dialog shown by your browser"
for i in str.split():
    if i == "Open" or i == "link":
        print(i[::-1])
print("-----------------------------------------")

#Note:Use num string in below questions:
#1.Print only numbers not comma
num="1,2,3,4,5,6,7,8,9"
for i in range(0,len(num),2):
    print(num[i])
print("-----------------------------------------")
 
#2.Print all even numbers
num="1,2,3,4,5,6,7,8,9"
for i in range(0,len(num),2):
    if int(num[i])%2 == 0:
        print(i)
print("-----------------------------------------")
#3.Fetch "1" and "5" from string and perform numerical addition
num="1,2,3,4,5,6,7,8,9"
print(int(num[0])+int(num[8]))
print("-----------------------------------------basicc------------------")

#1.Write a code to find out which number is greater out of four number
x=[8,1,5,2,3,4]
x.sort()
print(x[-1])

#2.Write a code to print day of the week.
day_num=int(input("Enter the week day num:-"))

if day_num == 1:
    print("this week day number belongs to sunday")
elif day_num == 2:
    print("this week day number belongs to monday")
elif day_num == 3:
    print("this week day number belongs to tuesday")
elif day_num == 4:
    print("this week day number belongs to wensday")
elif day_num == 5:
    print("this week day number belongs to thrusday")
elif day_num == 6:
    print("this week day number belongs to friday")
elif day_num == 7:
    print("this week day number belongs to saturday")
else:
    print("this numbers doesnot exists im weekdays")
    
#3.Write a code to print table of given number.
num=5
for i in range(1,11):
    print(i*num)

#4.Write a menu driven calculator, Addition,Substraction,Muliplication,Divison,Floor divison,Modulas(Try float values for all operation)
    
#5.Write a menu driven code to print table of given number for given range.

print("-----------------------------------------")


#reverse string
x="gopi"
y=""
for i in x:
    y=i+y
print(y)

print("-----------------------------------------------------------------")

#reverse list
y=[]
x=[1,2,3,4,5]
for i in range(len(x)-1,-1,-1):
    y.append(x[i])
print(y)

print("-----------------------------------------------------------------")

#prime number
num=28
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

print("-----------------------------------------------------------------")
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

print("-----------------------------------------------------------------")
#recursive function:--> recursive function which means a function name calling itself.

#factorial num

def fact(n):
    if n<=1:
        return n
    else:
        return n*fact(n-1)

res=fact(5)
print(res)

print("-----------------------------------------------------------------")

#fibonacci series
def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-2) + fibo(n-1)
res=fibo(9)
print(res)




print("----------------------------------------------------------------")

#count the dupicate elements
x=[1,2,3,4,5,1,2,3,4,5,1,2,3,45,4,5]
d={}
c=0
for i in x:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)

print("-----------------------------------------------------------------")
#anaysyzing the most frequent num
x=[1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,5]
print(max(set(x),key = x.count))

print("-----------------------------------------------------------------")

#sum the elements
x=[1,2,3,4,5]
c=0
for i in x:
    c=c+i
print(c)

print("-----------------------------------------------------------------")
x=["1","2","9","8","5"]

x.sort(key =int)
print(x)

x=["gopi","a","kkddd","kdksd","ldddddddds"]
x.sort(key=len)
print(x)


print("-----------------------------------------------------------------")
#sum the duplicate elements
x=[1,2,3,4,5,1,2,3,4,5,1,2,3,5]
c=0
print(c)
y=[]
for i in x:
    if i not in y:
        y.append(i)
    else:
        c=c+1
print(c)

print("-----------------------------------------------------------------")
#wap convert the lower to upper
s="gopi"
for i in s:
    if ord(i)>97 or ord(i)<122:
        res=chr(ord(i)-32)
        print(res,end="")
print("-----------------------------------------------------------------")
#wap convert the all vowel lower to upper
s="gopiaeipu"
vo="aeioe"
for i in s:
    for v in vo:
        if i == v:
            print(i.upper(),end="")
print("-----------------------------------------------------------------")
#convert every second num of           
    
x=["jon","boy","jose","dfe","jimmy"]
for i in x:
    if i.startswith == "j":
        print(i)

print("---------------------------------------------------------------")
x=["1","2","9","8","5"]

x.sort(key =int)
print(x)

x=["gopi","a","kkddd","kdksd","ldddddddds"]
x.sort(key=len)
print(x)

print("------------------------------------------------------------------")
x=[1,2,3,5]
y=[10,20,30,40]

res=list(map(lambda x,y:x+y,x,y))
print(res)
print("---------------------------------------------------------------")
    
















                



    
