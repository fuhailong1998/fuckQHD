#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : ENV.py
@author      : fxkxb.com
@date        : 2021/3/15 16:44
@description : 
"""
import re
import urllib

global null
null = ''
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
header = {
    'host': "jxjy.qhdjxjy.com",
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/x-www-form-urlencoded',
    'Referer': 'https://servicewechat.com/wxe4ed7b5ec8531d2a/34/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',
}
def getStr(text):
    t = ''
    for each in text:
        t += each + '=' + str(text[each])
        t += '&'
    t = urllib.parse.quote(t[:-1])
    # data = re.sub('%7B', '{', data)
    # data = re.sub('%7D', '}', data)
    t = re.sub('%5B', '[', t)
    t = re.sub('%5D', ']', t)
    t = re.sub('%27', '\"', t)
    t = re.sub('%22', '\'', t)
    t = re.sub('%2C', ',', t)
    t = re.sub('%3A', ':', t)
    t = re.sub('%3D', '=', t)
    t = re.sub('%26', '&', t)
    return t