 
#引入模組
import os,sys

def mkdir():
    
    """
    path1 = '/home/lab/Chinese/output2/image/'   
    path2 = '/home/lab/Chinese/output2/text/'
    i=1
    for i in range(1,21):
        
        filename1=path1+str(i)
        filename2=path2+str(i)
        os.mkdir(filename1)
        os.mkdir(filename2)
        i=i+1
    """
    
    path = '/home/lab/Chinese/output2/text/'
    filename = path+"2x2"
    os.mkdir(filename)
    
    path = '/home/lab/Chinese/output2/image/'
    filename = path+"2x2"
    os.mkdir(filename)
    
    
    
mkdir()