#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/9 16:40
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : writereport.py
# @Software: PyCharm
#自动获取状态为归档完成的报告并签名

import json
import time

from requests import request

import FakerData
import config
from config import HOST, USERINFO

#1.获取到归档完成的报告列表（调接口）
"""获取报告工作列表接口"""
def PageList():
    api_url = HOST + "/api/ReportList/PageList"  #RIS接口地址
    header = {'content-type': 'application/octet-stream',  # 头信息
              'Authorization': config.get_token(),
              'userinfo': USERINFO}
    #导入protobuf入参文件
    from ProtobufPy.ViOrderReportRequestPb_pb2 import ViOrderReportRequestPb
    ar_body = ViOrderReportRequestPb()
    """对象入参赋值"""
    ar_body.observationEndDate = '2021-05-08 00:00:00|2021-05-08 23:59:59'
    ar_body.resultStatus = '2090'
    ar_body.currentPage = 1
    ar_body.pageSize = 20
    ar_body = ar_body.SerializeToString()  # 将对象转化成字符串

    """模拟客户端发出请求"""
    with request(method='POST', url=api_url, data=ar_body, headers=header,timeout=5,
                             ) as ar_res:

        """解析返回结果"""
    # print(ar_res.content)
    # print(ar_res.status_code)
    from ProtobufPy.PageResponsePb_pb2 import PageResponsePb
    ar_data = PageResponsePb()  # 创建返回参数pb对象
    res_str = ar_res.content  # 获取返回的正文
    ar_data.ParseFromString(res_str)  # 从返回正文解析（第一层解析）
    # print(ar_data)
    # print("---------------------")
    from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
    from ProtobufPy.ReportListResponsePb_pb2 import ReportListResponsePb  # 导入返回参数中的相关pb
    ar_json = MessageToJson(ar_data)
    # print(ar_data)
    ar_dict = json.loads(ar_json.encode('utf-8').decode("unicode_escape"),
                         strict=False)  # 先处理unicode成中文，然后转化成字典
    # print(ar_dict)
    # 获取检查列表信息
    orderlist = ar_dict['data'][0]['orderReport']
    print(orderlist,type(orderlist))
    for a in orderlist:
        print(a,type(a))
        orderid = a['orderID']
        reportid = Loading(orderid)
        Signature(orderid,reportid)
        print('orderid为{0},reportid为{1}的检查签名成功'.format(orderid,reportid))


#加载报告获取reportid
def Loading(orderid):
    api_url = HOST + "/api/Report/Loading"
    header = {'content-type': 'application/octet-stream',  # 头信息
              'Authorization': config.get_token(),
              'userinfo': USERINFO}

    from ProtobufPy.ReportRequestPb_pb2 import ReportRequestPb
    rr_body = ReportRequestPb()
    """对象入参赋值"""
    rr_body.orderID = orderid
    from ProtobufPy.OrderReportRequestPb_pb2 import OrderReportRequestPb
    orr_body = OrderReportRequestPb()
    orr_body.report.CopyFrom(rr_body)
    orr_body = orr_body.SerializeToString()  # 将对象转化成字符串

    """模拟客户端发出请求"""
    with request(method='POST', url=api_url, data=orr_body, headers=header,timeout=5,
                             ) as ar_res:

        """解析返回结果"""
    from ProtobufPy.PageResponsePb_pb2 import PageResponsePb
    ar_data = PageResponsePb()  # 创建返回参数pb对象
    res_str = ar_res.content  # 获取返回的正文
    ar_data.ParseFromString(res_str)
    # print(ar_data)
    from google.protobuf.json_format import MessageToJson  # 用于第二层解析特殊的类型
    from ProtobufPy.ReportWriteListResponsePb_pb2 import ReportWriteListResponsePb
    ar_json = MessageToJson(ar_data)
    # print(ar_data)
    ar_dict = json.loads(ar_json.encode('utf-8').decode("unicode_escape"),
                         strict=False)  # 先处理unicode成中文，然后转化成字典
    # print(ar_dict)
    report = ar_dict['data'][0]['report']
    # print(report,type(report))
    # print(report['reportID'])
    return report['reportID']
#根据获取到的报告ID调RIS接口完成报告书写
def Signature(orderid,reportid):
    api_url = HOST + "/api/Report/Signature"
    header = {'content-type': 'application/octet-stream',  # 头信息
              'Authorization': config.get_token(),
              'userinfo': USERINFO}

    from ProtobufPy.ReportRequestPb_pb2 import ReportRequestPb
    rr_body = ReportRequestPb()
    """对象入参赋值"""
    rr_body.orderID = orderid
    rr_body.reportID = reportid
    rr_body.abnormalFlag = '0'
    # rr_body.imagingFinding = '影像所见测试内容'
    rr_body.imagingFinding = FakerData.fake.paragraph()
    print(rr_body.imagingFinding)
    # rr_body.imagingDiagnosis = '影像诊断测试内容'
    rr_body.imagingDiagnosis = FakerData.fake.paragraph()
    rr_body.resultAssistantID = '42819E01-C077-4DB5-8B09-ACBC00A5343E'
    rr_body.resultAssistantName = '贾苗'
    rr_body.resultPrincipalID = '42819E01-C077-4DB5-8B09-ACBC00A5343E'
    rr_body.resultPrincipalName = '贾苗'
    rr_body.isCheckedWriteAndAudit = 1
    from ProtobufPy.OrderReportRequestPb_pb2 import OrderReportRequestPb
    orr_body = OrderReportRequestPb()
    orr_body.report.CopyFrom(rr_body)
    orr_body = orr_body.SerializeToString()  # 将对象转化成字符串
    print(orr_body)

    """模拟客户端发出请求"""
    with request(method='POST', url=api_url, data=orr_body, headers=header,timeout=5,
                             ) as ar_res:

        """解析返回结果"""
        res_str = ar_res.content  # 获取返回的正文
        # print(res_str)
        # print(ar_res.status_code)

PageList()

# if __name__=='__main__':
#     i =0
#     while i <50:
#         PageList()
#         i+=1
#         time.sleep(2)
#     # Loading()