#PIP AND CLASS IN PYTHON#

#Installation of PIP from link "https://bootstrap.pypa.io/get-pip.py"
#open Terminal and type the following code
#python get-pip.py
#pip --version
#pip install howdoi
# 1. howdoi write python function  
# #2.howdoi declare variables in python #
# 3. howdoi write class in python

#class in python

class car(object):
    def __init__(self,model,color,company,speed):
        self.model=model
        self.color=color
        self.company=company
        self.speed=speed
    def start(self):
        print("start")
    def stop(self):
        print("self")
    def accelarated(self):
        print("speed")   
        "accelarator function here...." 
    def gear(self,grear_type):
        print("good") 

audi=car("audi","red","Audi",20)
audi.start()
audi.gear(90)

#Sample class

class student(object):
    def __init__(self,name,age,grade,gender):
        self.name=name 
        self.age=age 
        self.grade=grade 
        self.gender = gender 
    def gradewithage(self,age,grade):
        if age<10:
            print("kindergarden")
        elif 12<age<15:
            print("Middle school")
        else:
            print("High school")

stu=student("pree",13,10,"female")
stu.gradewithage(stu.age,stu.grade)

        