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

#学院信息页面
class College_Info_Page(BasePage):
    #返回按钮
    login_back = "login_back"
    #学校名称
    register_school_info = "register_school_info"
    #院系名称
    register_school_academy = "register_school_academy"
    #年级名称
    register_school_year = "register_school_year"
    #下一步
    ok = "ok"


    def touch_login_back(self):
        self.find_element(By.ID,self.login_back).click()

    def touch_register_school_name(self):
        self.find_element(By.ID, self.register_school_info).click()

    def touch_register_academy_name(self):
        self.find_element(By.ID, self.register_school_academy).click()

    def touch_register_year(self):
        self.find_element(By.ID, self.register_school_year).click()

    def touch_ok(self):
        self.find_element(By.ID,self.ok).click()




