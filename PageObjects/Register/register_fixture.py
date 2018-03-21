"""
-------------------------------------------------
   File Name：     register_fixture
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

from Common.BaseDriver import BaseDriver
from PageObjects.Register.basicInfo_page import Basic_Info_Page
from PageObjects.Register.setThePassword_page import Set_The_Password_Page
from PageObjects.Register.setThePhoneNumber_page import Set_The_Phone_Number_Page
from PageObjects.Register.uploadHeadPicture_page import Upload_Head_Picture
from PageObjects.Register.collegeInfo_page import College_Info_Page
from PageObjects.Register.collegeSearch_page import Collega_Search_Page
from TestDatas import COMM_DATA as CD


@pytest.fixture
def init_register():
    driver = BaseDriver().init_driver()
    basic_info_page = Basic_Info_Page()
    set_the_password_page = Set_The_Password_Page()
    set_the_phone_umber_page =Set_The_Phone_Number_Page()
    upload_head_picture =Upload_Head_Picture()
    college_info_page = College_Info_Page()
    collega_search_page = Collega_Search_Page()

    set_the_phone_umber_page.




    yield driver

