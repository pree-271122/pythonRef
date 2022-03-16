#MODULES IN PYTHON#

import os
import shutil

#Create a folder
os.mkdir("/Users/DELL/Desktop/Python/newFolder")

#create a file
f=open("/Users/DELL/Desktop/Python/newFolder/myfile.txt",'x')
#write in a file
f.write("Hi i am preethi")

#checking for path exists
path = "/Users/DELL/Desktop/Python/newFolder"
isExist = os.path.exists(path)
print(isExist)

#spliting the file name from its extension
path1 ="/Users/DELL/Desktop/Python/test.txt"
split = os.path.splitext(path1)
print(split)

#list the folder
path3="/Users/DELL/Desktop/Python"

print("Before copying file:")
print(os.listdir(path3))

#Source path
source="/Users/DELL/Desktop/Python/test.txt"
#destination path
destination = "/Users/DELL/Desktop/Python/test1.txt"
#Moving
dest = shutil.move(source,destination)

print("File Moved")
#print(os.listdir(path3))

#Remove folder
#os.rmdir("newFolder")
#os.remove("pree.txt")
