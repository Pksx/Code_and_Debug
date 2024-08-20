"""
from threading import *

class hello:
    def run(self):
        for i in range(5):
            print("hello")
class hi:
    def run(self):
         for i in range(5):
            print("hi")

t1=hello()
t2=hi()
t1.run()
t2.run()


import threading

def coder(number):
    print ('Coders:  %s' , %number)
    return

threads = []
for k in range(5):
    t = threading.Thread(target=coder, args=(k,))
    threads.append(t)
    t.start()


#Program to print the fibonacci series upto n_terms

# Recursive function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 12

# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
for i in range(n_terms):
	print(recursive_fibonacci(i))

"""
"""
import threading

def cal_sqr():

    for i in n:
        print(i*i)

def cal_Cube():
    for i in n:
        print(i*i*i)

ar=[2,3,4,5]

th1 = threading.Thread(target=cal_sqr, args=(ar, ))  
th2 = threading.Thread(target=cal_Cube, args=(ar, ))  
th1.start()  
th2.start()  
th1.join()  
th2.join()

"""

"""

from threading import *
import time


class Hello(Thread):

    def run (self):
        for i in range(5):
            print("hello")

            
class Hi(Thread):

    def run(self):
        for i in range(5):
            print("hi")

t1=Hello()
t2=Hi()

#t1.run()
#t2.run()

t1.start()
time.sleep(0.2)
t2.start()

t1.join()#it is tell to main to stop the excute program after complte the excution process
t2.join()

print("exit")
"""

          
"""
import threading
import time

def cube_num(n):
    print("cube numbers:",n*n*n)

def square_num(n):
    print("square numbers:",n*n)

#t1=threading.Thread(target=cube_num,args=(10,))
#Thread class that is used for implementing threads,
#t2=threading.Thread(target=square_num,args=(10,))

#t1.start()
#t2.start()

#t1.join()
#t2.join()

print("exit")

thread=[]
thread2=[]
for i in range(20):
    t1=threading.Thread(target=cube_num,args=(10,))
    thread.append(t1)
    t1.start()
    time.sleep(0.5)
    t1.join()
    t2=threading.Thread(target=square_num,args=(10,))
    thread2.append(t2)
    t2.start()
    time.sleep(0.2)
    t2.join()

print("exuction complete")

"""


"""

memory management:

in python divided the two way

1.Stacj memory: stack memory exexutes all the code in squence.
2.Heap Memory:heap memory all the memory allocation is done in heap memory

Remebber:python always excutes  main memory

use of garabge collecter:
1.Optimum Memory Utilizaton
2.Slower speed of execution

reference counting:it will count the each value as reference
ex:10  : 1
   20 :2
"""
    

"""

MULTI PROCESSING:

"""

"""
import multiprocessing
import os

def fun1():
    print("ID of process runinng fun1 {}".format(os.getpid()))

def fun2():
    print("ID of process of running fun2 {}".format(os.getpid()))

#print the main program id
print("id of process main running".format(os.getpid()))

#creating Process
p1=multiprocessing.Process(target=fun1)
p2=multiprocessing.Process(target=fun2)

#start processing
p1.start()
p2.start()

#process id
print("id of process p1: {}".format(os.getpid()))
print("id of process p2: {}".format(os.getpid()))

#wait untill process are finished.we can use join() method
p1.join()
p2.join()

print("both process or finishe")

print("process p1 is alive: {}".format(p1.is_alive()))
print("process p2 is alive: {}".format(p1.is_alive()))
"""






    

        

























