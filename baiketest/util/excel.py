import xlrd
import time
from xlutils.copy import copy
import os
from commons.common import base


class ExcelUtil:
    def __init__(self, excel_path=None, index=None):
        base_name = base()
        repost_name = os.path.join(base_name,'config','casetest.xls')
        if excel_path is None:
            self.excel_path = repost_name
        else:
            self.excel_path = excel_path

        if index is None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        # 获取所有工作表的列表
        self.table = self.data.sheets()[index]

    # 获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows != None:
            for i in range(1,rows):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        # 行数
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格的数据
    def get_col_value(self, row, col):
        # 行和列坐标值
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # 写入数据
    def write_value(self, row, value):
        read_value = xlrd.open_workbook(self.excel_path)
        # copy数据
        write_data = copy(read_value)
        # 写入数据
        write_data.get_sheet(0).write(row, 9, value)
        # 保存数据
        write_data.save(self.excel_path)
        time.sleep(1)



if __name__ == '__main__':
    ex = ExcelUtil()
    li = ex.get_data()
    # for i in range(len(li)):
    #     url = '--proxy-server=http://'+li[i][1]+":"+li[i][2]
    #     print(url)
    print(li)

