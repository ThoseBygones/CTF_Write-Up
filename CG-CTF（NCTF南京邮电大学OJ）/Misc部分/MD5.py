# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:40:04 2020

@author: Sherlock Holmes
"""

import hashlib

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

cipher = "TASC?O3RJMV?WDJKX?ZM"
text = "e9032???da???08????911513?0???a2"


length = len(cipher)

def check(string):
    text.lower()
    cnt = 0
    for i in range(0, len(text)):
        if text[i] != '?' and text[i] == string[i]:
            cnt += 1
    if cnt == 32 - 14:
        return True
    return False

def dfs(pos, guess):
    if pos == length:
        #print(guess)
        result = hashlib.md5(guess.encode(encoding='UTF-8')).hexdigest()
        #print(result)
        if check(result):
            print("flag: nctf{" + result + "}")
        return
    if cipher[pos] == '?':
        for c in alpha:
            guess += c
            dfs(pos + 1, guess)
            guess = guess[:-1]
    else:
        guess += cipher[pos]
        dfs(pos + 1, guess)

#print(length)
dfs(0, '')
print("Test over")