# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:29:44 2020

@author: ThoseBygones
"""

import binascii
import struct

crc_val = 0x932F8A6B

with open("error_pic.png", "rb") as file:
    data = file.read()

for width in range(0, 65535):
    tmp = data[12:16] + struct.pack('>i', width) + data[20:29]
    if (binascii.crc32(tmp) & 0xFFFFFFFF) == crc_val:
        print(hex(width))
        break

