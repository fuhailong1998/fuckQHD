#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@file        : test1.py
@author      : fxkxb.com
@date        : 2021/3/15 23:52
@description : 
"""
# re_data = {'{': '%7B', '}': '%7D', '[': '%5B', ']': '%5D', '"': '%22', "'": '%27', ',': '%2C', ':': '%3A'}
# tem = {}
# for i in re_data:
#     tem[re_data[i]]=i
# print(re_data)
# print(tem)
#
# for i in range(1,61):
#     print(i)
#
# import wmi as wmi
#
# s=wmi.WMI()
#
#
# for i in s.Win32_NetworkAdapterConfiguration():
#     print(i)
from scapy.all import *
# import re
# #
# #
# def get_netdev():
#     ethList = []
#     t = get_ips()
#     for i in t:
#         eth = re.search('\[(.*)\]', str(i)).group(0)
#         ethList.append(eth[1:-1])
#     return ethList
#
#
# devs = get_netdev()
# for index, v in enumerate(devs):
#     print(str(index + 1) + "：" + v)
#
# devopt = int(input())
# #
# dev_name = devs[devopt - 1]

# from scapy.all import *
#
# # while True:
# dpkt = sniff(filter='', iface='Qualcomm Atheros AR8171/8175 PCI-E Gigabit Ethernet Controller (NDIS 6.30)',count=100)
# for i in dpkt:
#     i.show()
#
from scapy.all import *
#
#
# # 定义回调函数，嗅探一次返回执行一次
def pack_callback(pack):
    try:
        for i in pack:
            i.show()

    except Exception as e:
        print(e)

dpkt = sniff(iface="Qualcomm Atheros AR8171/8175 PCI-E Gigabit Ethernet Controller (NDIS 6.30)", prn = pack_callback)
# dpkt = sniff(iface="Apple Mobile Device Ethernet", count=100)

# for i in dpkt:
#     i.show()
