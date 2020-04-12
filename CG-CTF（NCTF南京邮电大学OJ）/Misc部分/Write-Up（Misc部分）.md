# Write-Up（Misc部分）

## MD5

+ 想了想好像没有什么直接试出来的捷径（也许有但我不会），于是就写了个暴力枚举每个 **?** 位代表的字符然后求其 **MD5** 值的 **Python** 脚本...
+ 实际上脚本是个很丑的 **dfs** （毕竟 **ACM** 是我的老本行hhhhhh）。

```Python
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
```

+ 一度因为把密文明文搞反而死活求不出答案（雾）...
+ flag: **nctf{e9032994dabac08080091151380478a2}**

