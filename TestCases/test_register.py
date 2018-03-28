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



@pytest.mark.usefixtures('init_register')
class Test_Register:

    #注册正常
    @pytest.mark.register
    def test_register_ok(self,init_register):
        basic_info =Basic_Info_Page(init_register)
        register_1 = Set_The_Phone_Number_Page(init_register)
        register_1.action_register_step1(phone='13700105430',verification_code='1234')


