#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : getTaskList.py
@author      : fxkxb.com
@date        : 2021/3/15 18:43
@description : 
"""
from ENV import header

global null
null = ''
def getTaskList(sess, access_token, data):
    url = "https://jxjy.qhdjxjy.com/index.php/study/default/course-task"
    data.update(access_token)
    text = sess.get(url=url, headers=header, params=data).text
    text_dict = eval(text)


    taskList = []

    for i in range(1, text_dict['totalPage']+1):
        data.update({'page': i})
        text = sess.get(url=url, headers=header, params=data).text
        taskL = eval(text)
        for each in taskL['data']:
            taskList.append(each)
    return taskList