#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : getCourseList.py
@author      : fxkxb.com
@date        : 2021/3/15 17:11
@description : 
"""

from ENV import *

url = 'https://jxjy.qhdjxjy.com/index.php/study/default/my-course'


def getCourseList(sess, access_token):
    clist = {}
    t = sess.get(url=url, headers=header, params=access_token, verify=False)
    text_dict = eval(t.text)
    temp = {'grade_id': '班级ID', 'course_name': '课程名称', 'class_hour': '学时', 'course_id': '课程ID'}
    # for iii in text_dict['data']:
    #     print(iii)
    i = 1

    for eachi in text_dict['data']:
        # i = 1
        print('\n')
        print(str(i) + "：" + eachi["course_name"])
        print('\n')
        clist[i] = {'grade_id': eachi['grade_id'], 'course_id': eachi['course_id'], 'course_name': eachi["course_name"]}
        i += 1
    # print(clist)
    return clist
