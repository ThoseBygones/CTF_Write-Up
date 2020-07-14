# Write-Up（Crypto部分）

## base64

+ 下载附件，得到一个 ***.txt*** 文件。

+ 打开看到一串包含数字和英文字母大小写的字符串：

  > Y3liZXJwZWFjZXtXZWxjb21lX3RvX25ld19Xb3JsZCF9

+ 考虑到题目提示 “base64” ，于是直接使用 **[在线 Base64编码解码](https://base64.us/)** 网站处理一下，即得到 flag 。

+ flag: **cyberpeace{Welcome_to_new_World!}**



## Caesar

+ 下载附件，得到一个 ***.txt*** 文件。

+ 打开看到一串仅包含英文小写字母、下划线和花括号的字符串：

  > oknqdbqmoq{kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz}

+ 考虑到这个字符串已经初具 flag 形式了，而且题目提示了 “Caesar” ，猜测这个字符串应该被**凯撒密码加密**过。于是使用 **[凯撒密码在线加密解密](https://www.qqxiuzi.cn/bianma/kaisamima.php)** 解密，根据 flag 形式估计位移值（或者直接暴力尝试也行），最终当**位移量为 12** 时，解密即可得到 flag 。

+ flag: **cyberpeace{you_have_learned_caesar_encryption}**



## Morse

+ 下载附件，得到一个 ***.txt*** 文件。

+ 打开看到一串仅包含数字 '0'、'1' 和空格的字符串：

  > 11 111 010 000 0 1010 111 100 0 00 000 000 111 00 10 1 0 010 0 000 1 00 10 110

+ 题目提示 “Morse” ，猜测这是**摩尔斯电码**，于是使用**在线 [摩斯密码\_摩斯密码翻译器\_摩斯密码转换器](http://www.dugupiao.cn/Tools/morse/)** 转换一下，**分割符设为空格**，**长设为 1** ，**短设为 0** 即可得到翻译后的字符串：

  > MORSECODEISSOINTERESTING

+ 但题目要求 flag 的内容为小写字母，于是使用 **[在线英文字母大小写转换工具](https://www.iamwawa.cn/daxiaoxie.html)** 转换得到全小写的字符串，再修改为 flag 的格式即可。

+ flag: **cyberpeace{morsecodeissointeresting}**



## 不仅仅是Morse

+ 下载附件，得到一个 ***.txt*** 文件。

+ 打开看到一串仅包含 '-' ，'.' 和 '/' 字符的字符串：

  > --/.-/-.--/..--.-/-..././..--.-/..../.-/...-/./..--.-/.-/-./---/-/...././.-./..--.-/-.././-.-./---/-.././..../..../..../..../.-/.-/.-/.-/.-/-.../.-/.-/-.../-.../-.../.-/.-/-.../-.../.-/.-/.-/.-/.-/.-/.-/.-/-.../.-/.-/-.../.-/-.../.-/.-/.-/.-/.-/.-/.-/-.../-.../.-/-.../.-/.-/.-/-.../-.../.-/.-/.-/-.../-.../.-/.-/-.../.-/.-/.-/.-/-.../.-/-.../.-/.-/-.../.-/.-/.-/-.../-.../.-/-.../.-/.-/.-/-.../.-/.-/.-/-.../.-/.-/-.../.-/-.../-.../.-/.-/-.../-.../-.../.-/-.../.-/.-/.-/-.../.-/-.../.-/-.../-.../.-/.-/.-/-.../-.../.-/-.../.-/.-/.-/-.../.-/.-/-.../.-/.-/-.../.-/.-/.-/.-/-.../-.../.-/-.../-.../.-/.-/-.../-.../.-/.-/-.../.-/.-/-.../.-/.-/.-/-.../.-/.-/-.../.-/.-/-.../.-/.-/-.../.-/-.../.-/.-/-.../-.../.-/-.../.-/.-/.-/.-/-.../-.../.-/-.../.-/.-/-.../-.../.-

+ 必须是**摩尔斯电码**，没什么好解释的，于是使用**在线 [摩斯密码\_摩斯密码翻译器\_摩斯密码转换器](http://www.dugupiao.cn/Tools/morse/)** 转换一下，**分割符设为 '/' **，**长设为 '-' ** ，**短设为 '.' ** 即可得到翻译后的字符串：

  > MAY_BE_HAVE_ANOTHER_DECODEHHHHAAAAABAABBBAABBAAAAAAAABAABABAAAAAAABBABAAABBAAABBAABAAAABABAABAAABBABAAABAAABAABABBAABBBABAAABABABBAAABBABAAABAABAABAAAABBABBAABBAABAABAAABAABAABAABABAABBABAAAABBABAABBA

+ 有种被耍了的感觉... 但是仔细一看发现 'H' 后面一堆的 'A' 和 'B' 似乎有点玄机，一时想不起来什么密码时用 'A' 和 'B' 来表示明文。于是百度一下，发现是**培根密码**。

  > 培根密码（Bacon's cipher）是由法兰西斯·培根发明的一种隐写术。
  >
  > | 明文 | 密文  | 明文 | 密文  | 明文 | 密文  | 明文 | 密文  |
  > | ---- | ----- | ---- | ----- | ---- | ----- | ---- | ----- |
  > | A/a  | aaaaa | H/h  | aabbb | O/o  | abbba | V/v  | babab |
  > | B/b  | aaaab | I/i  | abaaa | P/p  | abbbb | W/w  | babba |
  > | C/c  | aaaba | J/j  | abaab | Q/q  | baaaa | X/x  | babbb |
  > | D/d  | aaabb | K/k  | ababa | R/r  | baaab | Y/y  | bbaaa |
  > | E/e  | aabaa | L/l  | ababb | S/s  | baaba | Z/z  | bbaab |
  > | F/f  | aabab | M/m  | abbaa | T/t  | baabb |      |       |
  > | G/g  | aabba | N/n  | abbab | U/u  | babaa |      |       |

+ 于是使用 **在线工具|培根密码加解密** 在线解密，即可得到解密后的字符串，再修改为 flag 的格式即可。

  > ATTACKANDDEFENCEWORLDISINTERESTING
  > attackanddefenceworldisinteresting

+ flag: **cyberspace{attackanddefenceworldisinteresting}**



## 混合编码

+ 下载附件，得到一个 ***.txt*** 文件。

+ 打开看到一串包含数字和英文字母大小写的字符串，末尾还有两个 '=' ：

  > JiM3NjsmIzEyMjsmIzY5OyYjMTIwOyYjNzk7JiM4MzsmIzU2OyYjMTIwOyYjNzc7JiM2ODsmIzY5OyYjMTE4OyYjNzc7JiM4NDsmIzY1OyYjNTI7JiM3NjsmIzEyMjsmIzEwNzsmIzUzOyYjNzY7JiMxMjI7JiM2OTsmIzEyMDsmIzc3OyYjODM7JiM1NjsmIzEyMDsmIzc3OyYjNjg7JiMxMDc7JiMxMTg7JiM3NzsmIzg0OyYjNjU7JiMxMjA7JiM3NjsmIzEyMjsmIzY5OyYjMTIwOyYjNzg7JiMxMDU7JiM1NjsmIzEyMDsmIzc3OyYjODQ7JiM2OTsmIzExODsmIzc5OyYjODQ7JiM5OTsmIzExODsmIzc3OyYjODQ7JiM2OTsmIzUwOyYjNzY7JiMxMjI7JiM2OTsmIzEyMDsmIzc4OyYjMTA1OyYjNTY7JiM1MzsmIzc4OyYjMTIxOyYjNTY7JiM1MzsmIzc5OyYjODM7JiM1NjsmIzEyMDsmIzc3OyYjNjg7JiM5OTsmIzExODsmIzc5OyYjODQ7JiM5OTsmIzExODsmIzc3OyYjODQ7JiM2OTsmIzExOTsmIzc2OyYjMTIyOyYjNjk7JiMxMTk7JiM3NzsmIzY3OyYjNTY7JiMxMjA7JiM3NzsmIzY4OyYjNjU7JiMxMTg7JiM3NzsmIzg0OyYjNjU7JiMxMjA7JiM3NjsmIzEyMjsmIzY5OyYjMTE5OyYjNzc7JiMxMDU7JiM1NjsmIzEyMDsmIzc3OyYjNjg7JiM2OTsmIzExODsmIzc3OyYjODQ7JiM2OTsmIzExOTsmIzc2OyYjMTIyOyYjMTA3OyYjNTM7JiM3NjsmIzEyMjsmIzY5OyYjMTE5OyYjNzc7JiM4MzsmIzU2OyYjMTIwOyYjNzc7JiM4NDsmIzEwNzsmIzExODsmIzc3OyYjODQ7JiM2OTsmIzEyMDsmIzc2OyYjMTIyOyYjNjk7JiMxMjA7JiM3ODsmIzY3OyYjNTY7JiMxMjA7JiM3NzsmIzY4OyYjMTAzOyYjMTE4OyYjNzc7JiM4NDsmIzY1OyYjMTE5Ow==

+ 猜测是 **Base 64 编码** ，于是使用 **[在线 Base64编码解码](https://base64.us/)** 处理一下，得到如下内容：

  > \&#76;\&#122;\&#69;\&#120;\&#79;\&#83;\&#56;\&#120;\&#77;\&#68;\&#69;\&#118;\&#77;\&#84;\&#65;\&#52;\&#76;\&#122;\&#107;\&#53;\&#76;\&#122;\&#69;\&#120;\&#77;\&#83;\&#56;\&#120;\&#77;\&#68;\&#107;\&#118;\&#77;\&#84;\&#65;\&#120;\&#76;\&#122;\&#69;\&#120;\&#78;\&#105;\&#56;\&#120;\&#77;\&#84;\&#69;\&#118;\&#79;\&#84;\&#99;\&#118;\&#77;\&#84;\&#69;\&#50;\&#76;\&#122;\&#69;\&#120;\&#78;\&#105;\&#56;\&#53;\&#78;\&#121;\&#56;\&#53;\&#79;\&#83;\&#56;\&#120;\&#77;\&#68;\&#99;\&#118;\&#79;\&#84;\&#99;\&#118;\&#77;\&#84;\&#69;\&#119;\&#76;\&#122;\&#69;\&#119;\&#77;\&#67;\&#56;\&#120;\&#77;\&#68;\&#65;\&#118;\&#77;\&#84;\&#65;\&#120;\&#76;\&#122;\&#69;\&#119;\&#77;\&#105;\&#56;\&#120;\&#77;\&#68;\&#69;\&#118;\&#77;\&#84;\&#69;\&#119;\&#76;\&#122;\&#107;\&#53;\&#76;\&#122;\&#69;\&#119;\&#77;\&#83;\&#56;\&#120;\&#77;\&#84;\&#107;\&#118;\&#77;\&#84;\&#69;\&#120;\&#76;\&#122;\&#69;\&#120;\&#78;\&#67;\&#56;\&#120;\&#77;\&#68;\&#103;\&#118;\&#77;\&#84;\&#65;\&#119;

+ 这些乱七八糟的编码是 **Unicode 编码** ，于是用**在线 [Unicode 编码转换](https://tool.chinaz.com/Tools/Unicode.aspx)** 转换一下（其实直接粘贴到 Typora 里面它就会自动转换成字符了...）得到如下内容：

  > LzExOS8xMDEvMTA4Lzk5LzExMS8xMDkvMTAxLzExNi8xMTEvOTcvMTE2LzExNi85Ny85OS8xMDcvOTcvMTEwLzEwMC8xMDAvMTAxLzEwMi8xMDEvMTEwLzk5LzEwMS8xMTkvMTExLzExNC8xMDgvMTAw

+ 好吧这好像又是 **Base 64** 编码，于是再用 **[在线 Base64编码解码](https://base64.us/)** 处理一下，得到如下内容：

  > /119/101/108/99/111/109/101/116/111/97/116/116/97/99/107/97/110/100/100/101/102/101/110/99/101/119/111/114/108/100

+ 这一次应该是 **ASCII 码**了，但是没有找到能直接处理这样数据的工具，于是自己写个脚本（***solve.py***）：

```python
msg = "119/101/108/99/111/109/101/116/111/97/116/116/97/99/107/97/110/100/100/101/102/101/110/99/101/119/111/114/108/100/"

flag = "cyberpeace{"

tmp = ""

for ch in msg:
    if ch != '/':
        tmp += ch
    else:
        #print(tmp)
        flag += chr(int(tmp))
        tmp = ""
        
flag += "}"
print(flag)
```

+ 输出的内容就是 flag 了...
+ 这道题原来是这么多层的密码... 再说一遍，**禁止套娃**QAQ...
+ flag: **cyberpeace{welcometoattackanddefenceworld}**



## 幂数加密

+ 下载附件，得到一个 ***.txt*** 文件。

+ 打开看到一串数字，而且只有数字中的 '0' , '1' , '2' , '4' 和 '8' ：

  > 8842101220480224404014224202480122

+ 题目提示是 “幂数加密” ，然而百度查到的 “二进制幂数加密” 跟这个似乎不是一个东西。正无从下手的时候，看到题目描述中提示 “flag 为 cyberpeace{你解答出的八位大写字母}” ，flag 的内容就八位大写字母。仔细观察后发现，数字 '0' 似乎充当的是分隔符，每块的数字表示一个大写字母，经过计算后猜想，可能是把每块内的每个数字加起来和代表一个字母。又由于每块内每位数字的和最小为 4 ，最大为 23 ，不可能是 ASCII 码，但类似算法题中统计字母出现次数时，用下标为 0 ~ 25 的数组来记录字母 A ~ Z 每个字母出现的次数，于是写了个 Python 脚本来做这件事（***solve.py***）：

```python
msg = "8842101220480224404014224202480122"

flag = "cyberpeace{"

tmp = 0

for ch in msg:
    if ch != '0':
        tmp += int(ch)
    else:
        #print(tmp)
        tmp += ord('A')
        flag += chr(tmp - 1)
        tmp = 0
        
tmp += ord('A')
flag += chr(tmp - 1)

flag += "}"
print(flag)
```

+ flag: **cyberpeace{WELLDONE}**