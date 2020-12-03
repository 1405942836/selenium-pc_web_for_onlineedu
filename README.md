1.项目结构：
onlineedulib                    -项目库文件夹
    course_detail.py            -封装页面操作方法
    course_detail_element.py    -元素封装文件
    pool.py                     -进程池实现文件
onlineedutest                   -项目测试用例文件夹
    course_detail.py            -页面测试用例（for window system）
    course_detail_linux.py      -页面测试用例（for Linux system）
settings.py                     -配置文件
requirements.txt                -库文件配置
README.md                       -操作说明文件

2.安装python依赖：
pip install -r requirements.txt

3.测试方法：
进入onlineedutest，执行course_detail.py：python course_detail.py

4.root url可配置：
可以设置要自动遍历的URL链接，在setting文件中的URL

4.遍历层级可配置：
可以设置遍历层级，在setting文件中的MAX_LEVEL

备注：
有任何问题欢迎联系我QQ/微信：1405942836，欢迎一起探讨
