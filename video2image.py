#a image in a round

import cv2
import time
#start = time.perf_counter()

cameraCapture = cv2.VideoCapture('demoVideo/0225金喜淑.mp4')
# 從攝影機擷取一張影像
success, frame = cameraCapture.read() 

#Declare variables
crop_img=dict()
current_time=dict()
i=0
timeF=30 #30
counter=1.0

while success:
    
    #等待期間有按鍵：返回按鍵的ASCII碼(ESC)
    if cv2.waitKey(1) == 27:  
        break
    
    #crop img
    x=500 #500
    y=250 #300
    w=900
    h=780
    crop_img=frame[y:y+h,x:x+w]
    
    
    if (counter%timeF == 0):
        
        
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
        crop_img=cv2.putText(crop_img,(current_hours+":"+current_minutes+":"+current_seconds+":"+current_milliseconds),(50,28),font,0.8,(0,0,0),2,cv2.LINE_AA)
        
        #show the frame
        cv2.imshow('camera', crop_img)
        
        
        #write file
        i_str=str(i)
        filename='output2/image/demo/'+i_str+'.png'
        cv2.imwrite(filename, crop_img, [cv2.IMWRITE_JPEG_QUALITY, 90])
        i=i+1
        
    counter=counter+1.0
    # 從攝影機擷取the next影像
    success, frame = cameraCapture.read()

print(i)

cv2.destroyAllWindows()
cameraCapture.release()


"""
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="future-shuttle-323208-1e6aebdb018d.json"
# Imports the Google Cloud client library
from google.cloud import vision        
from PIL import Image
import cv2


for i in range(0,(len(crop_img)-1)):      

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath("output2/image/test/%d.png"%(i))

    # Loads the image into memory
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    i_str=str(i)
    filename='output2/text/test/'+i_str+'.txt'
    
    
    f = open(filename, 'w')    
    for text in texts:    
        print('\n"{}"'.format(text.description))
        
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
"""

    

    

   
    
        

    

   
    
    


    

   
    
    
    

    
    



    
    


    
    













       






