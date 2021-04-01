#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : fuckQHD.py
@author      : fxkxb.com
@date        : 2021/3/15 16:33
@description : 
"""
import os
import time

import requests
from past.builtins import raw_input

from do.finishLesson import finishLesson
from do.finishExam import finishExam
from func.getCourseList import getCourseList
from func.getTaskList import getTaskList
from func.getUserInfo import getUserInfo
from do.checkFace import checkFace

# iiEK25zeEhWg


import base64

if __name__ == '__main__':

    print("Welcome!\n")

    # print("Choose Your Photo")
    # time.sleep(1)
    #
    # import tkinter as tk
    # from tkinter import filedialog
    #
    # root = tk.Tk()
    # root.withdraw()
    #
    # file_path = filedialog.askopenfilename()
    #
    # with open(file_path, "rb") as f:
    #     base64_data = base64.b64encode(f.read())
    # ImageB = str(base64_data)[2:-1]

    while True:

        token = input("Please Input access-token:\n")
        if token == '0':
            exit()

        access_token = {
            'access-token': token
        }

        sess = requests.session()

        try:
            nickname, mobile, photo = getUserInfo(sess, access_token)
            print("Getting Your Photo...\n")
            r = sess.get(photo)
            path = os.path.abspath(os.getcwd()) + '\photo.png'
            open(path, 'wb').write(r.content)
            print("Photo Saved To " + path + ".")
            while True:
                print("Choose the Choise：\n")
                print("1：Get Course List")
                print("Anyelse Key to Exit\n")
                opt = int(input())
                if opt == 1:
                    cli = getCourseList(sess, access_token)
                    while True:
                        opti = int(input())
                        data = cli[opti]

                        with open(path, "rb") as f:
                            base64_data = base64.b64encode(f.read())
                            ImageB = str(base64_data)[2:-1]

                        chdata = {}
                        chdata['ImageB'] = ImageB
                        chdata['UrlA'] = photo
                        chdata['photo'] = photo
                        chdata['nickname'] = nickname
                        chdata['mobile'] = mobile
                        chdata['courseName'] = data['course_name']
                        del data['course_name']
                        chdata['courseId'] = data['course_id']
                        chdata['exercName'] = ''



                        finishLesson(sess, access_token, data, chdata)
                        finishExam(sess, access_token, data)
                        input("Press Enter to Exit")

                else:
                    exit()

        except KeyError:
            print("Token Error！Please Input Again！\n")
