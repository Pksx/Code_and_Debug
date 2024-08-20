#wap print the even number in one line
nums=range(1001)
new_list=[]
res=[new_list.append(num) for num in nums if num%2==0]#list comprehsion used
print(new_list)
print("-------------------------------------------------------")

print(new_list[0:4])
print(new_list[-5:-1])

print("-------------------------------------------------------")

def mani_0(x):
    yield[i*5 for i in x]
x=[1,2,3,4,5]
res=mani_0(x)
y=[]
r=[y.append(i) for i in res]
print(y)

#or

def mani(x):
    return [i*5 for i in x]
x=[1,5,10,15,20]
print(mani(x))

print("-------------------------------------------------------")
def mani2(x):
    return list(map(lambda i:i*5, x))
x=[1,2,3,4,5]
print(mani2(x))

print("-------------------------------------------------------")


# 7. Make the above three functions as methods of a class named ManipulatorClass
# and invoke them.

class ManipulatorClass:

    def mani(self,x):
        return [i*5 for i in x]

    def mani2(self,x):
        return list(map(lambda i:i*5, x))

obj=ManipulatorClass()
m1=obj.mani([1,2,3,4,5])
print(m1)
m2=obj.mani2([1,2,3,4,5])
print(m2)

print("-------------------------------------------------------")
#wap for try and excepation

try:
    z=3//2
    print("result is success")

except:
    print("we cannot divided by zero")

print("-------------------------------------------------------")

try:
    z=3//0
    print("results is success")
except:
    print("cannot divide by zero! please give another values expect zero:-")





