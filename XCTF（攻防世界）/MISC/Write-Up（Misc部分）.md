# Write-Up（Misc部分）

## this is flag

+ 题目中直接给的 flag ，复制粘贴即可...
+ flag: **flag{th1s_!s_a_d4m0_4la9}**



## pdf

+ 附件是一个 ***.pdf*** 文件，打开就是一张图片，看起来没什么特别的。
+ 丢进 **WinHex** 里面查看，查找 **flag** 字符串，也没发现什么东西。
+ 放进 **Kali Linux** 里面尝试 `binwalk` 一下，也没发现什么隐藏着什么文件。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/pdf/1.png?raw=true)

+ 于是找了个有编辑 pdf 功能的 pdf 阅读器（编辑器），试图把这张图片从 pdf 文件中抠下来。
+ 然后就神奇的发现，flag 就藏在图片后面，原来是被图片挡住了...
+ flag: **flag{security_through_obscurity}**



## 如来十三掌

+ 附件是一个 ***.docx*** 文件，内容貌似是佛经之类的，看的我一脸懵逼...

  > 夜哆悉諳多苦奢陀奢諦冥神哆盧穆皤三侄三即諸諳即冥迦冥隸數顛耶迦奢若吉怯陀諳怖奢智侄諸若奢數菩奢集遠俱老竟寫明奢若梵等盧皤豆蒙密離怯婆皤礙他哆提哆多缽以南哆心曰姪罰蒙呐神。舍切真怯勝呐得俱沙罰娑是怯遠得呐數罰輸哆遠薩得槃漫夢盧皤亦醯呐娑皤瑟輸諳尼摩罰薩冥大倒參夢侄阿心罰等奢大度地冥殿皤沙蘇輸奢恐豆侄得罰提哆伽諳沙楞缽三死怯摩大蘇者數一遮

+ 百度一下 “如来十三掌” 是啥东西，发现是 **ROT13** 。

  > **ROT13**（**回转13位**）是一种简易的替换式密码。它是一种在英文网络论坛用作隐藏八卦、妙句、谜题解答以及某些脏话的工具，目的是逃过版主或管理员的匆匆一瞥。ROT13 被描述成 “杂志字谜上下颠倒解答的 Usenet 点对点体”。ROT13 也是过去在古罗马时代凯撒密码的一种变体。

+ 但是 ROT13 是用来处理英文字母的，不能直接处理中文字符，因此还需要先进行一步别的处理。

+ 然而 rot13 不是用来加解密中文的，因此还需要先进行一步别的解密。

+ 百度了半天与佛经加解密相关的东西，终于找到了这个网站 **[与佛论禅](http://www.keyfc.net/bbs/tools/tudoucode.aspx)**  。按照说明解密，得到一串字符串：

  > MzkuM3gvMUAwnzuvn3cgozMlMTuvqzAenJchMUAeqzWenzEmLJW9

+ 看着很像 **Base64 编码** ，用在线加解密工具试一下，却什么都没得到。

+ 想起 **rot13** ，也许应该先用 rot13 处理一下，**[在线 ROT13](https://rot13.com/)** 得到新的字符串如下：

  > ZmxhZ3tiZHNjamhia3ptbmZyZGhidmNraWpuZHNrdmJramRzYWJ9

+ 这会儿再 **[在线 Base64 解码](https://base64.us/)** 一下，得到 flag 。

+ flag: **flag{bdscjhbkzmnfrdhbvckijndskvbkjdsab}**



## 掀桌子

+ 题目中给了密文：

  > c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2

+ 仔细观察发现每个字符像是十六进制数，直接拿去解密并不能得到说明有用的信息，于是考虑每两个一组然后转化为 ASCII 码字符。转换后发现全是一些扩展 ASCII 码的字符，显示出来的结果乱七八糟——因为每两个字符一组构成的十六进制字符转换为十进制后值均大于 128 。

+ 于是考虑把最高位的 1 给屏蔽掉（毕竟 ASCII 码实际上只有 7 位有效），于是写个简简单单的脚本即可得到明文：

  > Hi, FreshDog! The flag is: hjzcydjzbjdcjkzkcugisdchjyjsbdfr

```python
msg = "c8e9aca0c6f2e5f3e8c4efe7a1a0d4e8e5a0e6ece1e7a0e9f3baa0e8eafae3f9e4eafae2eae4e3eaebfaebe3f5e7e9f3e4e3e8eaf9eaf3e2e4e6f2"

for i in range(0, len(msg), 2):
    offset_val = int(msg[i] + msg[i+1], 16) & 127
    ch = chr(offset_val)
    print(ch, end="")

print("")
```

+ **这题的坑点是，flag 的形式不是 ddctf{xxx...xxx}，也不是DDCF{xxx...xxx}，同样也不是直接提交那一串字符串。flag 的形式是 flag{xxx...xxx}，然而题目中并没有说明orz...**
+ flag: **flag{hjzcydjzbjdcjkzkcugisdchjyjsbdfr}**



## give_you_flag

+ 下载附件，是一个 ***.gif*** 文件。
+ 打开看到就是一只很萌的小龙在数钱，但是看完完整的内容会发现，动图的最后几帧似乎有一个小小的类似二维码的东西一闪而过。
+ 于是使用 **Stegsolve** 打开，然后使用 **Frame Browser** 功能找到有二维码的那一帧并保存下来。
+ 保存下来打开后发现，这个 “二维码” 并不完整，左上角、左下角、右上角一共三个定位点都缺失，而且图片中的二维码比较小，所以直接扫码识别是无法识别出来的，需要用图片处理软件处理一下：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/give_you_flag/give_you_flag.png?raw=true)

+ 于是 P 图开始了，直接用画图就可以搞定了：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/give_you_flag/QRCode.png?raw=true)

+ P 完后可以使用微信扫一扫或者使用 **[在线二维码解码器](https://jiema.wwei.cn/)** 或者 **[草料二维码解码器](https://cli.im/deqr/)** 在线解码，即可得到 flag。
+ flag: **flag{e7d478cf6b915f50ab1277f78502a2c5}**



## 坚持60s

+ 下载附件，发现是一个 ***.jar*** 文件。
+ 在安装了 Java 的环境下打开，发现是一个~~有趣~~（智障）的小游戏，键盘的 “上下左右” 键操作一个图片躲避一堆满屏幕乱跑（而且越跑越快）的 “绿帽子” 图片。
+ 经过多次失败的尝试以后发现，把图片移动到屏幕的**右上角**或者**右下角**但是不要移除屏幕可视范围（否则就移不回来了）即可：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E5%9D%9A%E6%8C%8160s/1.png?raw=true)

+ 60 秒以后再移动出来 “自杀” ，即可在屏幕上看到一串类似 flag 的字符串：

  > flag{RGFqaURhbGlfSmlud2FuQ2hpamk=}

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E5%9D%9A%E6%8C%8160s/2.png?raw=true)

+ **这里有个坑点是，貌似坚持了太久反而不显示 flag 字符串，所以坚持 60 秒多一点就可以马上出来自杀了。**
+ 然而把这串类似 flag 的字符串提交上去并不能通过，说明这并不是最终的 flag 。注意到这串字符串花括号内的部分似乎是 **Base 64 编码** 过的，因此使用 **[Base64 在线编码解码](https://base64.us/)** 网站在线解码，成功得到 flag 。
+ flag: **flag{DajiDali_JinwanChiji}**



## gif

+ 下载压缩包，发现压缩包内有两个文件夹，其中文件夹里面有 104 张图片；解压后发现这些图片要么全黑要么全白...

+ 猜测全白和全黑的图片可能分别代表二进制的 0 和 1 ，但是需要分组。由于 ASCII 码是通过 8 个二进制位表示的，且 104 能被 8 整除，因此每八个二进制位一组，得到如下字符串：

  > 01100110
  > 01101100
  > 01100001
  > 01100111
  > 01111011
  > 01000110
  > 01110101
  > 01001110
  > 01011111
  > 01100111
  > 01101001
  > 01000110
  > 01111101

+ 利用得到的字符串，写个简简单单的 Python 脚本（***solve.py***）转换一下即可得到 flag 。

```python
val = ["01100110", 
       "01101100", 
       "01100001", 
       "01100111", 
       "01111011", 
       "01000110", 
       "01110101", 
       "01001110", 
       "01011111", 
       "01100111", 
       "01101001", 
       "01000110", 
       "01111101"
       ]

for i in val:
    print(chr(int(i, 2)), end="")
print("")
```

+ flag: **flag{FuN_giF}**



## ext3

+ 下载附件，发现一个无后缀的文件。

+ 根据题目的提示 “一个linux系统光盘” ，猜想可能需要使用 Linux 挂载光盘，于是创建文件夹 `/xctf` ，然后使用光盘挂载命令 `mount f1fc23f5c743425d9e0073887c846d23 xctf/` 。

+ 在挂载点所在的文件夹里发现许多文件夹，一下子无法找到 flag ，于是使用 `find ./ -name flag*` 查找当前目录下文件名中含有 “flag” 的目录或者文件，很顺利的找到了 `./O7avZhikgKgbF/flag.txt` 。

+ 直接打开这个文本文件，发现一串字符串：

  > ZmxhZ3tzYWpiY2lienNrampjbmJoc2J2Y2pianN6Y3N6Ymt6an0=

+ 看起来很像是 **Base 64** 编码过的，于是使用 **[Base64 在线编码解码](https://base64.us/)** 网站在线解码，成功得到 flag 。

+ flag: **flag{sajbcibzskjjcnbhsbvcjbjszcszbkzj}**



## base64÷4

+ 下载附件压缩包并解压，发现一个后缀为 ***.txt*** 的文件。

+ 打开看到一串字符串：

  > 666C61677B45333342374644384133423834314341393639394544444241323442363041417D

+ 看起来很像是十六进制数，而且题目的名字就是 “base64÷4”，因此猜测可能俩俩凑个对可以构成一个 ASCII 码对应的字符。

+ 于是写个简简单单的 Python 脚本（***trans.py***） ：

```python
code = "666C61677B45333342374644384133423834314341393639394544444241323442363041417D"

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
+ flag: **flag{E33B7FD8A3B841CA9699EDDBA24B60AA}**



## wireshark-1

+ 下载附件压缩包并解压，发现一个 ***.pcap*** 文件。
+ 果断上 **wireshark** ，查看拦截到的数据包。
+ 大部分是 **TCP包**，也有部分的 **HTML包** 和 **DNS包**。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/1.png?raw=true)

+ 发现第二个 **HTML包** 的内容是一个 **php网站** 的登录操作，故右键选择 **追踪流** -> **TCP流**

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/2.png?raw=true)

+ 仔细查看流的内容即可发现其中隐藏着 flag ——登录的 **email** 字段值为 **flag** ，**password** 字段值即为我们要的 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/3.png?raw=true)

+ 也可以在弹出来的框底部的 **查找** 中直接查找字段 **flag** 。
+ flag: **flag{ffb7567a1d4f4abdffdb54e022f8facd}**



## János-the-Ripper

+ 下载附件压缩包并解压，发现一个无后缀的文件。
+ 果断丢进 **WinHex** 里面查看，发现文件头出现 **PK** 字段，说明这是个 ***.zip*** 压缩包文件。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/J%C3%A1nos-the-Ripper/1.png?raw=true)

+ 将文件后缀改为 ***.zip*** ，然后解压缩，解压缩的时候发现需要密码，题目却并没有给任何提示...
+ 于是使用工具 **ARCHPR** 尝试爆破口令，勾上 “所有大写拉丁文(A - Z)” ， “所有小写拉丁文(a - z)” 和 “所有数字(0 - 9)” 三个勾选框，长度先设为 4 ，开始爆破... 瞬间得到密码 “**fish**” ：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/J%C3%A1nos-the-Ripper/2.png?raw=true)

+  用该密码解压 **flag.txt** 后打开即可看到 flag 。
+ flag: **flag{ev3n::y0u::bru7us?!}**



## Test-flag-please-ignore

+ 下载附件压缩包并解压，发现一个无后缀的文件。

+ 右键用 **Notepad++** 打开，发现文件里就一串字符串：

  > 666c61677b68656c6c6f5f776f726c647d

+ 看着像是十六进制数，猜测可能俩俩凑个对可以构成一个 ASCII 码对应的字符。

+ 于是写个简简单单的 Python 脚本（***trans.py***） ：

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



## Banmabanma

+ 下载附件压缩包并解压，发现一个 ***.png*** 文件。

+ 打开图片，发现图片里是一只斑马，但是背上的斑纹挺奇怪的，看起来像个条形码XD

+ 于是到处去找在线条形码识别网站，百度无果（没有能成功识别的），最终谷歌找到一个在线识别条形码的靠谱网站 搜索结果 **[Barcode Reader. Free Online Web Application](https://online-barcode-reader.inliteresearch.com/)** 。

+ 识别结果如下：

  > FLAG IS TENSHINE

+ flag: **flag{TENSHINE}**



## Hear-with-your-Eyes

+ 下载附件，发现一个没有后缀的文件。
+ 丢到 **WinHex** 里发现很大，也没看出什么名堂来，于是放进 **Kali Linux** 中，发现系统显示该文件为 **Gzip archive (application/gzip)，即压缩包文件**。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Hear-with-your-Eyes/1.png?raw=true)

+ 修改后缀为 ***.zip*** 并解压缩，发现一个 ***sound.wav*** 文件，打开播放，发现是一段长度为 10 秒的鬼畜音频（不能算音乐吧）...
+ 题目提示 “用眼睛听这段音频” ，猜想需要搞个音频处理软件啥的来看看这段音频有没有藏着什么东西，于是用 **Audacity** 打开音乐文件。
+ 默认显示的是这段音频的**波形**，波形没有什么特别的，于是切换到**频谱图**，然后就看到了用频谱硬生生 “画” 出来的 flag 字符串...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Hear-with-your-Eyes/2.png?raw=true)

+ flag: **e5353bb7b57578bd4da1c898a8e2d767**



## What-is-this

+ 下载附件压缩包并解压，发现一个没有后缀的文件。
+ 丢进 WinHex 查看内容，并没有发现有什么文件类型标志。
+ 于是打开 Kali Linux 系统，把文件复制进去 `binwalk` 一下。这个没有后缀的文件在 Linux 文件系统下显示的是 **Gzip archive (application/gzip)** ，猜测是个压缩包，`binwalk` 的结果也证实了这一点：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/What-is-this/1.png?raw=true)

+ 于是将文件的后缀改为 ***.zip*** ，解压缩得到两张图片 ***pic1.jpg*** 和 ***pic2.jpg*** 。两张图片看起来十分像，都是杂乱的分布着黑白像素点。猜测可能 **combine** 一下也许会变出个二维码什么的，于是使用工具 **Stegsolve** 中的 **Image Combiner** 功能把两张图合成一下。
+ 合成的图片中并没有二维码，却是一个字符串 “**AZADI TOWER**” ，即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/What-is-this/2.png?raw=true)

+ flag: **AZADI TOWER**



## embarrass

+ 下载附件压缩包并解压，发现一个 ***.pcap*** 文件。
+ 果断上 **wireshark** ，查看内容，发现拦截到的数据包种类非常多，大部分是 **TCP 包**，还有少量的 **HTTP 包**、**FTP-DATA 包**等等。内容太多不知道从哪来开始找 flag ，于是考虑在 Kali Linux 系统下 `binwalk` 或者利用 `foremost` 找，找到各种 xml 文档，htm/html 页面以及少量的 doc 文件甚至一个 jpg 文件（打开发现还是张有问题的图片），但是没有什么有用的内容。
+ 无奈之下回归 wireshark ，开始追踪流。首先**对 HTTP 包追踪 HTTP 流**，然后在弹出的窗口底部查找 “flag” 字符串，但一无所获。
+ 注意到 **FTP-DATA 包**，于是尝试**追踪 TCP 流**，并在弹出的窗口底部查找 “flag” 字符串，成功搜索到 flag ：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/embarrass/1.png?raw=true)

+ 另解，还可以通过 Linux 下的 `strings` 来查找文件里的字符串数据：

  > <code>strings misc_02.pcapng | grep flag</code>

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/embarrass/2.png?raw=true)

+ 因此同样可以把数据包丢进 **WinHex** 内然后查找 flag 字段...
+ flag: **flag{Good_b0y_W3ll_Done}**



## 神奇的Modbus

+ 下载附件压缩包并解压，发现一个 ***.pcap*** 文件。

+ 用 **wireshark** 打开，发现数据包类型很杂。由于题目是 “神奇的Modbus” ，因此特别关注 **Modbus/TCP** 包。

  > + Modbus 协议是应用于电子控制器上的一种通用语言。通过此协议，控制器相互之间、控制器经由网络（例如以太网）和其它设备之间可以通信。它已经成为一通用工业标准。有了它，不同厂商生产的控制设备可以连成工业网络，进行集中监控。
  >
  > + 此协议定义了一个控制器能认识使用的消息结构，而不管它们是经过何种网络进行通信的。它描述了一控制器请求访问其它设备的过程，如果回应来自其它设备的请求，以及怎样侦测错误并记录。它制定了消息域格局和内容的公共格式。 

+ 在过滤器中筛选出 Modbus/TCP 数据包，右键 -> **追踪流** -> **TCP流** ，发现新窗口中显示出一些奇奇怪怪的内容：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E7%A5%9E%E5%A5%87%E7%9A%84Modbus/1.png?raw=true)

+ 粗略查看发现一些类似 flag 形式的字段（字符之间用空格隔开了），由于混着客户端分组和服务器分组，因此在窗口的底部选择 **192.168.120.120:052 -> 192.168.130.1:62234 (34KB)** （即服务器向客户端发送的分组），查看筛选后的数据后，可以看到如下一段类似 flag 的字段：

  > s.c.t.f.{.E.a.s.y._.M.d.b.u.s.}


![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E7%A5%9E%E5%A5%87%E7%9A%84Modbus/2.png?raw=true)

+ 去掉其中的 '.' 提交，发现不对，猜测可能出题者故意漏掉了 Modbus 中的字母 'o' ，补上提交即可通过。

+ flag: **sctf{Easy_Modbus}**



## MISCall

+ 下载附件，发现又是一个没有后缀的文件...
+ 用 **WinHex** 打开，发现文件开头出现字段 `BZh91AY&SY` ，百度得知这是 ***.bz2*** 文件的文件头，于是打开 **Kali Linux** 在终端用 `tar -jxvf` 命令解压文件。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/1.png?raw=true)

+ 仔细查看解压的详细过程，发现解压得到的文件像是某个项目或者 repo 的 **git 目录** 。其中有个 ***flag.txt*** 文件没有被隐藏，打开后却只看到一行字：

  > Nothing to see here, moving along...

+ 查看其它被隐藏的 ***.git*** **文件夹**中的文件，没看出什么东西，于是百度 git 命令，在终端对该文件夹进行操作。

+ 首先是用 `git log`  和 `git log all` 命令查看版本演变历史和所有分支的历史：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/2.png?raw=true)

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/3.png?raw=true)

+ 发现有演变历史，显示最近有上传一个文件夹，但是目录中并不存在，于是再用 `git stash list` 命令查看当前 stash 中内容的列表：

  > `git stash` 能够将所有未提交的修改（工作区和暂存区）保存至堆栈中，用于后续恢复当前工作目录。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/4.png?raw=true)

+ 发现列表里是有东西的，于是进一步使用 `git stash show` 命令查看堆栈中最新保存的stash和当前目录的差异，发现 stash 中有个 ***s.py*** 文件，还有个 ***flag.txt*** 文件：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/5.png?raw=true)

+ 于是用 `git stash apply` 命令将堆栈中的内容应用到当前目录，即可在目录中看到 ***s.py*** 文件和**新的** ***flag.txt*** 文件：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/6.png?raw=true)

+ 打开 flag.txt 文件，发现一大段内容，像是一封电子邮件...

  > From: mailto: torvalds@klaava.Helsinki.Fi (Linus Benedict Torvalds)
  > To: Newsgroups: comp.os.inix
  > Subject: What would you like to see most in minix?
  > Summary: small poll for my new operating system
  > Message-ID: <mailto: 1991Aug25.205708.9541@klaava.Helsinki.Fi
  >
  > Hello everybody out there using minix — I’m doing a (free) operating
  > system (just a hobby, won’t be big and professional like gnu) for 386
  > (486) AT clones. This has been brewing since april, and is starting to
  > get ready. I’d like any feedback on things people like/dislike in
  > minix, as my OS resembles it somewhat (same physical layout of the
  > file-system (due to practical reasons) among other things).
  >
  > I’ve currently ported bash (1.08) and gcc (1.40), and things seem to
  > work. This implies that I’ll get something practical within a few
  > months, and I’d like to know what features most people would want. Any
  > suggestions are welcome, but I won’t promise I’ll implement them :-).
  >
  > Linus (mailto: torvalds@klaava.helsinki.fi)
  >
  > PS. Yes — it’s free of any minix code, and it has a multi-threaded fs.
  > It is NOT protable (uses 386 task switching etc), and it probably
  > never will support anything other than AT-harddisks, as that’s all I
  > have :-(.

+ 而 ***s.py*** 文件看起来则像是处理 ***flag.txt*** 文件的：

```python
#!/usr/bin/env python
from hashlib import sha1
with open("flag.txt", "rb") as fd:
    print "NCN" + sha1(fd.read()).hexdigest()
```

+ 于是在终端输入 `python s.py` 命令，得到一串字符串，即为 flag 。
+ flag: **NCN4dd992213ae6b76f27d7340f0dde1222888df4d3**



## flag_universe

+ 下载附件，解压后得到一个 ***.pcapng*** 文件。
+ 用 **Wireshark** 打开，分析其中数据包的类型，发现主要为 **TCP 包**，**FTP包**，**FTP-DATA包** 等。观察 **FTP-DATA包**，发现客户和服务器之间的数据交换包括图片文件 ***universe.png*** ，***new_universe.png*** 以及文本文件 ***flag.txt*** 文件。于是打开 **Kali Linux**  使用 `binwalk` 查看一下，发现几个 **PNG image** ：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/flag_universe/1.png?raw=true)

+ 尝试使用 `foremost` 的命令提取，但不成功。于是回到 Wireshark ，观察 FTP-DATA 数据包的命令及内容。发现图片文件 ***universe.png*** 的命令是 **RETR（获取文件）**，***new_universe.png*** 的命令是 **STOR（存储文件）**，而 ***flag.txt*** 则是两种命令都有。于是首先对 **RETR /flag.txt** 进行操作 **追踪流 -> TCP流** ，在弹出的窗口中看到一串字符串，非常像 Base 64 编码后的内容：

  > ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9

+ 于是使用 **[Base64 在线编码解码](https://base64.us/)** 网站在线解码，得到 flag 如下：

  > flag{This is fake flag hahaha}

+ 提交上去果然是假的，于是尝试对 **STOR /flag.txt** 进行操作 **追踪流 -> TCP流** ，在弹出的窗口中看到一大段字符串，也很像 Base 64 编码后的内容：

  > ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9ZmxhZ3tUaGlzIGlzIGZha2UgZmxhZyBoYWhhaGF9

+ 于是使用 **[Base64 在线编码解码](https://base64.us/)** 网站在线解码，得到 flag 如下：

  > flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}flag{This is fake flag hahaha}

+ 还是没得到正确的 flag 。猜测可能真正的 flag 藏在别的地方，于是考虑序号靠前的涉及图片获取和操作的数据包。通过追踪 TCP 流发现，从服务器获取图片次数很多，但上传图片（将图片存储到服务器上）的操作只有一次，猜想这次上传的图片可能有东西，于是对 **STOR /new_universe.png** 进行操作 **追踪流 -> TCP流** ，在弹出的窗口中看到该图片的整个文件数据，于是在窗口底部将 “显示和保存数据为” 的默认值 “ASCII” 改为 **“原始数据”** ：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/flag_universe/2.png?raw=true)

+ 然后另存为保存为 ***new_universe.png*** 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/flag_universe/new_universe.png?raw=true)

+ 然后首先用 **Stegsolve** 打开，遍历各个 **Plane** 检查是否有隐藏内容。没有发现任何结果，于是打开 **Kali Linux** ，使用命令 `zsteg new_universe.png` 来查看隐藏信息，成功得到 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/flag_universe/3.png?raw=true)

+ flag: **flag{Plate_err_klaus_Mail_Life}**



## Reverse-it

+ 下载附件，发现是一个无后缀的文件。

+ 打开 **Kali Linux** ，使用 `binwalk` 处理一下，但是并没有发现文件隐藏着什么东西。

+ 于是使用 **WinHex** 打开，但仔细查看整个文件也没发现有什么有价值的数据。

+ 这是想到题目是 “Reverse-it” ，考虑可能要把文件内容反向一下。于是写了个 Python 脚本直接读取文件的字节流后，以字节为单位把整个文件的数据反向后写入新的文件。但是发现这样输出的文件文件头为：

  > FF8DFF0E......

+ 百度一下并没有发现哪种常见的文件格式文件头是这样的，但是发现 **JPEG (jpg)** 格式的文件文件头是：

  > FFD8FF

+ **常见文件文件头：**

  > + JPEG (jpg)，文件头：FFD8FF
  > + PNG (png)，文件头：89504E47
  > + GIF (gif)，文件头：47494638
  > + TIFF (tif)，文件头：49492A00
  > + Windows Bitmap (bmp)，文件头：424D
  > + XML (xml)，文件头：3C3F786D6C
  > + HTML (html)，文件头：68746D6C3E
  > + MS Word/Excel (xls.or.doc)，文件头：D0CF11E0
  > + MS Access (mdb)，文件头：5374616E64617264204A
  > + Adobe Acrobat (pdf)，文件头：255044462D312E
  > + ZIP Archive (zip)，文件头：504B0304
  > + RAR Archive (rar)，文件头：52617221
  > + Wave (wav)，文件头：57415645
  > + AVI (avi)，文件头：41564920
  > + Real Audio (ram)，文件头：2E7261FD
  > + Real Media (rm)，文件头：2E524D46
  > + MPEG (mpg)，文件头：000001BA
  > + MPEG (mpg)，文件头：000001B3
  > + Quicktime (mov)，文件头：6D6F6F76
  > + Windows Media (asf)，文件头：3026B2758E66CF11
  > + MIDI (mid)，文件头：4D546864
  >
  > 参考链接：[**常见文件文件头 - eWFuZw==的博客 - CSDN博客**](http://www.baidu.com/link?url=SUE6EFxeJZvkqFifI9mu_G2OqKDetxXjPTb96LX3KZb3ThIBa0VcIg4Rl06fnIPHog8jRn89A5tQ3k2NmEHWg4kT9GG-g9fW0AqJuwZgdQC&wd=&eqid=f3b096d70012a586000000065f09c518)

+ 于是修改 Python 脚本，以字为单位把整个文件的数据反向后写入新的文件（***reverse.py***）：

```python
with open("0da9641b7aad4efb8f7eb45f47eaebb2", "rb") as infile:
    data = infile.read()
    
rev_data = bytes.fromhex(data.hex()[::-1])

print(rev_data)

with open("reversed.jpg", "wb") as outfile:
    outfile.write(rev_data)
```

+ 输出的文件打开后发现是一张被水平镜面翻转的字符串图片。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Reverse-it/reversed.jpg?raw=true)

+ 于是用图片处理软件处理一下，即可得到包含 flag 的图片。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Reverse-it/flag.jpg?raw=true)

+ flag: **SECCON{6in_tex7}**



## something_in_image

+ 下载附件，发现是一个无后缀的文件。
+ 首先在 **WinHex** 中打开，稍微查看一下发现文件中有一些内容是可打印字符，于是尝试直接搜索字符串 “flag” ，没有搜到有用的结果。但是仔细查看后发现，文件中有类似出现 “Flag.txt” 的字段，于是打开 **Kali Linux** ，使用命令 `binwalk` 查看一下，但是没有得到任何结果：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/something_in_image/1.png?raw=true)

+ 于是直接用 Linux 的命令 `strings | grep Flag` 查找 “Flag” 字段，然后就得到了 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/something_in_image/2.png?raw=true)

+ 直接在 **WinHex** 里面直接查找字符串 “Flag” 也是可以的...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/something_in_image/3.png?raw=true)

+ flag: **Flag{yc4pl0fvjs2k1t7T}**



## 打野

+ 下载附件，解压得到一个 ***.bmp*** 文件。
+ 打开图片... rua！一张大大的 cxk 美照 “闪现” 眼前（题目真的取得好啊...）
+ 打开 **Stegsolve** ，查看各个 Plane （从各种角度）审视 cxk 的美照，然而并未发现照片中存在任何隐藏内容。
+ 猜想可能需要 **Extract Data** 来从图片中提取数据，然而懒得用 **Stegsolve** 调参（确实也不知道从哪里调起...），于是悄咪咪的打开 **Kali Linux** ，直接在终端输入命令 `zsteg 瞅啥.bmp` 然后就得到了 flag...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E6%89%93%E9%87%8E/1.png?raw=true)

+ PS. 后来尝试在 Stegsolve 中按照 `zsteg` 得到的参数去调，但是貌似两个工具处理数据的差距挺大，一直没法调出来...
+ **鸡你太美 ~**
+ flag: **qwxf{you_say_chick_beautiful?}**



## pure_color

+ 下载附件发现是一个 ***.bmp*** 图片文件。
+ 打开图片，发现是一张空白的图片... 感觉不能这么简单，于是丢进 **StegSolve** 里面查看。
+ 翻了好几个图层以后，在 **Blue plane 0** 层看到隐藏的 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/pure_color/1.png?raw=true)

+ flag: **flag{true_steganographers_doesnt_need_any_tools}**



## Aesop_secret

+ 下载附件，解压缩得到一个 ***.gif*** 文件。
+ 打开图片，发现这个动态图的每一帧似乎就是某张图片的某一部分。
+ 于是使用 **Stegsolve** 的 **Frame Browser** 分解每一帧后再用 **Image Combiner** 拼起来得到完整的图片，也可以直接使用 **在线[GIF动态图片分解](https://tu.sioe.cn/gj/fenjie/)** 直接得到网站帮你分解后并且拼起来的图片XD：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Aesop_secret/1.png?raw=true)

+ 拼成的图片中有四个字符 **ISCC** ：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Aesop_secret/combined.png?raw=true)

+ 然而这个是出题方的名称缩写，肯定不是 flag 。于是查看压缩包和解压得到的 gif 图片里面还有没有什么隐藏的东西。

+ 打开 **Kali Linux** 使用 `binwalk` 处理并没有发现什么东西，于是用 **WinHex** 打开 gif 文件查看文件数据，终于在文件末尾发现一段很像 Base 64 编码的字符串：

  > U2FsdGVkX19QwGkcgD0fTjZxgijRzQOGbCWALh4sRDec2w6xsY/ux53Vuj/AMZBDJ87qyZL5kAf1fmAH4Oe13Iu435bfRBuZgHpnRjTBn5+xsDHONiR3t0+Oa8yG/tOKJMNUauedvMyN4v4QKiFunw==

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Aesop_secret/2.png?raw=true)

+ 但是用 Base 64 解码并不能得到有用的信息（乱码）。这时想到题目名字是 “Aesop” ，猛然想起 **AES 加密解密算法**，不学密码学多年几乎忘了还有这个东西（骗人，明明准备复试的时候还把密码学包括 AES 加解密从头到尾非常详细的复习过一遍QAQ[捂脸]）...

+ 于是使用 **[在线 AES 加密 | AES 解密 - 在线工具](https://www.sojson.com/encrypt_aes.html)** 解密一下，密码正好就用之前合成的图片里面的四个字符 **ISCC** 试试，第一次解密得到一个仍然不是 flag 但是很像 Base 64 编码的字符串：

  > U2FsdGVkX18OvTUlZubDnmvk2lSAkb8Jt4Zv6UWpE7Xb43f8uzeFRUKGMo6QaaNFHZriDDV0EQ/qt38Tw73tbQ==

+ 使用 Base 64 解码并不能得到 flag ，于是无奈之下抱着试试的心态再次使用 AES 解密，密码还是 ISCC。然后就得到了 flag ...

+ flag: **flag{DugUpADiamondADeepDarkMine}**



## 2017_Dating_in_Singapore

+ 下载附件，发现一个 ***.pdf*** 文件，文件内容是张 2017 年的新加坡日历（？？？）

+ 题目描述给了一串数字，这串数字分好几段，每段之间用 '-' 隔开：

  > 01081522291516170310172431-050607132027262728-0102030209162330-02091623020310090910172423-02010814222930-0605041118252627-0203040310172431-0102030108152229151617-04050604111825181920-0108152229303124171003-261912052028211407-04051213192625

+ 仔细观察发现这串数字分为 12 段，猜测每段数字可能对应一个月份。

+ 于是将每个分段中的每两个数字对应一个日期，在日历上标记出来。然后就很神奇的发现，每个分段在每月的日历上标记出来的结果对应一个字符，12 个字符合起来就是 flag ...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/2017_Dating_in_Singapore/1.png?raw=true)

+ flag: **HITB{CTFFUN}**



## simple_transfer

+ 下载附件，发现一个 ***.pcap*** 文件。

+ 果断用 **Wireshark** 打开，发现拦截到的数据包大部分是 **TCP 包**，还有一些 **NFS 包** 等各种不同的协议数据包，使用 追踪流 -> TCP 流 试图查看双方交换的数据，但没有什么有用的发现。

+ 这时把重点转向 **NFS 数据包**，发现其中有使用 “Remote Procedure Call (RPC)” ，于是尝试从中分离出双方共享的文件。

  > + NFS协议是一种用于文件共享的协议，它可以使得主机之间进行文件的共享。客户端可以像在本机上的文件一样操作远程主机的文件。NFS 协议最初仅支持 UDP 协议，目前最新版本的 NFS 可以支持 UDP 和 TCP 协议，不过 UDP 协议的速度会更快。
  > + NFS 协议是一个十分简单的协议，它本身没有提供信息传输的协议和功能。之所以 NFS 能够让主机之间通过网络进行资料共享，这是因为 NFS 使用了一些其它的传输协议，主要用到了 RPC (Remote Procedure Call) 功能。所以在启动 NFS 服务器的时候需要启动 RPC 服务。

+ 于是打开 **Kali Linux** ，使用 `binwalk` 命令，发现其中有一个 **PDF 文件**。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/simple_transfer/1.png?raw=true)

+ 使用 `foremost` 命令将其分离出来，打开这个 PDF 文件，文件中的字符串即为 flag 。
+ flag: **HITB{b3d0e380e9c39352c667307d010775ca}**



## hit-the-core

+ 下载附件，发现一个文件后缀为 ***.core*** 的文件。

+ 完全不知道用什么软件能打开，先用 **Notepad++** 或者 **WinHex** 打开瞧瞧，发现文件最前面几个可打印字符写着 **ELF** ，于是打开 **Kali Linux** 系统，使用 `strings` 命令查看可打印字符，发现其中有一串很长很长的字符串，带有 '{' 和 '}' ，很有可能是 flag ：

  > cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/hit-the-core/1.png?raw=true)

+ 但是完全没有规律，考虑到可能被打乱或者被加密，于是用 **[栅栏密码在线加密解密](https://www.qqxiuzi.cn/bianma/zhalanmima.php) 网站**尝试每组字数为不同值时候的结果，一直从 2 试到 26 都没有找到正确的 flag 。
+ 于是试图找规律。由于题目来源为 **alexctf** ，猜测 '{' 和 '}' 前很可能是 alexctf ，即 flag 的形式很可能是 **alexctf{xxx...xxx}** ，于是开始查找，发现从第 4 个字符开始，每隔 5 个字符正好能够成 flag 的形式，于是写了个简简单单的 Python 脚本 ***solve.py*** ：

```python
msg = "cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}"

flag = ""

for i in range(3, len(msg), 5):
    flag += msg[i]
    
print(flag)
```

+ 输出即为 flag 。
+ flag: **ALEXCTF{K33P_7H3_g00D_w0rk_up}**



## glance-50

+ 下载附件发现是一个 ***.gif*** 图片文件。
+ 打开图片，发现这个图片的尺寸很奇怪，呈细长条形的，宽度非常非常小，看不清楚图片的内容，仔细看也只能看到动图随着时间帧的变化图片中有什么东西在滚动播放或者平移（或者别的方式移动）...
+ 于是考虑将其按照时间帧分解，这里可以使用 **Stegsolve** 的 **Frame Browser** 分解后保存每一帧，也可以使用别的专业图片处理软件保存每一帧，甚至也可以使用 **在线[GIF动态图片分解](https://tu.sioe.cn/gj/fenjie/)**。
+ 没想到这个网站直接将分解后的图片按照时间帧顺序平铺在页面上展示出来，于是直接看到图片的内容，其中有一段字符串，即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/glance-50/1.png?raw=true)

+ 附上在线图片拼接网站：**在线[图片拼接——免费在线拼接多个图片成长图](http://www.zuohaotu.com/image-merge.aspx)** 。
+ flag: **TWCTF{Bliss by Charles O'Rear}**



## Training-Stegano-1

+ 下载附件发现是一个 ***.bmp*** 图片文件。
+ 打开图片，发现这个图片非常非常奇怪，尺寸非常小，放大好几倍看发图片现没什么有价值的内容，图片只是些色块。
+ 在线1)是折腾了半天，什么都没有找到。
+ 于是丢进 **WinHex** 里面看看图片里有没有藏着什么东西，于是在文件末尾发现一段字符串 “**passwd:steganoI**” ，就成功的得到了 flag ...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Training-Stegano-1/1.png?raw=true)

+ flag: **steganoI**



## a_good_idea

+ 下载压缩包解压以后看到一张很普通的表情包：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/a_good_idea/001.jpg?raw=true)

+ 常规操作丢进 **WinHex** 里面查看代码：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/a_good_idea/002.jpg?raw=true)

+ 看到 **PK** 字段以及目录下的一个 ***txt*** 文件和两个 ***png*** 文件，就知道这个图片其实隐藏着一个压缩包。
+ 将后缀改为 ***.zip*** ，解压以后得到三个文件：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/a_good_idea/003.jpg?raw=true)

+ 解压，发现两个 ***png*** 文件是两个 ~~几乎一模一样~~ 的表情包；于是打开 ***hint.txt*** 看到提示：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/a_good_idea/004.jpg?raw=true)

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

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/a_good_idea/result.png?raw=true)

+ 丢到 **[在线二维码识别网站](https://cli.im/deqr/)** 上识别，得到一个字符串就是flag。
+ flag: **NCTF{m1sc_1s_very_funny!!!}**



## 4-1

+ 下载附件，解压缩得到一个 ***.png*** 文件。
+ 第一反应打开 **Kali Linux** 使用 `binwalk` 查看一下。发现里面有一个压缩包，压缩包里有一个 ***tips.txt*** 和另一个压缩包 ***day2's secret.zip*** 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/4-1/1.png?raw=true)

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/4-1/2.png?raw=true)

+ 于是用 `foremost` 命令将压缩包分离出来，其中 `tips.txt` 文件的内容如下：

  > Although two days doing the same things, but day2 has a secret than day1
  > -。-

+ 而 ***day2's secret.zip*** 压缩包内有两张看起来一模一样的图片 ***day1.png*** 和 ***day2.png*** ，但是两张图片大小差不少，***day2.png*** 为 408K ，比 ***day1.png*** 的 243K 大不少。因此猜测 ***day2.png*** 是在 ***day1.png*** 上加了盲水印，百度 “盲水印” 即可找到大佬的盲水印处理脚本 ***bwmforpy3.py*** （Python3版本的）：

```python
#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import random

cmd = None
debug = False
seed = 20160930
oldseed = False
alpha = 3.0

if __name__ == '__main__':
    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 2:
        print ('Usage: python bwm.py <cmd> [arg...] [opts...]')
        print ('  cmds:')
        print ('    encode <image> <watermark> <image(encoded)>')
        print ('           image + watermark -> image(encoded)')
        print ('    decode <image> <image(encoded)> <watermark>')
        print ('           image + image(encoded) -> watermark')
        print ('  opts:')
        print ('    --debug,          Show debug')
        print ('    --seed <int>,     Manual setting random seed (default is 20160930)')
        print ('    --oldseed         Use python2 random algorithm.')
        print ('    --alpha <float>,  Manual setting alpha (default is 3.0)')
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd != 'encode' and cmd != 'decode':
        print ('Wrong cmd %s' % cmd)
        sys.exit(1)
    if '--debug' in sys.argv:
        debug = True
        del sys.argv[sys.argv.index('--debug')]
    if '--seed' in sys.argv:
        p = sys.argv.index('--seed')
        if len(sys.argv) <= p+1:
            print ('Missing <int> for --seed')
            sys.exit(1)
        seed = int(sys.argv[p+1])
        del sys.argv[p+1]
        del sys.argv[p]
    if '--oldseed' in sys.argv:
        oldseed = True
        del sys.argv[sys.argv.index('--oldseed')]
    if '--alpha' in sys.argv:
        p = sys.argv.index('--alpha')
        if len(sys.argv) <= p+1:
            print ('Missing <float> for --alpha')
            sys.exit(1)
        alpha = float(sys.argv[p+1])
        del sys.argv[p+1]
        del sys.argv[p]
    if len(sys.argv) < 5:
        print ('Missing arg...')
        sys.exit(1)
    fn1 = sys.argv[2]
    fn2 = sys.argv[3]
    fn3 = sys.argv[4]

import cv2
import numpy as np
import matplotlib.pyplot as plt

# OpenCV是以(BGR)的顺序存储图像数据的
# 而Matplotlib是以(RGB)的顺序显示图像的
def bgr_to_rgb(img):
    b, g, r = cv2.split(img)
    return cv2.merge([r, g, b])

if cmd == 'encode':
    print ('image<%s> + watermark<%s> -> image(encoded)<%s>' % (fn1, fn2, fn3))
    img = cv2.imread(fn1)
    wm = cv2.imread(fn2)

    if debug:
        plt.subplot(231), plt.imshow(bgr_to_rgb(img)), plt.title('image')
        plt.xticks([]), plt.yticks([])
        plt.subplot(234), plt.imshow(bgr_to_rgb(wm)), plt.title('watermark')
        plt.xticks([]), plt.yticks([])

    # print img.shape # 高, 宽, 通道
    h, w = img.shape[0], img.shape[1]
    hwm = np.zeros((int(h * 0.5), w, img.shape[2]))
    assert hwm.shape[0] > wm.shape[0]
    assert hwm.shape[1] > wm.shape[1]
    hwm2 = np.copy(hwm)
    for i in range(wm.shape[0]):
        for j in range(wm.shape[1]):
            hwm2[i][j] = wm[i][j]

    if oldseed: random.seed(seed,version=1)
    else: random.seed(seed)
    m, n = list(range(hwm.shape[0])), list(range(hwm.shape[1]))
    if oldseed:
        random.shuffle(m,random=random.random)
        random.shuffle(n,random=random.random)
    else:
        random.shuffle(m)
        random.shuffle(n)

    for i in range(hwm.shape[0]):
        for j in range(hwm.shape[1]):
            hwm[i][j] = hwm2[m[i]][n[j]]

    rwm = np.zeros(img.shape)
    for i in range(hwm.shape[0]):
        for j in range(hwm.shape[1]):
            rwm[i][j] = hwm[i][j]
            rwm[rwm.shape[0] - i - 1][rwm.shape[1] - j - 1] = hwm[i][j]

    if debug:
        plt.subplot(235), plt.imshow(bgr_to_rgb(rwm)), \
            plt.title('encrypted(watermark)')
        plt.xticks([]), plt.yticks([])

    f1 = np.fft.fft2(img)
    f2 = f1 + alpha * rwm
    _img = np.fft.ifft2(f2)

    if debug:
        plt.subplot(232), plt.imshow(bgr_to_rgb(np.real(f1))), \
            plt.title('fft(image)')
        plt.xticks([]), plt.yticks([])

    img_wm = np.real(_img)

    assert cv2.imwrite(fn3, img_wm, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    # 这里计算下保存前后的(溢出)误差
    img_wm2 = cv2.imread(fn3)
    sum = 0
    for i in range(img_wm.shape[0]):
        for j in range(img_wm.shape[1]):
            for k in range(img_wm.shape[2]):
                sum += np.power(img_wm[i][j][k] - img_wm2[i][j][k], 2)
    miss = np.sqrt(sum) / (img_wm.shape[0] * img_wm.shape[1] * img_wm.shape[2]) * 100
    print ('Miss %s%% in save' % miss)

    if debug:
        plt.subplot(233), plt.imshow(bgr_to_rgb(np.uint8(img_wm))), \
            plt.title('image(encoded)')
        plt.xticks([]), plt.yticks([])

    f2 = np.fft.fft2(img_wm)
    rwm = (f2 - f1) / alpha
    rwm = np.real(rwm)

    wm = np.zeros(rwm.shape)
    for i in range(int(rwm.shape[0] * 0.5)):
        for j in range(rwm.shape[1]):
            wm[m[i]][n[j]] = np.uint8(rwm[i][j])
    for i in range(int(rwm.shape[0] * 0.5)):
        for j in range(rwm.shape[1]):
            wm[rwm.shape[0] - i - 1][rwm.shape[1] - j - 1] = wm[i][j]

    if debug:
        assert cv2.imwrite('_bwm.debug.wm.jpg', wm)
        plt.subplot(236), plt.imshow(bgr_to_rgb(wm)), plt.title(u'watermark')
        plt.xticks([]), plt.yticks([])

    if debug:
        plt.show()

elif cmd == 'decode':
    print ('image<%s> + image(encoded)<%s> -> watermark<%s>' % (fn1, fn2, fn3))
    img = cv2.imread(fn1)
    img_wm = cv2.imread(fn2)

    if debug:
        plt.subplot(231), plt.imshow(bgr_to_rgb(img)), plt.title('image')
        plt.xticks([]), plt.yticks([])
        plt.subplot(234), plt.imshow(bgr_to_rgb(img_wm)), plt.title('image(encoded)')
        plt.xticks([]), plt.yticks([])

    if oldseed: random.seed(seed,version=1)
    else: random.seed(seed)
    m, n = list(range(int(img.shape[0] * 0.5))), list(range(img.shape[1]))
    if oldseed:
        random.shuffle(m,random=random.random)
        random.shuffle(n,random=random.random)
    else:
        random.shuffle(m)
        random.shuffle(n)

    f1 = np.fft.fft2(img)
    f2 = np.fft.fft2(img_wm)

    if debug:
        plt.subplot(232), plt.imshow(bgr_to_rgb(np.real(f1))), \
            plt.title('fft(image)')
        plt.xticks([]), plt.yticks([])
        plt.subplot(235), plt.imshow(bgr_to_rgb(np.real(f1))), \
            plt.title('fft(image(encoded))')
        plt.xticks([]), plt.yticks([])

    rwm = (f2 - f1) / alpha
    rwm = np.real(rwm)

    if debug:
        plt.subplot(233), plt.imshow(bgr_to_rgb(rwm)), \
            plt.title('encrypted(watermark)')
        plt.xticks([]), plt.yticks([])

    wm = np.zeros(rwm.shape)
    for i in range(int(rwm.shape[0] * 0.5)):
        for j in range(rwm.shape[1]):
            wm[m[i]][n[j]] = np.uint8(rwm[i][j])
    for i in range(int(rwm.shape[0] * 0.5)):
        for j in range(rwm.shape[1]):
            wm[rwm.shape[0] - i - 1][rwm.shape[1] - j - 1] = wm[i][j]
    assert cv2.imwrite(fn3, wm)

    if debug:
        plt.subplot(236), plt.imshow(bgr_to_rgb(wm)), plt.title(u'watermark')
        plt.xticks([]), plt.yticks([])

    if debug:
        plt.show()

```

（代码来源链接：**[大佬的盲水印脚本 - Github](https://github.com/chishaxie/BlindWaterMark)** ）

+ 注意，该代码使用了 **cv2** 模块，需要安装第三方库 **opencv_python** ，可以使用 **[opencv_python 的清华源](https://pypi.tuna.tsinghua.edu.cn/simple/opencv-python/)** 下载后本地安装。
+ 将该脚本和两张图片放在同一个文件夹中，使用脚本中说明的命令 `python bwmforpy3.py decode --oldseed day1.png day2.png flag.png` 解码得到水印图片 ***flag.png*** ，图片中内容即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/4-1/flag.png?raw=true)

+ **注意这里有个坑：如果使用 Python3 版本的脚本，则必须加上 `--oldseed` 参数（使用 Python2 中的随机种子方法），否则无法得到包含 flag 内容的水印图片...**
+ ~~我好菜啊，我什么时候才能自己写个这样的脚本呢QAQ~~
+ flag: **wdflag{My_c4t_Ho}**



## 适合作为桌面

+ 下载附件，解压缩得到一个 ***.png*** 文件。
+ 第一反应，用 **Stegsolve** 分离图层查看其中是否有隐藏信息，很快在 **Red Plane 1** 中看到一个二维码：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E9%80%82%E5%90%88%E4%BD%9C%E4%B8%BA%E6%A1%8C%E9%9D%A2/2.png?raw=true)

+ 保存下来后把二维码部分单独保存下来：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E9%80%82%E5%90%88%E4%BD%9C%E4%B8%BA%E6%A1%8C%E9%9D%A2/3.png?raw=true)

+ 丢到 **[在线二维码识别网站](https://cli.im/deqr/)** 上识别，得到一大段疑似十六进制数的字符串：

  > 03F30D0A79CB05586300000000000000000100000040000000730D0000006400008400005A000064010053280200000063000000000300000016000000430000007378000000640100640200640300640400640500640600640700640300640800640900640A00640600640B00640A00640700640800640C00640C00640D00640E00640900640F006716007D00006410007D0100781E007C0000445D16007D02007C01007400007C0200830100377D0100715500577C010047486400005328110000004E6966000000696C00000069610000006967000000697B000000693300000069380000006935000000693700000069300000006932000000693400000069310000006965000000697D000000740000000028010000007403000000636872280300000074030000007374727404000000666C6167740100000069280000000028000000007304000000312E7079520300000001000000730A0000000001480106010D0114014E280100000052030000002800000000280000000028000000007304000000312E707974080000003C6D6F64756C653E010000007300000000

+ 于是打开 **WinHex** ，把剪贴板内容保存到新文件，保存方式为 **ASCII (Hex)** ，发现文件中有 ***1.py*** 和 ***1.pyc*** 的内容，猜想可能跟 Python 文件有关，百度以后发现头部字段对应的是 ***.pyc*** 文件。于是保存为 ***.pyc*** 文件。

  > pyc 文件的头部是 03 F3 0D 0A ，表示 Python 的版本。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E9%80%82%E5%90%88%E4%BD%9C%E4%B8%BA%E6%A1%8C%E9%9D%A2/4.png?raw=true)

+ 然后在 **Anaconda Prompt** 中使用命令 `pip install uncompyle` 安装 **uncompyle** 后反编译 pyc 文件，然后稍微修改一下反编译得到的 ***tmp.py*** 文件，运行即可得到 flag ：

```python
def flag():
    str = [
     102, 108, 97, 103, 123, 51, 56, 97, 53, 55, 48, 51, 50, 48, 56, 53, 52, 52, 49, 101, 55, 125]
    flag = ''
    for i in str:
        flag += chr(i)

    print(flag)
# okay decompiling tmp.pyc

flag()
```

+ flag: **flag{38a57032085441e7}**



## easycap

+ 下载文件，发现是一个 ***.pcap*** 文件。
+ 果断用 **wireshark** 打开，查看数据包，发现全是 **TCP** 数据包...
+ 于是直接右键 -> **追踪流** -> **TCP流**，然后在弹出的窗口中直接就能看到 flag ...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/easycap/1.png?raw=true)

+ flag: **FLAG:385b87afc8671dee07550290d16a8071**



## 隐藏的信息

+ 下载压缩包解压以后看到一个文本文件 ***message.txt*** ，打开以后发现一串数字，有的数字之间有空格：

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

+ 猜测可能是Base64编码，立即推，丢到 **[在线 Base64 编码解码](https://base64.us/)** 网站上处理，得到如下内容：

> Well done!
>
>  Flag: ISCC{N0_0ne_can_st0p_y0u}

+ flag: **ISCC{N0_0ne_can_st0p_y0u}**



## Get-the-key.txt

+ 下载附件，发现是一个无后缀的文件。
+ 用 **WinHex** 打开，扫了一下没看到什么有用的内容，直接搜索 “flag” 字符串也没有结果。于是打开 **Kali Linux** ，`binwalk` 一下：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Get-the-key.txt/1.png?raw=true)

+ `binwalk` 没有发现什么隐藏的文件，但是却看出这个文件是 **Linux EXT filesystem** 。于是新建一个文件夹 `/xctf` ，然后使用 Linux 的挂载命令 `mount forensic100 xctf/` 来查看。挂载后得到一堆压缩包：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Get-the-key.txt/2.png?raw=true)

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Get-the-key.txt/3.png?raw=true)

+ 题目提示 “get-the-key.txt” ，猜测要找 ***key.txt*** 。于是进入挂载点所在的文件夹 `/xctf` 使用 `grep -r key.txt` 命令递归查找文件 *key.txt* 文件，发现在压缩包 ***1*** 中存在 *key.txt* 文件：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Get-the-key.txt/4.png?raw=true)

+ 查看压缩包类型，发现压缩包是 **Gzip archive (application/gzip)** 类型，于是使用解压 *.gz* 文件的命令 `gunzip 1` ，但是得到 “后缀未知” 的解压失败提示。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Get-the-key.txt/5.png?raw=true)

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Get-the-key.txt/6.png?raw=true)

+ 无奈之下只能修改文件后缀，使用命令 `mv 1 1.gz` 修改压缩包为 ***1.gz*** 后再使用命令 `gunzip 1.gz` 解压。解压后使用 `chmod +x 1` 修改对该文件的访问模式，然后再使用命令 `cat 1` 打开文件即可得到 flag 字符串。

+ **（注：别的压缩包中也有 *.txt* 文件，但都是 *key2.txt* ，*key3.txt* 等等，而且里面都有一个类似 flag 的字符串，但是根据题目提示在加上运气，直接在压缩包 *1* 中找到了正确的 flag 。** 
+ flag: **SECCON{@]NL7n+-s75FrET]vU=7Z}**



## 肥宅快乐题

+ 下载附件，发现是一个 ***.swf*** 文件。
+ 打开发现是一个貌似年代久远的古老的 **flash 小游戏**... 题目提示 “真正的快乐的游戏题，打通就给flag哦，与肥宅快乐水搭配更佳。 Flash游戏，通关后，注意与NPC的对话哦;)”。于是开始打，奈何我太菜，第一关都过不去...
+ 于是开始动歪脑筋，发现 swf 文件在视频播放器下方也有进度条，于是开始 “跳关”，试图找到最后通关后与NPC的对话。
+ 终于在**第 57 帧**发现了所谓的通关后与NPC的对话，在对话中发现一串奇怪的字符串...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E8%82%A5%E5%AE%85%E5%BF%AB%E4%B9%90%E9%A2%98/1.png?raw=true)

+ 然而把这个字符串提交上去并不能通过，看着像 Base64 编码，于是丢到 **[Base64 在线编码解码](https://base64.us/)** 网站上处理，得到最后的 flag 。
+ flag: **SYC{F3iZhai_ku4ile_T111}** 



## 小小的PDF

+ 下载附件，发现是一个 ***.pdf*** 文件。
+ 打开文件，一共两页，内容没什么营养：第一页上放了两张表情包；第二页空白，看起来十分可疑。
+ 于是打开 **Kali Linux** 系统，用 `binwalk` 命令查看一下，发现这个 pdf 文件包含了三个 JPEG 文件和三个 Zlib 压缩数据文件。而 pdf 中却只能看到两张 JPEG文件，显然有一张图片被隐藏了。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E5%B0%8F%E5%B0%8F%E7%9A%84PDF/1.png?raw=true)

+ 于是用 `foremost` 命令提取 pdf 中包含的文件，提取出来的三个 JPEG 文件中，前两个图片为 pdf 文件中显示的那两张表情包，第三张图片上显示了一串字符串，即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E5%B0%8F%E5%B0%8F%E7%9A%84PDF/2.png?raw=true)

+ flag: **SYC{so_so_so_easy}**



## Cephalopod

+ 下载附件，发现是一个 ***.pcap*** 文件。

+ 直接使用 **Wireshark** 打开，分析其中数据包的类型，发现主要为 **TCP 包**和一种和奇怪的 **Ceph包**。

  > + Ceph 是一种为优秀的性能、可靠性和可扩展性而设计的统一的、分布式文件系统。
  > + Ceph 是一种软件定义存储，可以运行在几乎所有主流的 Linux 发行版（比如 CentOS 和 Ubuntu）和其它类UNIX操作系统（典型如 FreeBSD）。
  > + Ceph 的分布式基因使其可以轻易管理成百上千个节点、PB 级及以上存储容量的大规模集群，同时基于计算的扁平寻址设计使得Ceph客户端可以直接和服务端的任意节点通信，从而避免因为存在访问热点而导致性能瓶颈。
  > + Ceph 独一无二地用统一的系统提供了对象、块、和文件存储功能，它可靠性高、管理简便、并且是自由软件。 Ceph 的强大足以改变贵公司的 IT 基础架构、和管理海量数据的能力。Ceph 可提供极大的伸缩性——供成千用户访问 PB 乃至 EB 级的数据。 Ceph 节点以普通硬件和智能守护进程作为支撑点， Ceph 存储集群组织起了大量节点，它们之间靠相互通讯来复制数据、并动态地重分布数据。

+ 好吧又是文件系统。这次学乖了，上来不直接 `binwalk` 了，而是直接在 Wireshark 中进行分析。对第一个 Ceph 包进行操作 **追踪流 -> TCP流** ，此时过滤器中显示 `tcp.stream eq 0` ，弹出的窗口内容如下，像是进行文件传输之前的准备工作，类似TCP的握手或者登录文件系统时的各种身份验证工作。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Cephalopod/1.png?raw=true)

+ 继续追踪其它的 TCP 流，把过滤器中的内容修改为 `tcp.stream eq 1` ，查看弹出窗口中的数据内容。这次有了重要发现——服务端发送给客户端或者客户端发送给服务端的数据中都出现了 **“flag.png”** 字段：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Cephalopod/2.png?raw=true)

+ 根据题目提示，flag 很有可能就在这张图片里面。下面的问题就在于如何把图片给分离出来。`binwalk` 后使用 `foremost` 并不能成功得到这张图片，于是直接在数据包中寻找这张图片的数据信息。预先知道 PNG 文件的文件结构信息如下：

  > + PNG 文件的文件头标识为：89 50 4e 47 0d 0a 1a 0a ，对应 ASCII 码为：.PNG....
  > + 然后是IHDR数据块信息：00 00 00 0d 49 48 44 52 ，对应 ASCII 码为：....IHDR
  >   + `0000 000d` 说明 IHDR 头块长为 13 ，
  >   + `4948 4452` 为 IHDR 字段标识。
  > + PNG 文件的文件结尾为：00 00 00 00 49 45 4E 44 AE 42 60 82 ，对应 ASCII 码为：....IEND.B`.

+ 该 TCP 流中没有发现传输 *flag.png* 文件的内容，于是修改过滤器内容继续追踪别的 TCP 流。发现一共就 3 条 TCP 流，修改为 `tcp.stream eq 2` 时，窗口中显示的数据就包含了 *flag.png* 文件传输的数据内容。在窗口底部将 “显示和保存数据为” 的默认值 “ASCII” 改为 **“原始数据”** 后搜索 `89504e470d0a1a0a` 字段和 `0000000049454E44AE426082` 都能搜索到：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Cephalopod/3.png?raw=true)

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Cephalopod/4.png?raw=true)

+ 将该窗口中的数据保存为 ***flag.png*** ，在 **WinHex** 中打开，去掉文件中 `89504e470d0a1a0a` 前的数据和 `0000000049454E44AE426082` 后的数据后保存，即可在图片中看到 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Cephalopod/flag.png?raw=true)

+ flag: **HITB{95700d8aefdc1648b90a92f3a8460a2c}**



## Excaliflag

+ 下载附件，发现是一个 ***.png*** 文件。
+ 打开文件发现这是张很普通的图片，除了图片是一个旗子（flag）插在一片绿油油的草地上（逗我么...）
+ 先用图片隐写工具 **Stegsolve** 分离各个图层的图片试试，翻了几个图层就发现某些图层能隐隐约约看到图片里隐藏了一串字符串。
+ 最后在 **Gray bits** 层发现非常清晰的隐藏字符串，即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Excaliflag/1.png?raw=true)

+ flag: **3DS{Gr4b_Only_th1s_B1ts}**



## 签到题

+ 题目描述真直白：“SSCTF线上选举美男大赛开始了，泰迪拿着他的密码去解密了，提交花括号内内容（Z2dRQGdRMWZxaDBvaHRqcHRfc3d7Z2ZoZ3MjfQ==）”。

+ 然而这个签到题并没这么简单，直接把 “Z2dRQGdRMWZxaDBvaHRqcHRfc3d7Z2ZoZ3MjfQ==” 当做 flag 提交并不能通过。

+ 这个字符串结尾有两个 **=** ，看起来非常像是 **Base64** 编码，于是用 **[在线 Base64编码解码](https://base64.us/)** 网站在线解码，得到一个新的字符串：

  > ggQ@gQ1fqh0ohtjpt_sw{gfhgs#}

+ 这显然不可能是 flag ，考虑到 flag 的格式应该是 xxxx{xxxx..xxxx}，而题目来源又是 **SSCTF-2017** ，猜测 flag 的格式应该是 **SSCTF{xxx...xxx}** ，而刚得到的字符串中，花括号前面的字段显然太长了，猜测可能是用某种密码（**栅栏密码**）加密过的（别问为什么是栅栏密码，以前做过 Crypto 题，这种密码的形式一看就是栅栏密码...），于是用 **[栅栏密码在线加密解密](https://www.qqxiuzi.cn/bianma/zhalanmima.php)** 网站在线解密，得到一个新的字符串：

  > ggqht{ggQht_gsQ10jsf#@fopwh}

+ 显然这仍然不是 flag ... 根据上面的分析，flag 的格式应该是 **SSCTF{xxx...xxx}** ，这个形式已经接近了，但是字母不对。仔细观察，发现 **gg** 可能对应 flag 中的 **SS** ，因此考虑可能字符串又被**凯撒密码**加密过，于是用 **[凯撒密码在线加密解密](https://www.qqxiuzi.cn/bianma/kaisamima.php)** 网站在线解密，得到最后的 flag 。

+ 三层加密，疯狂加密，**禁止套娃**啊喂...

+ flag: **ssctf{ssCtf_seC10ver#@rabit}**



## Avatar

+ 下载附件，发现是一张 ***.jpg*** 文件。
+ 首先使用 **Stegsolve** 查看各个 Plane 是否有隐藏的信息，并没有发现。
+ 于是打开 **Kali Linux** 系统，使用 `zsteg` 命令查看，但是得到提示 `zsteg` 并不能对 *.jpg* 格式的文件进行操作：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Avatar/1.png?raw=true)

+ 于是使用 `binwalk` 命令查看一下，但也没有发现隐藏的文件。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Avatar/2.png?raw=true)

+ 于是百度，了解到 **JPG** 格式图片的隐写套路：

  > - 在图片右击查看属性，在详细信息中隐藏数据。
  > - 将数据类型进行改写（rar或者zip数据改为jpg等格式）。
  > - 根据各种类型图像的固定格式，隐藏数据。
  > - 在编译器中修改图像开始的标志，改变其原来图像格式。
  > - 在图像结束标志后加入数据。
  > - 在图像数据中加入数据，不影响视觉效果情况下修改像素数据，加入信息。
  > - 利用隐写算法将数据隐写到图片中而不影响图像（仅限于jpg图像） 隐写常用的算法有F5，guess jsteg jphide。

+ 解决方法有：

  > - 查看图像属性详细信息是否有隐藏内容。
  > - 利用 Winhex 或 Nodepad++ 打开搜索 ctf, CTF, flag, key 等关键字是否存在相关信息。
  > - 检查图像的开头标志和结束标志是否正确，若不正确修改图像标志恢复图像，打开查看是否有 flag 或 ctf 信息（gif 格式图片需要分帧查看各帧图像组合所得数据。若不是直接的 ctf 或 flag 信息，需要考虑将其解码）。
  > - 在 Kali Linux 系统中执行 `binwalk` 查看图片中是否是多个图像组合或者包含其他文件（若存在多幅图像组合，再执行 `foremost` 分离内容；若检测出其他文件修改其后缀名即可，如改为 *.zip* ）。
  > - 使用 StegSolve 对图像进行分通道扫描（是否为LSB隐写等）。
  > - 在 Kail Linux 系统中进入目录 `/F5-steganography` ，执行 `java Extract` 命令（需要先从 Github 上使用 `git clone https://github.com/matthewgao/F5-steganography ` 命令获取该工具），检测是否是 steganography 算法隐写。
  > - 在 Kail Linux 系统中使用 outguess 工具（需要预先从 Github 上使用 `git clone https://github.com/crorvick/outguess` 命令获取该工具，然后进入 `/outguess` 目录下使用 `./configure && make && make install` 安装），检测是否为 guess 算法隐写。

+ 查看图像属性详细信息后并未发现有隐藏内容。同时使用 F5-steganography 工具解析失败：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Avatar/3.png?raw=true)

+ 最后输入命令 `outguess -r /root/035bfaa85410429495786d8ea6ecd296.jpg -t /root/output.txt` 使用 outguess 工具检测：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Avatar/4.png?raw=true)

+ 得到输出的 ***output.txt*** 后，使用命令 `chmod +x output.txt` ，再使用命令 `cat output.txt` 即可得到 flag 。
+ flag: **We should blow up the bridge at midnight**