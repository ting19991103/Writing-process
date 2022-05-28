import re
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="future-shuttle-323208-1e6aebdb018d.json"
# Imports the Google Cloud client library
from google.cloud import vision        
from PIL import Image
import cv2

L=[]
strText1=[]
k=0
minute=0
strText2=[]
strText3=[]
textsLength=[]



for i in range(0,20):      

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath("output2/image/demo/%d.png"%(i))

    # Loads the image into memory
    
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    i_str=str(i)
    filename='output2/text/test/'+i_str+'.txt'
    
    #labal the delay frame
    """
    #total number of words
    textsLength.append(len(texts))
    if (textsLength[i]==textsLength[i-1]):
        delay=delay+1
    else :
        delay=0
    if (delay>=3):
        
        #print("stay: ",delay,"second"," in ",i," txt")
         #text recognition
        for text in texts:        
            f.write('"{}"'.format(text.description)) 
        f.write('({} second stay)'.format(delay) )
                #vertices = (['({},{})'.format(vertex.x, vertex.y)
                             #for vertex in text.bounding_poly.vertices])
                #f.write('bounds: {}'.format(','.join(vertices)))
       # f.close()
    """
    
    
    
    strText1.append(str(texts[0].description))
    L.append(texts[-2].description)#句尾抓出來
    
    #只算中文長度
    Clen = len(re.findall(u'[\u4e00-\u9fff]', str(texts)))
    textsLength.append(Clen)
    
    #print(texts[1].description)#時間抓出來
    #print(strText1[i])
    #print(L[i])
    
    filename1='/home/lab/Chinese/output2/log.txt'
    f1 =open(filename1, 'a' ,encoding='utf-8')
    
    

    #first frame
    if i==0:
        f1.write("{}\n".format(strText1[i]))
        print(strText1[i])
    
    #other frame
    else:
        
        if(textsLength[i]==textsLength[i-1] and L[i-1]==L[i]):
            print(strText1[i],"=>No action")
          
        
        elif(textsLength[i]>textsLength[i-1] and L[i]!=L[i-1] or
             textsLength[i]<textsLength[i-1] and L[i]!=L[i-1]):
            print(strText1[i])
    
        
        elif(textsLength[i]>textsLength[i-1] and L[i]==L[i-1]):
            
            strText2 = [x for x in strText1[i] if x in strText1[i-1]]
            print ("相同的字:",strText2) 
            f1.write("{} {}\n".format("相同的字:",strText2))
            
            strText3 = [y for y in strText1[i] if not y in strText1[i-1]]
            print("新增的字:",strText3)
            f1.write("{} {}\n".format("新增的字:",strText3))
            
      
                   
        elif(textsLength[i]<textsLength[i-1] and L[i]==L[i-1]):
            
            strText2 = [x for x in strText1[i-1] if x in strText1[i]]
            print ("相同的字:",strText2) 
            f1.write("{} {}\n".format("相同的字:",strText2))
            
            strText3 = [y for y in strText1[i-1] if not y in strText1[i]]
            print("刪除的字:",strText3)
            f1.write("{} {}\n".format("刪除的字:",strText3))
                

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
f1.close()