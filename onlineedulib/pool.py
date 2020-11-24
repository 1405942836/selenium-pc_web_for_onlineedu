#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
进程池方法实现
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from multiprocessing import Pool, cpu_count             # 导入cpu核数

# 全局变量
cache_history_finall = []       # 缓存历史点击过的a标签


class Pool():
# 进程池处理，打开多个chrome
    def processing_pool(self, res_list):
        print ('begin processing pool')
        url = "https://ke.qq.com/"
        # 打开多个浏览器窗口
        # browser = Browser("Chrome")
        # browser.open_url(url, Course_Detail)
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print(driver)
        page = driver.get(url)
        for url in res_list:
            # self.exec_script('location.href="%s"' % url)
            driver.get(url)
            self.find_url_404(driver)



        # 把所有的标签分组成5分，在浏览器中分别模拟点击所有a标签
        res_list = []           # 均分列表
        chrome_number = 5       # 打开5+1个浏览器窗口
        colnum = len(cache_history_finall) / chrome_number
        print(colnum)
        for i in range(0, len(cache_history_finall), int(colnum)):          # 强制转为int
            res_list.append(cache_history_finall[i:i + int(colnum)])

        # 创建一个进程池，里面最多cpu_count()个进程
        # p = Pool(cpu_count())
        pool = Pool(5)
        for i in range(0, chrome_number):
            pool.apply_async(self.processing_pool(res_list[i]), args=(res_list[i]))     # 进程池回调函数

        print ('Waiting for all sub processes done...')
        # 关闭进程池 关闭后po不再接受新的请求
        pool.close()
        # 等待po中所有子进程执行完成，必须放在close语句之后
        # 如果没有join，会导致进程中的任务不会执行
        pool.join()
        print ('All sub processes done.')

        print ('<The total traversal_level is:' + str(traversal_level) + 'and total len:' + str(len(cache_history_finall)))
        print ('end+++++++++++++++++++++++')

