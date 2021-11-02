# -*- coding: utf-8 -*-
__author__ = '蕴奥'

from page.login_page import LoginPage
from util.get_code import GetCode
from log.user_log import UserLog


class LoginHandle(object):
    def __init__(self, driver):
        self.driver = driver
        self.login_p = LoginPage(self.driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    # 输入邮箱
    def send_user_email(self, email):
        self.loger.info("输入的邮箱值是：" + email)
        self.login_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self, username):
        self.loger.info("输入的用户名是："+username)
        self.login_p.get_email_element().send_keys(username)

    # 输入密码
    def send_user_password(self, password):
        self.loger.info("输入的密码是：" + password)
        self.login_p.get_password_element().send_keys(password)

    # 输入验证码
    def send_user_code(self, file_name):
        get_code_text = GetCode(self.driver)
        code = get_code_text.code_online(file_name)
        self.login_p.get_code_element().send_keys(code)

    # 获取文字信息
    def get_user_text(self, info, user_info):
        try:
            if info == "user_email_error":
                text = self.login_p.get_email_error_element().text
            elif info == "user_name_error":
                text = self.login_p.get_user_error_element().text
            elif info == 'password_error':
                text = self.login_p.get_password_element().text
            else:
                text = self.login_p.get_code_element().text

        except:
            text = None

        return text

    # 点击注册/登录按钮
    def click_login_button(self):
        self.login_p.get_button_element().click()

    # 获取注册按钮文字
    def get_login_text(self):
        return self.login_p.get_button_element().text
