# -*- coding: utf-8 -*-
__author__ = ''

from base.find_element import FindElement
from logs.user_log import UserLog
from commons.common import base
import time, os


class PageHandle:
    """数据逻辑处理"""

    def __init__(self, driver):
        self.driver = driver
        self.fd = FindElement(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        self.base_file = base()

    def click_user_log(self):
        # 点击返回首页
        self.loger.info("点击返回首页")
        time.sleep(1)
        self.fd.get_element('baidu_label').click()

    def click_v_ency(self):
        # 点击V百科
        self.loger.info("点击V百科")
        time.sleep(2)
        self.fd.get_element('v_ency').click()

    def switch_win(self):
        time.sleep(2)
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])

    def get_assert_v(self):
        # 返回v百科参数
        self.loger.info("返回断言参数，判断是否跳转成功")
        time.sleep(2)
        element = self.fd.get_element('assert_v')
        return element

    def filename(self, file):
        # 保存图片路径
        file = os.path.join(self.base_file + "/images/" + self.now + file + ".png")
        self.driver.save_screenshot(file)
        time.sleep(0.5)

    def click_create_entry(self):
        # 点击返回首页
        self.loger.info("点击“创建词条”")
        time.sleep(1)
        self.fd.get_element('create_entry').click()

    def get_assert_create(self):
        # 返回v百科参数
        self.loger.info("判断词条页是否跳转成功")
        time.sleep(1)
        element = self.fd.get_element('assert_create')
        return element

    def click_home_push(self):
        # 点击首页推送
        time.sleep(1)
        self.fd.get_element('home_push').click()

    def click_bai_down(self):
        # 点击下载百科app
        time.sleep(1)
        self.fd.get_element('baike_app').click()

    def get_assert_down(self):
        # 判断下载百科页面是否跳转
        time.sleep(1)
        element = self.fd.get_element('assert_baike')
        return element
