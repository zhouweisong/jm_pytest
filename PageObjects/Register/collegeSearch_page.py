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
from Common.logger2 import *

class Collega_Search_Page(BasePage):

    #关闭按钮
    close = "com.jiemoapp:id/close"
    #搜索输入框
    search = "com.jiemoapp:id/search"
    #清空按钮
    delete = "com.jiemoapp:id/delete"
    #搜索按钮
    search_icon = "com.jiemoapp:id/search_icon"
    #搜索结果为"北京邮电大学"
    bjyd_college_xpath = '//android.widget.TextView[@resource-id=\"com.jiemoapp:id/group_name\" and @text=\"北京邮电大学\"]'


    def touch_close(self):
        self.find_element(By.ID,self.close).click()

    def input_search(self,message):
        self.find_element(By.ID,self.search).send_keys(message)

    def touch_delete(self):
        self.find_element(By.ID,self.delete).click()

    def touch_search_icon(self):
        self.find_element(By.ID,self.search_icon).click()

    def touch_bjyd_college(self,xpath):
        self.find_element(By.XPATH,xpath).click()

    #选择北京邮电大学
    def action_collage_search(self,college_name,college_xpath):
        self.input_search(message=college_name)
        self.touch_search_icon()
        self.touch_bjyd_college(college_xpath)






