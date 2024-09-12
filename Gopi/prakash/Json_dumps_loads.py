# my_dict = {1: 4, 2: 3, 3: 4, 4: 4, 5: 7}
my_dict = {"apple": 10, "mango": 15, "banana": 10, "grape": 10, "manage": 20}

import collections

value_occurrences = collections.Counter(my_dict.values())
print(value_occurrences)

filtered_dict = {
    key: value for key, value in my_dict.items() if value_occurrences[value] > 1
}
print(filtered_dict)

# ------------------------------------------------------------
# #update keys
# my_dict={"apple":10,"mango":15,"banana":10,"grape":10,"manage":20}
# my_dict.update({"apple":20})
# my_dict.update({"banana":100})
# print(my_dict)

# #delete the keys
# my_dict={"apple":10,"mango":15,"banana":10,"grape":10,"manage":20}
# del my_dict["grape"]
# print(my_dict)

# #add values for all dict values
# my_dict={"apple":10,"mango":15,"banana":10,"grape":10,"manage":20}
# for key in  my_dict:
#     my_dict[key]=my_dict[key]+10
# print(my_dict)

# #update the all dict values
# my_dict={"apple":10,"mango":15,"banana":10,"grape":10,"manage":20}
# for key in my_dict:
#     my_dict[key]=50
# print(my_dict)

# x={"a":1,"b":2,"c":3}
# y={"d":4,"e":5,"f":6}

# combined_dic={}

# for key in x:
#     combined_dic[key]=x[key]
# for key in y :
#     combined_dic[key]=y[key]

# print(combined_dic)

# x={"a":1,"b":2,"c":3}
# y={"d":4,"e":5,"f":6}

# res={**x,**y}
# print(res)

# sum=0
# for k,v in res.items():
#     sum=sum+v
# print(sum)

# x=[1,2,3,4]
# y=[4,5,6,7]

# res={k:v for k,v in zip(x,y)}
# print(res)

# x=["a","b","c","d"]
# y=["e","f","d","h"]

# res2={k+v for k,v in zip(x,y)}
# print(res2)
