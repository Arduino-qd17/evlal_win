#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
#coding : gbk
#LOG日志记录
import logging
import logging.config
from logging.handlers import RotatingFileHandler
CONF_LOG = "main.log"

logging.basicConfig(level=logging.DEBUG,
                    #format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    format='time:%(asctime)s py_name:%(filename)s def_Name:%(funcName)s [line:%(lineno)d]--%(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=CONF_LOG,
                    filemode='a+')

Rthandler = RotatingFileHandler(CONF_LOG, maxBytes=10*1024*1024,backupCount=20)
Rthandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter)
logging.getLogger('').addHandler(Rthandler)
#################################################################################################


if __name__ == "__main__":
    #add_log()
    logging.debug('This is debug message')
