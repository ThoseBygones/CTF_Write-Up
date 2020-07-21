# uncompyle6 version 3.7.2
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: test.py
# Compiled at: 2016-06-22 13:48:38


def flag():
    str = [
     65, 108, 112, 104, 97, 76, 97, 98]
    flag = ''
    for i in str:
        flag += chr(i)

    print(flag)
# okay decompiling test.pyc

flag()