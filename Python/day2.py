#FUNCTIONS IN PYTHON#

#pre defined function
# print(),open(),split()
f=open("test.txt")
p=f.read()
print(p)

#open the file and read line by line
f = open("test.txt")
fileLines = f.readlines()
for line in fileLines:
    print(line)

#split a file with space
name="My name is python,I love coding"
words=name.split()
print(words)

#split the file with a condition
words1=name.split(",")
print(words1)

#Customized function
def greet(name):
    print("Hello " + "Mr/Ms " +name + ", welcome")

greet("Venkatesh")

#function to read a file , split them and print them
def readfile():
    filename = input("enter the file name : ")
    number=0
    file = open(filename,'r')
    for i in file:
        words=i.split()
        number=number+len(words)
    print("Number of words:" )
    print(number)

readfile()