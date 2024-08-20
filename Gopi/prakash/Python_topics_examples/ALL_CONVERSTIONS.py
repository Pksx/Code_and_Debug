#convert the list to string
x=[1,2,3,4]
s=str(x)
print(s)
print(type(s))
#convert the num into list
x=1234
con_list=list(str(x))
print(con_list)

#without built-in
num=36775
n_list=[]
while num>0:
    digit=num%10
    n_list.append(digit)
    num//=10
n_list.reverse()
print(n_list)
    
    
#convert the list to tuple
x=[2,3,4]
t=tuple(x)
print(t)
print(type(t))
#convetr the list to set
x=[5,6,7,8]
print(type(x))
s=set(x)
print(s)
print(type(s))
#convert the list to dict
x=[1,2,3,4]
out={index:value for index,value in enumerate(x)}#it is give the index values
print(out)
#how to convert list to the decimal value without using built in method
x=[1,2,3,4]
decimal_val=0
for num in x:
    decimal_val=(decimal_val*10)+num
print(decimal_val)

#by using built in method
out=''.join(str(i) for i in x)#converting list to str
print(out)
dec=int(out)#converting into str to decimal
print(dec)

#convert the str to list
s="gopi"
con_list=list(s)
print(con_list)
con_list2=[ch for ch in s]
print(con_list2)

#convert the str to tuple
s="hello"
con_tup3=(char for char in s),
print(con_tup3)
con_tup=tuple(s)
print(con_tup)
con_tup2=tuple(ch for ch in s)
print(con_tup2)

#convert the str to dict
s="python"
#enumerate takes an iterable as an argument and returns.it is an arugumen
#as(index,element)which add a counter to each iterable element.
out={index: ch for index,ch in enumerate(s)}
print(out)
s="python"
s2="hello"
out={s:s2 for s,s2 in zip(s,s2)}
print(out)

#convert the str to decimal
d="abc"
x=0
chr_to_int={"a":1,"b":2,"c":3}
for ch in d:
    x=x*10+chr_to_int[ch]
print(x)
    




    




