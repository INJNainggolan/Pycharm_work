2017-10-29

知乎是自己经常用的一个app，经常看到知乎上很多人说知乎的很多的用户是程序员，也看到过有人爬取过有人知乎的用户然后进行分析。我就在想自己可不可以也通过python实现这个过程。

前面几次写了几个简单的爬虫，熟悉了爬虫基本的思路，这次是想写一个复杂一点的爬虫，尽量多的爬取更多的数据，并且能够避免爬取重复的内容。可能会用到数据库多线程等内容。

这几天都在忙学校的实验，没有更新github，一定要坚持啊啊啊啊啊啊啊啊！！！！！

redis中维护两个集合，一个list一个hash。list中作为待抓取的用户，hash中代表已经抓取过的用户

当找到新的用户url的时候，先在hash中查询是否存在该url，如果不存在，就将该url加入到list和hash中。要爬取用户数据的时候，从list弹出数据，进行爬取

防止爬虫被屏蔽

代理IP、ua、cookies、减速减速再减速

Bloom Filter算法(布隆过滤器)

```
                        CookieJar____
                        /     \      \
            FileCookieJar      \      \
             /    |   \         \      \
 MozillaCookieJar | LWPCookieJar \      \
                  |               |      \
                  |   ---MSIEBase |       \
                  |  /      |     |        \
                  | /   MSIEDBCookieJar BSDDBCookieJar
                  |/
               MSIECookieJar
```

Python中cookielib库（python3中为http.cookiejar）

CookieJar，FileCookieJar，MozillaCookieJar,LWPCookieJar

CookieJar对象存储在内存中

FileCookieJar(filename)创建FileCookieJar实例，检索cookie信息并将信息存储到文件中，filename是文件名。

MozillaCookieJar(filename)创建与Mozilla cookies.txt文件兼容的FileCookieJar实例。

LWPCookieJar(filename)创建与libwww-perl Set-Cookie3文件兼容的FileCookieJar实例。

参数ignore_discard=True表示即使cookies将被丢弃也把它保存下来，它还有另外一个参数igonre_expires表示当前数据覆盖（overwritten）原文件。注意，除非你通过传递一个真实的*ignore_discard*参数，否则`save()`方法不会保存会话cookie。



它们并不返回布尔值，而是返回它们实际进行比较的值之一。

对于and操作符：只要左边的表达式为真，整个表达式返回的值是右边表达式的值，否则，返回左边表达式的值对于or操作符：只要两边的表达式为真，整个表达式的结果是左边表达式的值。如果是一真一假，返回真值表达式的值如果两个都是假，比如空值和0，返回的是右边的值。（空值或0）

dump和dumps是将python对象转换成json格式；load和loads是将json格式转换成python对象

redis操作

在redis中维护两个集合：一个hash，一个list。 当从网页中抓取到一个url_token时，检查在hash中时候存在，如果不存在就将它放入list的尾部，作为还没有抓取的用户。当需要抓取用户信息的时候从list 的头部弹出一个url_token，进行抓取。当抓取完成后，将该url_token存取hash

redis数据库中的原始命令

HSET key field value 将哈希表 key 中的字段 field 的值设为 value 。

HEXISTS key field 查看哈希表 key 中，指定的字段是否存在。

BLPOP key1 [key2 ] timeout 移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。

RPUSH key value1 [value]在列表中添加一个或多个值



python random

random.random():生成一个[0, 1)之间的随机浮点数

random.uniformrandom.uniform(a, b):生成[a,b)之间的浮点数

random.randint(a, b):生成[a,b]之间的整数

random.randrange(a, b, step):在指定的集合[a,b)中,以step为基数随机取一个数.如random.randrange(0, 20, 2),相当于从[0,2,4,6,...,18]中随机取一个

python 多线程

join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

setDaemon() 默认情况下，主线程在退出时会等待所有子线程的结束。如果希望主线程不等待子线程，而是在退出时自动结束所有的子线程，就需要设置子线程为后台线程(daemon)。方法是通过调用线程类的setDaemon()方法。