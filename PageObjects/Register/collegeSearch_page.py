"""
-------------------------------------------------
   File Name：     collegeSearch_page
   Description :
   Author :       zws
   date：          2018/3/14
-------------------------------------------------
   Change Activity:
                   2018/3/14:
-------------------------------------------------
"""
__author__ = 'zws'

from Common.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class Collega_Search_Page(BasePage):

    #关闭按钮
    close = "com.jiemoapp:id/close"
    #搜索输入框
    search = "com.jiemoapp:id/search"
    #清空按钮
    delete = "com.jiemoapp:id/delete"
    #搜索按钮
    search_icon = "com.jiemoapp:id/search_icon"


    def touch_close(self):
        self.find_element(By.ID,self.close).click()

    def input_search(self,message):
        self.find_element(By.ID,self.search).send_keys(message)

    def touch_delete(self):
        self.find_element(By.ID,self.delete).click()

    def touch_search_icon(self):
        self.find_element(By.ID,self.search_icon).click()




