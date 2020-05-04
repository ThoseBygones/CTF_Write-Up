# Write-Up（Misc部分）

## a_good_idea

+ 下载压缩包解压以后看到一张很普通的表情包：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/001.jpg)

+ 常规操作丢进 **WinHex** 里面查看代码：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/002.jpg)

+ 看到 **PK** 字段以及目录下的一个 **txt** 文件和两个 **png** 文件，就知道这个图片其实隐藏着一个压缩包。
+ 将后缀改为 **.zip** ，解压以后得到三个文件：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/003.jpg)

+ 解压，发现两个 **png** 文件是两个 ~~几乎一模一样~~ 的表情包；于是打开 **hint.txt** 看到提示：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/004.jpg)

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

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/a_good_idea/result.png)

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

