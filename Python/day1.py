#BASICS VAR,IF,FOR,LIST#

#variabels
myname="Preethi"
myage=25

#Print the output
print(myname)

#List or array
myfriends=["preethi","busybee","candy"]
print(myfriends)
print(myfriends[2])

#if statement
age=int(input("Enter your age"))
if(age<12):
    print("you are a kid")
elif(age<18):
    print("you are a teen")
else:
    print("you are an adult now")

#Loop
#for loop
for i in myfriends:
    print(myfriends)
#while loop
count=5
while(count>=0):
    print(count)
    count=count-1

#code to count the words and characters in a name
intostring = input("Enter your name")
character=0
word=1
for i in intostring:
    character=character+1
    if(i==' '):
        word=word+1
print(character)
print(word)