# -*- coding: utf-8 -*-

from handle.login_handle import LoginHandle
from handle.page_handle import PageHandle
import time


class LoginBusiness(object):
    """业务逻辑处理"""

    def __init__(self, driver):
        self.driver = driver
        self.login_hd = LoginHandle(self.driver)
        self.page_win = PageHandle(self.driver)

    def case_login(self, username, password):
        """登录"""
        # time.sleep(10)
        self.login_hd.login_user(username, password)
        if self.login_hd.forgot_assert() == None:
            print('登录成功')
            return False
        else:
            print('登录失败')
            return True

    def case_v_baike(self):
        """v_百科页面跳转"""
        self.page_win.click_user_log()
        self.page_win.click_v_ency()
        self.page_win.switch_win()
        if self.page_win.get_assert_v() == None:
            print('页面跳转失败')
            return True
        else:
            print('页面跳转成功')
            self.driver.refresh()
            time.sleep(2)
            self.page_win.filename('v百科页面')
            time.sleep(2)
            self.driver.close()
            return False

    def case_create_entry(self):
        """下载百科app"""
        self.page_win.switch_win()
        self.page_win.click_create_entry()
        self.page_win.switch_win()

        if self.page_win.get_assert_create() == None:
            print('页面跳转失败')
            return True
        else:
            print('创建词条页面跳转成功')
            self.driver.refresh()
            time.sleep(2)
            self.page_win.filename('创建词条页面')
            time.sleep(2)
            self.driver.close()
            return False

    def case_home_push(self):
        """首页信息推送页面跳转"""
        self.page_win.switch_win()
        self.page_win.click_home_push()
        self.driver.refresh()
        self.page_win.switch_win()
        time.sleep(2)
        self.page_win.filename('首页信息推送')
        time.sleep(2)
        self.driver.close()

    def case_baike_app(self):
        """下载百科app"""
        self.page_win.switch_win()
        self.page_win.click_bai_down()
        self.page_win.switch_win()

        if self.page_win.get_assert_down() == None:
            print('页面跳转失败')
            return True
        else:
            print('下载百科app页面跳转成功')
            self.driver.refresh()
            time.sleep(2)
            self.page_win.filename('下载百科app页面')
            time.sleep(2)
            self.driver.close()
            return False
