# -*- coding: utf-8 -*-
'''
课程详情页测试用例
'''

from onlineedulib.course_detail import Course_Detail        # 导入封装的方法库
from settings import URL, MAX_LEVEL                         # 导入settings中传进来的url和遍历层级

from selenium import webdriver                              # 导入selenium的浏览器驱动库
from webdriver_manager.chrome import ChromeDriverManager    # 导入chrome浏览器驱动管理库
import random, time


class Course_Detail_Test():
    '''
    方法功能：测试函数，程序入口
    '''
    def run_test(self):
        start = time.time()         # 获取当前时间

        # 初始化一个浏览器对象，打开URL的页面
        driver = webdriver.Chrome(ChromeDriverManager().install())
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

