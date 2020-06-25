# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:28:49 2020

@author: ThoseBygones
"""

code = "666C61677B45333342374644384133423834314341393639394544444241323442363041417D"

flag = ""

for i in range(0, len(code)):
    if i % 2 == 0:
        tmpstr = code[i]
    else:
        tmpstr += code[i]
        flag += chr(int(tmpstr, 16))
        
print(flag)
