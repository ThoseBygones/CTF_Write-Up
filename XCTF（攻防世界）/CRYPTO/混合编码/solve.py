# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:44:31 2020

@author: ThoseBygones
"""

msg = "119/101/108/99/111/109/101/116/111/97/116/116/97/99/107/97/110/100/100/101/102/101/110/99/101/119/111/114/108/100/"

flag = "cyberpeace{"

tmp = ""

for ch in msg:
    if ch != '/':
        tmp += ch
    else:
        #print(tmp)
        flag += chr(int(tmp))
        tmp = ""
        
flag += "}"
print(flag)
