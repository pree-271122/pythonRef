#WEB CAMERA SECURITY#

#pip install openCV-python

#Capture image
from os import access
import cv2

def vedioCapture():
    cap=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=cap.read()
        print(ret)
        cv2.imwrite("preethi.jpg",frame)
        result=False
    
    cap.release()
    cv2.destroyAllWindows()

vedioCapture()

#Capture image and store it in dropbox
import cv2
import dropbox
import time
import random

starttime=time.time()
def vedioCapture():
    rand=random.randint(0,100)
    cap=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=cap.read()
        print(ret)
        imgname="pree"+str(rand)+".jpg"
        cv2.imwrite(imgname,frame)
        starttime=time.time
        result=False
    return imgname

    print("sanptaken")
    cap.release()
    cv2.destroyAllWindows()

def upload(imgname):
    access="sl.BCySXyefvQlz8SbjNgPjRIR_anbPPWVRWdnBSDB1_AtMx-LzJCHAb7udfZeOrnx_HFhvVvYCeztUng7ANJNK1I7tWRpcSLihkf5lYwq9jcLduLofqkMf4oMVyYLXZrqtp6BVu1c3rzp6"
    file=imgname
    fromfile=file
    tofile=input("enter the path: ")
    dbx=dropbox.Dropbox(access)

    f= open(fromfile,'rb')
    dbx.files_upload(f.read(),tofile)
    print("uploaded")

def main():
    while(True):
        if ((time.time()-starttime) >=5):
            name=vedioCapture()
            upload(name)

main()

