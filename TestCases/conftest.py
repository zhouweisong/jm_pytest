"""
-------------------------------------------------
   File Name：     conftest
   Description :
   Author :       zws
   date：          2018/3/6
-------------------------------------------------
   Change Activity:
                   2018/3/6:
-------------------------------------------------
"""
__author__ = 'zws'

import pytest

from Common.BaseDriver import BaseDriver
from PageObjects.home_page import Home_Page
from PageObjects.login_page import Login_Page
from TestDatas import COMM_DATA as CD


@pytest.fixture
def init_driver():
    driver = BaseDriver().init_driver()
    yield driver


@pytest.fixture
def init_add_friend():
    driver = BaseDriver().init_driver()
    home_page = Home_Page(driver)
    login_pag = Login_Page(driver)
    home_page.touch_login()
    login_pag.login_by_password_action(CD.login_username_zws, CD.login_passwd_zws)
    home_page.touch_do_next()
    home_page.touch_home_friend()
    yield driver

@pytest.fixture()
def init_register():
    driver = BaseDriver().init_driver()
    home_page = Home_Page(driver)
    home_page.touch_to_sign_up()
    yield driver


