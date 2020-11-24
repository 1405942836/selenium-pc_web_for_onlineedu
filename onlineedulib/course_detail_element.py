#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
课堂详情页页面元素
包括元素的封装，和控件的具体方法封装实现
方法依赖库：qt4w
'''

import time, os
from qt4w import XPath
from qt4w.browser.browser import IBrowser, Browser
from qt4w.webcontrols import  WebPage, WebElement, InputElement, SelectElement, FrameElement,IWebElement


class Course_Detail_Element():
    '''
    课程详情页页面元素封装
    '''
    ui_map = {'url_404':{'type': WebElement,'locator': XPath('//link[@href="https://ke.qq.com/404.html"]')},
              'url_502': {'type': WebElement, 'locator': XPath('//div[@class="error-code" and @jscontent="errorCode"]')},
              'url_403': {'type': WebElement, 'locator': XPath('//body[@bgcolor="white"]')},
              'body': {'type': WebElement, 'locator': XPath('//body')},
            'loginframe': {
                'type': FrameElement,
                'locator': XPath('//iframe[@name="login_frame_qq"]'),
                'ui_map': {
                    '帐号密码登录': XPath('//a[@id="switcher_plogin"]'),
                    '帐号': {'type': InputElement, 'locator': XPath('//input[@class="inputstyle" and @type="text"]')},
                    '清空账号': XPath('//a[@id="uin_del"]'),
                    '密码': {'type': InputElement, 'locator': XPath('//input[@class="inputstyle password" and @type="password"]')},
                    '登录qq': XPath('//input[@id="login_button" and @value="登 录"]'),
                    }
                },

            'course_task': {'type': WebElement, 'locator': XPath('//div[@class="before-btn play-btn"]')},
            'task': {'type': WebElement, 'locator': XPath('//li[@data-taid="3380594528670565"]')},
            'agency_logo': {'type': WebElement, 'locator': XPath('//img[@src="//p.qpic.cn/qqcourse/QFzQYCgCrxkME0JpnXdyHvL8Qp5ibroNYxoKLRGARbAiaB5PCBSeHPdnDQ6uibpdAg5/"]')},
            'agency_name': {'type': WebElement, 'locator': XPath('//a[@class="tt-link js-agency-name"]')},
            'teacher_logo': {'type': WebElement, 'locator': XPath('//img[@src="//10.url.cn/eth/ajNVdqHZLLB30NjBSlDo1SeeLd1bPnDPr3BMBJ1KfTe56iaFCz6QzRCyDqZ8tyfQ6sWZwTicMBvO8/"]')},
            'teacher_name': {'type': WebElement, 'locator': XPath('//a[@class="tt-link js-teacher-name" and @title="咕泡教育-Mic"]')},
            'aside_course_image': {'type': WebElement, 'locator': XPath('//img[@alt="课程封面"]')},
            'aside_course_link': {'type': WebElement, 'locator': XPath('//a[@class="aside-course-link"]')},
            'course_card_list': {'type': WebElement, 'locator': XPath('//li[@data-report-position="1"]')},
              }



    '''
    控件的具体方法封装实现
    '''
    # 点击logo
    def click_header_index_logo(self):
        self.control('header-index-logo').click()   # 点击该标签
        time.sleep(1)                           # 等待1s
        self.find_url_404()                     # 判断跳转链接是否404
        # self.exec_script('window.history.back()')
        self.exec_script('location.href = "https://ke.qq.com/course/185189"')   # 跳转回来原来的地址

    # 点击分类
    def click_fenlei_list(self):
        self.control('分类').click()
        time.sleep(2)
        self.find_url_404()
        self.exec_script('location.href = "https://ke.qq.com/course/185189"')
        # self.exec_script('location.href = "https://ke.qq.com/404.html"')

    # 选择课程
    def select_search_course(self):
        self.control('select-course').click()

    # 选择机构
    def select_search_agency(self):
        self.control('select-agency').click()

    # 点击搜索课程、机构
    def click_search(self):
        self.control('search-course').click()
        time.sleep(1)
        self.find_url_404()
        self.exec_script('location.href = "https://ke.qq.com/course/185189"')

    # 输入搜索词
    def search_keyword(self,keyword):
        self.control('search-keyword').value=keyword

    # 点击下载
    def click_download(self):
        self.control('download').click()

    # 点击登录
    def click_login(self):
        self.control('login').click()

    # 点击QQ登录
    def click_qq_login(self):
        self.control('qq_login').click()

    # 点击QQ登录(方法二)
    def click_qq_login_other(self):
        self.control('qq_login_other').click()

    # 点击切换QQ登录
    def click_qq_login_text(self, account, password):
        self.control('loginframe.帐号密码登录').click()
        self.control('loginframe.帐号').value = account
        self.control('loginframe.密码').value = password
        self.control('loginframe.登录qq').click()

    # 点击切换QQ登录
    # def click_qq_login_account(self, account):
    #     # self.control('qq_login_text').click()
    #     self.control('loginframe.帐号').value=account

    # 点击切换QQ登录
    # def click_qq_login_password(self, password):
    #     # self.control('qq_login_text').click()
    #     self.control('loginframe.帐号').value=password
    #     time.sleep(1)
    #     self.control('loginframe.登录qq').click()

    # 点击课程封面播放按钮
    def click_course_task(self):
        self.control('course_task').click()

    # 点击课程封面播放按钮
    def click_task(self):
        self.control('task').click()

    # 点击机构logo
    def click_agency_logo(self):
        self.control('agency_logo').click()
        time.sleep(1)
        self.find_url_404()
        # test = self.url
        # print test
        # print self.browser_type
        # print self.title
        # print self.cookie
        # print self.ready_state

    # 点击机构name
    def click_agency_name(self):
        self.control('agency_name').click()
        time.sleep(1)
        self.find_url_404()

    # 点击老师logo
    def click_teacher_logo(self):
        self.control('teacher_logo').click()
        time.sleep(1)
        self.find_url_404()

    # 点击老师name
    def click_teacher_name(self):
        self.control('teacher_name').click()
        time.sleep(1)
        self.find_url_404()

    # 点击关联付费课程封面
    def click_aside_course_image(self):
        self.control('aside_course_image').click()
        time.sleep(1)
        self.find_url_404()

    # 点击关联付费课程立即查看
    def click_aside_course_link(self):
        self.control('aside_course_link').click()
        time.sleep(1)
        self.find_url_404()

    # 点击底部课程卡片
    def click_course_card_list(self):
        self.control('course_card_list').click()
        time.sleep(1)
        self.find_url_404()



    '''
    浏览器通用方法实现：
    '''
    # 获取页面url
    def get_page_url(self):
        # self.activate()
        page_url = self.url
        return page_url

    # 执行js回退
    def run_exec_script(self):
        # self.exec_script('window.onerror = (e) => { console.error(e) };throw Error(123123)')
        self.exec_script('location.href = "https://ke.qq.com/404.html"')
        print ('test')

    # 断言是否为404、502、403页面，捕获js error
    def find_url_404(self, driver):
        # if self.exec_script('location.href === "https://ke.qq.com/404.html"') == 'true':        # 判断是否存在元素
        if driver.current_url == "https://ke.qq.com/404.html":  # 判断是否存在元素
            raise RuntimeError('This is 404 page!!!')
        else:
            print ("no 404 page, it's ok")

        # if self.control('url_502').exist == 'true':                 # 判断是否存在元素
        try:
            driver.find_element_by_xpath('//div[@class="error-code" and @jscontent="errorCode"]')       # 判断是否存在元素
            print('This is 502 page!!!')
        except:
            print("no 502 page, it's ok")
            # raise RuntimeError('This is 502 page!!!')

        # if self.control('url_403').exist == 'true':                 # 判断是否存在元素
        #     raise RuntimeError('This is 403 page!!!')
        # else:
        #     print ("no 403 page, it's ok")

        try:
            driver.find_element_by_xpath('//body[@bgcolor="white"]')            # 判断是否存在元素
            print('This is 403 page!!!')
        except:
            print("no 403 page, it's ok")

        # if self.exec_script('window.onerror') == 'false':           # 判断是否有js error
        #     raise RuntimeError('This is 502 page!!!')
        # else:
        #     print ("no js error page, it's ok")



