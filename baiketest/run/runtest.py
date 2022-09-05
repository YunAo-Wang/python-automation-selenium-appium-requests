import unittest
from unittestreport import TestRunner
from commons.common import base
import sys,os

dir_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir_path)

Basepath = base()
file_name = os.path.join(Basepath,'case')
# filename = Basepath + "\\case"


def runtest():
    # 主程序-收集测试用例
    discovers = unittest.defaultTestLoader.discover(file_name, pattern="test_*.py")  # 2
    return discovers


if __name__ == "__main__":
    fp = Basepath + '\\testResult'
    runner = TestRunner(runtest(), filename="report.html", report_dir=fp, title="UI测试报告", tester="YUN",
                        desc="测试报告",templates = 3)
    runner.run()
