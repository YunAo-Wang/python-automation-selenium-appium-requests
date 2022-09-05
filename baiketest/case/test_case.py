# -*- coding: utf-8 -*-
__author__ = ''

import unittest
from selenium import webdriver
from business.login_business import LoginBusiness
from logs.user_log import UserLog
from time import sleep
from util.excel import ExcelUtil
import ddt
import threading
from util.dome4 import *
ex = ExcelUtil()
data = ex.get_data()


@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    """case"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get('https://passport.baidu.com/v2/?login&tpl=wk&u=http%3A%2F%2Fbaike.baidu.com%2Fusercenter')
        self.driver.maximize_window()
        self.th = threading.Thread(target=video_record)
        self.th.start()

        # self.driver.refresh()
        self.log = UserLog()
        self.logger = self.log.get_log()
        self.business = LoginBusiness(self.driver)

    def tearDown(self):
        sleep(5)
        self.driver.quit()
        # with keyboard.Listener(on_press=on_press(flag)) as listener:
        #     listener.join()
        on_press(key=True)
        self.th.join()
        video_info()

    @ddt.data(*data)
    def test_key_metrics_case(self, data):
        """登录购买收藏case"""
        test_id,username, password = data
        # print(test_id, username, password)
        login_error = self.business.case_login(username, password)
        self.assertFalse(login_error, "断言登录失败，用户名或密码不正确")
        # v_error = self.business.case_v_baike()
        # self.assertFalse(v_error, "“v百科”页面断言跳转失败")
        # home_error = self.business.case_home_push()
        # self.assertFalse(home_error, "“首页推荐”页面断言跳转失败")
        # create_error = self.business.case_create_entry()
        # self.assertFalse(create_error, "“创建词条”页面断言跳转失败")
        # baikeapp_error = self.business.case_baike_app()
        # self.assertFalse(baikeapp_error, "“下载百科app”页面断言跳转失败")


