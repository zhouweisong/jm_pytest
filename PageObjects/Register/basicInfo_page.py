"""
-------------------------------------------------
   File Name：     basicInfo
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

class Basic_Info_Page(BasePage):
    #返回 按钮
    login_back = "com.jiemoapp:id/login_back"
    #姓名 输入框
    user_name_et = "com.jiemoapp:id/user_name_et"
    #性别女 按钮
    gender_female_tv = "com.jiemoapp:id/gender_female_tv"
    #性别男 按钮
    gender_male_tv = "com.jiemoapp:id/gender_male_tv"
    #下一步 按钮
    ok = "com.jiemoapp:id/ok"
    #非百家姓 alert提示
    alert_name = "com.jiemoapp:id/message"


    def touch_login_back(self):
        self.find_element(By.ID,self.login_back).click()

    def input_user_name_et(self,message):
        self.find_element(By.ID,self.user_name_et).send_keys(message)

    def touch_gender_female_tv(self):
        self.find_element(By.ID,self.gender_female_tv).click()

    def touch_gender_male_tv(self):
        self.find_element(By.ID,self.gender_male_tv).click()

    def touch_ok(self):
        self.find_element(By.ID,self.ok).click()

    def get_alert_name_message(self):
        self.find_element(By.ID,self.alert_name).get_attribute("name")



