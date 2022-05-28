# -*- coding: utf-8 -*-

import re

s = '你好 hello, world,今天星期三'

# First find all 'normal' words and interpunction
# '[x21-x2f]' includes most interpunction, change it to ',' if you only need to match a comma
count = len(re.findall(u'[\u4e00-\u9fff]', s))

print (count)


"""
minute=0
s=0
for i in range (0,130):
        s=s+1
        if s>=60:
            s=0
            minute=minute+1
            
        print(minute,":",s)
    
    """