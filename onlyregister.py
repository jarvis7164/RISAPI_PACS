#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 15:43
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : onlyregister.py
# @Software: PyCharm
import time

from config import HOST, API_NAME, HEAD
import requests
from FakerData import Person, choice
import json

p = Person()
# 登记
def register():
    url = HOST + API_NAME
    from ProtobufPy.OrderRequestPb_pb2 import OrderRequestPb
    """赋值第一层参数值"""
    body = OrderRequestPb()
    # 科室ID
    body.observationDeptID = '05b0b964-c092-40ac-aac0-acc400eb2bcc'
    # 机构ID
    body.organizationID = '0dbd1600-6e0e-4e42-8215-acc400eb0de3'
    body.serviceSectID = choice(["CT","MR","DR"])
    body.name = p.name
    body.iDCard = p.idcardno
    body.nameSpell = p.name_spell
    body.sex = p.sex
    body.birthDate = p.birth_date.strftime('%Y-%m-%d')
    body.patientClass = choice([1000, 2000, 3000, 4000])
    body.age = p.age
    body.ageUnit = '岁'
    body.chargeFlag = choice([0,1])
    body.charges = 60
    if body.serviceSectID == "CT":
        body.observationLocationID = '0A56138D-C7D2-486B-9D57-ACC400EB30AD'
        body.observationLocation = 'CT#1'
        body.examBodyPart = "颌面CT定位"
        body.examBodyPartID = "F7A6F0BC-69BF-4A5D-8332-ACC400EB3312"
        body.procedureID = "E8F0B7B7-17A7-484A-80DD-ACC400EB35EA"
        body.procedureName = "鼻咽部平扫(定位)"
        body.procedureWorkload = '1.00'
        body.diagnosticGroupID = "00AF0C33-8C8F-4B57-98B0-ACC400EB32E2"
        body.allProcedureName = "鼻咽部平扫(定位)"
    elif body.serviceSectID == "MR":
        body.observationLocationID = '03F05DC7-873A-46A4-BFE9-ACC400EB30AD'
        body.observationLocation = 'MR#1'
        body.examBodyPart = "头颅"
        body.examBodyPartID = "837C3B63-E724-4596-9C48-ACC400EB3312"
        body.procedureID = "D04894AF-98C5-4F3D-8077-ACC400EB35EA"
        body.procedureName = "头颅MRA"
        body.procedureWorkload = '1.00'
        body.diagnosticGroupID = "00AF0C33-8C8F-4B57-98B0-ACC400EB32E2"
        body.allProcedureName = "头颅MRA"
    else:
        body.observationLocationID = '0B98D1B2-E081-485E-A716-ACC400EB3098'
        body.observationLocation = 'DR#1'
        body.examBodyPart = "胸部"
        body.examBodyPartID = "C607DD1D-645E-49E9-8A47-ACC400EB3312"
        body.procedureID = "FAD02D2E-AF55-4FE8-8004-ACC400EB35EA"
        body.procedureName = "左肩关节正位"
        body.procedureWorkload = '1.00'
        body.diagnosticGroupID = "70711B83-2F12-43B8-B85F-ACC400EB32E2"
        body.allProcedureName = "左肩关节正位"
    """追加第二层参数值"""
    from ProtobufPy.OrderListRequestPb_pb2 import OrderListRequestPb
    olr_body = OrderListRequestPb()
    olr_body.datas.append(body)
    olr_body = olr_body.SerializeToString()
    res = requests.request(method='POST', url=url, data=olr_body, headers=HEAD)

    register()
    print("登记成功")

# i=0
# while i<10:
#     register()
#     print("登记成功")
#     i+=1
#     # 延迟10秒执行
#     time.sleep(60)
