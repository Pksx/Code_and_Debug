
#1
"""
def v_upper(str_inp):
    output=""
    y="aeiou"
    for ch in str_inp:
        if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
            ch=chr(ord(ch)-32)
            print(ch)         
    return (ch)          
resp=v_upper("hyderbadaa")
print(resp)
"""
#3
"""
def rev_list(x):
    for e in x:
        x.reverse()
    return(x)
x=[5,4,3,2,1]
resp=rev_list(x)
print(x)
"""
#perfet num
""""
def per_num(num):
    sum=0
    for i in range(1,num):
        if(num%i)==0:
            sum=sum+i
    if(sum==num):
        print(" perfect num" )
    else:
        print(" not perfect num" )
    #return num
num=int(input("enter a number"))
resp=per_num(num)
#print(resp)
"""
#8
"""
def v_occur(str):
    y={}
    z="aeiou"
    for ch in str:
        if ch in z:
            if ch not in y:
                y[ch]=1
            else:
                y[ch]=y[ch]+1
    return(y)
x=input("enter a string")
resp=v_occur(x)
print(resp)       
"""
#10
"""
def upper(str_inp):
    output=""
    for ch in str_inp:
        if ord(ch)>=ord('a') and ord(ch)<=ord('z'):
            ch=chr(ord(ch)-32)
        output=output+ch
        
    return(output)
x=input("enter a string")

resp=upper(x)
print(resp)
"""
#15
"""
def count(x):
    y=[]
    for i in x:
        y=x.count(i)
    return y                  
x=[403,403,405,409,444,403]
resp=count(x)
print(resp)
"""
#13
"""
def max_num(x):
    for e in x:
        x.sort()
        y=x[-1]   
    return y
x=[10,34,200,25,94,94,21,74,2,89]
resp=max_num(x)
print(resp)
"""
        
