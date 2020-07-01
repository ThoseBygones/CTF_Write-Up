# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:16:37 2020

@author: ThoseBygones
"""

msg = "cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}"

flag = ""

for i in range(3, len(msg), 5):
    flag += msg[i]
    
print(flag)