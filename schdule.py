#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 17:12
# @Author  : jarvis
# @Email   : 309194437@qq.com
# @File    : schdule.py
# @Software: PyCharm
import datetime

import schedule
import time

def job():
    print("I'm working...")
    print(datetime.datetime.now())

schedule.every(5).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(2)