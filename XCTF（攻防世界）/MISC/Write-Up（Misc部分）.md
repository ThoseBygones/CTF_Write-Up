# Write-Up（Misc部分）

## this is flag

+ 题目中直接给的 flag ，复制粘贴即可...
+ flag: **flag{th1s_!s_a_d4m0_4la9}**



## Test-flag-please-ignore

+ 下载附件压缩包并解压，发现一个无后缀的文件 **misc10** 。

+ 右键用 **Notepad++** 打开，发现文件里就一串字符串：

  > 666c61677b68656c6c6f5f776f726c647d

+ 看着像是十六进制数，猜测可能俩俩凑个对可以构成一个 ASCII 码对应的字符。

+ 于是写个简简单单的 Python 脚本 **trans.py** ：

```python
code = "666c61677b68656c6c6f5f776f726c647d"

flag = ""

for i in range(0, len(code)):
    if i % 2 == 0:
        tmpstr = code[i]
    else:
        tmpstr += code[i]
        flag += chr(int(tmpstr, 16))
        
print(flag)
```

+ 输出的内容即为 flag 。
+ flag: **flag{hello_world}**



## wireshark-1

+ 下载附件压缩包并解压，发现一个 **.pcap** 文件。
+ 果断上 **wireshark** ，查看数据包内容。
+ 大部分是 **TCP包**，也有部分的 **HTML包** 和 **DNS包**。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/1.png?raw=true)

+ 发现第二个 **HTML包** 的内容是一个 **php网站** 的登录操作，故右键选择 **追踪流** -> **TCP流**

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/2.png?raw=true)

+ 仔细查看流的内容即可发现其中隐藏着 flag ——登录的 **email** 字段值为 **flag** ，**password** 字段值即为我们要的 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/3.png?raw=true)

+ 也可以在弹出来的框底部的 **查找** 中直接查找字段 **flag** 。
+ flag: **flag{ffb7567a1d4f4abdffdb54e022f8facd}**



## pdf

+ 附件是一个 **pdf** 文件，打开就是一张图片，看起来没什么特别的。
+ 丢进 **WinHex** 里面查看，查找 **flag** 字符串，也没发现什么东西。
+ 放进 **Kali Linux** 里面尝试 `binwalk` 一下，也没发现什么隐藏着什么文件。
+ ![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/pdf/1.png?raw=true)
+ 于是找了个有编辑 pdf 功能的 pdf 阅读器（编辑器），试图把这张图片从 pdf 文件中抠下来。
+ 然后就神奇的发现，flag 就藏在图片后面，原来是被图片挡住了...
+ flag: **flag{security_through_obscurity}**



## 如来十三掌

+ 附件是一个 **docx** 文件，内容貌似是佛经之类的，看的我一脸懵逼...

  > 夜哆悉諳多苦奢陀奢諦冥神哆盧穆皤三侄三即諸諳即冥迦冥隸數顛耶迦奢若吉怯陀諳怖奢智侄諸若奢數菩奢集遠俱老竟寫明奢若梵等盧皤豆蒙密離怯婆皤礙他哆提哆多缽以南哆心曰姪罰蒙呐神。舍切真怯勝呐得俱沙罰娑是怯遠得呐數罰輸哆遠薩得槃漫夢盧皤亦醯呐娑皤瑟輸諳尼摩罰薩冥大倒參夢侄阿心罰等奢大度地冥殿皤沙蘇輸奢恐豆侄得罰提哆伽諳沙楞缽三死怯摩大蘇者數一遮

+ 百度一下 “如来十三掌” 是啥东西，发现是 **ROT13** 。

  > **ROT13**（**回转13位**）是一种简易的替换式密码。它是一种在英文网络论坛用作隐藏八卦、妙句、谜题解答以及某些脏话的工具，目的是逃过版主或管理员的匆匆一瞥。ROT13 被描述成 “杂志字谜上下颠倒解答的 Usenet 点对点体”。ROT13 也是过去在古罗马时代凯撒密码的一种变体。

+ 但是 ROT13 是用来处理英文字母的，不能直接处理中文字符，因此还需要先进行一步别的处理。

+ 然而 **rot13** 不是用来加解密中文的，因此还需要先进行一步别的解密。

+ 百度了半天与佛经加解密相关的东西，终于找到了这个网站 **[与佛论禅](http://www.keyfc.net/bbs/tools/tudoucode.aspx)**  。按照说明解密，得到一串字符串：

  > MzkuM3gvMUAwnzuvn3cgozMlMTuvqzAenJchMUAeqzWenzEmLJW9

+ 看着很像 **Base64 编码** ，用在线加解密工具试一下，却什么都没得到。

+ 想起 **rot13** ，也许应该先用 rot13 处理一下，**[在线 ROT13](https://rot13.com/)** 得到新的字符串如下：

  > ZmxhZ3tiZHNjamhia3ptbmZyZGhidmNraWpuZHNrdmJramRzYWJ9

+ 这会儿再**在线 Base64 解码**一下，得到 flag 。

+ flag: **flag{bdscjhbkzmnfrdhbvckijndskvbkjdsab}**



## a_good_idea

+ 下载压缩包解压以后看到一张很普通的表情包：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/001.jpg?raw=true)

+ 常规操作丢进 **WinHex** 里面查看代码：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/002.jpg?raw=true)

+ 看到 **PK** 字段以及目录下的一个 **txt** 文件和两个 **png** 文件，就知道这个图片其实隐藏着一个压缩包。
+ 将后缀改为 **.zip** ，解压以后得到三个文件：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/003.jpg?raw=true)

+ 解压，发现两个 **png** 文件是两个 ~~几乎一模一样~~ 的表情包；于是打开 **hint.txt** 看到提示：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/004.jpg?raw=true)

+ 猜测可能是要找两个几乎一模一样的图片不同的像素点？
+ 于是写 **Python** 脚本，用 **PIL** 库的 **Image** 来处理图片，代码如下：

```Python
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 11:26:00 2020

@author: Sherlock Holmes
"""

from PIL import Image

# 打开图像
img1 = Image.open("to.png")
img2 = Image.open("to_do.png")

# 读取图像
pic1 = img1.load()
pic2 = img2.load()

# 获取图像的宽和高
w, h = img1.size

# 新建一个图像
img = Image.new('RGB', (w, h))

# 读取这个新建的图像
pic = img.load()

# 比较两个表情包的每个像素点，不同的点在新图片的对应位置设置为黑色
for i in range(w):
    for j in range(h):
        if pic1[(i, j)] != pic2[(i, j)]:
            pic[(i, j)] = (255, 255, 255)
            
img.save("result.png")
```

+ 生成的图片是个二维码：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/result.png?raw=true)

+ 丢到在线二维码识别网站 https://cli.im/deqr/ 上识别，得到一个字符串就是flag。
+ flag: **NCTF{m1sc_1s_very_funny!!!}**



## 隐藏的信息

+ 下载压缩包解压以后看到一个文本文件 **message.txt** ，打开以后发现一串数字，有的数字之间有空格：

> 0126 062 0126 0163 0142 0103 0102 0153 0142 062 065 0154 0111 0121 0157 0113 0111 0105 0132 0163 0131 0127 0143 066 0111 0105 0154 0124 0121 060 0116 067 0124 0152 0102 0146 0115 0107 065 0154 0130 062 0116 0150 0142 0154 071 0172 0144 0104 0102 0167 0130 063 0153 0167 0144 0130 060 0113 

+ 仔细观察发现每个数字的大小不超过7，猜测可能是八进制数。
+ 于是写个 **Python** 脚本转换为 **ASCII码** ：

```Python
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 12:22:09 2020

@author: Sherlock Holmes
"""

text = "0126 062 0126 0163 0142 0103 0102 0153 0142 062 065 0154 0111 0121 0157 0113 0111 0105 0132 0163 0131 0127 0143 066 0111 0105 0154 0124 0121 060 0116 067 0124 0152 0102 0146 0115 0107 065 0154 0130 062 0116 0150 0142 0154 071 0172 0144 0104 0102 0167 0130 063 0153 0167 0144 0130 060 0113"

string = text.split(' ')

for s in string:
    print(chr(int(s, 8)), end = '')
```

+ 得到一串字符：

> V2VsbCBkb25lIQoKIEZsYWc6IElTQ0N7TjBfMG5lX2Nhbl9zdDBwX3kwdX0K

+ 猜测可能是Base64编码，立即推，丢到在线Base64编码解码网站 https://base64.us/ 处理，得到如下内容：

> Well done!
>
>  Flag: ISCC{N0_0ne_can_st0p_y0u}

+ flag: **ISCC{N0_0ne_can_st0p_y0u}**

