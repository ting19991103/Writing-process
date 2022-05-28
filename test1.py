import io
import re
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
s=0

import openpyxl
from openpyxl import Workbook
# 用python建立一個Excel空白活頁簿
excel_file = Workbook()
# 建立一個工作中表
sheet = excel_file.active
# 先填入第一列的欄位名稱
sheet['A1'] = 'Action'
sheet['B1'] = 'Time'
sheet['C1'] = 'text before change'
sheet['D1'] = 'change texts'
sheet['E1'] = 'text after change'


for i in range(0,310):      

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
    Clen = len(re.findall(u'[\u4e00-\u9fff]', str(texts[0].description)))
    textsLength.append(Clen)
    
    #時間抓出來
    s=s+1
    if s>=60:
        s=0
        minute=minute+1
    #print(strText1[i])
    #print(L[i])
    
    filename1='/home/lab/Chinese/output2/log.txt'
    f1 =open(filename1, 'a' ,encoding='utf-8')
    

    #first frame
    if i==0:
        #f1.write("{}\n".format(strText1[i]))
        print(strText1[i])
    
    #other frame
    else:
        
       

        #elif
        if(textsLength[i]>textsLength[i-1] and L[i]==L[i-1]):
            
            strText2.append(str(texts[0].description))
            strText2=str(strText2)
            
            #新增的字詞抓出來
            strText3 = [y for y in str(strText1[i]) if not y 
                        in str(strText1[i-1])]
            
            print("新增:")
            columnA = '新增'
            #時間
            print(minute,":",s)
            columnB = str(str(minute)+":"+str(s))
            
            #新增字詞前的所有字 
            for element in strText3[0]:
                print(strText2[0:strText2.index(element)])
                columnC =strText2[0:strText2.index(element)]
            
            #新增的字詞抓出來
            print(strText3)
            columnD = str(strText3)
            
            #新增字詞後的所有字 
            for element in strText3[-1]:
                print(strText2[strText2.index(element)+1:
                               len(strText1)])
                columnE = strText2[strText2.index
                    (element)+1:len(strText1)]
            sheet.append([columnA, columnB, columnC, columnD,columnE])
                
            strText3=[]
            strText2=[]
            
      
                   
        elif(textsLength[i]<textsLength[i-1] and L[i]==L[i-1]):
            
            texts[0].description=strText1[i-1]
            strText2.append(str(texts[0].description))
            strText2=str(strText2)
            
            strText3 = [y for y in str(strText1[i-1]) if not y 
                        in str(strText1[i])]
            
            print("刪除:")
            columnA = '刪除'
            
            #時間抓出來
            print(minute,":",s)
            columnB = str(str(minute)+":"+str(s))
            
            #刪除字詞前的所有字 不包含時間
            for element in strText3[0]:
                print(strText2[0:strText2.index(element)])
                columnC = strText2[0:strText2.index(element)]
           
            #刪除的字詞抓出來
            print(strText3)
            columnD=str(strText3)
            
            #刪除字詞後的所有字 
            for element in strText3[-1]:
                print(strText2[strText2.index(element)+1:
                               len(strText1)])
                columnE=strText2[strText2.index(element)+1:
                               len(strText1)]
                    
            sheet.append([columnA, columnB, columnC, columnD,columnE])        
                    
            strText2=[]
            strText3=[]
                

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
        
        
excel_file.save('sample.xlsx')
f1.close()


