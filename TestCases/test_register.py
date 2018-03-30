"""
-------------------------------------------------
   File Name：     test_register
   Description :
   Author :       zws
   date：          2018/3/14
-------------------------------------------------
   Change Activity:
                   2018/3/14:
-------------------------------------------------
"""
__author__ = 'zws'


import pytest
from Common.logger2 import *
from PageObjects.Register.basicInfo_page import Basic_Info_Page
from PageObjects.Register.setThePassword_page import Set_The_Password_Page
from PageObjects.Register.setThePhoneNumber_page import Set_The_Phone_Number_Page
from PageObjects.Register.uploadHeadPicture_page import Upload_Head_Picture
from PageObjects.Register.collegeInfo_page import College_Info_Page
from PageObjects.Register.collegeSearch_page import Collega_Search_Page
from appium.webdriver.common.mobileby import MobileBy as By
from Common.RW_Config import RW_Config



@pytest.mark.usefixtures('init_register')
class Test_Register:

    #注册正常
    @pytest.mark.register
    def test_register_ok(self,init_register):
        rw_config = RW_Config()
        rw_config.set_config('register.conf','REGISTERCONF','register_ok','phone')
        config_data = rw_config.read_config('register.conf','REGISTERCONF','register_ok')
        basic_info =Basic_Info_Page(init_register)
        set_the_phone_number_page = Set_The_Phone_Number_Page(init_register)
        #输入注册的手机号 填写验证码，点击下一步
        set_the_phone_number_page.action_register_step1(phone=config_data['phone'],verification_code=config_data['verification_code'])
        #设置密码为 123456 点击下一步
        set_the_password_page = Set_The_Password_Page(init_register)
        set_the_password_page.action_set_password(config_data['password'])
        #点击学校名称进入搜索学校页
        college_info_page = College_Info_Page(init_register)
        college_info_page.touch_register_school_name()
        #学校搜索页面搜索北京邮电大学并选择
        collega_search_page = Collega_Search_Page(init_register)
        collega_search_page.input_search(config_data['collega'])
        collega_search_page.action_collage_search(config_data['collega'],collega_search_page.bjyd_college_xpath)
        #点击院系入口，打开院系原则弹框
        college_info_page.touch_register_academy_name()
        college_info_page.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("{0}")'.format(config_data['academy'])).click()
        #点击年级入口，打开入学时间弹框
        college_info_page.touch_register_year()
        college_info_page.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("确定")').click()
        #点击【下一步】按钮
        college_info_page.touch_ok()
        basic_info = Basic_Info_Page(init_register)
        #填写基本信息 - 姓名
        basic_info.input_user_name_et(config_data['user_name'])
        #填写基本信息 - 性别
        basic_info.touch_gender_male_tv()
        basic_info.touch_ok()
        upload_head_picture = Upload_Head_Picture(init_register)
        upload_head_picture.touch_user_avatar()
        upload_head_picture.find_element(By.ANDROID_UIAUTOMATOR,'new UiSelector().text("从相册选择")').click()
        upload_head_picture.find_element(By.XPATH,'//android.widget.GridView[@resource-id=\"com.jiemoapp:id/grid\"]/android.widget.FrameLayout[2]/android.widget.ImageView[1]').click()
        upload_head_picture.find_element(By.ID,'ok').click()
        upload_head_picture.find_element(By.ID,'ok').click()





