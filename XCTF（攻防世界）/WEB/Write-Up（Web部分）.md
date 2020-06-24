# Write-Up（Web部分）

## view_source

+ 打开网页，只看到一个大大的 “FLAG is not here” 的提示。
+ 题目的提示是 **查看源代码** ，因此直接在火狐浏览器中按下 **F12** ，即可看到源代码中有一行注释。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF（攻防世界）/WEB/view_source/1.png?raw=true)

+ 注释中的内容就是flag。
+ flag: **cyberpeace{2d6b553891b29fd9ed11a89127bade69}**



## robots

+ 看到题目，直接想到可能与 **robots.txt** 有关。
+ 不了解 [**robots协议**](https://baike.baidu.com/item/robots%E5%8D%8F%E8%AE%AE/2483797?fr=aladdin) 的百度一下。
+ 在题目 **URL** 的后面加上 `/robots.txt` ，查看网站的 **robots.txt**：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/robots/1.png?raw=true)

+ 发现 **robots.txt** 中禁止了 **f1ag_1s_h3re.php** 的显示：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/robots/1.png?raw=true)

+ 直接在原 **URL** 后面加上 `/f1ag_1s_h3re.php` 。
+ f1ag_1s_h3re.php 页面中的内容就是 flag 。
+ flag: **cyberpeace{c1d5ab0f1dc36f04d10beed108ca8345}**



## cookie

+ 点开网页，发现一句话： “你知道什么是cookie吗？”。
+ 果断 **F12** ，然后在 **存储（storage）** 一栏看到 **cookie** ，数据内容里有一栏 **look-here: "cookie.php"**。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/cookie/1.png?raw=true)

+ 于是在 **URL** 后面加上 `/cookie.php` ，发现跳转到另一个网页，网页上显示一句话： “See the http response”。
+ 于是再次 **F12** ，在 **网络（Network）** 一栏下方选择 **cookie.php** ，并观察右侧 **响应头** 的内容，看到一行 **flag: cyberpeace{e46eded4dad3ed1d66bf4cfdaf86c531}**

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/cookie/2.png?raw=true)

+ flag: **cyberpeace{e46eded4dad3ed1d66bf4cfdaf86c531}**



## backup

+ 点开网页，发现一句话： “你知道index.php的备份文件名吗？”。
+ 实话说，真的不记得了QAQ...
+ 开始瞎猜，什么 **.bak** ，**.phpbak**，发现都不对。
+ 无奈之下百度，发现是 **.php~** 或者 **.php.bak** 。
+ 前者不对，后者输入 **URL** 地址栏后会提示下载一个 **bak文件** 。
+ 下载下来用 **notepad++** 打开，然后阅读代码发现其中有一段 **php** 代码里面有flag：

```php+HTML
<html>
<head>
    <meta charset="UTF-8">
    <title>备份文件</title>
    <link href="http://libs.baidu.com/bootstrap/3.0.3/css/bootstrap.min.css" rel="stylesheet" />
    <style>
        body{
            margin-left:auto;
            margin-right:auto;
            margin-TOP:200PX;
            width:20em;
        }
    </style>
</head>
<body>
<h3>你知道index.php的备份文件名吗？</h3>
<?php
$flag="Cyberpeace{855A1C4B3401294CB6604CCC98BDE334}"
?>
</body>
</html>

```

+ flag: **Cyberpeace{855A1C4B3401294CB6604CCC98BDE334}**



## disabled_button

+ 打开网页发现一个灰色的不能按的按钮，上面写着 “flag”。
+ 为了让他能按，按 **F12** ，发现这个按钮的 HTML 是这么写的：

```html
<input class="btn btn-default" disabled="" class="btn btn-default" style="height:50px;width:200px;" type="submit" value="flag" name="auth">
```

+ 于是尝试在 `disabled=""` 里面加上 false 变成 `disabled="false"` ，但是按钮依然不能按。
+ 填进去各种值都不成功，索性删掉，于是就能点了...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/disabled_button/1.png?raw=true)

+ 点下去即显示出一行 flag 。
+ flag: **cyberpeace{bf48a972642983285b427ee951f8a1d9}**



## weak auth

+ 打开网页看到一个登录页面。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/weak_auth/1.png?raw=true)

+ 一度以为是 **SQL注入** ，看提示发现应该不是—— “随手设了一个密码” 按时应该是弱口令可以爆破。
+ 先测试 **username** 是什么，直接点 **login** ，发现弹出一个提示框提示必须使用 **admin** 登录：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/weak_auth/2.png?raw=true)

+ 对于密码，打开 **burpsuite** ，考虑利用 **intruder** 爆破这个弱口令。
+ 首先设置 **burpsuite** 的 **proxy（代理）** ，**接口（interface）** 设为 **127.0.0.1:8080** 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/weak_auth/3.png?raw=true)

+ 接着在 **firefox（火狐）浏览器** 的 **preference** -> **proxy** 中设置 **Manual proxy configuration（手动设置代理）**，**HTTP Proxy** 设为 **127.0.0.1** ，**Port** 设为 **8080**，与 burpsuite 中 代理的设置一致即可。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/weak_auth/4.png?raw=true)

+ 然后随便填写一个 username 和 password 以后，在 burpsuite 中把拦截到的页面 **Send to Intruder** ，然后在 **Intruder** 中的 **Payloads** 选项卡中设置 **Payload** 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/weak_auth/5.png?raw=true)

+ 这个页面的 **Payload Sets** 有两个需要设置：

  + 第一个是 **username** ，直接在 **Payload type** 中选择 **Simple list** 即可；然后在 **Payload Options** 中添加唯一字段 **admin** 即可。

  ![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/weak_auth/6.png?raw=true)

  + 第二个是 **password** ，这个字段可以通过设定密码可能的字符范围和类型进行**暴力破解**，也可以准备一个**弱口令字典**爆破（能不能成功要看提供的字典是否正好包含了正确的密码）。在 **Payload type** 中选择 **Simple list** ；然后在 **Payload Options** 中使用 **load** 选项从弱口令字典中导入所有的弱口令字段即可。

  ![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/weak_auth/7.png?raw=true)

+ 设置完以后就可以开开心心的点下页面右上角的 **start attack** 按钮了。

+ 爆破过程长短与计算机的计算能力以及字典的大小有关（大概吧）... 爆破过程中注意观察弹出的窗口中的爆破状态，特别注意 **Length** 项。当某个 username 和 password 组合对应的 **Length** 长度与众不同时，说明这个 username 和 password 组合很可能就是正确的组合（图中显示 Length 与众不同的 username 为 **admin**，password 为 **123456**）

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/weak_auth/8.png?raw=true)

+ 在网页中使用上述的组合尝试登录，页面跳转到一个新的页面，即得到 flag。
+ flag: **cyberpeace{b0bc0057eb39e23d1c5a8e711370f66b}**



## simple_php

+ 听说 “php是最好的语言” ？[滑稽] [滑稽]
+ 打开网页就看到一坨写的很丑的 php 代码（好吧我 php 可能写的差不多也这样）...

```php
<?php
show_source(__FILE__);
include("config.php");
$a=@$_GET['a'];
$b=@$_GET['b'];
if($a==0 and $a){
    echo $flag1;
}
if(is_numeric($b)){
    exit();
}
if($b>1234){
    echo $flag2;
}
?>
```

+ 分析代码，大意是 flag 包括两段，分别由变量 `$flag1` 和 `$flag2` 接起来得到。
+ 要显示这两个变量，需要用 **GET 方法** 传变量 `a` 和变量 `b` 的参数。
+ 对于变量 `a` ，需要满足 `$a==0 and $a` ，看起来不合逻辑（ `a` 的值要为 0 ，又要 `a` 的值不是 `false`）。这里要利用 php 语言的特点——弱类型语言，php 中的 `==` 是比较运算符，不会检查条件表达式的类型是否相同（与 `===` 恒等运算符区别，`===` 会检查条件表达式类型是否相同） 。因此只需要在 **URL** 后面输入 `?a=0a` 即可，比较的时候 php 发现 0 后面的 a 不是数字，直接截断，只取前面的 0 。这样就使得 `echo $flag1; ` 语句能被执行。
+ 也可以输入 `?a=a` 或 `?a=[]` 同样能符合逻辑~
+ 对于变量 `b` ，要使其不满足 `is_numeric($b)` 的判断，又要使其满足 `$b>1234` 的判断。php 中 `is_numeric()` 函数是用来判断是否是数字和数字字符串的。因此同样用对变量 `a` 使用过的小伎俩，在 **URL** 后面输入 `?a=0a&b=1235a` 即可。php 会截去 1235 后面不是数字的 a 字符，但是却能将变量 `b` 判定为不是数字（所以你们还说 php 是世界上最好的语言吗？[滑稽] [滑稽]）。
+ 正确输入 URL 后得到完整的 flag 。
+ flag: **Cyberpeace{647E37C7627CC3E4019EC69324F66C7C}**



## get_post

+ 打开网页，看到一行字 “请用GET方式提交一个名为a,值为1的变量”。

+ 直接在 **URL** 后面加上 `?a=1` 即可。

+ 回车后又出现一行字 “请再以POST方式随便提交一个名为b,值为2的变量”。

+ **POST方法** 无法像 GET 方法一样直接在地址栏修改 URL 得到。解决方法有两种：

  + 在火狐浏览器中安装插件 **hackbar** ，安装成功后按 **F12** ，可以看到导航栏的最后一项多了一个 **hackbar** 。此时先点击 **Load URL** ，然后再勾上 **Post data** 的勾选框，并在下方弹出的输入框中填上 `b=2`，最后点击 **Execute** 即可得到 flag。

  ![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/get_post/1.png?raw=true)

  + 使用 **Burpsuite** 。在使用 GET 方法收到显示了第二行字的新网页后，点击 **Send to Repeater** 。在 Repeater 中修改 Headers，把原来的 **GET** 改为 **POST** ，然后点击 **Send**，发现并没有得到 flag 。百度发现使用 POST 方法需要添加 **Content-Type** 和 **Content-Length** 字段，最后在 **raw** 中直接添加 `b=2` 才能成功。

  ![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/get_post/2.png?raw=true)

+ flag: **cyberpeace{c9b6fecf90fe60bc102f5f4b45e249f8}**



## xff_referer

+ 打开网页，发现一行很小的字 “ip地址必须为123.123.123.123” 。

+ 又要上 **Burpsuite** 了，用 Burpsuite 修改发送的数据，在 **Header** 中添加一行 `X-Forwarded-For: 123.123.123.123` ，使满足 IP 为 123.123.123.123 。

  > **X-Forwarded-For**（**XFF**）是用来识别通过 HTTP 代理或负载均衡方式连接到 Web 服务器的客户端最原始的 IP 地址的 HTTP 请求头字段。

+ 点击 **Send** 后发现多了一行 `<script>` 的内容：

```html
<script>
    document.getElementById("demo").innerHTML="必须来自https://www.google.com";</script>
```

+ 于是按照要求添加 **Referer** 的值：`Referer: https://www.google.com` ，即可得到 flag。

  > 当浏览器向 web 服务器发送请求的时候，一般会带上 Referer ，告诉服务器该网页是从哪个页面链接过来的，服务器因此可以获得一些信息用于处理。
  >
  > Referer 的正确英语拼法是 referrer 。由于早期 HTTP 规范的拼写错误，为了保持向后兼容就将错就错了。其它网络技术的规范企图修正此问题，使用正确拼法，所以拼法不统一。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/xff_referer/1.png?raw=true)

+ flag: **cyberpeace{36017c947d347900bf6bc21882924614}**



## webshell

+ 打开网页，看到如下内容：

  > ### 你会使用webshell吗？
  >
  > <?php @eval($_POST['shell']);?>

+ 【来自解题过后的百度】关于 webshell ：

  > + webshell 就是就是 web 的一个管理工具，可以对 web 服务器进行操作的权限，也叫 webadmin 。webshell 一般是被网站管理员用于网站管理、服务器管理等等一些用途，但是由于 webshell 的功能比较强大，可以上传下载文件，查看数据库，甚至可以调用一些服务器上系统的相关命令（比如创建用户，修改删除文件之类的），通常被黑客利用，黑客通过一些上传方式，将自己编写的 webshell 上传到 web 服务器的页面的目录下，然后通过页面访问的形式进行入侵，或者通过插入一句话连接本地的一些相关工具直接对服务器进行入侵操作。
  >
  > + webshell 根据脚本可以分为 PHP 脚本， ASP 脚本，也有基于 .NET 的脚本和 JSP 脚本。在国外，还有用 Python 脚本语言写的动态网页，故也有与之相关的 webshell 。
  >   根据功能也分为大马与小马，小马通常指的一句话木马，例如：`<%eval request(“pass”)%>` 通常把这句话写入一个文档里面，然后文件名改成 xx.asp 。然后传到服务器上面。这里 eval 方法将 request(“pass”) 转换成代码执行，request 函数的作用是应用外部文件，这相当于一句话木马的客户端配置。

+ 于是 **F12** ，用 **hackbar** 先点击 **Load URL** 再勾上 **Post data** 勾选框，然后开始倒腾...

+ ... （以下省略 N 多无效操作...）

+ 在 Post data 下面的输入框中输入 `shell=print_r(getcwd());` 在页面上打印出当前页面对应的 html 文件所在的目录。

  > getcwd函数：获取当前工作目录

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/webshell/1.png?raw=true)

+ 页面显示当前目录为 `/var/www/html`，于是输入 `shell=print_r(scandir("/var/www/html"));` 在页面上打印出当前页面所在工作目录下的所有文件（及目录）。

  > scandir函数：列出指定路径中的文件和目录

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/webshell/2.png?raw=true)

+ 页面显示内容为 `Array ( [0] => . [1] => .. [2] => flag.txt [3] => index.php ) <?php ` 。发现当前目录下隐藏着一个 **flag.txt** 文件，于是直接在 **URL** 后面加上 `/flag.txt` 即可访问 **flag.txt** 文件，得到 flag 。
+ 也可以输入 `shell=system("ls");` 在页面上打印出当前页面对应的 html 文件所在的目录，然后再输入 `shell=system('cat flag.txt');` 在页面上直接打印出 **flag.txt** 的内容。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/webshell/3.png?raw=true)

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/webshell/4.png?raw=true)

+ ... （心态崩了，看来我的 PHP 需要回炉重学QAQ）
+ 这里最省事的方法其实是用工具 **“中国菜刀”** 或者 **“中国蚁剑”** ... 涨姿势了QAQ
+ flag: **cyberpeace{1314db684c1a2094dd83e1f495920623}**



## command_execution

+ 打开网页，发现网页中有个输入框，让你输入一个 IP 地址，然后有个 ping 按钮：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/command_execution/1.png?raw=true)

+ 随便输入一个 IP 地址试试，发现这个网页实际上很类似一个 cmd 的窗口：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/command_execution/2.png?raw=true)

+ 注意题目的提示：“小宁写了个ping功能,但没有写waf” ，百度一下就知道什么是 waf ：

  > Web 应用防护系统（Web Application Firewall，简称 WAF，也称网站应用级入侵防御系统）。利用国际上公认的一种说法：Web应用防火墙是通过执行一系列针对 HTTP/HTTPS 的安全策略来专门为 Web 应用提供保护的一款产品。

+ 考虑到该网页后台服务器应该是 Linux/Unix 系统，故尝试使用 Linux 命令中的管道来执行一些别的命令。首先尝试显示当前网页所在的目录下的所有文件，对应 Linux 中的命令 `ls` ，在输入框中输入内容如下：`127.0.0.1 | ls` ，发现能成功执行：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/command_execution/3.png?raw=true)

+ 此时可以利用 Linux 命令查看上级目录的内容： `127.0.0.1 | ../` ，但对 Linux 系统熟悉的话，可以直接查看系统主目录（ **/home** ）下的内容（从根目录下开始查看）： `127.0.0.1 | ls /home` ：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/command_execution/4.png?raw=true)

+ 很巧的发现了主目录下有个 **flag.txt** 文件。于是再用 Linux 命令打开这个文件：`127.0.0.1 | cat /home/flag.txt`，顺利得到 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/command_execution/5.png?raw=true)

+ flag: **cyberpeace{d5646eacf9bd2cde07262689a97034be}**



## simple_js

+ 打开网站，弹出一个对话框，对话框里有一个输入框，要求往输入框里输入密码：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/simple_js/1.png?raw=true)

+ 随便输入个密码进去，弹出一个新的对话框，内容为 “FAUX PASSWORD HAHA”，大意是密码错误...

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/simple_js/2.png?raw=true)

+ 点击确定后即可按 **F12** 查看该页面的 JavaScript 代码，代码很长还很乱，整理后如下：

```JavaScript
function dechiffre(pass_enc){
    var pass = "70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65";
    var tab  = pass_enc.split(',');
    var tab2 = pass.split(',');
	var i,j,k,l=0,m,n,o,p = "";
	i = 0;
	j = tab.length;
    k = j + (l) + (n=0);
    n = tab2.length;
    for(i = (o=0); i < (k = j = n); i++ ){
		o = tab[i-l];
		p += String.fromCharCode((o = tab2[i]));
        if(i == 5)
			break;
	}
    for(i = (o=0); i < (k = j = n); i++ ){
        o = tab[i-l];
        if(i > 5 && i < k-1)
            p += String.fromCharCode((o = tab2[i]));
    }
    p += String.fromCharCode(tab2[17]);
    pass = p;
	eturn pass;
}
String["fromCharCode"](dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"));

h = window.prompt('Enter password');
alert( dechiffre(h) );
```

+ 看了半天发现，输入到输入框中的内容经过处理存在变量 `tab` 中，然而无论输入什么，都会被变量 `tab2` 给覆盖掉，而 `tab2` 的内容是代码中写死的。利用 Python 输出 `tab2` 后发现 `tab2` 的值即为之前随便输入某个密码时弹出的提示 “FAUX PASSWORD HAHA” 。处理文件为 **get_output.py** ：

```Python
msg = [70,65,85,88,32,80,65,83,83,87,79,82,68,32,72,65,72,65]

output = ""

for i in msg:
    output += chr(i)
    
print(output)
```

+  所以无论输入密码是什么，都会提示你输入的密码有误...
+ 好吧，于是继续看代码，发现代码中有一行内容十分可疑：

```javascript
String["fromCharCode"](dechiffre("\x35\x35\x2c\x35\x36\x2c\x35\x34\x2c\x37\x39\x2c\x31\x31\x35\x2c\x36\x39\x2c\x31\x31\x34\x2c\x31\x31\x36\x2c\x31\x30\x37\x2c\x34\x39\x2c\x35\x30"));
```

+ 于是用 Python 处理一下，得到一串字符串，按照格式提交上去发现就是 flag ...
+ 处理文件为 **get_flag.py** :

```python
msg = ['0x35', '0x35', '0x2c', '0x35', '0x36', '0x2c', '0x35', '0x34', '0x2c', 
       '0x37', '0x39', '0x2c', '0x31', '0x31', '0x35', '0x2c', '0x36', '0x39', 
       '0x2c', '0x31', '0x31', '0x34', '0x2c', '0x31', '0x31', '0x36', '0x2c',
       '0x31', '0x30', '0x37', '0x2c', '0x34', '0x39', '0x2c', '0x35', '0x30']

tmp = ""

for i in msg:
    tmp += chr(int(i, 16))

tmp = tmp.split(',')
#print(tmp)

flag = ""

for i in tmp:
    flag += chr(int(i, 10))

print("Cyberpeace{" + flag + "}")
```

+ 这题好折腾人啊QAQ...
+ flag: **Cyberpeace{786OsErtk12}**



## baby_web

+ 打开网页，看到只有左上角一行 “HELLO WORLD” ...
+ 题目的提示是 “想想初始页面是哪个” ，于是查看了一下网页的 **URL** ，发现是 **1.php** ，显然不是初始页面（初始页面应该是 **index.php**）。
+ 于是按下 **F12** ，然后把 URL 的 `/1.php` 改为 `/index.php` ，改完以后发现页面飞快的又跳转回了 **1.php** ，似乎什么都没有发生。但是导航栏的网络那一栏出现了一行 index.php 。
+ 查看其响应头发现其中有一项 **FLAG** ，对应内容即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/baby_web/1.png?raw=true)

+ flag: **flag{very_baby_web}**



## Training-WWW-Robots

+ 打开网页，一看又是关于 robots 协议的题目。
+ 老套路，在 URL 栏最后面补上 `/robots.txt` ，看到 **robots.txt** 的内容：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/Training-WWW-Robots/1.png?raw=true)

+ 看到对于一般的 User-agent ，**/fl0g.php** 页面被禁止访问。猜测 flag 很可能就在这个页面里，于是直接在 URL 栏最后面把 `/robots.txt` 修改为 `/fl0g.php` ，就得到了 flag 。
+ flag: **cyberpeace{8c99fae35728becfbe1c0032207a99b4}**



## ics-06

+ 打开网页，看到一个貌似很酷的平台：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/ics-06/1.png?raw=true)

+ 然后开始瞎点，发现网页里的大部分东西点击了都没有任何效果，只有一个按钮选项 “报表中心” 点击以后跳转到另外一个页面：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/ics-06/2.png?raw=true)

+ 页面中有个 “日期范围” 可以选择，但是折腾半天并没有发现什么 bug，而且尝试选择日期范围后点击 “确认” 以后网页也没有任何反应（或者跳转）。
+ 正在懵逼中发现 URL 栏有用 **GET方法** 传参数 **id**，尝试改变参数 id 的值发现没什么变化（感觉可能需要找到会变化的参数值），于是打开 burpsuite 爆破。
+ 抓包，然后点击 **Send to Intruder** ，**Payloads** 处设置爆破 id 参数的类型为 **Numbers** ，范围先设置为 1 - 100 。
+ 发现 Result 中的 Length 字段值一直是 1866 没有变化，于是继续尝试更大的 id 。
+ 一直试到 **id = 2333** 时（其实我只试到了 1000 就心态崩了，Burpsuite Community 版的貌似不支持多线程爆破，导致爆破速度极慢orz），发现 Length 字段值为 1901 与之前的都不同，查看 **Response** 发现多了一行字，即为 flag 。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/ics-06/3.png?raw=true)

+ flag: **cyberpeace{3efd547a84695f0489cc235d4579f7c8}**



## NewsCenter

+ 打开网页看到一个很朴素的页面，类似一个普通的新闻查询页面，页面正中间有一个搜索框：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NewsCenter/Hacker_News.png?raw=true)

+ 在搜索框中输入任意内容，例如输入 <code>1</code> 发现除了底下 **News** 部分显示出包含字段 <code>1</code> 的新闻以外，什么都没有发生，没有 **alert弹窗** 之类的。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NewsCenter/01.png?raw=true)

+ 猜测可能是 **SQL注入** ，首先尝试如下语句注入 `' and 1 = 1#` 什么都没发生...
+ 修改注入语句如下 `' and 1 = 2#` ，News部分变为空白，显然该 SQL 语句有效。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NewsCenter/02.png?raw=true)

+ 利用union联合注入试探该sql查询返回的列数，首先尝试 1 列 `' and 1 = 2 union select 1#` ，页面跳转显示无法访问，说明不是 1 列。

+ `' and 1 = 2 union select 1, 2#` 同样失败。

+ `' and 1 = 2 union select 1, 2, 3#` 时，News部分出现内容

  > **2**
  >
  > 3

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NewsCenter/03.png?raw=true)

+ 于是进一步查询数据库中所有的数据表名 `' and 1 = 2 union select 1, TABLE_SCHEMA, TABLE_NAME from INFORMATION_SCHEMA.COLUMNS #` ，发现一个 **secret_table** 表：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NewsCenter/03.png?raw=true)

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NewsCenter/05.png?raw=true)

+ 查询 **secret_table** 表中的所有字段 `' and 1 = 2 union select 1, 2, COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME = 'secret_table' #` ，发现表中字段如下：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NewsCenter/06.png?raw=true)

+ **fl4g** 字段非常引人注目，猜测可能其中隐藏着 **flag**，因此进一步查询 **fl4g** 的内容 `' and 1 = 2 union select 1, 2, fl4g from secret_table #`
+ 成功得到 flag 。
+ flag: **QCTF{sq1_inJec7ion_ezzz}**



## NaNNaNNaNNaN-Batman

+ 附件里是个没有后缀的文件，打开看发现很像 **JavaScript** 的代码，但是好多乱码字符...
+ 后缀改成 **.html** ，然后在浏览器中打开看看，发现竟然能运行orz，出来一个输入框，后面还有一个 “ok” 按钮（ **web100.html** 文件）：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NaNNaNNaNNaN-Batman/1.png?raw=true)

+ 直接点击没反应，随便输入点什么也没反应...
+ 于是滚去读源代码，发现代码的最后有一段 `eval(_)` ，而函数名就为 `_` 。JavaScript 中的 `eval()` 函数可计算某个字符串，并执行其中的的 JavaScript 代码。故改成 `alert(_)` 让其在弹窗中显示正常的 JavaScript 内容，结果如下（ **text1.html** 文件）：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/NaNNaNNaNNaN-Batman/2.png?raw=true)

+ 将弹窗中的内容复制到新文件中（ **JavaScript.js** ），整理后得到如下代码：

```javascript
function $(){
	var e=document.getElementById("c").value;
	if(e.length==16)
		if(e.match(/^be0f23/)!=null)
			if(e.match(/233ac/)!=null)
				if(e.match(/e98aa$/)!=null)
					if(e.match(/c7be9/)!=null){
						var t=["fl","s_a","i","e}"];
						var n=["a","_h0l","n"];
						var r=["g{","e","_0"];
						var i=["it'","_","n"];
						var s=[t,n,r,i];
						for(var o=0;o<13;++o){
							document.write(s[o%4][0]);
							s[o%4].splice(0,1)
						}
					}
}
document.write('<input id="c"><button onclick=$()>Ok</button>');
delete _
```

+ 仔细阅读后发现，flag 就在 `var s=[t,n,r,i]` 中，然后通过下一行的一层 `for` 循环打印出来。对代码熟悉的话研究一下就能直接写出 flag （需要知道 `splice()` 函数的作用）。

  > `splice()` 方法向/从数组中添加/删除项目，然后返回被删除的项目。
  >
  > <code>arrayObject.splice(index,howmany,item1,.....,itemX)</code>
  >
  > 参数：
  >
  > + `index` ：必需。整数，规定添加/删除项目的位置，使用负数可从数组结尾处规定位置。
  > + `howmany` ：必需。要删除的项目数量。如果设置为 0，则不会删除项目。
  > + `item1, ..., itemX` ：可选。向数组添加的新项目。
  >
  > 返回值：
  >
  > + `Array` ：包含被删除项目的新数组，如果有的话。

+ 否则对正则表达式了解的话也可以利用前面的几个 `if` 判断条件来得到应该在输入框中输入的字符串为 **be0f233ac7be98aa** （字符串**长度为 16** ，字符串**前缀必须为 be0f23** ，**后缀必须为 e98aa** ，**必须包含子串 233ac 和 c7be9** ），在输入框中输入该字符串即可得到 flag 。

+ flag: **flag{it's_a_h0le_in_0ne}**



## PHP2

+ 打开网页，看到一行字 “Can you anthenticate to this website?”。

+ 感觉大概是要以一个什么类似管理员或者有权限的用户的身份来访问这个网页才能得到 flag 。

+ 还是 **F12** ，然后查看网络选项卡里的消息头，并没有在响应头里面发现什么有价值的信息，cookie 选项则显示 “此请求无 cookie ” 。

+ 想到题目的名字是 **PHP2** ，于是尝试在 URL 后面加上 `/index.php` ，发现是个一模一样的网页，而且 F12 里面也没有什么新鲜的东西。

+ 既然是 PHP 页面，而页面显示给我的内容只有 HTML 的内容，因此就想查看 index.php 的源代码，尝试之前的套路试图查看备份文件 **index.php~** 或者 **index.php.bak** ，很不幸的是一无所获...

+ 各种查资料百度以后才知道应该通过 **index.phps** 查看（如果这个文件在服务器上能访问的话...）页面的 PHP 源代码。

  > + phps 文件就是 php 的源代码文件，通常用于提供给用户（访问者）直接通过 Web 浏览器查看 php 代码的内容。
  >
  > + 因为用户无法直接通过 Web 浏览器 “看到” php 文件的内容，所以需要用 phps 文件代替。
  >
  > + 其实，只要不用 php 等已经在服务器中注册过的MIME类型的文件扩展名即可，但为了国际通用，所以才用了 phps 文件类型。
  >
  > + phps 文件的 MIME 类型为：text/html, application/x-httpd-php-source, application/x-httpd-php3-source 。

+ 涨姿势了，于是在 URL 地址后面补上 `/index.phps` ，看到页面上显示出一行 “not allowed!” 以及一段有点像 php 但是很奇怪的代码...

```php
"); exit(); } $_GET[id] = urldecode($_GET[id]); if($_GET[id] == "admin") { echo "

Access granted!
"; echo "

Key: xxxxxxx
"; } ?> Can you anthenticate to this website? 
```

+ 起码能读懂代码，看到里面有个判断语句，当通过 URL 地址传参数 `id=admin` 时，页面会显示 **Access granted!** ，并且显示 **Key** 。

+ 于是满心欢喜的在 URL 地址后面补写上 `id=admin` ，结果得到了还是 “not allowed!” 的提示。

+ 再次阅读代码，发现 if 判断语句之前用了一个 `urldecode()` 函数，定义和用法如下：

  > **定义和用法**
  >
  > + `urldecode()` 解码 URL 字符串函数。
  >
  > + 此函数用于解码给出的已编码字符串中的任何 %## 以及中文等被编码的内容。 （加号（'+'）被解码成一个空格字符）。
  >
  > + 该函数经常被使用于 php 解码 URL 中的中文字符串。
  >
  > **语法**
  >
  > `string urldecode ( string $str )`

+ 猜测可能 admin 字符串被过滤了，因此将其替换成 ASCII 码后，得到的 payload 为 `id=%61%64%6D%69%6E` 。

+ 修改 URL 后很不幸再次得到一个 “not allowed!” 的提示... 仔细查看代码以及函数 `urldecode()` 的用法，发现一个重要的情况：

  > Note:
  > 注意：超全局变量 `$_GET` 和 `$_REQUEST` **已经被解码了**。对 `$_GET` 或 `$_REQUEST` 里的元素使用 `urldecode()` 将会导致不可预计和危险的结果。

+ 破案了，原来是因为用 `$_GET[id]` 的时候已经把我的 ASCII 码转换为字符了，因此需要再对 ASCII 码进行一次转换，即将 'admin' 转换为 ASCII 码后还要再对得到的 ASCII 码再次转换... （说好的**禁止套娃**呢...）

+ 最后得到一串编码，在 URL 地址最后补上 `/id=%25%36%31%25%36%34%25%36%44%25%36%39%25%36%45` ，即可在跳转后的页面中得到 flag 。

+ flag: **cyberpeace{b9fcfa7f54ab9b3d5f89944c04078154}**



## unserialize3

+ 打开页面，发现一段不完整的 php 代码：

```php
class xctf{
public $flag = '111';
public function __wakeup(){
exit('bad requests');
}
?code=
```

+ 题目叫做 “unserialize3” ，猜测跟 php 的反序列化有关，可能要在 URL 栏后面补上 `?code='(unserialized string)'` ，即用 GET 方法传参数，参数为该段代码反序列化后的序列。
+ 先将这段不完整的 php 代码补完整：

```php
<?php
class xctf{
	public $flag = '111';
	public function __wakeup(){
		exit('bad requests');
	}
}
$obj = new xctf();
$str = serialize($obj);
echo $str;
?>
```

+ 利用 [php 在线工具](https://c.runoob.com/compile/1)将其序列化，得到序列化后的字符串：

  > O:4:"xctf":1:{s:4:"flag";s:3:"111";}

+ 将这个字符串作为参数用 GET 方法传入 URL ，得到了一个 “bad request” 的页面。

+ 仔细阅读代码，发现类 `xctf` 中调用了一个 php 魔术函数 `__wakeup()` ，百度得知该函数会在**类的实例的序列化串被反序列化时触发（被调用）**，而这个函数一旦触发就会直接在网页上显示 bad request 并直接结束；因此要设法让这个函数在反序列化时不被调用。

+ 百度关于 php 的序列化和反序列化，了解到 php 序列化的格式如下：

  > 对象（object）通常被序列化为：
  >
  > O:<对象名字符长度>:<对象名（字符串）>:<对象包括的属性（字段）数量>:{<对象属性（字段）1类型>:<对象属性（字段）1 的长度>:<对象属性（字段）1 的内容>;<对象属性（字段）1 所对应的字段值类型>:<对象属性（字段）1 所对应的字段值长度>:<对象属性（字段）1 所对应的字段值内容>;<对象属性（字段）2 类型>:<对象属性（字段）2 的长度>:<对象属性（字段）2 的内容>;<对象属性（字段）2 所对应的字段值类型>:<对象属性（字段）2 所对应的字段值长度>:<对象属性（字段）2 所对应的字段值内容>;...;}
  >
  > 
  >
  > 当序列化字符串中，表示对象属性个数的值大于实际属性个数时，`__wakeup()` 方法将不会被执行。

+ 因此，将序列修改为 **O:4:"xctf":2:{s:4:"flag";s:3:"111";}** ，在序列前面加上 `?code=` 后补在 URL 地址后面即可得到 flag 。

+ 实际上也可以修改序列中别的值，例如如下的修改方案均可得到 flag 值：

  > + O:3:"xctf":1:{s:4:"flag";s:3:"111";}
  > + O:4:"xctf":1:{s:3:"flag";s:3:"111";}
  > + O:4:"xctf":1:{s:4:"flag";s:4:"111";}

+ 附上 [php 在线反序列化工具](https://www.w3cschool.cn/tools/index?name=unserialize)。

+ flag: **cyberpeace{c0b46ec16da5f1d926126639bbeb749e}**

