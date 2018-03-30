"""
-------------------------------------------------
   File Name：     setThePassword
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

class Set_The_Password_Page(BasePage):
    #返回按钮
    set_password_close = "com.jiemoapp:id/set_password_close"
    #设置密码输入框
    set_password_et = "com.jiemoapp:id/set_password_et"
    #显示密码按钮
    show_or_not_layout = "com.jiemoapp:id/show_or_not_layout"
    #下一步按钮
    ok ="com.jiemoapp:id/ok"
    #芥末协议按钮
    user_agreement = "com.jiemoapp:id/user_agreement"

    def inpu_set_password_et(self,message):
        self.find_element(By.ID,self.set_password_et).send_keys(message)

    def touch_ok(self):
        self.find_element(By.ID,self.ok).click()

    def action_set_password(self,password):
        self.inpu_set_password_et(password)
        self.touch_ok()




