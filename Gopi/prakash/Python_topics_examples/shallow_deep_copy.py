"""
import Copy
L=[1,[2,3,4],[5,6],7]
S=copy. Copy(l)
Print(s)
"""

x=[1,2,31,2,3,4,1,2,3,4,5,6,7,5,5,5]
c=0
for e in x:
    t_c=x.count(e)
    if t_c>c:
        c=t_c
        res=e
print(res)

res=max(x ,key=x.count)
print(res)

"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

class App:

    def __int__(self):
        self.driver=None
        self.driver_path=None
        self.intilize_driver()

    def intilize_driver(self):
        self.driver_path = "chromedriver_win32\\chromedriver.exe"
        if os.path.exists(self.driver_path):
            print("driver path is exits")
        else:
            print("unable to find the driver path")

    def lunch_browser(self):
        self.driver=webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get("https://demo.guru99.com/test/newtours/register.php")



obj=App()
obj.intilize_driver()
obj.lunch_browser()
"""



x={"a":1,"b":4,"c":8}

y=[]

for i in x.values():
    print(i)
    y.append(i)
print(max(y))
print(min(y))



#
x="aabccdeff"
y=""
for i in x:
    if x.count(i)>1:
        pass
        
    else:
        y=y+i
print(y)
    

n=3000
d=10000

try:
    n>100
    print("hfhfh")
    """
    if n<1:
        print("can buy product")
    """
except Excepation as Ae:
    print("cannot")
    raise Excepation ("cannot buy a product".format(str(ae)))



















