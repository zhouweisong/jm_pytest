"""
-------------------------------------------------
   File Name：     collegeInfo_page
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


class College_Info(BasePage):
    #返回按钮
    login_back = "com.jiemoapp:id/login_back"
    #学校名称
    register_school_name = "com.jiemoapp:id/register_school_name"
    #院系名称
    register_academy_name = "com.jiemoapp:id/register_academy_name"
    #年级名称
    register_year = "com.jiemoapp:id/register_year"


    def touch_login_back(self):
        self.find_element(By.ID,self.login_back).click()

    def touch_register_school_name(self):
        self.find_element(By.ID,self.register_school_name).click()

    def touch_register_academy_name(self):
        self.find_element(By.ID,self.register_academy_name).click()

    def touch_register_year(self):
        self.find_element(By.ID,self.register_year).click()



