"""
-------------------------------------------------
   File Name：     RW_Config
   Description :
   Author :       zws
   date：          2018/3/29
-------------------------------------------------
   Change Activity:
                   2018/3/29:
-------------------------------------------------
"""
__author__ = 'zws'

import configparser
import os

class RW_Config():


    def read_config(self,config_name,section,option):
        cur_dir = os.path.split(os.path.abspath(__file__))[0]
        conf_dir = cur_dir.replace('Common', 'TestDatas')
        # 指定你要读取哪个配置文件并打开
        cf = configparser.ConfigParser()
        cf.read(conf_dir + '/' + config_name)
        # 正式读取配置文件
        config = eval(cf.get(section,option))
        return config

    def set_config(self,config_name,section,option,dic_key):
        cur_dir = os.path.split(os.path.abspath(__file__))[0]
        conf_dir = cur_dir.replace('Common', 'TestDatas')
        # 指定你要读取哪个配置文件并打开
        cf = configparser.ConfigParser()
        cf_path = conf_dir + '/' + config_name
        cf.read(cf_path)
        # 正式读取配置文件
        config = eval(cf.get(section,option))
        config[dic_key] = int(config[dic_key])+1
        cf.set(section, option, value=str(config))
        cf.write(open(cf_path,'w'))





if __name__ == '__main__':
    abc = RW_Config()
    abc.set_config('register.conf','REGISTERCONF','register_ok','phone')
    print(abc.read_config('register.conf','REGISTERCONF','register_ok'))





