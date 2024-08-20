import requests as req
#get method
url="https://en.wikipedia.org/wiki/Facebook"
res=req.get(url)
print(res)
print(res.content)# content used for to get the data human format
print(type(res))
if res.status_code==200: # to verify the status we need to get the status code
    print("succesfully get the data")
else:

    print("not found")

#----------------------------
# #post method
import requests

# Define the API endpoint URL
API_ENDPOINT = "http://example.com/api/data"

#send the data to server
data={'name': 'Raju', 'age': 25}
res=requests.post(url=API_ENDPOINT, data=data)
print(res.content)
if res.status_code==201:
    print("Succesfully resource created")
else:
    print("check the status")
#__________________________________
import  requests

api_url="http://example.com/api/data"

data2={'name': 'Raju', 'age': 25,"roll":26}
res=requests.put(url=api_url,data=data2)
print(res.content)
print(res.status_code)
#------------------------------------
import requests

api_url="http://example.com/api/data"

res=requests.delete(url=api_url)
print(res.content)
print(res.status_code)

#-------------------------------------
"""
what is the diff between authorization and authinatcation.
1.Authentication: it is the process of verifying the identity of user or a client that requsets to access to web ui.
2.Authorization:It is the process of gatharing or denying permissiin to user or client based on their role.
how do you handle the authentiation and authrazation in python
by using bear token: Enables requests to authenticate using an access key (e.g., JSON Web Token).
You include the token in the request header (Authorization: Bearer <token>).
ou auth:
basic auth: Basic authentication involves sending a verified username and password with your request.
Commonly used for simple authentication scenarios.

Authentication verifies who you are.
Authorization defines what you’re allowed to do.

payload :
Definition: The payload contains the actual data being transferred between the client and the server.
Formats: Payloads can be structured in various formats, such as JSON, XML, or even plain text.
HTTP Headers: Accompanying the payload are HTTP headers, which provide meta-information about the payload
 (e.g., content type and length).

Headers: headers play a crucial role in transmitting metadata between clients (such as web applications) and servers
"""

