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
import pytest
from Common.logger2 import *



@pytest.mark.usefixtures('init_driver')
class Test_Login:

    @pytest.mark.smoke
    def test_login_by_password_ok(self, init_driver):
        home_page = Home_Page(init_driver)
        login_pag = Login_Page(init_driver)
        home_page.touch_login()
        login_pag.login_by_password_action(CD.login_username_zws, CD.login_passwd_zws)
        logging.info("测试用例：密码登录----成功")
        okname = home_page.get_ok_name()
        logging.info("这个okname元素的text值 ：%s"%okname)
        assert okname == '好'

    def test_login_by_wrong_password(self, init_driver):
        home_page = Home_Page(init_driver)
        login_page = Login_Page(init_driver)
        home_page.touch_login()
        login_page.login_by_password_action(LD.login_success_username, LD.login_wrong_passwd)
        logging.info("测试用例：密码登陆----密码错误")
        message ='手机号或密码错误，请重新输入'
        assert login_page.toast_exist(message)


    def test_login_by_verification_ok(self,init_driver):
        home_page = Home_Page(init_driver)
        login_pag = Login_Page(init_driver)
        home_page.touch_login()
        login_pag.login_by_verification_action(LD.login_success_username,LD.login_success_verification_code)
        logging.info("测试用例：验证码登录----成功")
        okname = home_page.get_ok_name()
        logging.info("这个okname元素的text值 ：%s"%okname)
        assert okname == '好'


    def test_login_by_wrong_verification(self,init_driver):
        home_page = Home_Page(init_driver)
        login_pag = Login_Page(init_driver)
        home_page.touch_login()
        login_pag.login_by_verification_action(LD.login_success_username,LD.login_wrong_verification_code)
        logging.info("测试用例：验证码登录----验证码错误")
        message ='验证码错误'
        assert login_pag.toast_exist(message)








