#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : finishExam.py
@author      : fxkxb.com
@date        : 2021/3/15 19:46
@description : 
"""
import re
import urllib.parse


import jsonpickle
import urllib3

from do.checkFace import checkFace

global null
null = 'null'
from ENV import header, getStr
from func.getTaskList import getTaskList




def finishExam(sess, access_token, data):
    examData = {}
    examData["courseId"] = data['course_id']
    iii = 1
    task = getTaskList(sess, access_token, data)
    for each in task:
        # print(task)
        examData["wareId"] = each['ware_id']
        examData["gradeId"] = data['grade_id']
        exercise_id = each['exercise_id']
        examData["exercId"] = exercise_id
        url = 'https://jxjy.qhdjxjy.com/index.php/study/exercise/exercise-info?access-token=' + access_token[
            'access-token'] + '&exercise_id=' + exercise_id
        text = sess.get(url=url, headers=header).text
        ans_dict = eval(text)['data']
        task_li = ["single", "multi", "duge", "fill"]
        for eacc in task_li:
            try:
                for i in range(0, len(ans_dict[eacc])):
                    ans_dict[eacc][i]["user_answer"] = ans_dict[eacc][i]["answer"]
            except TypeError:
                pass
        examData["exercInfo"] = ans_dict

        tata = getStr(examData)

        # checkFace(sess,access_token)
        toPosturl = "https://jxjy.qhdjxjy.com/index.php/study/exercise/exercise-result?access-token=" + access_token['access-token']

        text = sess.post(url=toPosturl, headers=header, data=tata).text
        print(str(iii) + "/" + str(len(task)) + " Test Competed！" + text + "\n")
        iii += 1


