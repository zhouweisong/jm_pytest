"""
-------------------------------------------------
   File Name：     phone_page
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
import time
from Common.logger2 import *


class Set_The_Phone_Number_Page(BasePage):
    #【X】按钮
    sign_up_close = "com.jiemoapp:id/sign_up_close"
    #手机号输入框
    sign_up_phone_number = "com.jiemoapp:id/sign_up_phone_number"
    #验证码输入框
    sign_up_verification_code = "sign_up_verification_code"
    #获取验证码按钮
    fetch_verification_code = "fetch_verification_code"
    #下一步按钮
    ok = "com.jiemoapp:id/ok"
    #已有账号，去登录按钮
    have_phone_number = "com.jiemoapp:id/have_phone_number"


    def touch_sign_up_close(self):
        self.find_element(By.ID,self.sign_up_close).click()

    def input_sign_up_phone_number(self,message):
        self.find_element(By.ID,self.sign_up_phone_number).send_keys(message)

    def input_sign_up_verification_code(self, ver_code):
        self.find_element(By.ID,self.sign_up_verification_code).send_keys(ver_code)

    def touch_fetch_verification_code(self):
        self.find_element(By.ID,self.fetch_verification_code).click()

    def touch_ok(self):
        self.find_element(By.ID,self.ok).click()

    def touch_have_phone_number(self):
        self.find_element(By.ID,self.have_phone_number).click()

    def action_register_step1(self,phone,verification_code):
        self.find_element(By.ID, self.sign_up_phone_number).send_keys(phone)
        self.find_element(By.ID, self.fetch_verification_code).click()
        self.find_element(By.ID, self.sign_up_verification_code).send_keys(verification_code)
        self.find_element(By.ID, self.ok).click()

