import time
from datetime import datetime, timedelta
from datetime import date
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl
import sys, os
import pyperclip
import pyautogui as pg


# 날짜 지정
today = str(date.today()) # 오늘 날짜 '2023-01-06' 과 같은 형식으로 지정
now = datetime.now()
before_1day = now - timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(before_1day.now)
before_2day = now - timedelta(days=2, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
before_2day.now()
before_3day = now - timedelta(days=3, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
selected_days = []