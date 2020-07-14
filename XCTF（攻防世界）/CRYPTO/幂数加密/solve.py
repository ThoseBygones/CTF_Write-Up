# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:17:48 2020

@author: ThoseBygones
"""

msg = "8842101220480224404014224202480122"

flag = "cyberpeace{"

tmp = 0

for ch in msg:
    if ch != '0':
        tmp += int(ch)
    else:
        #print(tmp)
        tmp += ord('A')
        flag += chr(tmp - 1)
        tmp = 0
        
tmp += ord('A')
flag += chr(tmp - 1)

flag += "}"
print(flag)
