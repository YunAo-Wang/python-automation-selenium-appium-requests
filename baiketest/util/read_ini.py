# -*- coding: utf-8 -*-
__author__ = ''

import configparser
import os
from commons.common import base


class ReadIni():
    def __init__(self, file_name=None, node=None):
        base_name = base()
        report_name = os.path.join(base_name, 'config', 'report.ini')
        if file_name is None:
            file_name = report_name
        if node is None:
            self.node = "LoginElement"
        else:
            self.node = node

        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        # 加载文件
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data
