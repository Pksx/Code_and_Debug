# s = "python is high level programming languag"

import re

# res = re.findall("level", s)  # return a list containing all matches
# print(res)

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)  # return the match object if there string matches
# print(x)


# #metacharacters
s = "python is high level programming languag"
# find the all lower case characters alphabatecally between the a to m
r = re.findall("[a-m]", s)
print(r)

# #Write a regular expression to accept email patterns

# import re

# def email_match(s):
#     pat=r'\b[A-Za-z0-9._%+-]+@[A_Za-z0-9.-]+\.[A_Z|a-z]{2,7}\b'
#     if re.match(pat,s):
#         print("valid email")
#     else:
#         print("not valied email")

# if __name__ == '__main__':
#     #Enter the email
#     email="ankitrai326@gmail.com"
#     email_match(email)

#     email = "my.ownsite@our-earth.org"
#     email_match(email)
#     email = "ankitrai326.com"
#     email_match(email)

# #how to validate the ip address
# import re

# def ip_add_match(s):

#     pat='\[0-9].'
#     if re.match(pat,s):
#         print("valid ipaddress")
#     else:
#         print("invalid ipaddress")

# ip='134.168.8.09'
# ip_add_match(ip)

# #find the digits in file
# with open("D:\\Gopi_all_python\\new2.txt","r")as f:
#     line=f.read().split()
#     for i in line:
#         res=re.findall("\d+",i)
#         print(res)

# #wap find the url


# import re

# #url = "https://www.example.com"
# url="https://www.w3schools.com/python/python_regex.asp"
# pattern = "^https?://[\w\-\.]+\.[\w\-]{2,}"


# if re.match(pattern, url):
#     print("Match found!")
# else:
#     print("No match.")


# import re
# x=["gopi@gmail.com","gopi@yahoo.com","gopi123@gmail.com"]
# pat=r"^[a-zA-z0-9._%+-]+@gmail\.com$"
# g=[email for email in x if re.search(pat,email)]
# print(g)


# import re
# x=["gopi@gmail.com","gopi@yahoo.com","gopi123@gmail.com"]
# domains=[]
# for emails in x:
#     print(emails)
#     '''pat=re.search(r"@([\w.]+)",emails).group(1)
#     domains.append(pat)
# print(domains)'''
