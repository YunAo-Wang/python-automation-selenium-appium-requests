# -*- coding: utf-8 -*-
__author__ = ''

from base.find_element import FindElement
from logs.user_log import UserLog
from commons.common import base
import time, os


class ArticleHandle:
    """数据逻辑处理"""

    def __init__(self, driver):
        self.driver = driver
        self.fd = FindElement(driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        self.base_file = base()



