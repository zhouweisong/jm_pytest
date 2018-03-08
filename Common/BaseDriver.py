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
        # chuizi_jianguo
        chuizi_jianguo = {}
        chuizi_jianguo['platformName'] = 'Android'
        chuizi_jianguo['platformVersion'] = '5.1.1'
        chuizi_jianguo['automationName'] = 'uiautomator2'
        chuizi_jianguo['deviceName'] = 'c8a135a3'
        #chuizi_jianguo['app'] = '/Users/zws/longbeach/appium/jiemo.apk'
        chuizi_jianguo['appPackage'] = 'com.jiemoapp'
        chuizi_jianguo['appActivity'] = 'com.jiemoapp.activity.SplashActivity'
        chuizi_jianguo['noReset'] = "False"
        chuizi_jianguo["unicodeKeyboard"] = "True"
        chuizi_jianguo["resetKeyboard"] = "True"

        # oppo_x9007
        oppo_x9007 = {}
        oppo_x9007['platformName'] = 'Android'
        oppo_x9007['platformVersion'] = '4.4.2'
        oppo_x9007['deviceName'] = '5b18cef9'
        oppo_x9007['app'] = 'http://apk.s.diandian.com/jiemoApp/dev/jiemo_jiemo_1.4.31_10430_%E5%86%85%E7%BD%91_debug.apk'
        oppo_x9007['noReset'] = "False"
        oppo_x9007["unicodeKeyboard"] = "True"
        oppo_x9007["resetKeyboard"] = "True"

        # htc_d820u
        htc_d820u = {}
        htc_d820u['platformName'] = 'Android'
        htc_d820u['platformVersion'] = '4.4.4'
        htc_d820u['deviceName'] = 'HC4BSYC03884 '
        htc_d820u[
            'app'] = 'http://apk.s.diandian.com/jiemoApp/dev/jiemo_jiemo_1.4.31_10430_%E5%86%85%E7%BD%91_debug.apk'
        htc_d820u['noReset'] = "False"
        htc_d820u["unicodeKeyboard"] = "True"
        htc_d820u["resetKeyboard"] = "True"

        # simulator
        simulator = {}
        simulator['platformName'] = 'Android'
        simulator['platformVersion'] = '7.1'
        simulator['automationName'] = 'uiautomator2'
        simulator['deviceName'] = 'Android Emulator'
        simulator['app'] = '/Users/zws/longbeach/appium/jiemo.apk'
        simulator['noReset'] = "True"
        simulator["unicodeKeyboard"] = "True"
        simulator["resetKeyboard"] = "True"

        # mate_10
        mate_10 = {}
        mate_10['platformName'] = 'Android'
        mate_10['platformVersion'] = '8.0'
        mate_10['automationName'] = 'uiautomator2'
        mate_10['deviceName'] = 'D3H0217A17005776'
        mate_10['app'] = '/Users/zws/longbeach/appium/jiemo.apk'
        mate_10['noReset'] = "False"
        mate_10["unicodeKeyboard"] = "True"
        mate_10["resetKeyboard"] = "True"

        # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', mate_10)
        # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', simulator)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', chuizi_jianguo)
        # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',oppo_x9007)
        # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',htc_d820u)
        driver.implicitly_wait(10)

        return driver



