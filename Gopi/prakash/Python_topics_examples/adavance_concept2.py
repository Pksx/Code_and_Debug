"""
lambda function: lambda is  a anonmys function and we can call it is as small function
lambda function can have mutliple  number of parameters but can have only one expressions
higher oreder functions:--> we can call as functiom name as function arguments.
there are two type of higher order function
map function:--> map fun is used for to iterate over through  the sequnce objects .map functiin deos return the values input as output.
filter function:--> filter fun is used for to iterate over through  the sequnce objects .filter function deos return the vlues of  when the condition is true.
decorators:---> decoratoper is function is used for modify the behaviour of exits function without modify the permentaly.decorator is wrap the one fucntion to  wrap another of objects.
here we are used to do '@' symbol for calling the decorator
generators:--> 
list comprehsions:---> list comprehsion are offerd as short sysntax of which means we can write the program whole thing in one line.
sysntax:[variable for var in sequence-obj expressions]
"""

#normal function
x=[1,2,3,4]
for i in x:
    print(i*i)
    
#map function
x=[1,2,3,4]
res= list(map(lambda i:i*i,x))# here it return the input as output
print(res)

#filter function
x=[1,2,3,4]
res= list(filter(lambda i:i*i,x))# here it return the output when conditionis true.otherwise it returns input only
print(res)

ex:2
x=range(20)
res=list(filter(lambda i:i%2==0,x))# here it returned only  condition true values.
print(res)

#normal fun

for i in x:
    if i%2==0:
        pass
        #print(i)


#list comprehension
res= [i for i in x if i%2==0]
print(res)


#decorators:
def upper_str(func):

    def inner():
        str1=func()
        return str1.upper()
    return inner

@upper_str
def print_str():
    return "python world"

print(print_str())


#generators:generator is a function .it generate the generator object.we can generate the object by using  "next" method and by using the  "loops"

#here we are generate the object by using the next method.
def fun():
    yield 1
    yield 2
    yield 3
    
res=fun()
print(next(res))
print(next(res))


#generate  the object by using loop
def fun():
    yield 1
    yield 2
    yield 3

for i in fun():
    print(i)

#list comprehsnion
x=[1,2,3,4,5]
res=[i*i for i in x]
print(res)

res2=[i for i in x if i%2==0]
print(res2)

res3=[i*i for i in x if i%2==0]
print(res3)

#common element by using list comprehnsion
list1=[1,2,3,4,5]
list2=[1,2,3,4,5,6,5,4,3]
res4=[i for i in list1 if i in list2]
print(res4)

strn=["data","machine","AI"]
upper_case=[i.upper() for i in strn]
print(upper_case)

strn=["data","machine","AI"]
upper=[i[0].upper() for i in strn]
print(upper)

#createing list of tuple from two lists
a=[1,2,3,4,5]
b=["a","b","c","d"]
res5=[(k,v) for k in a for v in b]
print(res5)

strn="data machine ai"
print(id(strn))
res6=[i[0] for i in strn.split()]
print(res6)
print(id(res6))

#create number 1 tp 100  that rae divisle by 5 and 7
x=range(1,100)
res7=[i for i in x if i%5 == 0 and i%7==0]
print(res7)

#unique elements
list2=[1,2,3,4,5,6,5,4,3,1,2,3,4,5]
res8=list(set([i for i in list2]))
print(res8)

#list of tuples each element stirng and list
strn=["data","machine","AI"]
res9=[(i,len(i))for i in strn]
print(res9)
print(dict(res9))

d={}
for i in res9:
    d[i[0]]=i[1]
print(d)
    






    




