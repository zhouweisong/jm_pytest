"""
-------------------------------------------------
   File Name：     BaseDriver
   Description :
   Author :       zws
   date：          2018/3/5
-------------------------------------------------
   Change Activity:
                   2018/3/5:
-------------------------------------------------
"""
__author__ = 'zws'

import os
from openpyxl import load_workbook
from appium import webdriver

class BaseDriver():

    def init_driver(self):
        #从配置文件中读取到设备信息。
        #获取当前文件的绝对路径
        caps_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"../caps/caps.xlsx"))
        wb = load_workbook(caps_file)
        sh = wb.get_sheet_by_name("Sheet1")

        desired_caps = {}
        desired_caps['platformName'] = sh.cell(row=2,column=1).value
        desired_caps['platformVersion'] = sh.cell(row=2,column=2).value
        desired_caps['deviceName'] = sh.cell(row=2,column=3).value
        desired_caps['appPackage'] = sh.cell(row=2,column=5).value
        desired_caps['appActivity'] = sh.cell(row=2,column=6).value
        desired_caps['automationName'] = 'Uiautomator2'

        #连接appium server,告诉appium自动化代码执行的对象。
        return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)



