import json


# #Serialization : JSON File to Python Data (json.loads)
# # print("Hello JSON")
# # jsonString = '["a","b","c","d"]'
# jsonString = '{"vowels":["a","e","i","o","u"],"Name":"Balaji"}'
# jsonData = json.loads(jsonString)
# print (type(jsonData), jsonData)


# some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parse x:
# y = json.loads(x)
# # the result is a Python dictionary:
# print(y["age"])


# with open('D:\\Testing\\Python Advaned Session\\Data\\data.txt') as json_file:  
#     data = json.load(json_file)

#     for p in data['people']:
#         print('Name: ' + p['name'])
#         print('Website: ' + p['website'])
#         print('From: ' + p['from'])
#         print('')

#     print(data['people'][0]['name'])

# ==================================================
# jsonFile = "D:\\Testing\\Python Advaned Session\\Data\\Example.json"

# with open(jsonFile,"r") as jsonFilePointer:
# 	jsonData = json.load(jsonFilePointer)
# print (jsonData)





#Deserialization : Python Data to JSON File
# jsonData = {"a" : 1, "b" : 2, "c" : 3, "d" : [4,5,6,7]}
# jsonWriteFile = "D:\\Testing\\Python Advaned Session\\Data\\jsonWrite3.json"
# with open (jsonWriteFile, "w") as jsonFilePointer:
# 	json.dump(jsonData,jsonFilePointer)

# jsonString = json.dumps(jsonData, indent = 2)
# print(jsonString)


# # a Python object (dict):
# x = { "name": "John", "age": 30,"city": "New York"}

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# Convert Python objects into JSON strings, and print the values:


# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# y=json.dumps(x,indent=4)
# print(y)
# print(json.dumps(x))
# print(json.dumps(x, indent=4))
# print(json.dumps(x, indent=4, separators=(": ", " = ")))
# print(json.dumps(x, indent=4, sort_keys=True))


#  Modify



with open("D:\\Testing\\Python Advaned Session\\Data\\jsonWrite1.json", "r") as f:
    data = json.load(f)
    print("Before:", data)
    data["a"] = "Suhail"
    print("After: ", data)
f.close()

# with open("D:\\Testing\\Python Advaned Session\\Data\\in.json", 'w') as outfile:  
#     json.dump(data, outfile)