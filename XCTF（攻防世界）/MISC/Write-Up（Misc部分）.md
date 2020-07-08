# Write-Up（Misc部分）

## this is flag

+ 题目中直接给的 flag ，复制粘贴即可...
+ flag: **flag{th1s_!s_a_d4m0_4la9}**



## pdf

+ 附件是一个 **pdf** 文件，打开就是一张图片，看起来没什么特别的。
+ 丢进 **WinHex** 里面查看，查找 **flag** 字符串，也没发现什么东西。
+ 放进 **Kali Linux** 里面尝试 `binwalk` 一下，也没发现什么隐藏着什么文件。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/pdf/1.png?raw=true)

+ 于是找了个有编辑 pdf 功能的 pdf 阅读器（编辑器），试图把这张图片从 pdf 文件中抠下来。
+ 然后就神奇的发现，flag 就藏在图片后面，原来是被图片挡住了...
+ flag: **flag{security_through_obscurity}**



## 如来十三掌

+ 附件是一个 **docx** 文件，内容貌似是佛经之类的，看的我一脸懵逼...

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



## give_you_flag

+ 下载附件，是一个 **.gif** 文件。
+ 打开看到就是一只很萌的小龙在数钱，但是看完完整的内容会发现，动图的最后几帧似乎有一个小小的类似二维码的东西一闪而过。
+ 于是使用 **Stegsolve** 打开，然后使用 **Frame Browser** 功能找到有二维码的那一帧并保存下来。
+ 保存下来打开后发现，这个 “二维码” 并不完整，左上角、左下角、右上角一共三个定位点都缺失，而且图片中的二维码比较小，所以直接扫码识别是无法识别出来的，需要用图片处理软件处理一下：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/give_you_flag/give_you_flag.png?raw=true)

+ 于是 P 图开始了，直接用画图就可以搞定了：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/give_you_flag/QRCode.png?raw=true)

+ P 完后可以使用微信扫一扫或者使用 **[在线二维码解码器](https://jiema.wwei.cn/)** 或者 **[草料二维码解码器](https://cli.im/deqr/)** 在线解码，即可得到 flag。
+ flag: **flag{e7d478cf6b915f50ab1277f78502a2c5}**



## 神奇的Modbus

+ 下载附件压缩包并解压，发现一个 **.pcap** 文件。

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



## base64÷4

+ 下载附件压缩包并解压，发现一个后缀为 **.txt** 的文件。

+ 打开看到一串字符串：

  > 666C61677B45333342374644384133423834314341393639394544444241323442363041417D

+ 看起来很像是十六进制数，而且题目的名字就是 “base64÷4”，因此猜测可能俩俩凑个对可以构成一个 ASCII 码对应的字符。

+ 于是写个简简单单的 Python 脚本 **trans.py** ：

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



## János-the-Ripper

+ 下载附件压缩包并解压，发现一个无后缀的文件 **misc100** 。
+ 果断丢进 **WinHex** 里面查看，发现文件头出现 **PK** 字段，说明这是个 **.zip** 压缩包文件。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/J%C3%A1nos-the-Ripper/1.png?raw=true)

+ 将文件后缀改为 **.zip** ，然后解压缩，解压缩的时候发现需要密码，题目却并没有给任何提示...
+ 于是使用工具 **ARCHPR** 尝试爆破口令，勾上 “所有大写拉丁文(A - Z)” ， “所有小写拉丁文(a - z)” 和 “所有数字(0 - 9)” 三个勾选框，长度先设为 4 ，开始爆破... 瞬间得到密码 “**fish**” ：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/J%C3%A1nos-the-Ripper/2.png?raw=true)

+  用该密码解压 **flag.txt** 后打开即可看到 flag 。
+ flag: **flag{ev3n::y0u::bru7us?!}**



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



## Banmabanma

+ 下载附件压缩包并解压，发现一个 **.png** 文件。

+ 打开图片，发现图片里是一只斑马，但是背上的斑纹挺奇怪的，看起来像个条形码XD

+ 于是到处去找在线条形码识别网站，百度无果（没有能成功识别的），最终谷歌找到一个在线识别条形码的靠谱网站 搜索结果 **[Barcode Reader. Free Online Web Application](https://online-barcode-reader.inliteresearch.com/)** 。

+ 识别结果如下：

  > FLAG IS TENSHINE

+ flag: **flag{TENSHINE}**



## Hear-with-your-Eyes

+ 下载附件，发现一个没有后缀的文件。
+ 丢到 **WinHex** 里发现很大，也没看出什么名堂来，于是放进 **Kali Linux** 中，发现系统显示该文件为 **Gzip archive (application/gzip)，即压缩包文件**。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Hear-with-your-Eyes/1.png?raw=true)

+ 修改后缀为 **.zip** 并解压缩，发现一个 **sound.wav** 文件，打开播放，发现是一段长度为 10 秒的鬼畜音频（不能算音乐吧）...
+ 题目提示 “用眼睛听这段音频” ，猜想需要搞个音频处理软件啥的来看看这段音频有没有藏着什么东西，于是用 **Audacity** 打开音乐文件。
+ 默认显示的是这段音频的**波形**，波形没有什么特别的，于是切换到**频谱图**，然后就看到了用频谱硬生生 “画” 出来的 flag 字符串...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/Hear-with-your-Eyes/2.png?raw=true)

+ flag: **e5353bb7b57578bd4da1c898a8e2d767**



## What-is-this

+ 下载附件压缩包并解压，发现一个没有后缀的文件。
+ 丢进 WinHex 查看内容，并没有发现有什么文件类型标志。
+ 于是打开 Kali Linux 系统，把文件复制进去 `binwalk` 一下。这个没有后缀的文件在 Linux 文件系统下显示的是 **Gzip archive (application/gzip)** ，猜测是个压缩包，`binwalk` 的结果也证实了这一点：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/What-is-this/1.png?raw=true)

+ 于是将文件的后缀改为 **.zip** ，解压缩得到两张图片 **pic1.jpg** 和 **pic2.jpg** 。两张图片看起来十分像，都是杂乱的分布着黑白像素点。猜测可能 **combine** 一下也许会变出个二维码什么的，于是使用工具 **Stegsolve** 中的 **Image Combiner** 功能把两张图合成一下。
+ 合成的图片中并没有二维码，却是一个字符串 “**AZADI TOWER**” ，即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/What-is-this/2.png?raw=true)

+ flag: **AZADI TOWER**



## embarrass

+ 下载附件压缩包并解压，发现一个 **.pcap** 文件。
+ 果断上 **wireshark** ，查看内容，发现拦截到的数据包种类非常多，大部分是 **TCP 包**，还有少量的 **HTTP 包**、**FTP-DATA 包**等等。内容太多不知道从哪来开始找 flag ，于是考虑在 Kali Linux 系统下 `binwalk` 或者利用 `foremost` 找，找到各种 xml 文档，htm/html 页面以及少量的 doc 文件甚至一个 jpg 文件（打开发现还是张有问题的图片），但是没有什么有用的内容。
+ 无奈之下回归 wireshark ，开始追踪流。首先**对 HTTP 包追踪 HTTP 流**，然后在弹出的窗口底部查找 “flag” 字符串，但一无所获。
+ 注意到 **FTP-DATA 包**，于是尝试**追踪 TCP 流**，并在弹出的窗口底部查找 “flag” 字符串，成功搜索到 flag ：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/embarrass/1.png?raw=true)

+ 另解，还可以通过 Linux 下的 `strings` 来查找文件里的字符串数据：

  > <code>strings misc_02.pcapng | grep flag</code>

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/embarrass/2.png?raw=true)

+ 因此同样可以把数据包丢进 **WinHex** 内然后查找 flag 字段...
+ flag: **flag{Good_b0y_W3ll_Done}**



## MISCall

+ 下载附件，发现又是一个没有后缀的文件...
+ 用 **WinHex** 打开，发现文件开头出现字段 `BZh91AY&SY` ，百度得知这是 **.bz2** 文件的文件头，于是打开 **Kali Linux** 在终端用 `tar -jxvf` 命令解压文件。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/1.png?raw=true)

+ 仔细查看解压的详细过程，发现解压得到的文件像是某个项目或者 repo 的 **git 目录** 。其中有个 **flag.txt** 文件没有被隐藏，打开后却只看到一行字：

  > Nothing to see here, moving along...

+ 查看其它被隐藏的 **.git 文件夹**中的文件，没看出什么东西，于是百度 git 命令，在终端对该文件夹进行操作。

+ 首先是用 `git log`  和 `git log all` 命令查看版本演变历史和所有分支的历史：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/2.png?raw=true)

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/3.png?raw=true)

+ 发现有演变历史，显示最近有上传一个文件夹，但是目录中并不存在，于是再用 `git stash list` 命令查看当前 stash 中内容的列表：

  > `git stash` 能够将所有未提交的修改（工作区和暂存区）保存至堆栈中，用于后续恢复当前工作目录。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/4.png?raw=true)

+ 发现列表里是有东西的，于是进一步使用 `git stash show` 命令查看堆栈中最新保存的stash和当前目录的差异，发现 stash 中有个 **s.py** 文件，还有个 **flag.txt** 文件：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/MISCall/5.png?raw=true)

+ 于是用 `git stash apply` 命令将堆栈中的内容应用到当前目录，即可在目录中看到 **s.py** 文件和**新的 flag.txt** 文件：

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

+ 而 s.py 文件看起来则像是处理 flag.txt 文件的：

```python
#!/usr/bin/env python
from hashlib import sha1
with open("flag.txt", "rb") as fd:
    print "NCN" + sha1(fd.read()).hexdigest()
```

+ 于是在终端输入 `python s.py` 命令，得到一串字符串，即为 flag 。
+ flag: **NCN4dd992213ae6b76f27d7340f0dde1222888df4d3**



## wireshark-1

+ 下载附件压缩包并解压，发现一个 **.pcap** 文件。
+ 果断上 **wireshark** ，查看拦截到的数据包。
+ 大部分是 **TCP包**，也有部分的 **HTML包** 和 **DNS包**。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/1.png?raw=true)

+ 发现第二个 **HTML包** 的内容是一个 **php网站** 的登录操作，故右键选择 **追踪流** -> **TCP流**

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/2.png?raw=true)

+ 仔细查看流的内容即可发现其中隐藏着 flag ——登录的 **email** 字段值为 **flag** ，**password** 字段值即为我们要的 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/wireshark-1/3.png?raw=true)

+ 也可以在弹出来的框底部的 **查找** 中直接查找字段 **flag** 。
+ flag: **flag{ffb7567a1d4f4abdffdb54e022f8facd}**



## pure_color

+ 下载附件发现是一个 **.bmp** 图片文件。
+ 打开图片，发现是一张空白的图片... 感觉不能这么简单，于是丢进 **StegSolve** 里面查看。
+ 翻了好几个图层以后，在 **Blue plane 0** 层看到隐藏的 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/pure_color/1.png?raw=true)

+ flag: **flag{true_steganographers_doesnt_need_any_tools}**



### 2017_Dating_in_Singapore

+ 下载附件，发现一个 **.pdf** 文件，文件内容是张 2017 年的新加坡日历（？？？）

+ 题目描述给了一串数字，这串数字分好几段，每段之间用 '-' 隔开：

  > 01081522291516170310172431-050607132027262728-0102030209162330-02091623020310090910172423-02010814222930-0605041118252627-0203040310172431-0102030108152229151617-04050604111825181920-0108152229303124171003-261912052028211407-04051213192625

+ 仔细观察发现这串数字分为 12 段，猜测每段数字可能对应一个月份。

+ 于是将每个分段中的每两个数字对应一个日期，在日历上标记出来。然后就很神奇的发现，每个分段在每月的日历上标记出来的结果对应一个字符，12 个字符合起来就是 flag ...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/2017_Dating_in_Singapore/1.png?raw=true)

+ flag: **HITB{CTFFUN}**



## hit-the-core

+ 下载附件，发现一个文件后缀为 **.core** 的文件。

+ 完全不知道用什么软件能打开，先用 **Notepad++** 或者 **WinHex** 打开瞧瞧，发现文件最前面几个可打印字符写着 **ELF** ，于是打开 **Kali Linux** 系统，使用 `strings` 命令查看可打印字符，发现其中有一串很长很长的字符串，带有 '{' 和 '}' ，很有可能是 flag ：

  > cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/hit-the-core/1.png?raw=true)

+ 但是完全没有规律，考虑到可能被打乱或者被加密，于是用 **[栅栏密码在线加密解密](https://www.qqxiuzi.cn/bianma/zhalanmima.php) 网站**尝试每组字数为不同值时候的结果，一直从 2 试到 26 都没有找到正确的 flag 。
+ 于是试图找规律。由于题目来源为 **alexctf** ，猜测 '{' 和 '}' 前很可能是 alexctf ，即 flag 的形式很可能是 **alexctf{xxx...xxx}** ，于是开始查找，发现从第 4 个字符开始，每隔 5 个字符正好能够成 flag 的形式，于是写了个简简单单的 Python 脚本 **solve.py** ：

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

+ 下载附件发现是一个 **.gif** 图片文件。
+ 打开图片，发现这个图片的尺寸很奇怪，呈细长条形的，宽度非常非常小，看不清楚图片的内容，仔细看也只能看到动图随着时间帧的变化图片中有什么东西在滚动播放或者平移（或者别的方式移动）...
+ 于是考虑将其按照时间帧分解，这里可以使用 **Stegsolve** 的 **Frame Browser** 分解后保存每一帧，也可以使用别的专业图片处理软件保存每一帧，甚至也可以使用 **在线[GIF动态图片分解](https://tu.sioe.cn/gj/fenjie/)**。
+ 没想到这个网站直接将分解后的图片按照时间帧顺序平铺在页面上展示出来，于是直接看到图片的内容，其中有一段字符串，即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/glance-50/1.png?raw=true)

+ 附上在线图片拼接网站：**在线[图片拼接——免费在线拼接多个图片成长图](http://www.zuohaotu.com/image-merge.aspx)** 。
+ flag: **TWCTF{Bliss by Charles O'Rear}**



## Training-Stegano-1

+ 下载附件发现是一个 **.bmp** 图片文件。
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

+ 看到 **PK** 字段以及目录下的一个 **txt** 文件和两个 **png** 文件，就知道这个图片其实隐藏着一个压缩包。
+ 将后缀改为 **.zip** ，解压以后得到三个文件：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/a_good_idea/003.jpg?raw=true)

+ 解压，发现两个 **png** 文件是两个 ~~几乎一模一样~~ 的表情包；于是打开 **hint.txt** 看到提示：

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



## easycap

+ 下载文件，发现是一个 **.pcap** 文件。
+ 果断用 **wireshark** 打开，查看数据包，发现全是 **TCP** 数据包...
+ 于是直接右键 -> **追踪流** -> **TCP流**，然后在弹出的窗口中直接就能看到 flag ...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/easycap/1.png?raw=true)

+ flag: **FLAG:385b87afc8671dee07550290d16a8071**



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

+ 猜测可能是Base64编码，立即推，丢到 **[在线 Base64 编码解码](https://base64.us/)** 网站上处理，得到如下内容：

> Well done!
>
>  Flag: ISCC{N0_0ne_can_st0p_y0u}

+ flag: **ISCC{N0_0ne_can_st0p_y0u}**



## 肥宅快乐题

+ 下载附件，发现是一个 **.swf** 文件。
+ 打开发现是一个貌似年代久远的古老的 **flash 小游戏**... 题目提示 “真正的快乐的游戏题，打通就给flag哦，与肥宅快乐水搭配更佳。 Flash游戏，通关后，注意与NPC的对话哦;)”。于是开始打，奈何我太菜，第一关都过不去...
+ 于是开始动歪脑筋，发现 swf 文件在视频播放器下方也有进度条，于是开始 “跳关”，试图找到最后通关后与NPC的对话。
+ 终于在**第 57 帧**发现了所谓的通关后与NPC的对话，在对话中发现一串奇怪的字符串...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/MISC/%E8%82%A5%E5%AE%85%E5%BF%AB%E4%B9%90%E9%A2%98/1.png?raw=true)

+ 然而把这个字符串提交上去并不能通过，看着像 Base64 编码，于是丢到 **[Base64 在线编码解码](https://base64.us/)** 网站上处理，得到最后的 flag 。
+ flag: **SYC{F3iZhai_ku4ile_T111}** 



## Excaliflag

+ 下载附件，发现是一个 **.png** 文件。
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

