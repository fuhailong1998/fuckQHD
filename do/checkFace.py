#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : checkFace.py
@author      : fxkxb.com
@date        : 2021/3/15 19:23
@description : 
"""

from ENV import header, getStr


def checkFace(sess, access_token,chdata):
    data = {
        "email": "null",
        "checkType": "video",
        "action": "2"
    }
    data.update(chdata)
    # print(data)
    data = getStr(data)

    url = 'https://jxjy.qhdjxjy.com/index.php/study/check-face/check-face?access-token=' + access_token['access-token']

    text = sess.post(url=url, headers=header, data=data).text
    print(text)
