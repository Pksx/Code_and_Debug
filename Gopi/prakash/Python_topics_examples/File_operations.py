#wap to find the sentence in file by using readliness
with open("D:\Gopi_all_python\Interview_questions_all\jenkins.txt","r") as f:
    lines=f.readlines()
    word="DevOps"
    for line in lines:
        if line.find(word)!=-1:
            print(word,"string exist in lines")
            print('line number: ',lines.index(line))
            print('line',line)

#wap find the word in line 
serch_word="DevOps"
f=open("D:\Gopi_all_python\Interview_questions_all\jenkins.txt","r")
lines=f.read().split()
for i,line in enumerate(lines):
    if serch_word in line:
        print(i,line)
        
#how to search the word in file
serch_word="to"
f=open("D:\Gopi_all_python\Interview_questions_all\jenkins.txt","r")
res=f.read().split()
for i in res:
    if serch_word in i:
        print(i)


"""
#READLINES:readlines() method to iterate each line from a file
f=open("D:\Gopi_all_python\Interview_questions_all\jenkins.txt","r")
res=f.readline()
print(res[0])
print(type(res))
for i in res:
    print(i)
"""


"""  
with open("D:\\oracle_db_project1\\oracle_db_project1\\input_data\\DATA_ENGG_SBP_PATCH_2021.xlsx", 'rb') as f:
    text = f.read()
    print(text.text)
"""
#Write a program to read a file and print all the lines with the word 'python'
with open("D:\Gopi_all_python\Interview_questions_all\jenkins.txt","r") as f:
    lines=f.read().split()
    for line in lines:
        if "to" in line.lower():
            print('lie',line)


f=open("D:\Gopi_all_python\Python_topics_examples\Multi_threading.txt","r")
lines=f.readlines()
res=lines[-5:]
print(res)
#print(lines)
print(type(lines))
for i,line in enumerate(res):
    print(i,line)




f=open("D:\\Gopi_all_python\\Python_topics_examples\\new_file.txt","a")
res=f.write("parrale exuteion")
print(res)
























    
    
