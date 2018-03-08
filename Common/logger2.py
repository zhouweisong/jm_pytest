"""
-------------------------------------------------
   File Name：     logger2
   Description :
   Author :       zws
   date：          2018/3/7
-------------------------------------------------
   Change Activity:
                   2018/3/7:
-------------------------------------------------
"""
__author__ = 'zws'

import logging
from Common import config
from logging.handlers import RotatingFileHandler
import time

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
logpath = config.log_dir + "app_autoTest_"+rq+".log"

handler_1 = logging.StreamHandler()
handler_1.setLevel(logging.INFO)

handler_2 = RotatingFileHandler(logpath, maxBytes=1024*1024*100,backupCount=10)
handler_2.setLevel(logging.INFO)

logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])