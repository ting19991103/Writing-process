#2*2 merge image

import cv2
import numpy as np
import time

cameraCapture = cv2.VideoCapture('writingvideo2/recording.mp4')

#Declare variables

crop_img1=dict()
crop_img2=dict()
crop_img3=dict()
crop_img4=dict()
#merge
crop_imgs=dict()
crop_imgs1=dict()
crop_imgs2=dict()
current_time=dict()


def count_the_current_hours(cameraCapture):
        milliseconds = cameraCapture.get(cv2.CAP_PROP_POS_MSEC)
        seconds = milliseconds//1000
        milliseconds = milliseconds%1000
        minutes = 0
        hours = 0
        if seconds >= 60:
            minutes = seconds//60
            seconds = seconds % 60  
        if minutes >= 60:
            hours = minutes//60
            minutes = minutes % 60
        #print(int(hours), int(minutes), int(seconds), int(milliseconds))
        #show the current time
        current_hours=str(int(hours))
        return current_hours
def count_the_current_minutes(cameraCapture):
        milliseconds = cameraCapture.get(cv2.CAP_PROP_POS_MSEC)
        seconds = milliseconds//1000
        milliseconds = milliseconds%1000
        minutes = 0
        hours = 0
        if seconds >= 60:
            minutes = seconds//60
            seconds = seconds % 60  
        if minutes >= 60:
            hours = minutes//60
            minutes = minutes % 60
        #print(int(hours), int(minutes), int(seconds), int(milliseconds))
        #show the current time
        current_minutes=str(int(minutes))
        return current_minutes
def count_the_current_seconds(cameraCapture):
        milliseconds = cameraCapture.get(cv2.CAP_PROP_POS_MSEC)
        seconds = milliseconds//1000
        milliseconds = milliseconds%1000
        minutes = 0
        hours = 0
        if seconds >= 60:
            minutes = seconds//60
            seconds = seconds % 60  
        if minutes >= 60:
            hours = minutes//60
            minutes = minutes % 60
        #print(int(hours), int(minutes), int(seconds), int(milliseconds))
        #show the current time
        current_seconds=str(int(seconds))
        return current_seconds
def count_the_current_milliseconds(cameraCapture):
        milliseconds = cameraCapture.get(cv2.CAP_PROP_POS_MSEC)
        seconds = milliseconds//1000
        milliseconds = milliseconds%1000
        minutes = 0
        hours = 0
        if seconds >= 60:
            minutes = seconds//60
            seconds = seconds % 60  
        if minutes >= 60:
            hours = minutes//60
            minutes = minutes % 60
        #print(int(hours), int(minutes), int(seconds), int(milliseconds))
        #show the current time
        current_milliseconds=str(int(milliseconds))
        return current_milliseconds


counter=0
total=0
i=0
success,frame = cameraCapture.read()
while success:
    
    #等待期間有按鍵：返回按鍵的ASCII碼(ESC)
    if cv2.waitKey(1) == 27:  
            break
    #crop img
    x=500
    y=300
    w=900
    h=650
         
    font=cv2.FONT_HERSHEY_SIMPLEX
    current_hours = count_the_current_hours(cameraCapture)
    current_minutes = count_the_current_minutes(cameraCapture)
    current_seconds = count_the_current_seconds(cameraCapture)
    current_milliseconds = count_the_current_milliseconds(cameraCapture)
    
    new_counter=counter/22
    if(new_counter!=0 and new_counter%4==1):
        crop_img1=frame[y:y+h,x:x+w]
        crop_img1=cv2.putText(crop_img1,(current_hours+":"+current_minutes+":"+current_seconds+":"+current_milliseconds),(150,50),font,1.2,(0,0,0),2,cv2.LINE_AA)
    
    elif(new_counter!=0 and new_counter%4==2):
        crop_img2=frame[y:y+h,x:x+w]
        crop_img2=cv2.putText(crop_img2,(current_hours+":"+current_minutes+":"+current_seconds+":"+current_milliseconds),(150,50),font,1.2,(0,0,0),2,cv2.LINE_AA)  
    
    elif(new_counter!=0 and new_counter%4==3):
        crop_img3=frame[y:y+h,x:x+w]
        crop_img3=cv2.putText(crop_img3,(current_hours+":"+current_minutes+":"+current_seconds+":"+current_milliseconds),(150,50),font,1.2,(0,0,0),2,cv2.LINE_AA)    
    
    elif(new_counter!=0 and new_counter%4==0):
        crop_img4=frame[y:y+h,x:x+w]
        crop_img4=cv2.putText(crop_img4,(current_hours+":"+current_minutes+":"+current_seconds+":"+current_milliseconds),(150,50),font,1.2,(0,0,0),2,cv2.LINE_AA)    
       
        
        #combine
        crop_imgs = np.hstack((crop_img1,crop_img2))
        crop_imgs1 = np.hstack((crop_img3,crop_img4))
        crop_imgs2 = np.vstack((crop_imgs,crop_imgs1))
        #resize the combine image
        crop_imgs2 = cv2.resize(crop_imgs2,(1200,650),interpolation = cv2.INTER_AREA)
        
        #show the frame
        cv2.imshow('camera', crop_imgs2)
        
        
        #write file
        i_str=str(i)
        filename='output2/image/2x2/'+i_str+'.png'
        cv2.imwrite(filename, crop_imgs2, [cv2.IMWRITE_JPEG_QUALITY, 90])
        i=i+1 
        
    counter=counter+1
    success, frame = cameraCapture.read()
    
    
    
cv2.destroyAllWindows()
cameraCapture.release()

  
    
    
    
    
    
    