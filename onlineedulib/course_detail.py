#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

# 全局变量初始化
cache_history_finall = []       # 缓存历史点击过的a标签
num_404_success = 0             # 非404链接个数
num_404_failure = 0             # 404链接个数
num_502_success = 0             # 非502链接个数
num_502_failure = 0             # 502链接个数
num_403_success = 0             # 非403链接个数
num_403_failure = 0             # 403链接个数

'''
类的作用：封装了页面相关操作方法，实现自动遍历页面a标签并自动判断是否有异常
'''
class Course_Detail():
    '''
    方法功能：获取页面所有的a标签
    参数：
    max_level：遍历层级，默认为1
    driver：浏览器驱动的页面对象
    '''
    def get_page_a_label(self, driver = '', max_level = 1, traversal_level = 1):
        # 获取页面HTML代码
        body_element = driver.page_source

        # 利用正则查找所有a标签链接
        label_number = 0                    # 标签序号
        finall_link_list = []               # 去重前
        finall_link = []                    # 去重后，最终href链接列表
        global cache_history_finall         # 全局变量
        link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", body_element)    # 从HTML代码中查找a标签链接

        # 替换&转码过来的amp;，替换无效href链接
        for url in link_list:
            finall_link_list_sub1 = re.sub(r'amp;', "", url)
            finall_link_list_sub2 = re.sub(r'javascript:void\(0\)\;+', "", finall_link_list_sub1)
            finall_link_list_sub3 = re.sub(r'javascript:void\(0\)+', "", finall_link_list_sub2)
            finall_link_list_sub4 = re.sub(r'javascript:;+', "", finall_link_list_sub3)
            finall_link_list_sub5 = re.sub(r'javascript:+', "", finall_link_list_sub4)

            # 不在起始位置匹配
            if (re.match('//', finall_link_list_sub5)) == None:         # 没有查找到'//'，做一层透传
                finall_link_list_sub6 = finall_link_list_sub5
            else:
                finall_link_list_sub6 = re.sub(r'//', "https://", finall_link_list_sub5)    # 查找到'//'，替换为'https://'

            # 查找到'https://'，替换为'https://'，用于过滤没有'https://'头的链接
            if (re.match('https://', finall_link_list_sub5)) != None:
                finall_link_list_sub7 = finall_link_list_sub6
            else:
                continue

            # 用于过滤不想保留的链接，可以去掉
            if finall_link_list_sub7 != "" and finall_link_list_sub7 != 'http://learning.cjol.com' and finall_link_list_sub7 != 'http://assessment.cjol.com' and finall_link_list_sub7 != 'http://cjol.com':
                finall_link_list.append(finall_link_list_sub7)

        # 去重，用于去掉重复的链接
        for url in finall_link_list:
            if not url in finall_link:
                finall_link.append(url)

        # 打印遍历层级
        print ('The max_level is:' + str(max_level) + '+++++++++++++++')

        # 打印a标签链接
        for url in finall_link:
            label_number = label_number + 1
            print ('label_number' + str(label_number) + ':' + url)

        # 遍历所有标签，存储所有的标签链接
        for url in finall_link:
            cache_history_finall.append(url)
        print('cache_history_finall total length is:' + str(len(cache_history_finall)))

        # 递归实现循环遍历
        i = 0
        if traversal_level < max_level:  # 递归遍历层级
            for url in finall_link:
                driver.get(url)
                i = i + 1
                print('traversal_level:' + str(traversal_level) + '+' + str(len(cache_history_finall)) + '+' + str(i) + ' url is:' + str(url))
                self.get_page_a_label(driver, max_level, traversal_level + 1)


    '''
    方法功能：去重，用于去掉重复的链接
    参数：无
    '''
    def deduplication(self):
        for url in cache_history_finall:
            if not url in cache_history_finall:
                cache_history_finall.append(url)


    '''
    方法功能：在浏览器中遍历点击a标签
    参数：
    driver：浏览器驱动的页面对象
    '''
    def processing(self, driver):
        # 全局变量定义
        global num_404_success, num_404_failure
        global num_502_success, num_502_failure
        global num_403_success, num_403_failure
        for url in cache_history_finall:
            driver.get(url)
            self.assert_url(driver)
        print("num_404_success is:" + str(num_404_success) + "and num_404_failure is:" + str(num_404_failure))
        print("num_502_success is:" + str(num_502_success) + "and num_502_failure is:" + str(num_502_failure))
        print("num_403_success is:" + str(num_403_success) + "and num_403_failure is:" + str(num_403_failure))


    '''
    方法功能：断言是否为404、502、403页面，捕获js error
    参数：
    driver：浏览器驱动的页面对象
    '''
    def assert_url(self, driver):
        # 全局变量定义
        global num_404_success, num_404_failure
        global num_502_success, num_502_failure
        global num_403_success, num_403_failure
        # 判断打开的链接是不是404页面，使用if-else判断
        if driver.current_url == "https://ke.qq.com/404.html":
            num_404_failure += 1
            print('This is 404 page!!!')
        else:
            num_404_success += 1
            print("no 404 page, it's ok")

        # 查找页面是否有502的元素，推荐使用try-except判断
        try:
            driver.find_element_by_xpath('//div[@class="error-code" and @jscontent="errorCode"]')
            num_502_failure += 1
            print('This is 502 page!!!')
        except:
            num_502_success += 1
            print("no 502 page, it's ok")

        # 查找页面是否有403的元素，推荐使用try-except判断
        try:
            driver.find_element_by_xpath('//body[@bgcolor="white"]')
            num_403_failure += 1
            print('This is 403 page!!!')
        except:
            num_403_success += 1
            print("no 403 page, it's ok")

        # 判断是否有js error
        # if self.exec_script('window.onerror') == 'false':
        #     raise RuntimeError('This is 502 page!!!')
        # else:
        #     print ("no js error page, it's ok")



    # 合并两个页面标签，并去重，用于调试使用
    def get_two_page_num(self, traversal_level = 1, cache_history = []):
        print ('begin+++++++++++++++++++++++')
        body_element = self.control('body').inner_html
        attributes = self.control('body').attributes
        print (attributes)

        # 利用正则查找所有连接
        label_number = 0  # 标签序号
        num = 0
        finall_link_list = []
        finall_link = []  # 最终href链接列表
        cache_history_first = []
        cache_history_finall = []
        link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", body_element)
        # 替换&转码过来的amp;，替换无效href链接
        for url in link_list:
            finall_link_list_sub1 = re.sub(r'amp;', "", url)
            finall_link_list_sub2 = re.sub(r'javascript:void\(0\)\;+', "", finall_link_list_sub1)
            finall_link_list_sub3 = re.sub(r'javascript:void\(0\)+', "", finall_link_list_sub2)
            finall_link_list_sub4 = re.sub(r'javascript:;+', "", finall_link_list_sub3)
            finall_link_list_sub5 = re.sub(r'javascript:+', "", finall_link_list_sub4)
            if finall_link_list_sub5 != "" and finall_link_list_sub5 != 'http://learning.cjol.com' and finall_link_list_sub5 != 'http://assessment.cjol.com' and finall_link_list_sub5 != 'http://cjol.com':
                finall_link_list.append(finall_link_list_sub5)

        # 去重
        # finall_link = {}.fromkeys(finall_link_list).keys()
        for item in finall_link_list:
            if not item in finall_link:
                finall_link.append(item)

        # 打印遍历层级
        print ('The traversal_level is:' + str(traversal_level) + '+++++++++++++++')

        # 打印a标签链接
        for url in finall_link:
            label_number = label_number + 1
            print ('label_number' + str(label_number) + ':' + url)
            cache_history_first.append(url)

        if traversal_level == 1:
            self.exec_script('location.href="https://ke.qq.com"')
            self.get_two_page_num(traversal_level + 1, cache_history_first)

        if traversal_level == 2:
            # cache_history_finall.append(url)
            cache_history_first.extend(cache_history)
            cache_history_first = list(set(cache_history_first))
            label_number = 0
            for url in cache_history_first:
                label_number = label_number + 1
                print ('label_number_two_page' + str(label_number) + ':' + url)


    # 获取页面所有的a标签另一种方法
    def get_page_tag(self):
        print ('get_page_a_tag+++++++++++++++++++++++')
        tag = self.get_elements('//a[@href]')
        print (tag)
        i = 0
        for url in tag:
            i = i + 1
            element = self.control(url).inner_html
            print (element)
            # print tag
        print ('get_page_a_tag+++++++++++++++++++++++')





'''
备注
1.Python 异常处理
https://www.runoob.com/python/python-exceptions.html

'''
