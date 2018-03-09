"""
-------------------------------------------------
   File Name：     test_login
   Description :
   Author :       zws
   date：          2018/3/6
-------------------------------------------------
   Change Activity:
                   2018/3/6:
-------------------------------------------------
"""
__author__ = 'zws'

from PageObjects.login_page import Login_Page
from PageObjects.home_page import Home_Page
from TestDatas import login_datas as LD
from TestDatas import COMM_DATA as CD
import logging
import pytest
from Common.logger2 import *



@pytest.mark.usefixtures('init_driver')
class Test_Login:

    @pytest.mark.smoke
    def test_login_ok(self,init_driver):
        home_page = Home_Page(init_driver)
        login_pag = Login_Page(init_driver)

        home_page.touch_login()
        login_pag.login_action(CD.login_username,CD.login_passwd)
        logging.info("测试用例：正常登陆芥末校园。")
        okname = home_page.get_ok_name()
        logging.info("这个okname元素的text值 ：%s"%okname)
        assert okname == '好'

    @pytest.mark.debug
    def test_login_wrong_password(self,init_driver):
        home_page = Home_Page(init_driver)
        login_page = Login_Page(init_driver)

        home_page.touch_login()
        login_page.login_action(LD.login_success_username, LD.login_wrong_passwd)
        logging.info("测试用例：登陆----密码错误")
        message ='啦啦号或密码错误，请重新输入'
        assert login_page.toast_exist(message)






