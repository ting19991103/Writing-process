#two image in a round

import cv2
import numpy as np
import time
start = time.perf_counter()

cameraCapture = cv2.VideoCapture('writingvideo2/recording.mp4')

# 從攝影機擷取一張影像
success, frame = cameraCapture.read() 

#Declare variables
crop_img=dict()
crop_img1=dict()
crop_imgs=dict()
current_time=dict()
i=0
timeF=22
timeF1=44
counter=1

while success:
    
    #等待期間有按鍵：返回按鍵的ASCII碼(ESC)
    if cv2.waitKey(1) == 27:  
        break
    
    #crop img
    x=500
    y=300
    w=900
    h=650
    """
    crop_img=frame[y:y+h,x:x+w]
    crop_img1=frame[y:y+h,x:x+w]
    """
    
    #(22*i)frame read
    if (counter%timeF == 0 and counter%timeF1 !=0):
        crop_img=frame[y:y+h,x:x+w]
        crop_img 
        
        
        
        #current time
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
        current_minutes=str(int(minutes))
        current_seconds=str(int(seconds))
        current_milliseconds=str(int(milliseconds))
        font=cv2.FONT_HERSHEY_SIMPLEX
        crop_img=cv2.putText(crop_img,(current_hours+":"+current_minutes+":"+current_seconds+":"+current_milliseconds),(150,50),font,1.2,(0,0,0),2,cv2.LINE_AA)
        
    
    #(44*i)frame read
    if(counter%timeF1==0):
        crop_img1=frame[y:y+h,x:x+w]
        crop_img1
        
        #current time
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
        current_minutes=str(int(minutes))
        current_seconds=str(int(seconds))
        current_milliseconds=str(int(milliseconds))
        font=cv2.FONT_HERSHEY_SIMPLEX
        crop_img1=cv2.putText(crop_img1,(current_hours+":"+current_minutes+":"+current_seconds+":"+current_milliseconds),(150,50),font,1.2,(0,0,0),2,cv2.LINE_AA)
        
        
        
        #combine
        crop_imgs = np.hstack((crop_img,crop_img1))
        #resize the combine image
        crop_imgs = cv2.resize(crop_imgs,(1200,650),interpolation = cv2.INTER_AREA)
        
        #show the frame
        cv2.imshow('camera', crop_imgs)
        
        
        
        
        #write file
        i_str=str(i)
        filename='output2/image/test2/'+i_str+'.png'
        cv2.imwrite(filename, crop_imgs, [cv2.IMWRITE_JPEG_QUALITY, 90])
        i=i+1
        
        
    counter=counter+1
    
    # 從攝影機擷取the next影像
    success, frame = cameraCapture.read()
    
    

cv2.destroyAllWindows()
cameraCapture.release()


import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="future-shuttle-323208-1e6aebdb018d.json"
# Imports the Google Cloud client library
from google.cloud import vision        
from PIL import Image
import cv2


for i in range(0,len(crop_imgs)):      

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath("output2/image/test2/%d.png"%(i))

    # Loads the image into memory
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    i_str=str(i)
    filename='output2/text/test2/'+i_str+'.txt'
    
    
    f = open(filename, 'w')    
    for text in texts:        
        f.write('\n"{}"'.format(text.description))  
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                     for vertex in text.bounding_poly.vertices])
        f.write('bounds: {}'.format(','.join(vertices)))
    f.close()
       

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


end = time.perf_counter()
result = end - start
print(result,"sec")