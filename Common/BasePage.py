"""
-------------------------------------------------
   File Name：     BasePage
   Description :
   Author :       zws
   date：          2018/3/5
-------------------------------------------------
   Change Activity:
                   2018/3/5:
-------------------------------------------------
"""
__author__ = 'zws'

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
import time

import logging
from Common import config

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    #查看toast内容是否出现
    def toast_exist(self, toastmessage):
        toast_loc = ("xpath", "//*[contains(@text,'%s')]" % toastmessage)
        try:
            t = WebDriverWait(self.driver,5,0.2).until(EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False



    #等待元素可见
    def element_wait(self,by,locator,wait_time=200):
        if by not in MobileBy.__dict__.values() and by not in By.__dict__.values():
            raise NameError("Please enter the correct targeting elements.")
        WebDriverWait(self.driver,wait_time,0.5).until(EC.presence_of_element_located((by,locator)))

    #将元素滚动到可见区域
    def element_scrollIntoView(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(0.5)

    #查找单个
    def find_element(self,by,locator,wait_time=10):
        self.element_wait(by,locator,wait_time)
        return self.driver.find_element(by,locator)


    #查找多个元素
    def find_elements(self,by,locator,wait_time=5):
        self.element_wait(by, locator, wait_time)
        return self.driver.find_elements(by, locator)

    # 截图
    def save_img(self, img_name):
        logging.info("截图位置：%s" % (config.image_dir + img_name))
        self.driver.save_screenshot(config.image_dir + img_name)

    # 向左滑动的函数
    def swipe_left(self, duration):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x * 9 / 10, y / 2, x / 10, y / 2, duration)

    # 向上滑动函数
    def swipe_up(self, duration):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y * 9 / 10, x / 2, y * 6 / 10, duration)

    # 向右滑动函数
    def swipe_right(self, duration):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 10, y / 2, x * 9 / 10, y / 2, duration)

    # 向下滑动函数
    def swipe_down(self, duration):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x / 2, y * 6 / 10, x / 2, y * 9 / 10, duration)



