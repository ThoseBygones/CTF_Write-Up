# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 21:49:26 2020

@author: ThoseBygones
"""

with open("0da9641b7aad4efb8f7eb45f47eaebb2", "rb") as infile:
    data = infile.read()
    
rev_data = bytes.fromhex(data.hex()[::-1])

print(rev_data)

with open("reversed.jpg", "wb") as outfile:
    outfile.write(rev_data)
