#!/usr/local/bin/python
#-*- coding: UTF-8 -*-
import re
import httplib
import gzip
import StringIO
import urllib
import urllib2
import requests
from Db_Model import db_shell #常用数据库操作
from Clicked_Controller import log #日志记录
from Ui_View import ui #UI变量
from PyQt4 import QtCore, QtGui ,QtNetwork
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


def Post_eval_php(ID,params):  #POST 提交内容
    try:
        id_shell_list=db_shell.id_sitetable_shell('%s'%(str(ID)))  #通过ID查询SHELL的状态

        url=str(id_shell_list[2])    #    网址
        PASS=str(id_shell_list[3])   #    密码

        coding=str(id_shell_list[6])     #  编码方式
        #script=str(id_shell_list[7])      #   asp   php
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        #values = {SitePass:Data}#得密码post内容
        values = PASS  + params#上面的方式会进行自动URL编码所以用这种方式+ "="

        req = requests.post(str(url), values, headers=headers, timeout=int(ui.link_shell_timeout))#强制转换为str
        if str(req.status_code)!="200":
            data=u"%s\n%s"%(str(req.status_code),str(req.headers))
            return 0,str(data)
        else:
            if coding=="65001":
                req.encoding = 'UTF-8'
            elif coding=="936":
                req.encoding = 'GB2312'
            elif coding=="950":
                req.encoding = 'BIG5'
            elif coding=="949":
                req.encoding = 'Euc-KR'
            elif coding=="20932":
                req.encoding = 'Euc-JP'
            elif coding=="932":
                req.encoding = 'Shift_JIS'
            elif coding=="1251":
                req.encoding = 'Windows-1251'
            elif coding=="874":
                req.encoding = 'Windows-874'
            elif coding=="1252":
                req.encoding = 'ISO-8859-1'
            else:
                req.encoding = 'GB2312'

            one_page = req.text

            real_page=GetRealTxt("->|", "|<-", str(one_page))
            if str(real_page)=="False":
                data=u"HTTP /1.1 OK\n%s\n%s"%(str(req.headers),str(req.text))
                return 0,str(data)
            else:
                return 1,str(real_page)
    except BaseException, e:
        #log.logging.debug("except:%s"%(str(e)))
        return 0,str("LINK SHELL error:"+str(e))


def GetRealTxt(start_str, end, html):#取两个字符串之间的值
    try:
        if str(html)=="":
            return("False")
        else:
            start = html.find(start_str)
            if start >= 0:
                start += len(start_str)
                end = html.rfind(end, start)  #从尾部查找
                if end >= 0:
                    return html[start:end].strip()
                else:
                    return ("False")
            else:
                return ("False")
    except BaseException, e:
        log.logging.debug("except:%s"%(str(e)))




