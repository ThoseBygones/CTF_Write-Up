# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:16:21 2020

@author: ThoseBygones
"""

code = "666c61677b68656c6c6f5f776f726c647d"

flag = ""

for i in range(0, len(code)):
    if i % 2 == 0:
        tmpstr = code[i]
    else:
        tmpstr += code[i]
        flag += chr(int(tmpstr, 16))
        
print(flag)