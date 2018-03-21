"""
-------------------------------------------------
   File Name：     uploadHeadPicture_page
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

class Upload_Head_Picture(BasePage):
    login_back = "com.jiemoapp:id/login_back"
    user_avatar = "com.jiemoapp:id/user_avatar"
    ok = "com.jiemoapp:id/ok"

    def touch_login_back(self):
        self.find_element(By.ID,self.login_back).click()

    def touch_user_avatar(self):
        self.find_element(By.ID,self.user_avatar).click()

    def touch_ok(self):
        self.find_element(By.ID,self.ok).click()
