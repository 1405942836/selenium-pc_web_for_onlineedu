# -*- coding: utf-8 -*-
'''
课程详情页测试用例
'''

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from selenium import webdriver                              # 导入selenium的浏览器驱动库
from webdriver_manager.chrome import ChromeDriverManager    # 导入chrome浏览器驱动管理库
import time

from onlineedulib.course_detail import Course_Detail        # 导入封装的方法库
from settings import URL, MAX_LEVEL                         # 导入settings中传进来的url和遍历层级


class Course_Detail_Test():
    '''
    方法功能：
    1、判断是在什么环境下运行
    2、no_ui win系统下默认为界面模式，无界面设为：True
    '''
    def is_driver(self, no_ui=False):
        if 'linux' in sys.platform:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')  # 浏览器不提供可视化页面
            option.add_argument('no-sandbox')  # 以最高权限运行
            option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
            option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            # option.add_argument('--window-size=1920,1080')  # 设置浏览器分辨率（窗口大小）
            driver = webdriver.Chrome(options=option)
        else:
            if no_ui:
                ''' win系统下无界面模式 '''
                option = webdriver.ChromeOptions()
                option.add_argument('headless')  # 浏览器不提供可视化页面
                option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）设置元素定位比较准确
                driver = webdriver.Chrome(chrome_options=option)
            else:
                # driver = webdriver.Chrome()
                driver = webdriver.Chrome(ChromeDriverManager().install())
                driver.maximize_window()  # 将浏览器最大化
        return driver


    '''
    方法功能：测试函数，程序入口
    '''
    def run_test(self):
        start = time.time()         # 获取当前时间

        # 初始化一个浏览器对象，打开URL的页面
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.is_driver()           # 类内部函数之间的调用，需要加上self，否则会被当成外部函数
        driver.get(URL)

        # 初始化自己封装的类对象
        detail = Course_Detail()
        detail.get_page_a_label(driver, MAX_LEVEL)       # 获取页面a标签
        detail.deduplication()      # 去重

        detail.processing(driver)   # 执行遍历点击a标签

        driver.quit()  # 关闭浏览器

        end = time.time()           # 获取当前时间
        print(end - start)          # 打印程序执行时间

if __name__ == '__main__':
    Course_Detail_Test().run_test()

