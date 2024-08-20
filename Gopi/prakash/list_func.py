#list functions:
#append: it is used foe to add the element at the end of list.
l=[1,2,3,4,5]
l.append(8)
l.append(9.0)
l.append("saff")
l.append([1567])
l.append([3,4,5,6,7])
print(l)

#insert:it is used for to insert the value based on the position.
b=[1,2,3,4,5]
b.insert(2,6)
b.insert(4,"string")
print(b)

#pop:pop fun is used for to remove the value based on the index postion.if you donot give index postion automaticaly end value will be deleted
c=[4,5,7,3,6,0,0]
c.pop(3)
c.pop()
print(c)

#remove:it used for remove the specific.
x=["a",4,5,6,7]
x.remove("a")
print(x)

#sort:it used for sort the elements form asecdinf order to descending.
x=[4,3,4,5,7,2,3,3,7]
x.sort()
print(x)

#reverse:it is used for reverse the order.
y=["gosd","jdjjd","jdjd",5,8,9.0]
y.reverse()
print(y)

#extend:it is used for to add the number of element in the list:
a=[1,2,3,4,5]
print(len(a))
a.extend([3,4,5,6,7])
print(a)
print(len(a))



#tuple function
#index:it is used for to get the index based on value postion.
i=[9,8,7,6,5,4]
t=i.index(6)
print(t)

#count:it is used for to get the number of the repeated values.
y=[9,8,7,6,5,4,4,4,4]
o=y.count(6)
print(o)


#slicing:slicing is used for to extract the data form given the sting or list.
s="pythonworld"
y=s[0:3]
print(y)





