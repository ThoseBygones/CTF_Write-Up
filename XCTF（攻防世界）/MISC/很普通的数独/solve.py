# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:19:07 2020

@author: ThoseBygones
"""

from PIL import Image

(w, h) = (45, 45)

img = Image.new('RGB', (w, h))

pic = img.load()

with open('bits.txt', 'r') as file:
    for i in range(h):
        line = file.readline()
        for j in range(w):
            if line[j] == '1':
                pic[(i, j)] = (0, 0, 0)
            else:
                pic[(i, j)] = (255, 255, 255)
                
img.save('result.png')
