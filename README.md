# health_auto_sign

### 江苏科技大学自动健康打卡
+ 1.利用python的selenium模块进行对网页表单中的元素进行匹配，源码这里放在了`auto_sign.py`中

+ 注意，这里我用的是chromedriver,需要自行查看google-chrome版本，以选择适合的chromedriver

+ 2.既然是每天都需要做的事情，自然不能每天打开电脑，运行一遍.所以，这里，我选择将脚本放在linux的服务器上，并制定一个计划任务，每天自动运行脚本。
