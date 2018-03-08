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

    #获取toast内容
    def get_toast_login_wrong(self,message):
        toast_login_wrong = '//*[@text=\'{}\']'.format(message)
        t = WebDriverWait(self.driver, 30, 0.1).until(EC.presence_of_element_located((By.XPATH,toast_login_wrong)))


    #等待元素可见
    def element_wait(self,by,locator,wait_time=5):
        if by not in MobileBy.__dict__.values() and by not in By.__dict__.values():
            raise NameError("Please enter the correct targeting elements.")
        WebDriverWait(self.driver,wait_time,0.5).until(EC.presence_of_element_located((by,locator)))

    #将元素滚动到可见区域
    def element_scrollIntoView(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(0.5)

    #查找单个
    def find_element(self,by,locator,wait_time=5):
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

    #获取当前设备的屏幕大小
    def getSize(self):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        return (width, height)

    # 右滑。x轴从小到大
    def swipe_right(self, size):
        self.driver.swipe(size[0] * 0.1, size[1] * 0.5, size[0] * 0.85, size[1] * 0.5, 500)

    # 左滑。x轴从大到小
    def swipe_left(self, size):
        self.driver.swipe(size[0] * 0.85, size[1] * 0.5, size[0] * 0.1, size[1] * 0.5, 500)

