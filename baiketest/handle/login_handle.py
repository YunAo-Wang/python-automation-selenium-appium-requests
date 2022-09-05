# -*- coding: utf-8 -*-
from base.find_element import FindElement
from logs.user_log import UserLog
from commons.common import base
import time, os


class LoginHandle:
    """数据逻辑处理"""

    def __init__(self, driver):
        self.driver = driver
        self.fd = FindElement(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        self.base_file = base()

    def click_user_log(self):
        # 点击用户登录
        time.sleep(2)
        self.fd.get_element('user_log').click()

    def send_username(self, username):
        # 用户名
        self.loger.info("输入用户名")
        time.sleep(1)
        self.fd.get_element('username').send_keys(username)

    def send_pwd(self, pwd):
        # 密码
        self.loger.info("输入密码")
        time.sleep(2)
        self.fd.get_element('password').send_keys(pwd)

    def click_btn(self):
        # 点击登录
        time.sleep(2)
        self.fd.get_element('login_sub').click()
        time.sleep(5)

    # alert确认
    def forgot_assert(self):
        # 检测是否有这个参数
        return self.fd.get_element('forgot')

    def filename(self, file):
        # 保存图片路径
        file = os.path.join(self.base_file + "/images/" + self.now + file + ".png")
        self.driver.save_screenshot(file)
        time.sleep(0.5)

    def login_user(self, username, pwd):
        """登录数据传参"""
        self.click_user_log()
        self.send_username(username)
        self.send_pwd(pwd)
        self.click_btn()
        # self.alert_ent()
        self.filename("登录成功")  # 登录成功截图

