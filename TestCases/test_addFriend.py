"""
-------------------------------------------------
   File Name：     test_addFriend
   Description :
   Author :       zws
   date：          2018/3/13
-------------------------------------------------
   Change Activity:
                   2018/3/13:
-------------------------------------------------
"""
__author__ = 'zws'

import pytest

from PageObjects.Add_Friend.addFriend_page import Add_Friend_Page


@pytest.mark.usefixtures('init_add_friend')
class Test_Add_Friend:

    #好友搜索成功
    @pytest.mark.debug1
    def test_add_friend(self,init_add_friend):
        add_friend_page = Add_Friend_Page(init_add_friend)
        add_friend_page.touch_my_colleage()
