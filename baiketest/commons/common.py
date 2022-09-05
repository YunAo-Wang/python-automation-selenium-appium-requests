# -*- coding: utf-8 -*-
__author__ = ''

import os

def base():
    Base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    return Base_path
# 当前包的动态路径
# print(base())

# def parameter(module,num):
#     def outer(func):
#         def inner(*args):
#             for i in range(num):
#                 t1 = int(time.time() * 1000)
#                 res = func(*args)
#                 t2 = int(time.time() * 1000)
#                 response = str(res.headers) + res.text
#                 li_res.append(len(response) / 1024)
#                 print(f"当前{module}的响应大小为:{len(response) / 1024}KB")
#                 li_time.append(t2 - t1)
#                 print(f"当前{module}响应时间为:{t2 - t1}ms")
#         return inner
#     return outer
