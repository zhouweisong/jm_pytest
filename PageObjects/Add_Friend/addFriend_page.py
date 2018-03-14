"""
-------------------------------------------------
   File Name：     add_friend_page
   Description :
   Author :       zws
   date：          2018/3/13
-------------------------------------------------
   Change Activity:
                   2018/3/13:
-------------------------------------------------
"""
__author__ = 'zws'
from Common.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy as By

class Add_Friend_Page(BasePage):
    #搜索输入框
    search = "com.jiemoapp:id/search"
    #展开全部学校按钮
    arrow = "com.jiemoapp:id/arrow"
    #新好友描述区
    someone_add_you_desc = "com.jiemoapp:id/someone_add_you_desc"
    #我的大学text
    my_college_text = 'new UiSelector().text("北京工业大学")'

    def touch_search(self):
        self.find_element(By.ID,self.search).click()

    def touch_arrow(self):
        self.find_element(By.ID,self.arrow).click()

    def touch_someone_add_you_desc(self):
        self.find_element(By.ID,self.someone_add_you_desc).click()

    def touch_my_colleage(self):
        self.find_element(By.ANDROID_UIAUTOMATOR,self.my_college_text).click()



