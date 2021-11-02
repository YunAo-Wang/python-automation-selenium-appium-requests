# -*- coding: utf-8 -*-
__author__ = '蕴奥'
import os
from util.excel_util import ExcelUtil
from settings import common
from keyword_selenium.actionMethod import ActionMethod


class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        base_name = common.base()
        excel_name = os.path.join(base_name + "\\" + 'config')
        file_name = excel_name + "\\" + "keyword.xlsx"
        handle_excel = ExcelUtil(file_name)
        case_lines = handle_excel.get_lines()
        if case_lines:
            for i in range(1, case_lines):
                is_run = handle_excel.get_col_value(i, 3)
                if is_run == "yes":
                    # 实际结果
                    except_result_method = handle_excel.get_col_value(i, 7)
                    # 预计结果
                    except_result = handle_excel.get_col_value(i, 8)
                    # 执行方法
                    method = handle_excel.get_col_value(i, 4)
                    # 输入数据
                    send_value = handle_excel.get_col_value(i, 5)
                    # 操作元素
                    handle_value = handle_excel.get_col_value(i, 6)
                    # 执行方法、输入元素、操作元素
                    self.run_method(method, send_value, handle_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            if except_value[1] in result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method, except_value[1])
                            if result:
                                handle_excel.write_value(i, 'pass')
                            else:
                                handle_excel.write_value(i, 'fail')
                        else:
                            print("没有else")
                    else:
                        print("预期结果为空")

        # 获取预期结果值

    def get_except_result_value(self, data):
        return data.split('=')

    def run_method(self, method, send_value='', handle_value=''):
        # 循环操作函数
        method_value = getattr(self.action_method, method)
        if send_value == '' and handle_value != '':
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        elif send_value != '' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value(send_value, handle_value)
        return result

    if __name__ == '__main__':
        test = KeywordCase()
        test.run_main()