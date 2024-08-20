"""
what is decorators
generators: generator is fucntion to generate the genarator object.generator object is
iterator the object by using "next" method on the generator onject. and by using "loops" on the generator object

DISADAVANTAGES:
slow excution:it will excuteion values one by one.

what is the adavantages of generators?


"""

"""
#normal function
def even_num():
    for i in range(0,2,2):
        return i
res=even_num()
print(type(res))

#for i in res:
    #print(i)


def even_num():
    for i in range(0,20,2):
        yield i
res=even_num()
print(res)
print(type(res))
for i in res:
    print(i)


def fun():
    yield 1
    yield 2
    yield 3
print(fun())

def fun():
    yield 1
    yield 2
    yield 3
res=fun()
print(next(res))
print(next(res))

"""
#decorators: decorators are used for modfiy the behavioure of function over class.decorator allow us to
#wrap one function  in order to extend the another function without permentily modify.
"""
def upper_str(func):

    def inner():
        str1=func()
        return str1.upper()
    return inner()

#def print_str():
 #   return "python"
 
@upper_str
def print_str():
    return "python world"

res=print_str()
print(res)

"""

#lambda and map
x=[1,2,3]
res=tuple(map(lambda i:i*i,x))
print(res)

x=range(50)
res=list(filter(lambda i:i%2==0,x))
print(res)


#class method
class Clsex:
    
    x=2
    @classmethod
    def modify(cls):
        cls.x=5
        print(cls.x)

print(Clsex.x)        
obj=Clsex()
print(obj.x)
print(Clsex.modify())
print(Clsex.x)
print(obj.x)
print(obj.modify())



class sts_ex:
    x=2
    @staticmethod
    def m():
        x=5
        print(x)
sts_ex.m()
print(sts_ex.x)
obj=sts_ex()
print(obj.x)
obj.m()

print("-----------------------------------------------------------")
"""
#how to pass the user input to lambda function
a=int(input("ENter the number: "))
b=int(input("Enter the sec number: "))

res=(lambda a,b:a+b)
print(res(a,b))
"""

"""
#Give an example for the map function using lambda function
x=range(20)
res=list(map(lambda i:i*i,x))
print(res)

#pass input form user
num1=int(input("Enter the num1: "))
num2=int(input("Enter the num2: "))

res=(lambda num1,num2:num1+num2)
print(res(num1,num2))

#Give an example for the map function using lambda function
y=range(20)
res=list(filter(lambda i:i%2==0,y))
print(res)
"""
#print the list of prime numbers
res=list(filter(lambda x:all(x%y !=0 for y in range(2,x)),range(2,11)))
print(res)

#Write an example to demonstrate the use of decorators.

def outer_fun(func):

    def inner_fun(num1,num2):
        return func(int(num1),int(num2))
    
    return inner_fun

@outer_fun
def add(num1,num2):
    res=num1+num2
    print(res)

add(12,13)


#iter()__ iter method is return the iterable object.this is required to allow an iterator to be used for and in statement.
#nextmethod:the next mathod  return the next elements in the sequence.once when it reaches the ends all subsquence call to method should stop element raise the an excepation.
# Function to generate all the non-negative numbers
# up to the given non-negative number.
class UpTo:
    # giving the parameter a default value of 0
    def __init__(self, max = 0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        # The next method will throw an
        # exception when the termination condition is reached.
        if self.n > self.max:
            raise StopIteration
        else:
            result = self.n
            self.n += 1
            return result
for number in UpTo(5):
    print(number)
















