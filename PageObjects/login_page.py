"""
-------------------------------------------------
   File Name：     logIn_page
   Description :
   Author :       zws
   date：          2018/3/6
-------------------------------------------------
   Change Activity:
                   2018/3/6:
-------------------------------------------------
"""
__author__ = 'zws'

from Common.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By


class Login_Page(BasePage):

    #手机号按钮
    login_in_phone_number_icon = "com.jiemoapp:id/login_in_phone_number"
    #获取验证码按钮
    verification_code_icon = "com.jiemoapp:id/login_in_verification_code"
    #验证码输入框
    login_in_verification_code_box = "com.jiemoapp:id/login_in_verification_code"
    #切换成密码登录按钮/验证码登录按钮
    password_login_in_icon = "com.jiemoapp:id/password_login_in"
    #获取验证码
    fetch_verification_code_icon ="com.jiemoapp:id/fetch_verification_code"
    #登录按钮
    new_login_in_icon = "com.jiemoapp:id/new_login_in"
    #没有密码去注册按钮
    have_no_phone_number_icon = "com.jiemoapp:id/have_no_phone_number"
    #密码输入框
    login_in_password_box = "com.jiemoapp:id/login_in_password"
    #显示密码
    show_password_img = "com.jiemoapp:id/show_password_img"
    #【X】按钮
    login_in_close = "com.jiemoapp:id/login_in_close"



    #密码登录操作
    def login_by_password_action(self, username, login_passwd):
        self.find_element(By.ID, self.login_in_phone_number_icon).send_keys(username)
        self.find_element(By.ID, self.password_login_in_icon).click()
        self.find_element(By.ID, self.login_in_password_box).send_keys(login_passwd)
        self.find_element(By.ID, self.new_login_in_icon).click()

    #验证码登录操作
    def login_by_verification_action(self,username,login_verification):
        self.find_element(By.ID, self.login_in_phone_number_icon).send_keys(username)
        self.find_element(By.ID, self.fetch_verification_code_icon).click()
        self.find_element(By.ID, self.login_in_verification_code_box).send_keys(login_verification)
        self.find_element(By.ID, self.new_login_in_icon).click()




