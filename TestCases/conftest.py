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
from PageObjects.login_page import Login_Page


from TestDatas import COMM_DATA as CD


@pytest.fixture
def init_driver():
    driver = BaseDriver().init_driver()
    yield driver


@pytest.fixture
def init_login():
    driver = BaseDriver().init_driver()
    loginpage = Login_Page(driver)
    loginpage.login_action(CD.web_url, CD.login_username, CD.login_passwd)
    yield  driver