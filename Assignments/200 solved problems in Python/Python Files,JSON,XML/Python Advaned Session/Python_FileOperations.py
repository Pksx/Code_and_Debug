# #Program to illustrate File Operations

# #Example 1 : Open & Read a file 

# fileName = "D:\\Testing\\Python Advaned Session\\Data\\FileOperations.txt"
# filePointer = open(fileName,"r")
# data = filePointer.read()
# print(data)
# filePointer.close()

# #Example 2: Open & read specified number of bytes

# fileName = "D:\\Testing\\Python Advaned Session\\Data\\FileOperations.txt"
# filePointer = open(fileName,"r")
# data = filePointer.read(10)
# print(data)
# filePointer.close()

# #Example 3: Read Line and read lines
# fileName = "D:\\Testing\\Python Advaned Session\\Data\\FileOperations.txt"
# filePointer = open(fileName,"r")
# data = filePointer.readline()
# # print(data)
# # print(filePointer.readline())
# # data = filePointer.readlines()
# # print(data)
# filePointer.close()

# ============================================
# #Eample 4: Seek and read
# fileName = "D:\\Testing\\Python Advaned Session\\Data\\FileOperations.txt"
# filePointer = open(fileName,"r")
# filePointer.seek(5,0) 
# data = filePointer.read()
# # filePointer.seek(3,1) 
# # data = filePointer.read()
# # filePointer.seek(-10,2) 
# # data = filePointer.read()
# print(data)
# filePointer.close()

# #Example 5: Tell the cursor position
# fileName = "D:\\Testing\\Python Advaned Session\\Data\\FileOperations.txt"
# filePointer = open(fileName,"r")
# cursorPosition = filePointer.tell()
# print(cursorPosition)
# filePointer.read(5)
# cursorPosition = filePointer.tell()
# print(cursorPosition)
# filePointer.close()

# #Example 6: Write the data to a file - Creates and writes the data to file 
# fileName = "D:\\Testing\\Python Advaned Session\\Data\\FileOperations.txt"
# filePointer = open(fileName,"w")
# data = "Dell Technologies"
# print(filePointer.tell())
# filePointer.seek(5)
# filePointer.write(data)
# filePointer.close()

# #Similar to read we can also change the cursor position and write the data

# #Example 7 : Append the data to a existing file 

# fileName = "D:\\Testing\\Python Advaned Session\\Data\\FileOperations1.txt"
# filePointer = open(fileName,"a")
# data = "Dell5 and Dell12 CPG Group"
# filePointer.write(data)
# filePointer.close()

# file = open("D:\\Testing\\Python Advaned Session\\Data\\FileOperations.txt", "r+")

# print("Opening mode : ", file.mode)

# print("Writing to the file")
# file.write( "Python is a great language.\nYeah its really great!!\n");

# # Before closing the file
# print ("Closed or not : ", file.closed)
# file.close()

# # After Closng the file
# print ("Closed or not : ", file.closed)

# import os

# # Rename a file from test1.txt to test2.txt
# os.rename( "test1.txt", "test2.txt" )


# import os

# # Delete file test2.txt
# os.remove("text2.txt")





# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")