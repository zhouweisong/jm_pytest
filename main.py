"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       zws
   date：          2018/3/5
-------------------------------------------------
   Change Activity:
                   2018/3/5:
-------------------------------------------------
"""
__author__ = 'zws'


import pytest

pytest.main(["-m zws","--junitxml=HtmlReport/result.xml","--html=HtmlReport/smoke_report.html","-s"])