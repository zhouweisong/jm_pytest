"""
-------------------------------------------------
   File Name：     home_page
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


class Home_Page(BasePage):
    #找到更对的TA们 alert 好 按钮
    ok = "com.jiemoapp:id/ok"
    #找到更对的TA们 alert 暂时不 按钮
    do_next = "com.jiemoapp:id/do_next"

    # 注册按钮
    to_sign_up_icon = "com.jiemoapp: id / to_sign_up"
    # 登录按钮
    to_login_icon = "com.jiemoapp:id/to_login"
    # 新鲜事按钮
    home_newsfeed_icon = "com.jiemoapp:id/home_newsfeed_icon"
    # 加好友按钮
    home_friend_icon = "com.jiemoapp: id / home_waterfall_icon"
    # 兴趣相投按钮
    home_rss_icon = "com.jiemoapp:id/home_rss_icon"
    # 悄悄话按钮
    home_message_icon = "com.jiemoapp:id/home_message_icon"
    # 我的按钮
    home_profile_icon = "com.jiemoapp:id/home_profile_icon"


    def touch_home_newsfeed(self):
        self.find_element(By.ID, self.home_newsfeed_icon).click()

    def touch_home_friend(self):
        self.find_element(By.ID, self.home_friend_icon).click()

    def touch_home_rss(self):
        self.find_element(By.ID, self.home_rss_icon).click()

    def touch_home_message(self):
        self.find_element(By.ID, self.home_message_icon).click()

    def touch_home_profile(self):
        self.find_element(By.ID, self.home_profile_icon).click()

    def touch_ok(self):
        self.find_element(By.ID,self.ok).click()

    def touch_do_next(self):
        self.find_element(By.ID,self.do_next).click()

    def touch_login(self):
        self.find_element(By.ID, self.to_login_icon).click()

    def touch_to_sign_up(self):
        self.find_element(By.ID,self.to_sign_up_icon).click()

    def get_ok_name(self):
        return self.find_element(By.ID, self.ok).get_attribute("name")





