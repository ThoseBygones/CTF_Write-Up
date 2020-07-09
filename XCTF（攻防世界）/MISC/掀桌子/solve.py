# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:06:56 2020

@author: ThoseBygones
"""

msg = "c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2"

for i in range(0, len(msg), 2):
    offset_val = int(msg[i] + msg[i+1], 16) & 127
    ch = chr(offset_val)
    print(ch, end="")
print("")
