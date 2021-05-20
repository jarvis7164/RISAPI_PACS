#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 10:07
# @Author  : Zhangyp
# @File    : modality_send.py
# @Software: PyCharm
# @license : Copyright(C), eWord Technology Co., Ltd.
# @Contact : yeahcheung213@163.com
import datetime
from FakerData import choice
from c_store import find_images, store_image
from config import Path_CT, Path_DR, Path_MR, Path_CT1
import os, time
from pydicom.uid import generate_uid
from importlib import reload
# import register
# reload(register)
from register import register

"""获取登记信息"""
def get_reginfo():
    image_info = register()
    # print(image_info)
    # 提取子集
    image_item = {'patientID', 'accessionNumber', 'nameSpell', 'name', 'observationEndDate'}
    image = {key: image_info[key] for key in image_info.keys() & image_item}
    print("登记成功：姓名-%s，检查号-%s，检查时间-%s" % (image['name'], image['accessionNumber'], image['observationEndDate']))
    print(image_info['serviceSectID'])
    return (image, image_info['serviceSectID'])


"""批量c-store"""
def send_image():
    reg_info = get_reginfo()
    # 根据检查类型发送相应的影像
    serviceSectID = reg_info[1]
    if serviceSectID == "CT":
        Path = choice([Path_CT, Path_CT1])
    elif serviceSectID == "DR":
        Path = Path_DR
    else:
        Path = Path_MR
    images = find_images(Path)
    studyUID = generate_uid()
    # seriesUID = generate_uid()
    reg_info1 = reg_info[0]
    starttime = datetime.datetime.now()
    for i in images:
        image_file = os.path.join(Path, i)
        # store_image(image_file, studyUID, seriesUID, **reg_info)
        store_image(image_file, studyUID, **reg_info1)
    print("发送影像成功: 开始发送时间：", starttime, "结束时间:", datetime.datetime.now())


if __name__ == '__main__':
    # while True:
    send_image()
