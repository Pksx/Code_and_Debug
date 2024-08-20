"""
d={"a":97,"b":98,"c":99,"d":100,"e":101}
#add the new value
d["f"]=65
print(d)
#
#print(d.pop("e"))
#print(d)
#print(d.popitem())
#print(d)

#merge two dict
s={"q":33,"d":54,"x":98,}
d={"a":32,"b":55,"h":99,"k":87}
s.update(d)
print(s)
#print(d)

res={**s,**d}
print(res)

x=["jon","jimmy","boy","sas","hsy","jing"]
for i in x:
    if i[0][0]=="j":
        print(i)

res=[i.upper()  for i in x]
print(res)

res=[i for i in x if i[0][0]=="j"  ]
print(res)

#print(d.keys())
#print(d.values())
#print(d.items())
for k in d.keys():
    print(k)
for v in d.values():
    print(v)
for k,v in d.items():
    print(k,v)


a={"a":97,"b":98,"c":99,"e":100,"f":101}
d=["a","b","c"]
d2={}
for i,k in a.items():
    if i not in d:
        d2[i]=k
print(d2)
"""
"""
#How to convert list of tuples into dict->use dict() function
ab = [("a", 1), ("b", 2), ("c", 3),("e",5)]
#print(dict(ab))
d3={}
for i in ab:
    d3[i[0]]=i[1]
print(d3)
    
"""
"""
#set functions
s={1,2,3,45.6,"gopi"}
a={23.5,23,1,5}
s.add(6)
s.remove(2)
s.update(a)
print(a)
"""
"""
print("------------------------------------------------------------------------")
#how to sort dict in acsending order and descending order by key ?
#ascending order by key

data = {"Bob": 23,"Charlie": 36,
    "Alice": 72,
    "Eric": 18,
    "David": 9
}

sort_dict=sorted(data.items())
print(sort_dict)

print("------------------------------------------------------------------------")

#descending order by key 
data = {"Bob": 23,"Charlie": 36,
    "Alice": 72,
    "Eric": 18,
    "David": 9
}
sort_dict=sorted(data.items(),reverse=True)
print(sort_dict)

print("-------------------------------------------------------------------------")
#how to sort dict in acsending order and descending order by value ?

#sort dict in acsending ordering by value
data = {
    "Bob": 23,
    "Charlie": 36,
    "Alice": 72,
    "Eric": 18,
    "David": 9
}

sort_dict=sorted(data.items() ,key=lambda x:x[1])
print(sort_dict)

print("--------------------------------------------------------------------")
#sort dict in descending order by value
data = {
    "Bob": 23,
    "Charlie": 36,
    "Alice": 72,
    "Eric": 18,
    "David": 9
}
sort_dict=sorted(data.items(), key=lambda x:x[1],reverse=True)
sort_dict_value=dict(sort_dict)
print(sort_dict_value)
"""
print("------------------------------------------------------------------")
#Difference b/n normal dict and default dict?

#"""
"""
d={"a":1,"b":2,"c":3}
d2={"a":1,"b":3,"c":6}

d.update(d2)
print(d)


#output={"a":3,"b":6,"c":9}
d={"a":1,"b":2,"c":3}
for k,v in d.items():
    d[k]=d[k]*3
    print(d)

#dict comprehsnionsions
d={"a":1,"b":2,"c":3,"d":5}
output={k:v*3 for k,v in d.items()}
print(output)

"""

print("--------------------------------------------------------------------------")

#sum dict values
d={"a":1,"b":2,"c":3}

c=0
for v in d.values():
    c=c+v
    print(c)

#dict comprension sum the valiues
d={"a":1,"b":2,"c":3}
out={k:v+3 for k,v in d.items()}
print(out)    

print("---------------------------------------------------------------")
"""
#convert into the dict
l1=["gopi","niranjan","mahesh"]
l2=[1,2,3]

print(dict(zip(l1,l2)))

d={}
for k in l1:
    for v in l2:
        d[i]=v
print(d)

dict_keys=["gopi","mahesh","niranjan"]
dict_values=[2,3,4]
#using dict comprasion
res={dict_keys[i]:dict_values[i] for i in range(len(dict_keys))}
print(res)

#using lamnda function

dict_keys=["gopi","mahesh","niranjan"]
dict_values=[2,3,4]

res2=dict(map(lambda k,v : (k,v), dict_keys,dict_values))
print(res2)


"""
print("---------------------------------------")
#same input
x=[1,2,3,4,5,5,6]
x[:]=x[2:]+x[0:2]
print(x)

print("="*70)
"""
#avrge of the dict values
d={"stu1":[65,68,59,52,69,65,55,59],"stu2":[60,64,60,60,88,64,68,75],
   "stu3":[50,72,64,62,66,68,72,73],"stu4":[82,62,61,54,71,89,75,73]}

d2={}
s=0
for k in d:
    for v in d[k]:
        s=s+v//len(k)
        d2[k]=s
print(d2)
        
print("-"*50)
"""

"""
#convert the  dict format
x= [("A", 65), ("B", 66), ("C", 67), ("D", 68)]

d={}

for i in x:
    d[i[0]]=i[1]
print(d)

#max key value in dict
dictt = {'1': 100, '2': 1292, '3': 88}

res=max(dictt,key=lambda x:dictt[x])
print(res)

print("--------------------------------------------------------------------------")
#max key value in dict
d={"1":2,"2":98,"3":109}
res2=min(d,key=lambda x:d[x])
print(res2)

print("----------------------------------------------------------------------------------")
"""
"""
d={"a":97,"b":98,"c":99,"d":100,"e":101}

d2=["c","a"]

d3={}
for k,v in d.items():
    if k not in d2:
        d3[k]=v
print(d3)
print("-------------------------------------------------------------------------------------------")
"""
"""
"print the name of the 1st employe  print the name of the second employe age print the speci"
d={"name":gopi,"age":29,"speci":"QA","name2":"mahe","age2":29,"speci2":"dev","name3":"sueresh","age3":39,"speci3":"dev2"}
"""
#wap if dict key is not prsent  we have to print none values .if dict key is
#there it should be print  key of the value

d={"a":2,"b":7,"c":5}

value=d.get("a",None)
print(value)

val=d.get("f",None)
print(val)


d={"a":3,"b":4,"c":6,"a":8,("a",1):9}#if u define the same keys .it will give the last key value
print(d["a"])
print(d[("a",1)])
















    
