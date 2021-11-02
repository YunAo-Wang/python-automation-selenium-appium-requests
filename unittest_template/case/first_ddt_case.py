# -*- coding: utf-8 -*-
__author__ = '蕴奥'
import ddt
import unittest
from business.login_business import LoginBusiness
from selenium import webdriver
import HTMLTestRunner
from util.excel_util import ExcelUtil
from settings import common
import os
from log.user_log import UserLog
import time

ex = ExcelUtil()
data = ex.get_data()


# 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.login = LoginBusiness(self.driver)
        self.log = UserLog()
        self.logger = self.log.get_log()
        base_name = common.base()
        code_name = os.path.join(base_name + "\\" + 'Image')
        self.file_name = code_name + "\\" + "test001.png"

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.join(os.getcwd() + "/report/" + case_name + ".png")
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email, username, password, self.file_name, assertCode, assertText)
        self.assertFalse(email_error, "测试失败")


if __name__ == '__main__':
    file_path = os.path.join(os.getcwd() + "/report/" + "first_case1.html")
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="This is first report1", description=u"这个是我们第一次测试报告1",
                                           verbosity=2)
    runner.run(suite)