#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 17:16
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : test.py
# @Software: PyCharm
import datetime
import schedule
import time


def job():
    time = datetime.datetime.now()
    print("现在时间是: ", time)


schedule.every(10).seconds.do(job)  # 每隔十分钟执行一次任务
# schedule.every().hour.do(job, time)  # 每隔一小时执行一次任务
# schedule.every().day.at("10:30").do(job, time)  # 每天的10:30执行一次任务
# schedule.every(5).to(10).days.do(job, time)  # 每隔5到10天执行一次任务
# schedule.every().monday.do(job, time)  # 每周一的这个时候执行一次任务
# schedule.every().wednesday.at("13:15").do(job, time)  # 每周三13:15执行一次任务

while True:
    schedule.run_pending()  # run_pending：运行所有可以运行的任务
    time.sleep(2)
