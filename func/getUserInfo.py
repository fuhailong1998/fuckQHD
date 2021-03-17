#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : getUserInfo.py
@author      : fxkxb.com
@date        : 2021/3/15 16:35
@description :
"""

from ENV import *

url = 'https://jxjy.qhdjxjy.com/index.php/profile/default/get-user-info'


def getUserInfo(sess, access_token):
    t = sess.get(url=url, headers=header, params=access_token, verify=False)
    text_dict = eval(t.text)
    # print(text_dict)
    tem = {'user_id': 'USER_ID', 'user_name': 'USER_NAME', 'real_name': 'REAL_NAME', 'id_code': 'ID_NUMBER', 'mobile': 'PHONE_NUMBER',
           'access_token': 'Token', 'visit_count': 'VISIT_ACCOUNT'}
    for each in tem:
        print(tem[each] + '：' + str(text_dict['data'][each]))
    return text_dict['data']['user_name'], text_dict['data']['mobile'], text_dict['data']['photo']