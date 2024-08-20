"""
dictinoary: dict is collection data type .it will collect the unordered datatype.
we can defined by usinf {}
it will store the value key :values pairs
dictinory properities :key and value
"""
#how to access the value?
#by using key
d={"a":1,"b":2,"c":3}
y=d["a"]
print(y)

#add the one more key:value
d["d"]=4
print(d)

#how to remove type value
d={"a":1,"b":2,"c":3}
z=d.pop("c")
print(z)


#operators
#arthamatic operators
#+,-,%,//,*
"""
x=float(input("enter a value:"))
y=float(input("enter a value2:"))

z=x+y
print(z)
"""

"""
membership opertaor:ir is used for to check the value is presenr or not.
in,not in
#realtional opertaion
#<>,<=,>=,==,=
#if ,if else:it is used for write the only one condition
#if elif:we can write multiple conditions
a=10
b=20

if a<b:
    print("a is lessthen b")

else:
    print("b is lessthan a")


a=10
b=20

if a>b:
    print("a is grtaer then b")                        

else:
    print("b is greater than a")


a=10
b=5

if a<=b:
    print("a is grtaer then b")

else:
    print("b is greater than a")


day=int(input("Enter the day: "))

if day ==1:
    print("num one is monday")

elif day == 2:
    print("num two is tuesday")

elif day == 3:
    print("num three is wensday")
elif day == 4:
    print("num four is thrusday")
elif day == 5:
    print("num five is friday")
elif day == 6:
    print("num six is saturday")
elif day == 7:
    print("num seven is sunday")

else:
    print("please enter the valid number from 1 to 7")


"""
"""
#for loop: for loop is used for to traverse the sequence itrable object. it traverse the each and every value.
#sequence: we can stofe the element line by line.(list,tuple,string)
#for loop syntax: for varibale in sequence object:
x=[1,2,3,4,5,6]

for i in x:
    print(i)
    if i==2:
        print(i
    else:
        print(i)
"""

#the word "OpenDoc()" by accesing it from the dictionary below.
exp = {"menu": {
	      "id": "file",
	      "value": "File",
	      "popup": {
		"menuitem": [
		  {"value": "New", "onclick": "CreateNewDoc()"},
		  {"value": "Open", "onclick": "OpenDoc()"},
		  {"value": "Close", "onclick": "CloseDoc()"}
		]
	      }
	    }}
print(exp["menu"]["popup"]["menuitem"][1]["onclick"])
print(exp["menu"]["popup"]["menuitem"][2]["onclick"])



    



    
    

    
















