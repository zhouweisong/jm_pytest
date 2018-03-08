"""
-------------------------------------------------
   File Name：     config
   Description :
   Author :       zws
   date：          2018/3/6
-------------------------------------------------
   Change Activity:
                   2018/3/6:
-------------------------------------------------
"""
__author__ = 'zws'

import os

base_dir = os.path.split(os.path.realpath(__file__))[0].replace("Common","")

#日志目录
log_dir = base_dir + "Logs/"

#测试报告目录
report_dir = base_dir + "HtmlReport/"

#截图目录
image_dir = base_dir + "Images/"

#测试用例目录



