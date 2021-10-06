#tesserocr loop

import tesserocr
from PIL import Image
import cv2

import time

start = time.perf_counter()



write=[]

for i in range(0,50):      
    
    img=Image.open("output2/image/12/%d.png"%(i))
    
    #圖片轉文字
    write.append(tesserocr.image_to_text(img,lang='chi_tra'))
    
    #指定文字檔路徑
    i_str=str(i)
    filename='output2/text/12/'+i_str+'.txt'
    f = open(filename, 'w')
    
    f.write(write[i])
    
    f.close()
    
    

print("This time is being calculated")
end = time.perf_counter()
result=end - start
print(result,"sec")