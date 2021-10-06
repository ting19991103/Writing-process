#vision loop
import io
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="future-shuttle-323208-1e6aebdb018d.json"
# Imports the Google Cloud client library
from google.cloud import vision        
from PIL import Image
import cv2

import time

start = time.perf_counter()


for i in range(1,12):      

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath("output2/image/test3/%d.jpg"%(i))

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    i_str=str(i)
    filename='output2/text/test3/'+i_str+'.txt'
    
    #write file
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

    
print("This time is being calculated")
end = time.perf_counter()
result = end - start
print(result,"sec")
   
    
    