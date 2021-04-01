#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : finishLesson.py
@author      : fxkxb.com
@date        : 2021/3/15 19:46
@description : 
"""
from ENV import header
from do.checkFace import checkFace
from do.finishExam import finishExam
from func.getTaskList import getTaskList


def finishLesson(sess, access_token, data, chdata):
    page = data
    task = getTaskList(sess, access_token, page)
    # print(task)
    ioo = 1
    url = "https://jxjy.qhdjxjy.com/index.php/study/watchtime/watch-time?access-token="+access_token['access-token']
    del page['access-token']
    del page['page']
    for each in task:
        temp = {
            'ware_id': each['ware_id'],
            'watch_time': each['hours'],
            'total_time': each['hours']
        }
        page.update(temp)
        chdata['taskId'] = each['ware_id']
        chdata['taskName'] = each['courseware_name']


        try:
            temp['watch_time'] = float(each['hours'])*0.95
        except ValueError:
            temp['watch_time'] = 60.0*0.95


        sess.post(url=url, headers=header, data=page)

        checkFace(sess, access_token, chdata)

        temp['watch_time'] = each['hours']

        text = sess.post(url=url, headers=header, data=page).text
        print(str(ioo)+"/"+str(len(task))+" Video Competed！" + text + "\n")
        ioo += 1

