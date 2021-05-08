#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 14:06
# @Author  : Zhangyp
# @File    : config.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
# 获取token
def get_token():
	import requests
	header = {'Content-Type': 'application/json'}
	url = "http://192.168.1.18:8709/Token/Retrive"  # token服务器地址
	payload ={
    "Audience":"eWordRIS",
    "HospitalCode":"QWYHZYFZX",
    "RequestIP":"192.168.1.58"
}
	res = requests.post(url, headers=header, json=payload)
	return res.json()['token']


"""58测试环境配置"""
HOST = "http://192.168.1.58:8900"


"""API配置"""
API_NAME = "/api/Order/Create"
# 全网云演示医院
USERINFO = '{"userID":"84934b3e-74c0-4978-a25a-acc900a72e6d","organizationID":"0dbd1600-6e0e-4e42-8215-acc400eb0de3","observationDeptID":"05b0b964-c092-40ac-aac0-acc400eb2bcc","clientAuthCode":"","useScenario":"1","cookieRequest":{"printTaskSolution":"00000000-0000-0000-0000-000000000001","printerSolution":"00000000-0000-0000-0000-000000000002","equipSolution":"","registableType":"CT,RF,XA,TJ,DR,MR,MG,CR"}}'

HEAD = {
	'content-type': 'application/octet-stream',
	'Authorization': get_token(),
	'userInfo': USERINFO
}


"""dicom参数配置"""
# 本地scu节点配置
LocalAE = 'jmModality'
Path_CT = r'D:\IMAGE\CT\Part1_HE DE MIN_CT004665_1.2.840.1.99.1.47.1.1619482157151.3362_1619489329647'
Path_CT1 = r'D:\IMAGE\CT\Part1_LI GUO QING_CT004667_1.2.840.1.99.1.47.1.1619482383171.3363_1619504688156'
Path_CT2 = r'D:\IMAGE\CT\Part1_LI YOU MIN_CT004675_1.2.840.1.99.1.47.1.1619483862269.3368_1619506051611'
Path_CT3 =r'D:\IMAGE\CT\Part1_PENG CHAO GANG_CT004677_1.2.840.1.99.1.47.1.1619483610248.3367_1619506188683'
Path_DR = r'D:\IMAGE\DR\Part1_CHEN KE RONG_0000474_1.3.6.2.25.17605975039128117117634935020602259405_1619507215332'
Path_MR = r'D:\IMAGE\MR\CENG AI JIN _10269068_032204029'


# 58存档
AETitle = 'qwySCP'
Addr = '192.168.1.58'
PORT = 8989


"""任务执行参数"""
# 每次任务发送间隔，单位秒
SendInterval = 15

# 任务休息时间，单位秒
SleepTime = 1
