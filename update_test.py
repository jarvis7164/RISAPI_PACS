#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 10:37
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : update_test.py
# @Software: PyCharm

from pydicom import dcmread
from pydicom.uid import generate_uid
import os


# 修改影像的方法
def update_image(file, studyuid, seriesuid):
    # 1.读取影像
    ds = dcmread(file)
    # 2.修改影像值
    ds.file_meta.TransferSyntaxUID = '1.2.840.10008.1.2'  # 'Implicit VR Little Endian'
    ds.file_meta.TransferSyntaxUID = '1.2.840.10008.1.2.1.99'
    ds.StudyInstanceUID = studyuid
    ds.SopInstanceUID = generate_uid()
    # 4.上下文添加影像类型
    class_uid = ds['SOPClassUID'].value
    ds.save_as(r'E:\testdemo\image\不同传输语法\新建文件夹\new' + '\\' + ds.SopInstanceUID + '.dcm')
    print("修改完成")


"""遍历影像文件"""


def find_images(path):
    images = []
    for file in os.listdir(path):
        if file.endswith('.dcm') or file.endswith('.DCM'):
            images.append(file)
    return images


path = r'E:\testdemo\image\不同传输语法\新建文件夹'

images = find_images(path)
for i in images:
    image_file = os.path.join(path, i)
    studyuid = generate_uid()
    seriesuid = generate_uid()
    update_image(image_file, studyuid, seriesuid)
